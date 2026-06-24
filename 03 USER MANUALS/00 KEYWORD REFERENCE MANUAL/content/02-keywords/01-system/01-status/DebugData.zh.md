---
keyword: DebugData
summary: 保留供 Agito 功能开发和测试使用的数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 224
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 200
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# DebugData

保留供 Agito 功能开发和测试使用的数组。

## 概述

`DebugData` 是保留供 Agito 功能开发和测试使用的大型暂存数组（大多数构建上为 200 个元素，某些构建上更大）。其内容和含义**并不固定**，可能在固件构建之间变化，因此不应在生产集成中使用。

## 工作原理

`DebugData` 是单个共享的非轴数组，固件模块直接读写它，以暴露内部值或在开发过程中注入测试条件。各个元素在固件内部通过命名索引寻址，因此任一给定元素的含义完全取决于构建。它所服务的用途示例包括：捕获控制中断时序（在实时中断的起点、中点和终点锁存的计数器）、为测试模拟数字量输入状态、报告 I²t 电机功率限值，以及为波形演示快照运动规划器/位置参考信号。

由于这些赋值随功能开发而增删，该数组没有稳定、有文档记录的布局。从 `DebugData` 读取的任何值，仅应在生成它的确切固件构建的上下文中视为有意义。

## 示例

```text
ADebugData[1]       ; read a development scratch value (meaning is build-specific)
```

## 另请参阅

- [RNDDebug](../02-operation/RNDDebug.md) — 相关的开发/调试命令
