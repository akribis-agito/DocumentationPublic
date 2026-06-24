---
keyword: EventGap
summary: 按间隔模式下相邻事件之间的位置间距。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 182
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
# EventGap

按间隔模式下相邻事件之间的位置间距。

## 概述

`EventGap` 定义在按间隔事件模式（参见 [EventType](EventType.md)）下，相邻事件生成之间的位置间距（以用户单位表示）。事件从 [EventBegPos](EventBegPos.md) 开始，每隔 `EventGap` 重复一次，直至越过 [EventEndPos](EventEndPos.md)。若 `EventGap` 较小而速度较高，较大的 [EventPulseWid](EventPulseWid.md) 可能导致相邻事件重叠。

## 工作原理

每次按间隔事件触发后，控制器将 `EventGap` 加到最近一次的比较位置，得到下一个比较位置，并将其加载为 [EventNextPos](EventNextPos.md)。窗口方向由 [EventBegPos](EventBegPos.md) 和 [EventEndPos](EventEndPos.md) 确定（参见 [EventEndPos](EventEndPos.md)）；对于正向运行的窗口，应使用正值 `EventGap`。事件位置网格依次为 `EventBegPos`、`EventBegPos + EventGap`、`EventBegPos + 2·EventGap`……，持续在 `EventEndPos` 范围内生成（或在 [EventAlwaysOn](EventAlwaysOn.md) = 1 时无限生成）。

当按间隔生成已使能时，窗口内的事件数量为 |([EventEndPos](EventEndPos.md) - [EventBegPos](EventBegPos.md)) / EventGap| + 1，生成在达到该数量的脉冲后自动停止（除非 [EventAlwaysOn](EventAlwaysOn.md) = 1）。`EventGap` 的符号仅决定比较位置推进的方向，其绝对值设定间距。因此，负值 `EventGap` 使网格向负方向步进，适用于 `EventEndPos` 低于 `EventBegPos` 的窗口。

最大可持续事件频率受 `EventGap` 除以轴速度的限制：当该时间间隔接近发出一个宽度为 [EventPulseWid](EventPulseWid.md) 的脉冲所需时间时，脉冲将开始合并。

## 示例

```text
AEventGap=2000       ; 每隔 2000 用户单位生成一个事件
AEventGap           ; 查询已配置的间距
```

## 另请参阅

- [EventType](EventType.md) — 选择按间隔模式
- [EventBegPos](EventBegPos.md) — 第一个事件的位置
- [EventEndPos](EventEndPos.md) — 生成事件的最后位置
- [EventNextPos](EventNextPos.md) — 下一个比较位置（前一个位置加 EventGap）
- [EventAlwaysOn](EventAlwaysOn.md) — 连续按间隔生成
- [EventPulseWid](EventPulseWid.md) — 脉冲宽度；间距较小时较大的宽度可能导致重叠
