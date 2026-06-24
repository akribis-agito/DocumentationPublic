---
keyword: AccUnitUnt
summary: 加速度工程单位的显示标签（名称），以短文本字符串形式存储。
availability:
  standalone: []
  central-i:
  - v5
can_code: 810
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
# AccUnitUnt

加速度工程单位的显示标签（名称），以短文本字符串形式存储。

## 概述

`AccUnitUnt` 存储**加速度工程单位的名称**——与 [AccUnitFct](AccUnitFct.md) 中的比例系数配套使用的文本标签，例如 `mm/s2` 或 `deg/s2`。它用于说明加速度组（参见 [AccUnitGrp](AccUnitGrp.md)）当前所使用的单位。该标签仅起说明作用：其与数值一同显示，但本身不执行任何换算——数值换算由 [AccUnitFct](AccUnitFct.md) 设置。

本关键字仅在 central-i v5 及以上版本中可用。

## 工作原理

`AccUnitUnt` 是一个保存至闪存的轴相关数组，以短文本字符串形式存储单位标签。每个数组元素存储名称中的一个字符（字符编码范围为 0–255）。数组为 1-indexed：第一个字符位于元素 [1]，元素 [0] 为保留项，不可使用。标签最多可包含 10 个字符，因此最高可用索引比数组大小少一；较短的标签会在可用长度内结尾。

通常通过上位机工具一次性写入整个字符串；逐字符数组布局是其在控制器上的存储方式。

## 示例

```text
AAccUnitUnt[1]      ; 读取加速度单位标签的第一个字符
AAccUnitUnt[2]      ; 读取第二个字符
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 系数 / 单位模型
- [AccUnitFct](AccUnitFct.md) — 加速度比例系数（数值换算）
- [AccUnitGrp](AccUnitGrp.md) — 该单位适用的关键字
- [UserUnitsEn](UserUnitsEn.md) — 总使能
- [PosUnitUnt](PosUnitUnt.md) · [VelUnitUnt](VelUnitUnt.md) · [FrcUnitUnt](FrcUnitUnt.md) — 其他物理量的单位标签
