---
keyword: MasterModRev
summary: 当主变量发生环绕时，用于修正 MasterPos 累积的取模除数。
availability:
- controller
- ci-master
can_code: 519
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    data_type: int64
last_updated: '2026-11-23'
doc_revision: '2026.11'
language: zh-CN
---
# MasterModRev

当主变量发生环绕时，用于修正 MasterPos 累积的取模除数。

## 概述

`MasterModRev` 是取模除数，用于确保当 [GearMaster](GearMaster.md) 所选变量参与取模运算时，[MasterPos](MasterPos.md) 能够正确累积。主变量在以下情况下会执行取模运算：

1. 与主变量相关的 `ModRev` 非零，且
2. 该变量通常为 [Pos](../01-kinematics-status/Pos.md)、PDPos、[MasterPos](MasterPos.md)、[PosRef](../01-kinematics-status/PosRef.md) 或 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) 之一。

必须将 `MasterModRev` 设置为与主变量的 [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) 相匹配（需手动赋值——固件不会自动复制）。若主变量不涉及取模运算，则 `MasterModRev` 必须为 `0`。这与从动轴自身 [Pos](../01-kinematics-status/Pos.md) 上的 `ModRev` 类似，但适用于齿轮的*主轴*侧。

## 工作原理

### 为何需要该参数

[MasterPos](MasterPos.md) 每个周期累积主变量的*变化量*。若主变量是一个在取模边界处发生环绕的连续旋转变量，一次环绕会在单个周期内产生近乎一整个 `ModRev` 的表观变化量——这是一个巨大的虚假变化量，会导致从动轴发生突变。`MasterModRev` 告知累加器该边界的大小，使其能够识别并消除该跳变。

### 修正方式

每个周期，若 `MasterModRev ≠ 0`，则将变化量与边界的一半进行比较：

- 变化量大于 `+MasterModRev/2`，视为正向环绕，减去 `MasterModRev`；
- 变化量小于 `−MasterModRev/2`，视为反向环绕，加上 `MasterModRev`。

因此，大于半圈的变化量被解释为反方向的环绕并予以消除，使 `MasterPos` 在主变量的取模边界处保持连续。这一假设前提是主变量每个控制周期移动量不超过其 `ModRev` 的一半——与从动轴自身取模处理所作的假设相同。

在 v5 中，控制器先对主变量的原始变化量进行回绕修正，再应用齿轮比。请将 `MasterModRev` 设为主变量以主轴计数表示的回绕周期。Central-i 主站以 64 位数值存储此设置。

## 示例

```text
AMasterModRev=0          ; 主变量无取模运算（默认）
AMasterModRev=3600000    ; 匹配主变量的 ModRev（例如旋转主轴）
AMasterModRev            ; 读取当前值
```

## 版本间变更

旧版 YiGuang 固件在应用齿轮比之后才进行回绕修正，因此保存的周期以从轴计数表示。旧齿轮比和周期均非零时，将旧周期的绝对值除以旧齿轮比（已保存的 `MasterFact / 65536`）的绝对值。例如，旧齿轮比为 1:2 或 −1:2 时，500 个从轴计数应换算为 1,000 个主轴计数。使用该设置前，请确认换算结果等于主轴的实际回绕周期。周期为零时仍然禁用修正。周期设置错误可能使主轴的一次正常回绕变成从轴的大幅运动指令。[迁移说明](https://github.com/akribis-agito/Firmware-Main/blob/develop/docs/engineering/Gearing-Migration.md)

## 另请参阅

- [MasterPos](MasterPos.md) — 该除数所保护的累积缩放主位置
- [GearMaster](GearMaster.md) — 选择主变量
- [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) — 主变量自身的取模值，`MasterModRev` 必须与之匹配
