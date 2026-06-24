---
summary: 保留的 CNC FIFO 段移除关键字（当前固件未开放）。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CNCARemove/CNCBRemove

保留的 CNC FIFO 段移除关键字。当前固件未开放此功能。

## 概述

`CNCARemove` / `CNCBRemove` 原本设计为 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) 的逐段补充操作，可将最近压入的段从 CNC FIFO 中移除，而不清空队列其余部分。

> **当前固件不支持。** 现有固件（LTS v3.X.X 或开发版）均未将 `CNCARemove` 或 `CNCBRemove` 作为关键字开放。若需撤销已入队的段，目前唯一的方法是通过 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) 清空队列，然后重新压入需要保留的段。

## 另请参阅

- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — 清除所有待处理段
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — 向队列压入段
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 已入队段数据
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — 队列可用空间及当前段参数计数
