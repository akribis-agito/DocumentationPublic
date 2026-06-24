---
keyword: PosUnitUnt
summary: 位置工程单位的显示标签（名称），以短文本字符串形式存储。
availability:
  standalone: []
  central-i:
  - v5
can_code: 804
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
# PosUnitUnt

位置工程单位的显示标签（名称），以短文本字符串形式存储。

## 概述

`PosUnitUnt` 保存**位置工程单位的名称**——该文本标签与 [PosUnitFct](PosUnitFct.md) 中的比例系数配合使用，例如 `mm` 或 `um`。它记录了位置组（参见 [PosUnitGrp](PosUnitGrp.md)）所使用的单位。该标签仅用于说明：显示时会与数值一同呈现，但本身不执行任何换算——数值换算由 [PosUnitFct](PosUnitFct.md) 设定。

本关键字仅在 central-i v5 及以上版本可用。

## 工作原理

`PosUnitUnt` 是一个保存在闪存中的每轴数组，以短文本字符串形式保存单位标签。每个数组元素保存名称中的一个字符（范围 0–255 的字符代码）。数组以 1 为起始索引：第一个字符位于元素 [1]，元素 [0] 保留，不可使用。标签最多可容纳 10 个字符，因此最高可用索引比数组大小小 1；较短的标签在可用长度范围内截止。

通常通过上位机工具一次性写入整个字符串来设置标签；逐字符的数组布局是控制器的内部存储方式。

## 示例

```text
APosUnitUnt[1]      ; 读取位置单位标签的第一个字符
APosUnitUnt[2]      ; 读取第二个字符
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 系数 / 单位模型
- [PosUnitFct](PosUnitFct.md) — 位置比例系数（数值换算）
- [PosUnitGrp](PosUnitGrp.md) — 该单位适用的关键字
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [VelUnitUnt](VelUnitUnt.md) · [AccUnitUnt](AccUnitUnt.md) · [FrcUnitUnt](FrcUnitUnt.md) — 其他物理量的单位标签
