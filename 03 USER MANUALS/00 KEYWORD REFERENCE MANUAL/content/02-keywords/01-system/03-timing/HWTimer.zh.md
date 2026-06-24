---
keyword: HWTimer
summary: 用于测量短时间间隔的高分辨率自由运行计数器。
availability:
  standalone: []
  central-i:
  - v5
can_code: 768
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# HWTimer

用于测量短时间间隔的高分辨率自由运行计数器。

## 概述

`HWTimer` 是一个快速、只读的自由运行计数器，用于以亚微秒分辨率对短时间间隔计时。它每微秒大约变化 433 次（大约每 1/433 µs 计数一次）。该计数器**递减**计数，因此在两个时刻读取它，并用较晚的读数减去较早的读数，即可得到两个事件之间的经过时间。计数器在约 9.9 秒后环绕，因此仅适用于短间隔；对于更长或粗粒度的计时请使用 [Time](Time.md)，对于以整个控制周期计数请使用 [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md)。

`HWTimer` 仅存在于 central-i 平台（固件 v5）上。

## 工作原理

`HWTimer` 不是固件维护的软件计数器；读取它返回的是一个以约 433 MHz 连续递减计数的自由运行硬件定时器的当前值，这就是它能提供远高于一秒 [Time](Time.md) 滴答或每周期计数器分辨率的原因。读数本身没有固定含义；它只有作为两次读数之差时才有用。

由于定时器递减计数，较早的（起始）读数是两者中较大的一个。要将两次读数之差转换为时间：

$$
\Delta t\ [\mu\text{s}] = \dfrac{\text{HWTimer}_{\text{start}} - \text{HWTimer}_{\text{end}}}{433}
$$

由于该值是 32 位计数，它在约 $2^{32} / (433 \cdot 10^6) \approx 9.9$ 秒后回绕。只要被测间隔短于此值，且减法以 32 位环绕算术执行，两次读数之间的单次回绕仍能得到正确的差值。超过一个完整环绕周期的间隔无法用 `HWTimer` 测量。

## 示例

```text
AHWTimer            ; read the counter at event A, again at event B, then subtract
```

在短操作之前和之后立即读取 `AHWTimer`；用较晚的读数减去较早的读数，再除以 433，即可得到以微秒为单位的持续时间。

## 参见

- [Time](Time.md) — 自上电以来的秒数（粗粒度，一秒分辨率）
- [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md) — 基于周期的计数器
