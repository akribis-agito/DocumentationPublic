---
summary: 选择 CNC 运动队列 A（或 B）的段末行为。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAEndSegMod/CNCBEndSegMod

选择控制器在队列 A（或 B）中连续 CNC 段之间出现不连续时的处理方式。

## 概述

`CNCAEndSegMod`（以及第二 CNC 引擎上的对应参数 `CNCBEndSegMod`）用于选择当新推入的段违反**连续运动**规则时控制器的响应方式——即前一段以非零速度结束，而新段无法从该速度平滑衔接。该参数为非轴参数，保存至闪存，可随时修改。

相关的段末速度由 [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) 报告，该模式触发修正的次数由 [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md) 计数。

## 工作原理

推入段时，控制器检查能否与前一段连续运行。当前一段的末速度非零，**且**满足以下任一条件时，连续性被破坏：

- 新段为非运动段或运动阻塞段（如延时、I/O 写入或等待），或
- 新段为运动段，但其涉及的轴与前一段不同。

`CNCAEndSegMod` 决定对此类不连续的响应方式：

| 值 | 不连续时的行为 |
|----|----|
| 0 | **拒绝。** 推入被拒绝并返回错误。上位机必须提供已在所请求速度下对齐的段。 |
| 1 | **自动修正。** 推入被接受；控制器将前一段的末速度改写为 0，使路径在新段开始前平稳停止，并将修正计数器 [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md) 加 1。 |

当不存在不连续时，`CNCAEndSegMod` 不起作用——段按推入原值入队，所请求的末速度得以保留。

## 示例

```text
ACNCAEndSegMod=0     ; 拒绝任何破坏连续运动的段
ACNCAEndSegMod=1     ; 自动修正：将前一段末速度强制置 0 并计数
```

## 另请参阅

- [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md) — 已执行自动修正的次数
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — 段末速度
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — 推入段（执行检查的位置）
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 已入队的段数据
