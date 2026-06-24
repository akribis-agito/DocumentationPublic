---
keyword: FFFiltOn
availability:
  standalone: []
  central-i:
  - v5
can_code: 728
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# FFFiltOn

使能或旁路前馈滤波器。

## 概述

`FFFiltOn` 使能或旁路前馈滤波器。该滤波器作用于合并后的前馈输出（[AccFFW](AccFFW.md) 与 [VelFFW](VelFFW.md) 项之和），然后将其叠加到速度环输出上，形成电流参考值。

| `FFFiltOn[1]` | 行为 |
|---|---|
| 0 | 滤波器旁路（默认）——合并后的前馈输出直接通过，不做任何处理。 |
| 1 | 滤波器使能——合并后的前馈输出通过 [FFFiltDef](FFFiltDef.md) 定义的滤波器。 |

## 工作原理

使能时，滤波器为二阶（双二次）节，其系数由 [FFFiltDef](FFFiltDef.md) 中的参数计算得出。滤波器置于合并前馈信号通路上：

$$
\text{AccFFW 项} + \text{VelFFW 项} \;\longrightarrow\; \boxed{\text{前馈滤波器}} \;\longrightarrow\; \text{叠加到速度环输出}
$$

前馈滤波器是置于合并前馈支路上的单个二阶（双二次）节——不同于速度输出滤波器的多节级联结构。其内部历史状态（存储的前一拍和前两拍采样值）每个控制周期独立更新，与环路其余部分无关。

旁路时，合并后的前馈输出直接使用。更改 `FFFiltOn` 或 [FFFiltDef](FFFiltDef.md) 后，运行 [CalcFilters](../01-general-keywords/CalcFilters.md) 以使控制器重新计算内部滤波器系数。

## 示例

```text
AFFFiltOn[1]=1       ; 使能前馈滤波器
AFFFiltOn[1]=0       ; 旁路前馈滤波器
ACalcFilters         ; 重新计算滤波器系数
```

## 另请参阅

- [FFFiltDef](FFFiltDef.md) — 前馈滤波器定义参数
- [CalcFilters](../01-general-keywords/CalcFilters.md) — 更改后重新计算滤波器系数
- [AccFFW](AccFFW.md) / [VelFFW](VelFFW.md) — 滤波器作用的前馈项
