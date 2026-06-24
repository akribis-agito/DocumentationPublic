---
summary: 启用或禁用每个示波器的连续时间记录。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# RecCTEnable

启用或禁用每个示波器的连续时间记录。

## 概述

`RecCTEnable` 是一个数组，用于为每个示波器启用或禁用连续（循环）记录模式。在连续记录模式下，示波器持续向循环缓冲区采样，始终保留最新的采样数据——最多保留由 [RecCTMaxSize](RecCTMaxSize.md) 设定的数量——而非在固定的 [RecLength](RecLength.md) 后停止。该参数为非轴参数，保存至闪存。

> **注意：** 当前固件中连续记录功能尚未激活。`RecCTEnable` 和 `RecCTMaxSize` 为保留参数，暂无实际效果；请使用[数据记录](00-overview.md)概述中描述的标准触发（单次）记录流程。

## 示例

```text
ARecCTEnable[1]=1    ; enable continuous-time recording on the first scope
ARecCTEnable[1]     ; query the continuous-time recording state
```

## 另请参阅

- [RecCTMaxSize](RecCTMaxSize.md) — 连续时间记录的缓冲区大小
- [RecStart](RecStart.md) — 启动记录
- [RecStat](RecStat.md) — 记录状态
