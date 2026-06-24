---
keyword: EventOn
summary: 使能事件生成；加载第一个比较位置，与 Lock 互斥。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 178
attributes:
  access: rw
  scope: axis
  flash: false
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EventOn

使能事件生成；加载第一个比较位置，与 Lock 互斥。

## 概述

`EventOn = 1` 使能位置比较引擎：控制器加载第一个比较位置（根据 [EventType](EventType.md)），并开始监测反馈位置，每当跨越一个已配置的比较位置时触发输出脉冲。应在轴位于第一个请求事件之前的位置时设置（正向运动时小于 [EventBegPos](EventBegPos.md)），以防止意外行为。

使能为 `0 → 1` 边沿触发：在已为 `1` 时写入 `EventOn = 1` 不起任何作用。`0 → 1` 跳变会将 [EventCntr](EventCntr.md) 复位为 `0`（在独立产品上，还会清除位置捕获使能，因为两者共用同一引脚）。

## 工作原理

### 使能（0 → 1）

当 `EventOn` 从 `0` 跳变至 `1` 时，控制器执行以下操作：

1. 将 [EventCntr](EventCntr.md) 复位为 `0`。
2. 根据 [EventType](EventType.md) 设置的方案选择第一个比较位置：单次事件和按间隔模式选择 [EventBegPos](EventBegPos.md)，表模式选择第一个表项（起始索引）。
3. 确定预期运动方向——单次事件模式根据当前位置相对于 [EventBegPos](EventBegPos.md) 确定；按间隔模式根据 [EventEndPos](EventEndPos.md) 相对于 [EventBegPos](EventBegPos.md) 确定（因此窗口可双向运行）；表模式在引擎推进时逐项确定方向。
4. 根据 [EventPulseWid](EventPulseWid.md) 配置输出脉冲形状，根据 [EventSelect](EventSelect.md) / [EventTableSel](EventTableSel.md) 配置路由，加载第一个比较位置，并启动比较单元。

第一个比较位置在 [EventNextPos](EventNextPos.md) 中报告。

### 每周期比较 → 触发 → 推进

使能后，引擎在每个控制周期将反馈位置与 [EventNextPos](EventNextPos.md) 进行比较。当位置在预期方向上到达比较点时，触发输出脉冲，[EventCntr](EventCntr.md) 递增，并准备下一个比较位置：

- **单次事件** — 生成停止；`EventOn` 返回 `0`。
- **按间隔** — 比较点按 [EventGap](EventGap.md) 推进。生成持续直至比较点越过 [EventEndPos](EventEndPos.md)，然后停止，`EventOn` 返回 `0`（除非由 [EventAlwaysOn](EventAlwaysOn.md) 强制连续运行）。
- **按表** — 引擎步进至下一个表项，并从 [EventTableSel](EventTableSel.md) 重新加载 [EventSelect](EventSelect.md)。最后一项完成后，生成停止，`EventOn` 返回 `0`。

对于增量式（或 SIN-COS）编码器，比较和脉冲由硬件完成，因此脉冲精确地放置在跨越点；控制器仅在每个周期处理记录工作。对于绝对式或其他非增量式编码器，比较在固件中每个控制周期针对反馈位置执行一次，因此时序受限于控制周期精度。

### 与 Lock 的互斥关系（仅限独立产品）

在独立产品上，位置比较输出和位置捕获触发（[LockEn](../03-encoder/03-event-based-feedback-logging/LockEn-AuxLockEn.md)）共用同一硬件引脚，因此两者不能同时激活。使能 `EventOn = 1` 会自动清除 `LockEn`，使能 `LockEn` 也会自动清除 `EventOn`。此限制不适用于 Central-i 产品，在 Central-i 产品上两项功能使用远程驱动器中独立的硬件。

## 示例

```text
AEventOn=1           ; 使能事件生成（在第一个事件位置之前设置）
AEventOn=0           ; 禁用事件生成
AEventOn            ; 查询当前状态
```

## 另请参阅

- [EventType](EventType.md) — 决定首先加载的位置
- [EventNextPos](EventNextPos.md) — 使能时报告下一个比较位置
- [EventCntr](EventCntr.md) — 在 0 → 1 使能边沿时复位为 0
- [EventAlwaysOn](EventAlwaysOn.md) — 强制连续（无限）按间隔生成
- [LockEn](../03-encoder/03-event-based-feedback-logging/LockEn-AuxLockEn.md) — 位置捕获；在独立产品上共用同一引脚
