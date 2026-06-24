---
keyword: Time
summary: 只读，自上电以来经过的秒数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 41
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
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
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# Time

只读，自上电以来经过的秒数。

## 概述

`Time` 保存自控制器上电（或复位）以来经过的整秒数。它是只读的、单元范围（非轴）、不保存至闪存，并在每次上电时复位为 0。可用它进行粗粒度、秒分辨率的时间戳或经过时间检查。要以亚微秒分辨率测量短间隔请使用 [HWTimer](HWTimer.md)；要进行周期精确计数请使用 [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md)。

`Time` 是错误日志的时间戳来源：[ErrLog](../../07-status-and-faults/ErrLog.md) 中的每个条目都会在错误码旁存储一份 `Time`（自上电以来的秒数）的副本。

## 工作原理

控制中断以固定采样率（每秒 16384 个采样）运行。一个自由运行的采样累加器在控制环内推进，当它达到相当于一秒的采样数时，累加器被清零，`Time` 加 1。由于该递增由采样时钟驱动，分辨率恰好为一秒，且在该上电周期的生命期内计数是单调的。

秒计数簿记并非在 16384 个周期的每一个上完成。每次控制中断中非时间关键的部分运行一个轮询，依次步进 16 个子阶段，每周期推进一个阶段，每 16 个周期环绕一次。秒累加器仅在其中一个阶段上推进，每次运行时 +16（因此每秒仍累计 16384），并在达到 16384 时使 `Time` 翻转。这样每秒得到 16384 / 16 = 1024 个累加步，即秒计数器的有效滴答约为一毫秒，尽管底层采样时钟为 16384 Hz。相比之下，每控制周期计数器 [CounterUp](CounterUp.md) 和 [CounterDown](CounterDown.md) 在每一个周期上都无条件推进，因此它们保留完整的 16384 Hz 分辨率。

`Time` 是有符号 32 位值。每秒递增一次的话，要逼近其正向最大值（2147483647）需要数十年量级的连续运行时间，因此回绕在实际中无需担心。

关于精度的说明：`Time` 通过计数控制器自身的控制环采样（16384 个标称采样 = 一秒）来测量经过的秒数，而不是对照单独的实时时钟。物理采样率略快于标称的 16384 Hz：实测速率为 16386.8 Hz，即标称值比真实速率低，比例为 16384 / 16386.8 = 0.999829131（时钟快约 0.0171 %）。由于 `Time` 无论真实速率如何都每 16384 个采样递增一次，它以相同的比例比真实墙钟时间推进得更快，每真实日大约多算 14–15 秒（≈ 14.77 s/day）。该误差很小但会随长时间运行累积，因此 `Time` 适用于相对经过时间测量和粗粒度时间戳，但不应在长时间段内作为精确的绝对时钟依赖。

实例计算（运行时间换算）：

| `Time` value | Elapsed run-time |
|-------------:|------------------|
| 60           | 1 分钟           |
| 3600         | 1 小时           |
| 86400        | 1 天             |
| 604800       | 1 周             |
| 2147483647   | ≈ 68 年（有符号 32 位最大值） |

## 示例

```text
ATime               ; seconds since power-on (e.g. 86400 -> 1 day of uptime)
```

通过在操作之前和之后读取 `ATime` 并相减，以一秒分辨率测量某操作耗时。

## 参见

- [HWTimer](HWTimer.md) — 高分辨率（亚微秒）间隔定时器
- [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md) — 基于周期的计数器
- [ErrLog](../../07-status-and-faults/ErrLog.md) — 用 `Time` 为每个条目打时间戳的错误日志
