---
keyword: EventOn
summary: 使能所选事件模式；已验证硬件表必须先显式预加载。
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
last_updated: '2026-10-25'
doc_revision: '2026.10'
language: zh-CN
---
# EventOn

使能事件生成；加载第一个比较位置，与 Lock 互斥。

## 已验证硬件事件表（EventType=3，且由 EventLoad 会话占用）

已验证表会话占用轴时，必须先由 [EventLoad](EventLoad.zh.md) 建立当前会话，并获得远程验证后的 Ready。写入 1 仅请求 ARM，不加载表、不重新学习偏移、不回退软件模式。设置回调不会隐式使能。ARM 待完成时 EventOn 保持 0，仅在匹配会话的新鲜 Armed/Running 确认后为 1；拒绝返回错误 151，原因见 [EventError](EventError.zh.md)。写入 0 请求 [EventAbort](EventAbort.zh.md)，并不直接证明远程清理完成。使能或运行已占用引擎时，重复使能被拒绝而不重新开始。Complete 需要全部目标及末脉冲完成。配置或原点改变会使捕获会话失效，须恢复并重新加载；下文传统坐标保持行为不适用于此模式。EventCntr 在加载被接受时清零，不在使能时隐式上传表。

下文的传统行为也适用于没有已验证表会话占用轴时的 EventType=3。已验证表能力仅限制 EventLoad，不限制传统硬件表使能。

## 传统硬件表使能

没有已验证表会话占用轴时，EventType=3 且 EventOn=1 使用下文所述的传统硬件表路径。使用增量编码器或已使能的硬件 SinCos 源时，在使能时传输所选表；其他源配置保持其原有传统行为。即使没有已验证表能力，此路径仍可用，但不具备已验证会话状态或完整性保证。传输、恢复或错误中的会话仍占用轴，不会静默切换到传统路径。

## 概述

`EventOn = 1` 使能位置比较引擎：控制器加载第一个比较位置（根据 [EventType](EventType.md)），并开始监测反馈位置，每当跨越一个已配置的比较位置时触发输出脉冲。应在轴位于第一个请求事件之前的位置时设置（正向运动时小于 [EventBegPos](EventBegPos.md)），以防止意外行为。

使能为 `0 → 1` 边沿触发：在已为 `1` 时写入 `EventOn = 1` 不会重新启动序列。该写入仍会执行下述有限按间隔配置检查；检查失败时，命令返回错误 14，并保留当前 `EventOn` 值。更改窗口或间隔前，请先禁用事件生成。`0 → 1` 跳变会将 [EventCntr](EventCntr.md) 复位为 `0`（在独立产品上，还会清除位置捕获使能，因为两者共用同一引脚）。

## 工作原理

### 使能（0 → 1）

对于有限的按间隔事件序列（`EventType = 1`、`EventAlwaysOn = 0`），`EventGap` 必须非零，且应从 `EventBegPos` 向 `EventEndPos` 推进：正向窗口使用正间隔，负向窗口使用负间隔。间隔为零或方向背离终点时，`EventOn = 1` 将被拒绝并返回错误 **14**；尚未使能的序列保持未使能，已配置的位置和间隔保留，便于修正。例如，起点为 `20000`、终点为 `200` 时，应使用 `-100` 等负间隔；`+100` 将被拒绝。此检查不改变单次事件、表格事件或无限模式的使能方式。

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

### Central-i 使能期间的坐标变更

`SetPosition` 和 `ZeroPosErr` 保持已经使能的硬件事件序列的物理目标位置，包括之后下发的表项。该事件序列继续运行时，锁存捕获可以使用新原点。下一次 `EventOn` 从 `0` 跳变至 `1` 时，新序列使用当前坐标系：模式 0 重新测定硬件偏移，模式 1 使用已初始化并随 `SetPosition` 和 `ZeroPosErr` 更新的偏移。在已经使能时再次写入 `1` 不会重新对齐。

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
