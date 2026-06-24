---
keyword: CounterUp
summary: 两个独立的加计数器，每个控制器周期递增一次。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 40
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CounterUp

两个独立的加计数器，每个控制器周期递增一次。

## 概述

`CounterUp` 提供两个独立的通用加计数器，`CounterUp[1]` 和 `CounterUp[2]`。（该数组按三个元素定维，因此可用索引从 `[1]` 开始；索引 `[0]` 不使用。）每个计数器在上电时从 0 开始，在每个控制周期递增 1。它们为读/写，因此用户程序可随时预置或复位任一计数器，然后稍后读取它，以控制周期为单位对事件进行计数或计时。

## 工作原理

这两个计数器在控制中断内一起推进，与固件维护其他周期性定时器的位置相同。控制中断以**每秒 16384 次采样**运行（每 61.04 µs 一个时钟节拍），因此每个计数器在每秒运行时间内增加 16384。向上计数是无界限的：到达有符号 32 位最大值（2147483647）时，计数器环绕至 −2147483648 并继续递增。

实例：

- 经过一秒的时间 = 16384 个控制周期。
- 一毫秒 ≈ 16 个控制周期（16384 / 1000 ≈ 16.4）。
- 一个从 0 开始自由运行的 `CounterUp[1]`，在约 2147483647 / 16384 / 86400 ≈ 1.5 天的运行时间后到达 2 147 483 647，然后环绕至 −2147483648。

典型用途：

- 将计数器复位为 0，执行某项操作，然后读取计数器以测量其耗费了多少个控制周期（每个 61.04 µs）。
- 预置一个计数器并监视其到达目标值，作为用户程序内部一个简单的已经过周期触发器。

如需一秒分辨率的墙钟计时，请使用 [Time](Time.md)；如需亚微秒级间隔，请使用 [HWTimer](HWTimer.md)；如需*向下*计数到目标值，请使用 [CounterDown](CounterDown.md)。

## 示例

```text
ACounterUp[1]       ; read the first up-counter
ACounterUp[1]=0     ; reset the first up-counter, then read it later to measure elapsed cycles
ACounterUp[2]       ; read the second, independent up-counter
```

例如，如果复位后 `ACounterUp[1]` 读取为 `16384`，则恰好经过了一秒的运行时间。

## 另见

- [CounterDown](CounterDown.md) — 基于周期的减计数器
- [Time](Time.md) / [HWTimer](HWTimer.md) — 墙钟定时器与高分辨率定时器
