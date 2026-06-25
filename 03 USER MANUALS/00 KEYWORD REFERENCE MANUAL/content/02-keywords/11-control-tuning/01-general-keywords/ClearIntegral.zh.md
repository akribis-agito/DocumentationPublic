---
keyword: ClearIntegral
summary: 将所寻址轴的速度环积分项清零的指令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 412
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ClearIntegral

将被寻址轴的速度环积分器清零的命令。

## 概述

`ClearIntegral` 将速度控制环积分项的累积状态重置为零。它是一个轴作用域的命令函数。可在电机使能时发出，但不能在轴运动过程中发出。

## 工作原理

收到该命令时，被寻址轴的速度环积分器被设置为 `0`，命令返回成功。此命令不触及任何其他环路状态——位置环积分器、电流环积分器及其他环路状态保持不变。

速度环积分器是由速度积分增益 [VelKi](../04-velocity-control/VelKi.md) 持续累积的运行值。清零操作在命令执行的瞬间移除已累积的值，积分器随后从零开始按有效增益正常累积。

当电机关闭时，控制器也会自动将积分器清零，因此新使能的轴始终以速度积分已清零的状态启动（参见 [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md)）。`ClearIntegral` 在轴使能且静止时按需提供相同的重置功能。

## 示例

```text
AClearIntegral        ; zero the velocity-loop integrator of axis A
```

### 操作流程：在测试运动之间重置速度积分器

常见用法是在连续整定运动之间清除残余积分器状态，使每次运动从相同的初始条件开始。由于 `ClearIntegral` 在轴运动期间会拒绝调用，操作顺序为"停止、清零、指令"。

1. **确认轴已静止**（命令要求无运动）。[MotionStat](../../10-motion/05-motion-status/MotionStat.md) 应读为 `0`：

   ```text
   AMotionStat
   ```

2. **清零积分器**：

   ```text
   AClearIntegral
   ```

3. **验证清零已生效**，在下一个采样周期读取环路下游信号——例如 [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) 将不再携带之前的积分器贡献。

4. **发出下一条指令**。速度环将从零开始重新累积积分。

> **作用域提示。** 此命令仅影响速度环积分器。位置环积分器 [PosKi](../03-position-control/PosKi.md) 和由 [CurrKi](../06-current-control/CurrKi.md) 驱动的两个电流环积分器不受影响——这些积分器仅在电机禁用时重置。

## 另请参阅

- [VelKi](../04-velocity-control/VelKi.md) — 驱动此积分器的速度环积分增益
- [PosKi](../03-position-control/PosKi.md) — 位置环积分增益（不受此命令影响）
- [CurrKi](../06-current-control/CurrKi.md) — 电流环积分增益（不受此命令影响）
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 21-23 报告电流/电压/速度饱和状态（不受此命令影响）
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — 电机关闭时环路积分器自动清零
