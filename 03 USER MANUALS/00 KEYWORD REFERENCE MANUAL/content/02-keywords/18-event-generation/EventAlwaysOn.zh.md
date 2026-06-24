---
keyword: EventAlwaysOn
summary: 使按间隔事件生成持续运行，不在 EventEndPos 处停止。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 619
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EventAlwaysOn

使按间隔事件生成持续运行，不在 EventEndPos 处停止。

## 概述

`EventAlwaysOn` 为按间隔事件生成（[EventType](EventType.md) = 1）选择连续（"无限"）运行模式。它**不会**强制输出电平为高；它改变的是引擎*停止*的时机。在正常（窗口）运行模式下，按间隔脉冲在位置超过 [EventEndPos](EventEndPos.md) 后停止。当 `EventAlwaysOn = 1` 时，生成器持续每隔 [EventGap](EventGap.md) 产生一个脉冲，不会到达结束位置，因此只要 [EventOn](EventOn.md) 保持置位，它就持续运行。

此设置仅适用于按间隔模式。单次事件、表、硬件表和立即触发方案不受 `EventAlwaysOn` 影响。

## 工作原理

| 值 | 按间隔行为 |
|-------|-----------------|
| 0 | 窗口模式：脉冲从 [EventBegPos](EventBegPos.md) 开始运行，超过 [EventEndPos](EventEndPos.md) 后停止；[EventOn](EventOn.md) 返回 `0`。 |
| 1 | 连续模式：脉冲每隔 [EventGap](EventGap.md) 重复，无结束位置；生成持续到 [EventOn](EventOn.md) 被清除。 |

当 `EventAlwaysOn = 1` 时，控制器在 [EventOn](EventOn.md) `0 → 1` 边沿以连续模式置位按间隔引擎，从而跳过通常会终止生成的结束位置检查。若要使其对下次运行生效，请在置位前更改 `EventAlwaysOn`。实际输出状态可通过 [EventLoopback](EventLoopback.md) 读回。

`EventAlwaysOn` 是保存至闪存的轴相关参数，可随时更改。

## 示例

```text
AEventType=1         ; by-gap mode
AEventBegPos=1000
AEventGap=500
AEventAlwaysOn=1     ; run continuously, ignoring EventEndPos
AEventOn=1           ; arm (set while below EventBegPos)
AEventAlwaysOn=0     ; return to windowed by-gap operation
AEventAlwaysOn      ; query the current setting
```

## 另请参阅

- [EventType](EventType.md) — 受影响的按间隔模式（值 1）
- [EventGap](EventGap.md) — 连续脉冲之间的间隔
- [EventEndPos](EventEndPos.md) — 当 EventAlwaysOn = 1 时被跳过的窗口结束位置
- [EventOn](EventOn.md) — 置位以启动生成；清除以停止连续输出
- [EventLoopback](EventLoopback.md) — 读回实际输出状态
