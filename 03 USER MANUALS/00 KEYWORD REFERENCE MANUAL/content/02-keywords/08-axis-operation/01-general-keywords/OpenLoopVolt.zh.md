---
keyword: OpenLoopVolt
summary: 电压开环模式下施加到调制的电压参考。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 146
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: scaling
  range: null
  default: 0
  scaling: 1.144
  implemented: final
overrides:
  central-i.v4:
    scaling: 1.526
  central-i.v5:
    data_type: float32
    scaling: 1.526
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# OpenLoopVolt

电压开环模式下施加到调制的电压参考。

## 概述

`OpenLoopVolt` 是在轴处于电压开环条件下时施加到 PWM 调制的电压幅值。仅当 [OpenLoopOn](OpenLoopOn.md) = 2 时才会使用，并且它会完全绕过电流控制环。

> **注意：** 如果您的应用中需要此功能，请联系 Agito 获取更多信息。

## 工作原理

当 [OpenLoopOn](OpenLoopOn.md) = 2 且电机使能时，控制器**仅向相 A 注入一个正弦波**，相 B 和相 C 保持为零。相位每个周期以 [InjectFreq](../../13-injection/InjectFreq.md) 设定的速率推进。由于电流环被绕过，这会直接以已知的电压波形激励电机绕组。

主要用途是**电机电阻与电感（R/L）测量**：控制器假定频率足够高以致转子几乎不动，且幅值足够小以免汲取过大电流。为强制满足后者，该值为 PWM 缩放（单位 `scaling`），并被**限制在最大 20 % PWM**；最小值为 `0`。超过上限的写入会被拒绝为超出范围，而不是被钳位。frontmatter 显示 `range: null`，因为绝对限值取决于驱动器的 PWM 周期。

只要 `OpenLoopOn ≠ 2` 或电机被禁用，该值就会被**强制为 0**，因此离开该模式时不会残留任何激励。

## 示例

```text
AOpenLoopOn=2        ; enter voltage open loop
AOpenLoopVolt=500    ; set the injection amplitude (PWM scaling, capped at 20%)
```

### 边界情况

- **模式错误**（[OpenLoopOn](OpenLoopOn.md) ≠ 2）——该值**每个周期被强制为 `0`**；调制器不使用它。
- **电机关闭**——每个电机关闭周期该值都被强制为 `0`。
- **写入时处于运动中**——被拒绝（`NOMOTN`）。
- **超过 20 % PWM**——超过 20 % PWM 上限的值会被拒绝（超出范围）；写入不生效，保留先前的值。
- **负值**——被拒绝；该参数仅接受非负幅值。
- **缺少频率**——未设置 [InjectFreq](../../13-injection/InjectFreq.md) 时，所注入的正弦波不会推进：相位停留在零，因此相 A 被保持在 `0`，不产生激励。
- **相 B/C**——保持在 `0`；该注入设计上为单相，因此电机几乎不动。
- **仿真**——被接受；在仿真的相 A 上产生纯数值激励。
- **保存**——不可保存至闪存；复位后从 `0` 重新开始。
- **平台**——v5 存储为 `float32` 并使用远程 PWM 缩放因子；v4 存储为 `int32`。20 % 上限保持不变。

## 版本间变更

在 **v5（central-i）** 中，`OpenLoopVolt` 存储为 32 位浮点数而非 v4 的整数，并使用远程 PWM 缩放因子；20 % PWM 上限和相 A 正弦波行为保持不变。**v5 仅适用于 central-i**——在 standalone 产品上 `OpenLoopVolt` 仍为 v4 整数值。

## 另请参阅

- [OpenLoopOn](OpenLoopOn.md) —— 选择开环点（2 = 电压开环）
- [OpenLoopCurr](OpenLoopCurr.md) —— 电流开环的电流参考
- [InjectFreq](../../13-injection/InjectFreq.md) —— 设定所注入电压正弦波的频率
- [MotorOn](MotorOn.md) —— 必须使能才能激励；禁用会将幅值强制为 0
