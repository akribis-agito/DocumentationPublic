---
keyword: RecTrigForce
summary: 覆盖触发检测并强制记录继续进行的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 252
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RecTrigForce

覆盖触发检测并强制记录继续进行的命令。

## 概述

`RecTrigForce` 覆盖触发检测，强制记录继续，效果等同于触发条件已满足。当配置的触发（[RecTrigTyp](RecTrigTyp.md)、[RecTrigSrc](RecTrigSrc.md)）未触发时，此命令非常有用。每个数组索引对应一个示波器。

`RecTrigForce` 可在 [RecStart](RecStart.md) 之后的任意时刻发出。若示波器仍在填充触发前数据（[RecStat](RecStat.md) 1），强制触发将被锁存，并在触发前部分填满、示波器开始等待触发（[RecStat](RecStat.md) 2）后的第一个记录采样时生效；它不会缩短触发前填充过程。若示波器已在等待触发（[RecStat](RecStat.md) 2），则在下一个记录采样时立即触发。强制触发标志将在下一次 [RecStart](RecStart.md) 时清除。

| 索引 | 说明 |
|-------|------------------------------|
| 1     | 第一示波器 |
| 2     | 第二示波器（如适用） |

## 示例

```text
ARecTrigForce[1]     ; force-trigger the first scope
ARecTrigForce[2]     ; force-trigger the second scope
```

## 另请参阅

- [RecStart](RecStart.md) — 开始记录
- [RecStat](RecStat.md) — 记录状态
- [RecTrigTyp](RecTrigTyp.md) — 触发激活类型
