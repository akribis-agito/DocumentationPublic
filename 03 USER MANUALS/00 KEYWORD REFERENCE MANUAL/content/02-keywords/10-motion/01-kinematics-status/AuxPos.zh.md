---
keyword: AuxPos
summary: 辅助编码器位置反馈，以辅助用户单位表示。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 3
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: aux_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# AuxPos

辅助编码器位置反馈，以辅助用户单位表示。

## 概述

`AuxPos` 报告辅助编码器反馈，以辅助用户单位（通过 [AuxUsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 配置）表示。它是主位置反馈 [Pos](Pos.md) 在辅助环中的对应量：它馈入双环控制，可作为误差映射的 [MapEncoder](../../04-error-mapping/MapEncoder.md) 源，并且是辅助速度 [AuxVel](AuxVel.md) 的导出依据。

尽管 `AuxPos` 可写，但只能在轴禁用时设置（它声明为 `RW`，并带有不可运动 / 不可电机使能标志）。其值在上电时重置为 `0`。

## 工作原理

### 读取

控制器在每个控制周期读取辅助编码器，计算每周期变化量并将其累加到辅助位置中；该每周期增量也驱动 [AuxVel](AuxVel.md)。在控制器硬件上，辅助编码器是一个物理输入；在 central-i 主站上，辅助值按轴通过网络传送。对于绝对式辅助编码器，它在启动时由绝对读数初始化。

### 在双环与误差映射中的使用

- **双环：** 当 [DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) = 1 时，辅助编码器作为负载端反馈。速度环使用经 [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) 缩放后的辅助速度（参见 [Vel](Vel.md)`[1]`），换相位置及其增量取自辅助编码器。
- **误差映射：** [误差映射编码器](../../04-error-mapping/MapEncoder.md)选择可将映射源指向某个轴的辅助位置，从而由辅助编码器提供映射坐标。默认情况下，辅助误差映射未启用；如需此功能，请联系 Agito。

### 边界情况

- **电机失能：** 无论电机状态如何，`AuxPos` 都持续跟踪辅助编码器读数——它是一个原始反馈值，而非闭环量。只有对 `AuxPos` 的写入才要求电机禁用。
- **仿真模式（`MotorType` = 5）：** 没有物理辅助编码器，因此 `AuxPos` 保持其上次写入的值（不会自动跟随某个辅助参考）。
- **取模（`ModRev`）：** 取模/连续旋转环绕仅应用于主反馈 [Pos](Pos.md)；`AuxPos` **不会**被 [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) 环绕。对于通过齿轮传动的旋转负载，应将 `AuxPos` 视为无界累加器。
- **龙门：** 辅助编码器为按轴配置，不会合并到龙门共模反馈中；它们对于龙门每条腿的按轴双环仍然有用。
- **超范围写入：** 超出声明范围的写入将被拒绝并返回错误；该值不会被钳位或静默截断，因此保留先前的值。
- **激活故障：** 即使轴处于故障状态，`AuxPos` 仍继续从辅助编码器更新；在故障期间读取它是检查负载端停止位置的常规方法。

## 示例

```text
AAuxPos             ; read the auxiliary encoder position
AAuxPos=0           ; preset to zero (axis must be disabled)
```

## 版本间差异

在 **v5（central-i）** 中，`AuxPos` 是 64 位值；其读取、双环和误差映射用途相同。数据类型/范围的差异显示在 frontmatter 中。**v5 仅适用于 central-i**，因此在 standalone 上 `AuxPos` 仍为 v4 的 32 位值。

## 另请参阅

- [AuxVel](AuxVel.md) — 辅助速度，由 `AuxPos` 导出
- [Pos](Pos.md) — 主编码器位置反馈
- [AuxUsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — 辅助用户单位缩放
- [DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) / [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) — 辅助编码器的双环使用
