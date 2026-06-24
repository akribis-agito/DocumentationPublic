---
summary: 从动驱动器复制其电流参考的主轴索引。
keyword: CurrRefMaster
availability:
  standalone: []
  central-i:
  - v5
can_code: 553
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 7
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CurrRefMaster

从动驱动器复制其电流参考的主轴索引。

## 概述

`CurrRefMaster` 是从动驱动模式中使用的主轴索引（从 0 开始）：从轴从主轴的 `CurrRef` 复制其电流参考（`CurrRef`）。它仅在 [CurrCmdSrc](CurrCmdSrc.md) = 3 时适用，该值仅存在于 central-i v5 固件中。

## 工作原理

每个控制周期，在电流模式且 `CurrCmdSrc` = 3 时，固件将本轴的 `CurrRef` 直接设为等于 `CurrRef[CurrRefMaster]` —— 即逐采样跟踪主轴的电流参考。主轴索引是一个普通的从 0 开始的轴号：

| 值    | 轴   |
|-------|------|
| 0     | A    |
| 1     | B    |
| …     | …    |

从动驱动操作的持续时间由 [CurrCmdHTime](CurrCmdHTime.md)`[1]` 控制，与模拟源完全相同：若 `CurrCmdHTime[1]` 为负，从轴无限期跟随主轴；若为 0 或正值，当 [CurrCmdCntr](CurrCmdCntr.md) 超过它时轴返回位置模式。此源不应用斜坡（[CurrCmdSlope](CurrCmdSlope.md)）或表步进。

> **注意：** `CurrRefMaster` 不能在电机使能或运动中更改。请在启用从动驱动操作之前配置它。

## 示例

```text
ACurrCmdSrc=3        ; follow a master axis (slave drive)
ACurrRefMaster=0     ; copy current reference from axis A
```

### 边界情况

- **写入时电机使能 / 运动中** —— 被拒绝。请在电机失能时配置。
- **`CurrCmdSrc ≠ 3`** —— 值被存储，但从轴不跟随任何对象。
- **自引用** —— 指向与从轴相同的轴会使复制成为空操作（轴复制自己的 `CurrRef`），因此 `CurrRef` 冻结在进入电流模式时所持有的值。
- **主轴不在电流模式** —— 从轴仍复制 `CurrRef[master]`；如果主轴处于位置或速度模式，从轴跟随位置 / 速度环在 `CurrRef` 中所保持的值。
- **超出范围** —— 超过轴数量的值被拒绝。
- **保存** —— 可保存至闪存。
- **平台** —— 仅 v5 central-i。

## 另请参见

- [CurrCmdSrc](CurrCmdSrc.md) —— 选择主轴电流指令（值 3）
- [CurrCmdHTime](CurrCmdHTime.md) —— `[1]` 设置从轴跟随主轴的时长
- [电流运行模式](00-overview.md) —— 电流模式关键字概述
