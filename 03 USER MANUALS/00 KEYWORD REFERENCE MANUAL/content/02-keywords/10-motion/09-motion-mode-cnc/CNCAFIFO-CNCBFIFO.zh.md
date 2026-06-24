---
summary: 只读数组，保存队列 A（或 B）CNC FIFO 中已入队的原始段数据。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAFIFO/CNCBFIFO

只读数组，保存队列 A（或 B）CNC FIFO 中已入队的原始段数据。

## 概述

`CNCAFIFO`（以及第二 CNC 引擎上的对应参数 `CNCBFIFO`）是只读数组，用于公开队列 A（或 B）CNC 段队列（FIFO）的原始内容。读取该数组可在执行前及执行过程中检查待处理的运动段。该参数为非轴只读数组，不保存至闪存。与所有通信数组一样，该数组为 1-indexed：索引 0 保留，元素索引从 1 开始。

段通过 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 加 [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md)（或 [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md)）加载，在回放时消耗，并通过 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) 清除。

## 工作原理

该数组是队列的底层存储。段以连续元素组成的字流打包，**而非**每段占用一个元素：

- 每段的第一个字保存段 ID（高 24 位）和入口计数（低 8 位）。
- 第二个字保存与 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 相同的类型/涉及轴编码（顶部字节 = 类型，低 24 位 = 涉及轴）。
- 后续各字按推入顺序保存段的参数。

因此，打开一个段消耗两个槽位（头部 + 类型字），每个参数再消耗一个槽位。两个队列的容量因产品而异：队列 A 通常可容纳数千个字，而队列 B 在某些产品上可能小得多。请使用 [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) 读取实际空闲空间，而非假定固定大小——状态数组的第 7 个元素报告空闲字数，刚清除的队列报告完整可用容量。

读取原始字主要用于诊断；每个字的含义遵循上述布局以及 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 中列出的各段类型的参数顺序。

## 示例

```text
ACNCAFIFO[1]        ; 读取第一个入队字（数组为 1-indexed）
ACNCAFIFO[2]        ; 读取第一段的类型/涉及轴字
```

## 另请参阅

- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — 空闲空间、队列指针及运动状态
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — 向队列推入段
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — 清除所有待处理段
- [StopCNCA](StopCNCA.md) — 停止队列 A 的 CNC 运动
