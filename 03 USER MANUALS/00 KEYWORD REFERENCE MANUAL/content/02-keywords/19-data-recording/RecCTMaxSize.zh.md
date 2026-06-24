---
summary: 设置每个通道的连续时间记录缓冲区最大采样数。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# RecCTMaxSize

设置每个通道的连续时间记录缓冲区最大采样数。

## 概述

`RecCTMaxSize` 是一个数组，用于设置每个示波器的连续（循环）记录缓冲区所保留的最大采样数。它限制了当 [RecCTEnable](RecCTEnable.md) 启用连续记录时所使用的缓冲区大小。该参数为非轴参数，保存至闪存。

> **注意：** 当前固件中连续记录功能尚未激活。`RecCTMaxSize` 和 [RecCTEnable](RecCTEnable.md) 为保留参数，暂无实际效果；请使用[数据记录](00-overview.md)概述中描述的标准触发（单次）记录流程。

## 示例

```text
ARecCTMaxSize[1]=16500   ; allocate up to 16500 samples on the first scope
ARecCTMaxSize[1]        ; query the configured buffer size
```

## 另请参阅

- [RecCTEnable](RecCTEnable.md) — 启用连续时间记录
- [RecStart](RecStart.md) — 启动记录
- [RecLength](RecLength.md) — 每个参数的数据点数（触发记录）
