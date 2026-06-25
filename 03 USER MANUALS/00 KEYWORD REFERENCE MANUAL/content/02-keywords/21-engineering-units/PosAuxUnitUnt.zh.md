---
keyword: PosAuxUnitUnt
summary: 辅助编码器位置的自由文本单位标签，每个数组元素存储一个字符。
availability:
  standalone: []
  central-i:
  - v5
can_code: 816
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
# PosAuxUnitUnt

辅助编码器位置的自由文本单位标签，每个数组元素存储一个字符。

## 概述

`PosAuxUnitUnt` 存储在全局用户单位功能启用时（[UserUnitsEn](UserUnitsEn.md) = 1），上位机为辅助编码器位置量显示的文本单位名称。该标签与辅助位置比例因子 [PosAuxUnitFct](PosAuxUnitFct.md) 配合使用，并适用于辅助位置单位组 [PosAuxUnitGrp](PosAuxUnitGrp.md) 中的所有关键字。它是主反馈 [PosUnitUnt](PosUnitUnt.md) 的辅助编码器对应项。

该标签仅用于显示目的：它只改变上位机对辅助位置单位的命名方式，不影响数值或控制计算。

## 工作原理

标签以每轴字符数组的形式存储，每个元素存储一个字符码。数组从 1 开始索引，元素 [0] 不存在。`array_size` 为 11，其中有一个保留槽，因此可用索引为 [1] 至 [10]，最多可存储 10 个字符。每个元素存储一个 0–255 范围内的字符码；0 作为字符串终止符。默认为空标签。

| 索引  | 元素          |
|-------|---------------|
| [1]   | 标签的第一个字符 |
| [2]   | 标签的第二个字符 |
| ...   | ...           |
| [10]  | 标签的第十个字符 |

标签保存至闪存，可在重新上电后保持。

此关键字仅在 v5（Central-i）中可用。

## 示例

设置三字符标签 `"deg"`（字符码 100、101、103）并添加终止符：

```text
APosAuxUnitUnt[1]=100   ; 'd'
APosAuxUnitUnt[2]=101   ; 'e'
APosAuxUnitUnt[3]=103   ; 'g'
APosAuxUnitUnt[4]=0     ; string terminator
APosAuxUnitUnt[1]       ; read back the first character code
```

## 另请参阅

- [PosAuxUnitFct](PosAuxUnitFct.md) — 辅助位置量的比例因子
- [PosAuxUnitGrp](PosAuxUnitGrp.md) — 此标签适用的关键字
- [PosUnitUnt](PosUnitUnt.md) — 主反馈位置单位标签
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
