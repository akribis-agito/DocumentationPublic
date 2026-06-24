---
keyword: VelAuxUnitUnt
summary: 辅助编码器速度的自由文本单位标签，每个数组元素存储一个字符。
availability:
  standalone: []
  central-i:
  - v5
can_code: 822
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
# VelAuxUnitUnt

辅助编码器速度的自由文本单位标签，每个数组元素存储一个字符。

## 概述

`VelAuxUnitUnt` 保存当全局用户单位启用（[UserUnitsEn](UserUnitsEn.md) = 1）时，上位机为辅助编码器速度量显示的文本单位名称。它是辅助速度比例系数 [VelAuxUnitFct](VelAuxUnitFct.md) 的配套标签，适用于辅助速度单位组 [VelAuxUnitGrp](VelAuxUnitGrp.md) 中的每个关键字。它是主反馈 [VelUnitUnt](VelUnitUnt.md) 的辅助编码器对应项。

该标签纯属显示用途：它改变的是上位机对辅助速度单位的名称显示，而非数值或控制计算。

## 工作原理

该标签以每轴字符数组的形式存储，每个元素存储一个字符代码。数组从 1 开始索引；元素 [0] 不存在。`array_size` 为 11，其中有一个保留槽，因此可用索引为 [1] 至 [10]——最多支持 10 个字符的标签。每个元素存储 0–255 范围内的一个字符代码；0 表示字符串结束。默认值为空标签。

| 索引 | 元素 |
|-------|---------|
| [1]   | 标签的第一个字符 |
| [2]   | 标签的第二个字符 |
| ...   | ... |
| [10]  | 标签的第十个字符 |

该标签存储于闪存，因此在重新上电后保持不变。

此关键字仅在 v5（central-i）及以上版本可用。

## 示例

设置五字符标签 `"deg/s"`（字符代码 100、101、103、47、115）并添加终止符：

```text
AVelAuxUnitUnt[1]=100   ; 'd'
AVelAuxUnitUnt[2]=101   ; 'e'
AVelAuxUnitUnt[3]=103   ; 'g'
AVelAuxUnitUnt[4]=47    ; '/'
AVelAuxUnitUnt[5]=115   ; 's'
AVelAuxUnitUnt[6]=0     ; 字符串终止符
AVelAuxUnitUnt[1]       ; 读取第一个字符代码
```

## 另请参阅

- [VelAuxUnitFct](VelAuxUnitFct.md) — 辅助速度量的比例系数
- [VelAuxUnitGrp](VelAuxUnitGrp.md) — 此标签适用的关键字
- [VelUnitUnt](VelUnitUnt.md) — 主反馈速度单位标签
- [UserUnitsEn](UserUnitsEn.md) — 每轴启用全局用户单位功能
