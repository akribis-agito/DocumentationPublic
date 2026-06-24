---
keyword: EventEndPos
summary: 按间隔事件生成停止的边界位置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 183
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EventEndPos

按间隔事件生成停止的边界位置。

## 概述

`EventEndPos` 是按间隔事件模式（参见 [EventType](EventType.md)）中生成事件的边界位置，以用户单位表示。它限定了从 [EventBegPos](EventBegPos.md) 开始、每隔 [EventGap](EventGap.md) 重复的事件序列。`EventEndPos` 不必与实际生成事件的位置重合。超过该位置后，不再产生更多事件，必须切换 [EventOn](EventOn.md) 才能重新启动生成。

## 工作原理

`EventEndPos` 既定义了按间隔窗口的结束，也与 [EventBegPos](EventBegPos.md) 共同确定窗口方向：

- 若 `EventEndPos` 大于 `EventBegPos`，事件沿正方向运行，当比较位置将超过 `EventEndPos` 时停止。
- 若 `EventEndPos` 小于 `EventBegPos`，事件沿负方向运行，当比较位置将低于 `EventEndPos` 时停止。

每次按间隔事件触发后，控制器将下一个比较点按 [EventGap](EventGap.md) 步进，并在被监视方向上与 `EventEndPos` 进行比较；当超过边界时，生成器解除置位（[EventOn](EventOn.md) 返回 `0`）。当 [EventAlwaysOn](EventAlwaysOn.md) = 1 时，跳过此结束检查，使按间隔生成持续运行并忽略 `EventEndPos`。

## 示例

```text
AEventType=1         ; event generation by gap
AEventBegPos=1000
AEventGap=2000
AEventEndPos=8000
AEventOn=1           ; set this while the axis is at a position smaller than EventBegPos
                    ; to prevent unexpected behavior
```

按照上述序列，事件输出在越过位置 1000、3000、5000 和 7000 时，接通持续时间由 [EventPulseWid](EventPulseWid.md) 设定的时长。超过位置 8000 后不再生成更多事件，必须切换 `EventOn` 才能重新启动。

## 另请参阅

- [EventType](EventType.md) — 选择按间隔模式
- [EventBegPos](EventBegPos.md) — 第一个事件的位置
- [EventGap](EventGap.md) — 事件之间的间隔
- [EventAlwaysOn](EventAlwaysOn.md) — 跳过 EventEndPos 以实现连续按间隔生成
- [EventOn](EventOn.md) — 超过 EventEndPos 后必须切换以重新启动
