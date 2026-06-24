---
keyword: CounterDown
summary: 两个独立的减计数器，每个控制器周期递减一次。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 39
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
# CounterDown

两个独立的减计数器，每个控制器周期递减一次。

## 概述

`CounterDown` 提供两个独立的通用减计数器，`CounterDown[1]` 和 `CounterDown[2]`。（该数组按三个元素定维，因此可用索引从 `[1]` 开始；索引 `[0]` 不使用。）每个计数器在上电时从 0 开始，当其大于 0 时，在每个控制周期递减 1。到达 0 后，计数器保持为 0——它停止，不会环绕也不会变为负值。它们为读/写，因此用户程序可写入一个起始值，然后监视计数器何时到达 0。

## 工作原理

这两个计数器在控制中断内一起递减，与固件维护其他周期性定时器的位置相同。控制中断以**每秒 16384 次采样**运行（每 61.04 µs 一个时钟节拍），因此写入计数器的值会在 (value / 16384) 秒内耗尽。每个计数器都受到保护，只在为正时递减；一旦到达 0，它便保持在那里，直到再次写入。

这使 `CounterDown` 成为用户程序内部一个便捷的自清零定时器或延时器：写入要等待的周期数，然后测试计数器是否为 0，以检测该间隔是否已经过去。

实例：

- `ACounterDown[1] = 16384` 恰好倒计时一秒。
- `ACounterDown[1] = 16` 倒计时约 1 ms（16 / 16384 ≈ 977 µs）。
- `ACounterDown[1] = 1000` 倒计时约 61 ms（1000 / 16384 ≈ 0.061 s）。

如需一秒分辨率的墙钟计时，请使用 [Time](Time.md)；如需亚微秒级间隔，请使用 [HWTimer](HWTimer.md)；如需递增的自由运行计数，请使用 [CounterUp](CounterUp.md)。

## 示例

```text
ACounterDown[1]=16384 ; count down 16384 control cycles (exactly 1 second)
ACounterDown[1]       ; read the remaining count; 0 means the interval has elapsed
ACounterDown[2]=820   ; second, independent down-counter (about 50 ms; 820 / 16384 ≈ 0.050 s)
```

## 另见

- [CounterUp](CounterUp.md) — 基于周期的加计数器
- [Time](Time.md) / [HWTimer](HWTimer.md) — 墙钟定时器与高分辨率定时器
