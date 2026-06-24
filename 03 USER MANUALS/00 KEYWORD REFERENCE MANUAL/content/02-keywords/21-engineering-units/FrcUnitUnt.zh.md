---
keyword: FrcUnitUnt
summary: 力工程单位的显示标签（名称），以短文本字符串形式存储。
availability:
  standalone: []
  central-i:
  - v5
can_code: 813
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
# FrcUnitUnt

力工程单位的显示标签（名称），以短文本字符串形式存储。

## 概述

`FrcUnitUnt` 保存**力工程单位的名称**——与 [FrcUnitFct](FrcUnitFct.md) 中的比例系数配套显示的文本标签，例如 `N` 或 `mN`。它记录了力分组（参见 [FrcUnitGrp](FrcUnitGrp.md)）当前所使用的单位。该标签仅用于描述：它与数值一同显示，但本身不执行任何换算——数值换算由 [FrcUnitFct](FrcUnitFct.md) 设置。

此关键字仅在 central-i v5 中可用。

## 工作原理

`FrcUnitUnt` 是一个按轴存储在闪存中的数组，以短文本字符串形式保存单位标签。每个数组元素保存名称中的一个字符（字符码范围为 0–255）。数组采用 1 索引：第一个字符位于元素 [1]，元素 [0] 保留，不可使用。标签最多可容纳 10 个字符，因此最高可用索引比数组大小少一；较短的标签在可用长度内终止。

通常通过上位机工具一次性写入整个字符串来设置标签；按字符存储的数组布局是其在控制器上的存储方式。

## 示例

```text
AFrcUnitUnt[1]      ; 读取力单位标签的第一个字符
AFrcUnitUnt[2]      ; 读取第二个字符
```

## 另请参阅

- [00-overview](00-overview.md) — 分组 / 系数 / 单位模型
- [FrcUnitFct](FrcUnitFct.md) — 力比例系数（数值换算）
- [FrcUnitGrp](FrcUnitGrp.md) — 该单位所适用的关键字
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [PosUnitUnt](PosUnitUnt.md) · [VelUnitUnt](VelUnitUnt.md) · [AccUnitUnt](AccUnitUnt.md) — 其他物理量的单位标签
