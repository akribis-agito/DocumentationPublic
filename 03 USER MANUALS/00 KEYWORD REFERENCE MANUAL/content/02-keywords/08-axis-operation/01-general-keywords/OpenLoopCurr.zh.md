---
keyword: OpenLoopCurr
summary: 电流开环模式下施加到电流环的电流参考。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 145
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# OpenLoopCurr

电流开环模式下施加到电流环的电流参考。

## 概述

`OpenLoopCurr` 是在轴处于电流开环条件下时施加到电流环上的电流参考，以毫安为单位。仅当 [OpenLoopOn](OpenLoopOn.md) = 1 时才会使用。

该值会绕过由位置、速度或力控制贡献的所有电流参考，但齿槽补偿（[UPMVelTable](../../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md)）和直流偏置（[CurrRefOffset](../../../02-keywords/09-current-and-voltage/03-current-compensation/CurrRefOffset.md)）除外。它按单个电机分别施加，这意味着不使用解耦矩阵（例如，激励不会跨龙门轴施加）。

## 工作原理

当 [OpenLoopOn](OpenLoopOn.md) = 1 且电机使能时，控制环每个周期使用该值作为电流参考，然后叠加齿槽补偿。闭合的电流环随后将电机相电流调节到该参考，从而使电机产生由该值直接设定的（大致）恒定力/力矩——这对调试投运、摩擦与力检查以及验证电流方向很有用。

幅值以毫安为单位。允许范围跟随驱动器的满量程电流指令（±满量程电流指令），在 frontmatter 中按最大满量程显示为 ±64000 mA；较小的驱动器会钳位到其自身的满量程。

只要 `OpenLoopOn ≠ 1` 或电机被禁用，该值就会被**强制为 0**，因此离开该模式时不会残留任何电流指令。

## 示例

```text
AOpenLoopOn=1        ; enter current open loop
AOpenLoopCurr=1000   ; apply a 1000 mA current reference
```

### 边界情况

- **模式错误**（[OpenLoopOn](OpenLoopOn.md) ≠ 1）——该值**每个周期被强制为 `0`**；电流环不使用它。
- **电机关闭**——每个电机关闭周期该值都被强制为 `0`，因此重新使能电机时绝不会遇到残留指令。
- **写入时处于运动中**——被拒绝（`NOMOTN`）。该关键字可在电机使能时更改（因为开环模式本身需要之后让电机接入），但不可在运动曲线运行期间更改。
- **超出范围**——超出驱动器 ±满量程电流指令的值会被参数表拒绝。
- **龙门**——该值按单个电机施加而不使用解耦矩阵；在龙门中，同一值直接驱动两个成员，没有共模/差模拆分。
- **UPM/齿槽补偿**——即使在开环中也会叠加在 `OpenLoopCurr` 之上，因此当 [UPMVelTable](../../09-current-and-voltage/03-current-compensation/UPMVelTable.md) 非零时，每个周期所指令的电流可能与 `OpenLoopCurr` 不完全一致。
- **直流偏置**——[CurrRefOffset](../../09-current-and-voltage/03-current-compensation/CurrRefOffset.md) 仍会被施加；如果希望以原始值驱动环路，请从 `OpenLoopCurr` 中减去它。
- **保存**——不可保存至闪存；复位后从 `0` 重新开始。
- **平台**——v5 存储为 `float32`（小数毫安）；v4 存储为 `int32`。

## 版本间变更

在 **v5（central-i）** 中，`OpenLoopCurr` 存储为 32 位浮点数而非 v4 的整数，因此可指令小数毫安级的参考；范围和行为在其他方面保持不变。**v5 仅适用于 central-i**——在 standalone 产品上 `OpenLoopCurr` 仍为 v4 整数值。

## 另请参阅

- [OpenLoopOn](OpenLoopOn.md) —— 选择开环点（1 = 电流开环）
- [OpenLoopVolt](OpenLoopVolt.md) —— 电压开环的电压幅值
- [MotorOn](MotorOn.md) —— 必须使能参考才能驱动；禁用会将其强制为 0
