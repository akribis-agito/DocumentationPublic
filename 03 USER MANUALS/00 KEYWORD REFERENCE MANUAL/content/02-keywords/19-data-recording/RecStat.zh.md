---
keyword: RecStat
summary: 报告每个示波器的记录状态。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 249
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 5
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RecStat

报告每个示波器的记录状态。

## 概述

`RecStat` 报告每个示波器的记录状态，使上位机能够在调用 [RecUpload](RecUpload.md) 之前跟踪从触发前填充到完成的整个进度。它是 [RecStart](RecStart.md) / [RecStop](RecStop.md) 命令的读回对应量。每个数组索引对应一个示波器。

| 索引 | 说明                         |
|-------|------------------------------|
| 1     | 第一个示波器                 |
| 2     | 第二个示波器（如适用）       |

## 工作原理

`RecStat` 返回的值定义如下。

| 值 | 状态 |
|----|----|
| 0 | 记录数据无效（上电后的默认状态） |
| 1 | 示波器正在填充触发前数据，由 RecTrigPos 定义 |
| 2 | 触发前数据已填满。示波器正在缓冲并等待触发。 |
| 3 | 已检测到触发，记录正在进行。 |
| 4 | 记录已无中断地完成。 |
| 5 | 记录已停止。 |
| 6 | 在检测到触发前记录已停止。 |

例如，若 RecStat\[1\] 返回值 4，表示第一个示波器记录成功，用户可开始流式传输已记录数据。

正常进度为 1 → 2 → 3 → 4：

- [RecStart](RecStart.md) 将示波器置于 **1**，在忽略触发事件的同时以滚动缓冲区填充 [RecTrigPos](RecTrigPos.md) 设定的触发前部分。
- 积累足够的触发前采样点后，示波器进入 **2**，并开始对每个记录采样评估触发条件。
- 触发发生后（或通过 [RecTrigForce](RecTrigForce.md) 强制触发），示波器前进至 **3** 并倒计数触发后采样点。
- 所有触发后采样点捕获完毕后，示波器稳定在 **4**，可上传数据。

触发前和触发后部分合计始终等于每个记录通道 [RecLength](RecLength.md) 个采样点。触发发生时，示波器为每个通道捕获固定数量的触发后采样点（等于 [RecLength](RecLength.md) 减去 [RecTrigPos](RecTrigPos.md) 设定的触发前采样点），然后稳定在状态 4，因此无论示波器在状态 2 等待多长时间，完成的捕获每通道恰好跨越 [RecLength](RecLength.md) 个点。对于无触发启动（[RecTrigTyp](RecTrigTyp.md) = 0，直接跳至状态 3），每通道的完整 [RecLength](RecLength.md) 均作为触发后数据记录。

若未配置触发，`RecStart` 直接跳至 **3**。[RecStop](RecStop.md) 在中断已触发的记录时产生 **5**，在触发前中断时产生 **6**。**4**、**5** 和 **6** 均为"完成"状态，[RecUpload](RecUpload.md) 均可运行（状态 6 无有效触发数据，上传时将报告为错误）。

## 示例

```text
ARecStat[1]         ; 查询第一个示波器的记录状态
```

## 另请参见

- [RecStart](RecStart.md) — 启动记录
- [RecStop](RecStop.md) — 停止记录
- [RecTrigPos](RecTrigPos.md) — 触发前数据（状态 1）
- [RecUpload](RecUpload.md) — 状态为 4 后流式传输数据
