---
keyword: About
summary: 返回所有控制器参数的内部命令（Agito PCSuite）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 223
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# About

返回所有控制器参数的内部命令（Agito PCSuite）。

## 概述

`About` 是一个只读函数，可在一次操作中转储控制器完整的关键字表定义。它**仅供 Agito PCSuite 内部使用**，不属于常规用户命令集：PCSuite 调用它来填充其参数面板和数据视图面板。如需从上位机软件查看单个参数的范围与默认值，请改用 [ParamAbout](ParamAbout.md)；如需读取固件构建信息，请使用 [FWInfo](FWInfo.md)。

## 工作原理

`About` 实现为非轴函数（它自身没有存储值）。被调用时，固件通过批量回复路径向发起请求的通信通道流式返回关键字表的定义——而非实时值。回复以参数表的列标题和属性名称开始，随后针对每个有效关键字发送其 CAN 码、助记符、属性字、最大数组索引、最小值、最大值、默认值和缩放因子，最后发送参数组名称列表。由于它意在由 PCSuite 发出并解析，其响应布局取决于 PCSuite 与固件之间的约定，并未为通用脚本编写而记录；用户集成应改为读取单个关键字（或使用 [ParamAbout](ParamAbout.md) 获取单个参数的限值和默认值）。

## 另请参见

- [ParamAbout](ParamAbout.md) — 单个参数的范围与默认值
- [FWInfo](FWInfo.md) — 固件构建信息字符串
- [Identity](Identity.md) — 控制器标识与特性
