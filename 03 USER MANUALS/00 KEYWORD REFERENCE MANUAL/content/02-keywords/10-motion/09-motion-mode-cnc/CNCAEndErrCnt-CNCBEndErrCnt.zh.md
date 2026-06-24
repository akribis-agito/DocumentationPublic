---
summary: CNC 引擎为保持路径连续性而应用的段末自动修正次数的累计计数。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAEndErrCnt/CNCBEndErrCnt

统计 CNC 引擎对队列 A（或 B）应用的段末自动修正次数。

## 概述

`CNCAEndErrCnt`（以及第二个 CNC 引擎上的 `CNCBEndErrCnt`）是控制器对队列 A（或 B）中连续 CNC 段之间的不连续性进行自动修正的累计次数。仅当 [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) 设置为自动修正模式（值 1）且引擎将上一段的末速度强制为 0 以保持路径连续时，该值才会增加。该参数为非轴参数，不保存至闪存，可在任何时候更改。

将其用作质量指标：非零值表示上位机推送的路径中存在请求速度不匹配的接合点，控制器在每处无声地插入了停止。路径规划良好时，该计数保持为 0。

## 工作原理

- 计数从 0 开始，由 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) 复位为 0。
- 每当推送的段违反连续运动规则**且** [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) = 1 时，控制器将上一段的末速度重写为 0，并将此计数加 1。（若 `CNCAEndSegMod` = 0，则推送被拒绝，计数不变。）
- 该值是当前队列生命周期内的累计计数，不是每段的值，也不是阈值。写入范围限制为 0–1，因此唯一有效的写操作是 `=0` 以清除计数；超过 1 的值将被拒绝为超出范围。正常使用方式是在流式传输路径后读取该值，检查是否仍为 0。

## 示例

```text
ACNCAEndErrCnt       ; 读取已应用的段末修正次数
ACNCAEndErrCnt=0     ; 在推送新路径之前重置修正计数
```

## 另请参阅

- [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) — 选择拒绝模式或自动修正模式（仅模式 1 会增加此计数）
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — 段末速度
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — 将此计数复位为 0
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 队列段数据
