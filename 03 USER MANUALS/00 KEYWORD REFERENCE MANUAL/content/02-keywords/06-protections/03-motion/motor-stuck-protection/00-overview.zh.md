# 电机堵转保护

电机堵转保护通过在一段时间内比较电流与速度来工作。当速度低于设定阈值且电流高于设定阈值，并持续设定的时间时，即发生堵转。如果发生堵转，轴将被禁用，并在 [ConFlt](../../../07-status-and-faults/ConFlt.md) 上报告错误码（ConFlt 码 1007）。

堵转检查的判据：

- $abs(\text{Vel}\lbrack 3\rbrack)\ \le\ \text{StuckVel}$，**且**

- $abs(\text{MotorCurr})\ \ge\ \text{StuckCurr}$

持续 [StuckTime](StuckTime.md) 个控制采样周期。

这意味着轴正在施加力却没有运动。该检查在一段时间内进行，以确保堵转持续存在，并防止在加速或减速期间发生误检测。

## 操作演示：配置并验证一次堵转跳闸

捕捉水平工作台机械卡死的典型设置：

```text
AStuckCurr[1]=4000      ; treat >= 4 A as "drive is pushing hard"
AStuckVel[1]=40000      ; treat <= 40000 user units/s as "not moving"
AStuckTime[1]=250       ; require 250 ms of unbroken stuck condition
```

将轴驱动至机械硬限位或模拟一次卡死：

```text
ABegin                  ; start the move
; ... obstruction encountered ...
AConFlt                 ; expect 1007 (motor stuck) after StuckTime elapses
AMotionReason           ; expect 8 (motor disabled)
```

如果跳闸始终未触发，说明 AND 条件未被持续满足：要么 `StuckCurr` 太高（驱动器实际从未推得那么用力），要么 `StuckVel` 太低（滤波后的速度 `Vel[3]` 仍在阈值之上略微漂移）。如果跳闸在正常加减速期间触发，请增大 `StuckTime` 或降低 `StuckCurr`。对于步进电机以及 Current/Force/自动定相/电机学习模式，堵转检测被**绕过**；在这些模式下请勿依赖它。

## 另请参阅

- [StuckCurr](StuckCurr.md) — AND 条件中的电流阈值部分
- [StuckVel](StuckVel.md) — AND 条件中的速度阈值部分
- [StuckTime](StuckTime.md) — 要求的持续时长
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 跳闸时的故障码 1007
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — 跳闸时记录的原因 8（电机失能）
