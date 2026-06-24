---
keyword: RecTrigSrc
summary: 每个触发的触发源变量的复合 CAN 码。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 243
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RecTrigSrc

每个触发的触发源变量的复合 CAN 码。

## 概述

`RecTrigSrc` 定义每个触发所监测变量的[复合 CAN 码](../../01-keyword-usage-and-syntax/complex-can-code.md)。触发将该源值（经 [RecTrigMask](RecTrigMask.md) 掩码处理后）与 [RecTrigVal](RecTrigVal.md) / [RecTrigValMax](RecTrigValMax.md) 按照 [RecTrigTyp](RecTrigTyp.md) 进行比较。每个索引对应不同的触发。

| 索引 | 示波器编号 | 触发 |
|---|---|---|
| 1 | 1（第一） | 1 |
| 2 | 1（第一） | 2 |
| 3 | 1（第一） | 3 |
| 4 | 2（第二） | 1 |
| 5 | 2（第二） | 2 |
| 6 | 2（第二） | 3 |

同一个变量可同时作为触发源和被记录变量使用。

触发源在开始记录时（由 [RecStart](RecStart.md)）进行验证。若源解析到命令/功能类关键字而非可读变量（错误 64）、无效轴（错误 68）或超出范围的数组索引（错误 70），则启动将失败。

## 示例

```text
ARecTrigSrc[4]=2     ; use APos as the source for trigger 1 of the second scope
ARecTrigSrc[1]      ; query the source of trigger 1 (first scope)
```

在上述示例中，`ARecTrigSrc[4]=2` 将 `APos` 选为第二示波器触发 1 的触发源。

## 另请参阅

- [RecTrigTyp](RecTrigTyp.md) — 触发激活类型
- [RecTrigMask](RecTrigMask.md) — 对源值进行位掩码处理
- [RecTrigVal](RecTrigVal.md) — 比较值
- [RecParamA/RecParamB](RecParamA-RecParamB.md) — 待捕获的参数
