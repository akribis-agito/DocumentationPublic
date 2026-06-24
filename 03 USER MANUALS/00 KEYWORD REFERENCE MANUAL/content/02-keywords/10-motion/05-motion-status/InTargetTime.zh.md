---
keyword: InTargetTime
summary: 在发出到位信号之前，需在整定窗口内持续驻留的最短时间。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 266
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 163840
  default: null
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# InTargetTime

在发出到位信号之前，需在整定窗口内持续驻留的最短时间。

## 概述

`InTargetTime` 是被监控信号的绝对值——[PosErr](../01-kinematics-status/PosErr.md) 或 [Vel](../01-kinematics-status/Vel.md) `[1]`——必须持续保持在整定窗口（[InTargetTol](InTargetTol.md) 或 [InTargetVelTh](InTargetVelTh.md)）内的最短时间，满足该时间后 [InTargetStat](InTargetStat.md) 才会发出到位信号（`InTargetStat = 4`）。

## 工作原理

`InTargetTime` 在内部以**控制器周期（采样点数）**存储和比较，而非毫秒。控制器维护一个驻留计数器：每个连续处于窗口内的控制周期计数器加 1，任意一个超出窗口的周期则将计数器重置为 0；当计数器累计达到所配置的时间后，到位状态即锁定（在位置/速度及电流/力模式下均如此）。

通过指令写入时，数值按 `16.384`（在 16384 Hz 采样率下每毫秒的采样点数）进行换算，因此该关键字以毫秒为单位提供：

$$
\text{samples} = \text{InTargetTime}_{\text{ms}} \cdot 16.384
$$

原始范围为 `0`…`163840` 个采样点（0 至 10 s）。默认值为 `16384 / 256 = 64` 个采样点，约合 **3.9 ms**。值为 `0` 时，到位条件在第一个窗口内周期即触发。该参数保存至闪存，运动中也可修改。

## 示例

```text
AInTargetTime=100    ; 保持整定窗口持续指定时长（ms）
AInTargetTime       ; 读取当前值
```

### 边界情况

- **电机关闭：**值保持不变；状态机处于 `0`，不参与判断。
- **超范围写入：**超出 `0`…`163840` 个采样点（`0`–`10 s`）的值将被**拒绝**，返回错误 14，存储值保持不变；不进行钳位。负值同样被拒绝。
- **仿真模式（`MotorType` = 5）：**行为不变；`PosErr` 为零，因此驻留计数器从第一个控制周期起即开始累加。
- **ModRev 环绕：**无关。
- **活动故障：**轴被禁用；驻留计数器重置。
- **其他运动模式：**驻留适用于所有模式（状态机始终运行，与运动模式无关）。
- **`InTargetTime = 0`：**到位状态在第一个窗口内周期即锁定；适用于整定不是瓶颈的高速点到点应用。
- **运动中实时修改：**允许；新值对后续整定判断生效，但不会重置正在进行中的计数器。

## 另请参阅

- [InTargetStat](InTargetStat.md) — 由该时间门控"到位"状态跳转的整定状态
- [InTargetTol](InTargetTol.md) — 位置整定窗口
- [InTargetVelTh](InTargetVelTh.md) — 速度整定窗口
- [MotionSamples](MotionSamples.md) — 在其 `[3]` 关系中使用该驻留时间
- [PosErr](../01-kinematics-status/PosErr.md) — 在位置/速度模式下被计入窗口驻留的信号
