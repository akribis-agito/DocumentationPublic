---
summary: 每轴、功能相关的 32 位单精度浮点数组，用于用户与上位机的共享存储。
keyword: UserParamF
availability:
  standalone: []
  central-i:
  - v5
can_code: 718
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# UserParamF

每轴、功能相关的 32 位单精度浮点数组，用于用户与上位机的共享存储。

## 概述

`UserParamF` 是用户参数数组系列中的32位单精度浮点成员。它是一个轴相关数组，提供与 [UserParam](UserParam.md) 相同类型的每轴存储——可由用户程序和上位机访问，并保存至闪存——但存储的是实数（单精度浮点）值，而非32位整数。如需更高精度，请使用双精度 [UserParamD](UserParamD.md)。

与用户参数系列的其他成员一样，这些数组是功能相关的：某些条目可能由控制器功能在内部使用（控制器保证同一时间内一个条目不会被多个功能共享），因此若需要用户程序、自定义函数或调试中的自由暂存存储，应优先使用通用数据数组，如 [GenDataF](GenDataF.md)。该数组可在任何时刻读写，包括运动中及电机使能时。数组采用1索引：第一个可用元素为 `UserParamF[1]`（索引0为保留项，不可访问）；可用元素数量取决于型号（通常为20，较小型号上可能更少）。

## 示例

```text
AUserParamF[1]=0.25 ; 存储一个单精度值
AUserParamF[1]      ; 读取第一个元素
```

## 另请参阅

- [UserParam](UserParam.md) — 32位整数每轴数组
- [UserParamD](UserParamD.md) — 64位双精度浮点数变体
- [UserParamLL](UserParamLL.md) — long-long（64位有符号整数）变体
