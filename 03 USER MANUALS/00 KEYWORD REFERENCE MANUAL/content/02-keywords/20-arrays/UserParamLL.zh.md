---
summary: 每轴、功能相关的 64 位有符号整数数组，用于用户/上位机共享存储。
keyword: UserParamLL
availability:
  standalone: []
  central-i:
  - v5
can_code: 774
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# UserParamLL

每轴、功能相关的 64 位有符号整数数组，用于用户/上位机共享存储。

## 概述

`UserParamLL` 是用户参数数组族中的 64 位有符号整数（长整型）成员。它是一个轴相关数组，提供与 [UserParam](UserParam.md) 相同类型的每轴存储——用户程序和上位机均可访问，并保存至闪存——但存储 64 位整数，适用于无法放入 [UserParam](UserParam.md) 32 位范围的整数值。

与用户参数族的其他成员一样，这些数组是功能相关的：某些条目可能由控制器功能内部使用（控制器保证一个条目不会同时被多个功能共享），因此，如需在用户程序、自定义函数或调试中使用自由暂存存储，请优先选用通用数据数组，例如 [GenDataLL](GenDataLL.md)。该数组在任何时刻均可读写，包括运动中及电机使能状态下。数组采用 1-indexed：第一个可用元素为 `UserParamLL[1]`（索引 0 为保留项，不可访问）；可用元素数量取决于型号（通常为 20，较小型号可能更少）。接受的值范围为 -2251799813685248 至 2251799813685247，即 ±2^51，而非完整的有符号 64 位范围，该限制确保值在以双精度形式记录和上报时不会溢出。

## 示例

```text
AUserParamLL[1]=5000000000   ; store a large 64-bit integer
AUserParamLL[1]              ; read the first element
```

## 另请参见

- [UserParam](UserParam.md) — 32 位整数每轴数组
- [UserParamD](UserParamD.md) — 64 位双精度浮点变体
- [UserParamF](UserParamF.md) — 32 位单精度浮点变体
