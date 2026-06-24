---
summary: 保存最新记录的元数据和原始值的数组。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RecData

保存最新记录的元数据和原始值的数组。

## 概述

> **注意：** `RecData` 在本参考手册所参考的固件中不作为控制器关键字出现——控制器上仅提供按示波器区分的 [RecDataA/RecDataB](RecDataA-RecDataB.md) 变体。本页面保留用于旧版/单缓冲区名称；在直接使用 `RecData` 之前，请对照当前固件确认其可用性。

`RecData` 是一个数组，保存与最新记录相关的所有信息。使用 Agito PC Suite 以图形方式查看这些数据效果最佳。此处的信息主要适用于希望编写自定义软件来分析数据的用户。

使用 [RecUpload](RecUpload.md) 接收 `RecData` 中各值的逗号分隔列表。请注意，`RecUpload` 不仅原样上传数值，还会在必要时将其转换为对用户有意义的值。部分转换使用内部比例系数，因此用户无法自行重现这些转换。

`RecData` 的各元素可通过查询 `RecData[n]` 单独访问。不建议这样做，原因在于操作不便，且 `RecUpload` 会将原始数据转换为用户数据。对于具有独立示波器缓冲区的产品，请参阅 [RecDataA/RecDataB](RecDataA-RecDataB.md) 进行按示波器访问。

## 工作原理

缓冲区由固定的元数据头部后跟采集的采样数据组成。前 80 个条目保存记录的元数据（请求长度、采样因子、触发设置、采集的参数列表、各通道缩放比例，以及标记数据起止位置的缓冲区索引）。采集的采样数据从头部之后开始存放。

采样数据按 [RecParam](RecParam.md) 设定的顺序以通道交错方式存储：每个采样时刻依次存储每个已记录参数的一个采样，然后是下一个时刻，以此类推。每个采样占用一个缓冲区槽。槽的宽度取决于固件：传统固件将每个采样存储为 32 位值，而较新的固件将其存储为 64 位值——32 位整数被扩展为 64 位，浮点值以其 64 位位模式存储。`RecUpload` 在流式传输转换后的数据时会进行逆向处理；直接读取 `RecData` 返回存储的原始形式。

在等待触发期间，控制器以循环缓冲区方式填充采样区域，因此对于已完成的触发记录，第一个有效采样不一定位于数据区域的起始处——头部索引（参见 [RecDataA/RecDataB](RecDataA-RecDataB.md)）记录了记录实际开始的位置、触发发生的位置以及记录结束的位置。

## 示例

```text
ARecData[1]         ; query the first raw element of the latest recording
```

## 另请参阅

- [RecUpload](RecUpload.md) — 流式传输转换后的用户单位数据
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — 按示波器区分的原始缓冲区
- [RecParam](RecParam.md) — 选定用于记录的参数
