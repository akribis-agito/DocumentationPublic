---
keyword: RecTrigTyp
summary: 每个触发的触发激活逻辑（边沿、比较或范围）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 245
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 12
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RecTrigTyp

每个触发的触发激活逻辑（边沿、比较或范围）。

## 概述

`RecTrigTyp` 定义每个触发的激活方式（触发类型）。它选择触发源值（[RecTrigSrc](RecTrigSrc.md)，经 [RecTrigMask](RecTrigMask.md) 掩码处理）与比较值 [RecTrigVal](RecTrigVal.md) 和 [RecTrigValMax](RecTrigValMax.md) 之间所应用的比较方式。每个索引对应不同的触发。

| 索引 | 示波器编号 | 触发 |
|---|---|---|
| 1 | 1（第一） | 1 |
| 2 | 1（第一） | 2 |
| 3 | 1（第一） | 3 |
| 4 | 2（第二） | 1 |
| 5 | 2（第二） | 2 |
| 6 | 2（第二） | 3 |

## 工作原理

每个 `RecTrigTyp` 值对应不同的触发激活逻辑。触发源值来自 [RecTrigSrc](RecTrigSrc.md) 所指向的变量，并经过掩码处理。仅当触发源为整数类型（32 位 int 或 64 位 long）时，[RecTrigMask](RecTrigMask.md) 的掩码才会生效；对于浮点触发源，掩码被忽略，比较在原始值上直接进行（详见 [RecTrigMask](RecTrigMask.md)）。

| 值 | 触发激活逻辑 |
|----|----|
| 0 | 立即触发（无需触发源） |
| 1 | 当源值大于 RecTrigVal 时激活 |
| 2 | 当源值等于 RecTrigVal 时激活 |
| 3 | 当源值不等于 RecTrigVal 时激活 |
| 4 | 当源值小于 RecTrigVal 时激活 |
| 5 | 当源值超过 RecTrigVal 的上升沿时激活 |
| 6 | 当源值跌破 RecTrigVal 的下降沿时激活 |
| 7 | 仅手动触发（仅由 [RecTrigForce](RecTrigForce.md) 激活；无需触发源） |
| 8 | 当源值与记录开始时的值不同时激活 |
| 9 | 当源值在范围（RecTrigVal, RecTrigValMax）内时激活 |
| 10 | 当源值不在范围（RecTrigVal, RecTrigValMax）内时激活 |
| 11 | 当源值进入范围（RecTrigVal, RecTrigValMax）时激活 |
| 12 | 当源值离开范围（RecTrigVal, RecTrigValMax）时激活 |

## 示例

```text
ARecTrigTyp[2]=5     ; trigger 2 (first scope) on rising edge above RecTrigVal
ARecTrigTyp[1]      ; query the activation type of trigger 1 (first scope)
```

> **注意：** 通常需要将 `RecTrigTyp[2] = 0`、`RecTrigTyp[3] = 0`、`RecTrigsLogic[1] = 1`、`RecTrigsLogic[2] = 1` 和 `RecTrigsMode[1] = 1` 组合配置，以实现第一示波器的单触发设置。第二示波器可进行类似配置。

## 另请参阅

- [RecTrigSrc](RecTrigSrc.md) — 触发源变量
- [RecTrigVal](RecTrigVal.md) — 比较值
- [RecTrigValMax](RecTrigValMax.md) — 范围上界（类型 9–12）
- [RecTrigMask](RecTrigMask.md) — 对源值进行位掩码处理
