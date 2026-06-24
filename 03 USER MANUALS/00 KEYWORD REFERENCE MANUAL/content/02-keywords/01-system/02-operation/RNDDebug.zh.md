---
keyword: RNDDebug
summary: 保留供 Agito 研发使用的部分实现诊断功能。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 1022
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 30
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# RNDDebug

保留供 Agito 研发使用的部分实现诊断功能。

## 概述

`RNDDebug` 是保留供 Agito 内部研究和调试使用的诊断功能。它在固件中标记为**部分实现**：其行为取决于固件构建，其确切语义在不同版本之间可能发生变化。它不适用于生产应用。

## 工作原理

在发布的固件镜像中，`RNDDebug` 实际上是一个占位符：它不执行任何外部可见的操作，只是返回标准确认。随附的值（在其声明范围内）仅在开发构建中选择内部诊断操作——在生产固件中该值没有任何已记录的作用。任何超出正常确认的行为都应视为特定于构建且不受支持。

由于其含义是保留的且在不同构建之间可能有所不同，请勿在应用代码中依赖 `RNDDebug`。请改用专用的状态和诊断关键字。

## 参见

- [DebugData](../01-status/DebugData.md) — 开发/测试暂存数组
- [DoNothing](DoNothing.md) — 受支持的空操作，用于通信检查
