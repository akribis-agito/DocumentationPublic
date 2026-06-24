---
keyword: FFFiltDef
availability:
  standalone: []
  central-i:
  - v5
can_code: 729
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# FFFiltDef

定义前馈滤波器参数。

## 概述

`FFFiltDef` 定义前馈滤波器的参数。当 [FFFiltOn](FFFiltOn.md) 使能该滤波器时，滤波器作用于合并后的前馈输出（[AccFFW](AccFFW.md) 与 [VelFFW](VelFFW.md) 项之和），然后将该输出叠加到速度环输出上，形成电流参考值。

前馈滤波器是本组中唯一的可定制滤波器，索引 N = 1。每个可定制滤波器由最多 5 个参数描述：一个滤波器类型选择器加最多四个特定类型参数。前馈滤波器的五个元素为 `FFFiltDef[1]` 至 `FFFiltDef[5]`。

| 索引 | 描述 |
|---|---|
| `FFFiltDef[1]` | 滤波器类型 |
| `FFFiltDef[2]` | 参数 1 |
| `FFFiltDef[3]` | 参数 2 |
| `FFFiltDef[4]` | 参数 3 |
| `FFFiltDef[5]` | 参数 4 |

## 工作原理

滤波器类型及其参数（截止/陷波/极点/零点频率、阻尼比等）在可定制滤波器参考手册中列出。控制器根据这些参数计算二阶（双二次）系数，并在 [FFFiltOn](FFFiltOn.md)`[1] = 1` 时将滤波器应用于合并后的前馈输出。这是前馈支路上的单个双二次节，而非多节级联。写入 `FFFiltDef`（及对应的 [FFFiltOn](FFFiltOn.md)）后，运行 [CalcFilters](../01-general-keywords/CalcFilters.md) 以重新计算系数。

完整的按类型分类的参数定义、传递函数和单位见附录：[可定制滤波器 (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md)（前馈滤波器的索引 N = 1）。

## 示例

```text
AFFFiltDef[1]=2      ; 滤波器类型：二阶低通
AFFFiltDef[2]=85000  ; 参数 1：截止频率（850 Hz，单位 Hz/100）
AFFFiltDef[3]=71     ; 参数 2：阻尼比（0.71，单位 %）
AFFFiltOn[1]=1       ; 使能前馈滤波器
ACalcFilters         ; 重新计算滤波器系数
```

## 另请参阅

- [FFFiltOn](FFFiltOn.md) — 使能/旁路前馈滤波器
- [CalcFilters](../01-general-keywords/CalcFilters.md) — 更改后重新计算滤波器系数
- [AccFFW](AccFFW.md) / [VelFFW](VelFFW.md) — 滤波器作用的前馈项
- 附录：[可定制滤波器 (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md) — 完整的滤波器类型与参数参考
