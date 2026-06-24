---
keyword: RecTrigsLogic
summary: 在并行检测中连接触发条件的逻辑运算符。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 518
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RecTrigsLogic

在并行检测中连接触发条件的逻辑运算符。

## 概述

`RecTrigsLogic` 定义如何将多个触发条件逻辑连接，以构成并行（逻辑）触发检测的整体触发条件。仅当 [RecTrigsMode](RecTrigsMode.md) = 1（并行检测）时适用。每个索引连接不同的触发器对。

## 工作原理

| 索引 | 示波器编号 | 连接的触发器 |
|---|---|---|
| 1 | 1（第一） | 触发器 1 与触发器 2 |
| 2 | 1（第一） | 触发器 2 与触发器 3 |
| 3 | 2（第二） | 触发器 1 与触发器 2 |
| 4 | 2（第二） | 触发器 2 与触发器 3 |

RecTrigsLogic 的值决定所使用的逻辑运算符。

| 值 | 逻辑运算符 |
|-------|------------------|
| 1     | && (AND)         |
| 2     | \|\| (OR)        |

> **注意：** 逻辑运算符（AND、OR）采用左结合性（从左至右依次运算）。

## 示例

若 `RecTrigsLogic[1] = 1`，`RecTrigsLogic[2] = 2`，则第一示波器的整体触发逻辑条件为

$$
(\text{Trigger 1})\ \&\&\ (\text{Trigger 2})\ ||\ (\text{Trigger 3})
$$

整体触发将在以下任一情况下发生：

1.  触发器 1 和触发器 2 同时激活，或

2.  触发器 3 激活

## 另请参阅

- [RecTrigsMode](RecTrigsMode.md) — 选择并行或串行检测模式
- [RecTrigTyp](RecTrigTyp.md) — 触发激活类型
- [RecTrigSrc](RecTrigSrc.md) — 触发源变量
