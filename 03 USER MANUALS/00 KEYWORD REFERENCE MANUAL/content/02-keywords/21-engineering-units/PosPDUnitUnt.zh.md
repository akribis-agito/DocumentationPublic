---
keyword: PosPDUnitUnt
summary: 脉冲方向位置的自由文本单位标签，每个数组元素保存一个字符。
availability:
  standalone: []
  central-i:
  - v5
can_code: 819
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
# PosPDUnitUnt

脉冲方向位置的自由文本单位标签，每个数组元素保存一个字符。

## 概述

`PosPDUnitUnt` 保存上位机在全局用户单位功能启用时（[UserUnitsEn](UserUnitsEn.md) = 1）为脉冲方向（P/D）位置量显示的文本单位名称。它是与 P/D 位置比例系数 [PosPDUnitFct](PosPDUnitFct.md) 配套的标签，适用于 P/D 位置单位分组 [PosPDUnitGrp](PosPDUnitGrp.md) 中的所有关键字。它是主反馈 [PosUnitUnt](PosUnitUnt.md) 的 P/D 对应项。

该标签纯粹用于显示：它改变上位机对 P/D 位置单位的命名，不影响数值或控制计算。

## 工作原理

标签以按轴字符数组形式存储，每个元素保存一个字符码。数组采用 1 索引；元素 [0] 不存在。`array_size` 为 11 时有一个保留槽，因此可用索引为 [1] 至 [10]——最多 10 个字符。每个元素保存范围 0–255 内的一个字符码；0 表示字符串终止。默认为空标签。

| 索引 | 元素 |
|------|------|
| [1]  | 标签的第一个字符 |
| [2]  | 标签的第二个字符 |
| ...  | ... |
| [10] | 标签的第十个字符 |

标签保存在闪存中，因此在重新上电后依然保留。

此关键字仅在 v5 (central-i) 中可用。

## 示例

设置两字符标签 `"mm"`（字符码 109）并终止：

```text
APosPDUnitUnt[1]=109   ; 'm'
APosPDUnitUnt[2]=109   ; 'm'
APosPDUnitUnt[3]=0     ; 字符串终止符
APosPDUnitUnt[1]       ; 读回第一个字符码
```

## 另请参阅

- [PosPDUnitFct](PosPDUnitFct.md) — P/D 位置量的比例系数
- [PosPDUnitGrp](PosPDUnitGrp.md) — 该标签所适用的关键字
- [PosUnitUnt](PosUnitUnt.md) — 主反馈位置单位标签
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
