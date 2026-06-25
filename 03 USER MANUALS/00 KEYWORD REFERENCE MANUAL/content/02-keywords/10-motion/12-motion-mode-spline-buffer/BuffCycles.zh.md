---
keyword: BuffCycles
summary: 样条缓冲轨迹的重复执行次数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 548
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BuffCycles

样条缓冲轨迹的重复执行次数。

## 概述

`BuffCycles` 设置样条缓冲轨迹在执行时的回放次数。有效范围为 1 到 2147483647，默认值为 1（单次执行）。该值从样条缓冲组的**主轴**读取。可通过 [StopBuff](../04-motion-command/StopBuff.md) 提前结束正在运行的运动。`BuffCycles` 保存至闪存，可随时修改。

## 工作原理

### 回放期间的周期计数

由 [BuffCalc](BuffCalc.md) 扩展生成的轨迹为一个周期。运动过程中，控制器为每个组维护一个周期计数器及周期内索引，均通过 [BuffStatus](BuffStatus.md) 报告：

- 每个控制周期，回放索引递增一次。当其超过该周期最后一个插值点时，索引回绕至第一个点，周期计数器加一。
- 当周期计数器超过 `BuffCycles` 时运动结束，即完成 `BuffCycles` 个完整周期后停止。此时控制器清除所有成员轴的运动中状态，运动正常结束。

由于路径点位置是**相对于每个周期起始点**应用的，重复周期将首尾相连：若轨迹的最后一个路径点与第一个不同，则每次重复将从上一次结束处继续（每周期净推进量），而非跳回原点。例如，若 `BuffPos` 在一个周期内从 `0` 变化至 `5000`，且 `BuffCycles = 4`，则轴每周期推进 `5000` 用户单位，最终超出 `Begin` 时捕获位置 `20000` 用户单位。

### 提前结束

[StopBuff](../04-motion-command/StopBuff.md) 不会在周期中途中断运动；它请求在**下一个周期边界**处结束运动，采用与 `BuffCycles` 耗尽时相同的周期结束路径。这保持了轨迹的连续性。结束原因以 [MotionReason](../05-motion-status/MotionReason.md) = 35 报告。

## 示例

```text
ABuffCycles=1        ; 轨迹执行一次（默认）
ABuffCycles=10       ; 轨迹重复十次，首尾相连
```

## 另请参阅

- [BuffCalc](BuffCalc.md) — 扩展生成一个周期的轨迹
- [BuffStatus](BuffStatus.md) — 报告实时周期计数器及周期内索引
- [BuffPos](BuffPos.md) — 路径点位置（相对于每个周期起始点应用）
- [StopBuff](../04-motion-command/StopBuff.md) — 在下一个周期边界处结束回放
