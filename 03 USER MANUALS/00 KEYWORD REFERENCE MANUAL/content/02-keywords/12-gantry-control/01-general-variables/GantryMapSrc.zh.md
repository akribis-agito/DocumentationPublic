---
summary: 选择用于索引龙门映射校正表的位置源。
keyword: GantryMapSrc
availability:
  standalone: []
  central-i:
  - v5
can_code: 753
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryMapSrc

选择索引龙门解耦映射表的位置源。

## 概述

`GantryMapSrc` 是一个指针，用于选择驱动龙门解耦映射表（[GantryMap](GantryMap.md)）查找的位置源。写入的值为源变量的数字代码——通常为龙门沿横梁方向的位置——使用与其他源指针关键字相同的编号方案；默认值 `0` 表示未选择任何源。该参数为轴范围，可保存至闪存，可在电机使能时设置但不能在运动中设置。

随着龙门运动，控制器读取所选源的实时值，并用其从映射表中插值得到解耦比值；该比值由 [GantryMapVal](GantryMapVal.md) 报告，并按 [GantryMapType](GantryMapType.md) 中的说明进行应用。第一个映射条目对应源位置 [GantryMapInit](GantryMapInit.md)，后续条目间距为一个映射间距。

## 工作原理

写入时，`GantryMapSrc` 被解析为目标变量的指针，以便控制器每个周期都能低成本地读取实时值。写入操作会针对所引用的关键字进行验证：代码须在范围内（否则报错 77），须指定有效轴（错误 78）和数组索引（错误 79），须引用参数而非函数（错误 80），且所引用的参数必须为 64 位位置类型值（错误 305）。未通过任何检查的引用将被拒绝，源保持不变。参数表允许在电机使能时写入，但在运动中（`NOMOTN`）拒绝；出于安全考虑，标准做法是在启用 [GantryOn](GantryOn.md) 之前配置好源。每个控制周期，当映射表启用时（[GantryMapType](GantryMapType.md) = 1），控制器获取该变量的当前值，减去 [GantryMapInit](GantryMapInit.md)，除以映射间距得到分数表索引，并在两个相邻的 [GantryMap](GantryMap.md) 条目之间进行线性插值。低于第一个条目或高于最后一个条目的位置将钳位至端部条目。

## 示例

```text
AGantryMapSrc=<code>  ; 以选定的龙门位置源索引映射表（使用该源的 CAN 代码）
AGantryMapSrc        ; 读取已配置的源代码
```

### 边界情况

- **运动中写入**——被拒绝（`NOMOTN`）。
- **映射类型关闭**（[GantryMapType](GantryMapType.md) = 0）——已存储但**不被查询**。
- **源 = 0（默认）**——未绑定任何源；在写入有效 CAN 代码之前，映射表实际上不可用。
- **无效引用**——代码超出范围、指定错误轴或索引、指向函数，或引用非 64 位位置类型参数，在写入时将被拒绝（错误 77、78、79、80 或 305），源保持之前的值；控制器不会静默接受无效引用。
- **设置在错误轴上**——仅在主轴上读取；其他轴的写入虽被存储，但将被忽略。
- **保存**——可保存至闪存；启动时重新解析指针。
- **平台**——仅限 v5 central-i。

## 另请参阅

- [GantryMap](GantryMap.md) — 由此源索引的表
- [GantryMapType](GantryMapType.md) — 启用映射表的使用
- [GantryMapVal](GantryMapVal.md) — 在索引位置处的实时插值比值
- [GantryMapInit](GantryMapInit.md) — 对应第一个表条目的源位置
