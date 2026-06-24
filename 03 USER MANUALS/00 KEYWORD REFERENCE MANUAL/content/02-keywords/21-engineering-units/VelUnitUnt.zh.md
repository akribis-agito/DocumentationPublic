---
keyword: VelUnitUnt
summary: 速度工程单位的显示标签（名称），以短文本字符串形式存储。
availability:
  standalone: []
  central-i:
  - v5
can_code: 807
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VelUnitUnt

速度工程单位的显示标签（名称），以短文本字符串形式存储。

## 概述

`VelUnitUnt` 保存**速度工程单位的名称**——与 [VelUnitFct](VelUnitFct.md) 中比例因子配套的文本标签，例如 `mm/s` 或 `deg/s`。它记录速度组（参见 [VelUnitGrp](VelUnitGrp.md)）当前所用的单位。标签为描述性信息：在数值旁显示，但本身不执行任何换算——数值换算由 [VelUnitFct](VelUnitFct.md) 设置。

本关键字仅适用于 central-i v5 及以上版本。

## 工作原理

`VelUnitUnt` 是一个存储在闪存中的逐轴数组，以短文本字符串形式保存单位标签。每个数组元素保存名称中的一个字符（范围 0–255 内的字符码）。数组从 1 开始索引：第一个字符位于元素 [1]，元素 [0] 为保留项，不可使用。标签最多可保存 10 个字符，因此最高可用索引比数组大小小 1；较短的标签在可用长度范围内终止。

通常通过上位机工具一次性写入整个字符串来设置标签；逐字符的数组布局是其在控制器上的存储方式。

## 示例

```text
AVelUnitUnt[1]      ; 读取速度单位标签的第一个字符
AVelUnitUnt[2]      ; 读取第二个字符
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 因子 / 单位模型
- [VelUnitFct](VelUnitFct.md) — 速度比例因子（数值换算）
- [VelUnitGrp](VelUnitGrp.md) — 本单位适用的关键字
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [PosUnitUnt](PosUnitUnt.md) · [AccUnitUnt](AccUnitUnt.md) · [FrcUnitUnt](FrcUnitUnt.md) — 其他量的单位标签
