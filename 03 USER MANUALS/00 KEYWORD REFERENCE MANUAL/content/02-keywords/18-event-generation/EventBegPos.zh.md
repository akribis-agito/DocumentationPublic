---
keyword: EventBegPos
summary: 单次事件和按间隔模式中第一个生成事件的位置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 181
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EventBegPos

单次事件和按间隔模式中第一个生成事件的位置。

## 概述

`EventBegPos` 是单次事件和按间隔事件模式（参见 [EventType](EventType.md)）中第一个生成事件的位置，以用户单位表示。在按间隔模式下，它是起始位置，后续事件从该位置起每隔 [EventGap](EventGap.md) 排列，直至 [EventEndPos](EventEndPos.md)。为确保正确行为，应在轴位于运动方向上 `EventBegPos` 之前的位置时置位 [EventOn](EventOn.md)。

## 工作原理

置位 [EventOn](EventOn.md) 时，`EventBegPos` 作为第一个比较位置被加载，并在 [EventNextPos](EventNextPos.md) 中报告。它还设置了生成器所监视的预期运动方向：

- 在**单次事件**模式下，方向由当前位置相对于 `EventBegPos` 的关系确定：若轴位于 `EventBegPos` 以下，引擎等待向上越过；否则等待向下越过。
- 在**按间隔**模式下，方向由 [EventEndPos](EventEndPos.md) 相对于 `EventBegPos` 的关系确定：若 `EventEndPos` 大于 `EventBegPos`，窗口沿正方向运行；否则沿负方向运行。这允许按间隔窗口在任一方向的运动中定义。

若在轴已沿被监视方向越过 `EventBegPos` 之后才置位，可能导致第一个事件被遗漏或立即触发，因此应在到达 `EventBegPos` 之前完成置位。

## 示例

```text
AEventBegPos=1000    ; first event at position 1000 (user units)
AEventBegPos        ; query the configured start position
```

## 另请参阅

- [EventType](EventType.md) — 选择单次事件、按间隔或表模式
- [EventGap](EventGap.md) — 按间隔模式中事件之间的间隔
- [EventEndPos](EventEndPos.md) — 生成事件的最后位置；其相对于 EventBegPos 的符号决定按间隔方向
- [EventNextPos](EventNextPos.md) — 报告已加载的第一个比较位置
- [EventOn](EventOn.md) — 置位事件生成
