---
keyword: ScopeParams
summary: 列出 Central-i 示波器捕获的信号。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 744
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 7
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
---
# ScopeParams

列出 Central-i 示波器捕获的信号。

## 概述

`ScopeParams` 是一个数组，用于指定 Central-i 示波器记录哪些控制器信号。每个元素存储一个信号的[复合 CAN 码](../../01-keyword-usage-and-syntax/complex-can-code.md)，供 [ScopeOn](ScopeOn.md) 启动的示波器确定采样对象。最多可选择 **六** 路信号。该参数为非轴参数，保存至闪存，因此选择在重新上电后仍然有效。

## 工作原理

该数组为 1 索引：`ScopeParams[1]` 为第一路捕获信号，最多至 `ScopeParams[6]`。值为 `0` 的元素视为空，不选择任何信号。复合 CAN 码同时编码参数以及（对于轴参数）所属轴，因此可同时捕获不同轴上的同一参数。

启动示波器时（参见 [ScopeOn](ScopeOn.md)）才分析该列表，而非在写入元素时分析。无法解析为可捕获信号的条目——未知 CAN 码、无效轴或数组索引、或指令关键字——将被静默跳过：不向数据包贡献任何内容，也不触发错误。

写入缓冲区的每个已捕获采样由一个时间戳加每个已配置信号各一个值组成；这决定了 [ScopeStatus](ScopeStatus.md)（索引 1）报告的数据包大小。选择的信号越多，每个采样越大，因此固定缓冲区在暂停前能够存储的采样数越少。示波器启动时，已配置的列表快照至 [ScopeAbout](ScopeAbout.md)，即使之后修改了选择，上位机仍可解析上传内容。

## 示例

```text
AScopeParams[1]=2      ; 第一路捕获信号（复合 CAN 码）
AScopeParams[2]=1026   ; 第二路捕获信号
AScopeParams[3]=0      ; 清除第三个槽（无信号）
AScopeParams[1]       ; 查询第一路捕获信号
```

## 另请参阅

- [ScopeOn](ScopeOn.md) — 启动/停止示波器
- [ScopeGap](ScopeGap.md) — 示波器采样间隔
- [ScopeAbout](ScopeAbout.md) — 已捕获信号集的快照
- [ScopeUpload](ScopeUpload.md) — 获取已捕获数据
