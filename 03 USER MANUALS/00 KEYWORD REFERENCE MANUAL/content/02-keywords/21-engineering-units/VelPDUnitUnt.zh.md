---
keyword: VelPDUnitUnt
summary: 脉冲方向速度的自由文本单位标签，每个数组元素存储一个字符。
availability:
  standalone: []
  central-i:
  - v5
can_code: 825
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
# VelPDUnitUnt

脉冲方向速度的自由文本单位标签，每个数组元素存储一个字符。

## 概述

`VelPDUnitUnt` 保存上位机在全局用户单位功能已启用（[UserUnitsEn](UserUnitsEn.md) = 1）时，为脉冲/方向（P/D）速度量显示的文本单位名称。它是与 P/D 速度比例因子 [VelPDUnitFct](VelPDUnitFct.md) 配套的标签，适用于 P/D 速度单位组 [VelPDUnitGrp](VelPDUnitGrp.md) 中的所有关键字。它是主反馈 [VelUnitUnt](VelUnitUnt.md) 的 P/D 对应项。

标签纯属外观显示：它改变上位机对 P/D 速度单位的命名，不影响数值或控制计算。

## 工作原理

标签以逐轴字符数组形式存储，每个元素保存一个字符码。数组从 1 开始索引；元素 [0] 不存在。`array_size` 为 11，有一个保留槽位，因此可用索引为 [1] 至 [10]——最多可存储 10 个字符的标签。每个元素保存范围 0–255 内的一个字符码；0 表示字符串结束。默认值为空标签。

| 索引 | 元素 |
|-------|---------|
| [1]   | 标签的第 1 个字符 |
| [2]   | 标签的第 2 个字符 |
| ...   | ... |
| [10]  | 标签的第 10 个字符 |

标签存储在闪存中，因此在重新上电后保持有效。

本关键字仅适用于 v5（central-i）及以上版本。

## 示例

设置一个四字符标签 `"mm/s"`（字符码 109、109、47、115）并终止字符串：

```text
AVelPDUnitUnt[1]=109   ; 'm'
AVelPDUnitUnt[2]=109   ; 'm'
AVelPDUnitUnt[3]=47    ; '/'
AVelPDUnitUnt[4]=115   ; 's'
AVelPDUnitUnt[5]=0     ; 字符串终止符
AVelPDUnitUnt[1]       ; 读取第一个字符码
```

## 另请参阅

- [VelPDUnitFct](VelPDUnitFct.md) — P/D 速度量的比例因子
- [VelPDUnitGrp](VelPDUnitGrp.md) — 本标签适用的关键字
- [VelUnitUnt](VelUnitUnt.md) — 主反馈速度单位标签
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
