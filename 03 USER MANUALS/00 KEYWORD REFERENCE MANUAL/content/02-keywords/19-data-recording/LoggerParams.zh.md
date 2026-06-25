---
keyword: LoggerParams
summary: 列出连续数据记录器所捕获的参数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 532
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 41
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# LoggerParams

列出连续数据记录器所捕获的参数。

## 概述

`LoggerParams` 是一个数组，用于指定连续数据记录器在记录会话期间记录的控制器参数。每个元素存储一个待采样参数的[复合 CAN 代码](../../01-keyword-usage-and-syntax/complex-can-code.md)，供 [LoggerOn](LoggerOn.md) 配置的记录器确定捕获内容。该参数为非轴参数，保存至闪存，因此参数选择在重新上电后保持不变。

## 工作原理

该数组为 1 索引：`LoggerParams[1]` 为第一个记录参数，最多可配置 40 个参数。值为 `0` 的元素视为空，不选择任何参数。复合 CAN 代码同时编码参数本身及（对于轴参数）其所属轴，因此同一参数在不同轴上的值可在同一会话中同时记录。

参数列表在记录器启动时（参见 [LoggerOn](LoggerOn.md)）而非写入元素时进行分析。无法解析为可记录参数的条目——未知 CAN 代码、无效轴或数组索引、命令关键字——将被静默跳过：该条目不计入数据包且不报错，因此也不会出现在上传数据中。

写入缓冲区的每个记录采样由一个时间戳加上每个已配置参数的一个值组成，这决定了 [LoggerStatus](LoggerStatus.md)（索引 1）报告的数据包大小。参数越多，每个采样越大，固定缓冲区能存储的采样数也越少。

记录启动时，参数列表被捕获至会话元数据，并从 [LoggerAbout](LoggerAbout.md) 的索引 4 起镜像，以便上位机在参数列表后续更改后仍能解析上传数据。采样率由 [LoggerGap](LoggerGap.md) 设定。

## 示例

```text
ALoggerParams[1]=2     ; 第一个记录参数（复合 CAN 代码）
ALoggerParams[2]=1026  ; 第二个记录参数
ALoggerParams[3]=0     ; 清除第三个槽位（无参数）
ALoggerParams[1]      ; 查询第一个记录参数
```

## 另请参阅

- [LoggerOn](LoggerOn.md) — 启动/停止记录器
- [LoggerGap](LoggerGap.md) — 记录器采样间隔
- [LoggerAbout](LoggerAbout.md) — 记录集的元数据
- [LoggerUpload](LoggerUpload.md) — 取回已记录数据
