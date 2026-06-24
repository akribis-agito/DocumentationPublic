---
keyword: PDEndTime
summary: PDPos 和位置参考停止变化后的到位检查延迟时间（ms）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 414
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
  default: 16
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PDEndTime

PDPos 和位置参考停止变化后的到位检查延迟时间（ms）。

## 概述

`PDEndTime` 是脉冲方向输入和生成的位置参考均停止变化后，控制器开始检查到位状态 [InTargetStat](../05-motion-status/InTargetStat.md) 之前必须等待的时间，单位为毫秒。由于直接和间接脉冲方向运动只要持续接收指令就会保持运动状态，此延迟可防止在脉冲流短暂暂停时过早报告到位。该延迟适用于直接（[MotionMode](../02-motion-configuration/MotionMode.md) = 3）和间接（`MotionMode` = 4）P/D 运动。

## 工作原理

到位检查在 P/D 运动期间每个控制周期运行一次：

- 当 P/D 增量和参考微分均为零时，内部计数器递增。一旦达到 `PDEndTime`，到位检查开始（`InTargetStat` 从"运动中"切换至"等待目标时间"，然后按常规评估 [InTargetTol](../05-motion-status/InTargetTol.md)/`InTargetTime`）。
- 如果输入或参考*任一*再次变化，计数器重置为 0，`InTargetStat` 返回"运动中"。

`PDEndTime` **在内部以控制采样数存储**，但与上位机**以毫秒交换**：该关键字具有采样数到毫秒的缩放（16.384 采样/ms），因此读写时使用 ms，而比较计数器以采样数计数。默认内部值为 16 采样（≈ 1 ms）；最大值为 10 s。

## 示例

```text
APDEndTime=1         ; wait ~1 ms of no change before checking settling (default)
APDEndTime=50        ; wait 50 ms of no change
APDEndTime          ; read the current value (ms)
```

## 另请参阅

- [InTargetStat](../05-motion-status/InTargetStat.md) — 在此延迟后检查的到位状态
- [PDPos](PDPos.md) — 其变化（通过 P/D 增量）重置计时器的计数器
- [MotionMode](../02-motion-configuration/MotionMode.md) — 适用于直接（3）和间接（4）P/D 运动
