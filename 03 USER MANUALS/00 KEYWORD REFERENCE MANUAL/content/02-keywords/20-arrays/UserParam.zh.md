---
keyword: UserParam
summary: 轴相关功能关联 32 位整数数组，用于用户/上位机共享存储。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 624
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 251
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
# UserParam

轴相关功能关联 32 位整数数组，用于用户/上位机共享存储。

## 概述

`UserParam` 是一个轴相关通用 32 位有符号整数数组，提供用户程序和上位机均可访问的每轴存储空间。可随时读写，包括在运动中和电机使能时，并保存至闪存，因此在参数存储后内容可在重新上电后保留。

与 [GenData](GenData.md) 系列不同，用户参数数组与功能关联：部分条目由内部用于存储临时变量（例如在回零序列和 CNC 运动变量中）。控制器确保任一条目同一时刻不会被超过一个功能使用，但由于部分条目被功能保留，不建议将 `UserParam` 用于用户程序、自定义函数或调试——请使用 [GenData](GenData.md)。`UserParam` 是该系列中的 32 位整数成员；其他数据类型请参见 [UserParamF](UserParamF.md)（32 位浮点）、[UserParamD](UserParamD.md)（64 位双精度浮点）和 [UserParamLL](UserParamLL.md)（64 位有符号整数）。

![通用数组系列：UserParam 行包含四个轴相关变体（UserParam、UserParamF、UserParamD、UserParamLL），其中部分条目由内部保留；GenData 行包含四个非轴变体，推荐用于用户程序](array-family-types.svg)

每个元素存储一个 32 位有符号整数，因此值范围为 -2147483648 至 2147483647，默认值为 0。数组为 1 索引：第一个可用元素为 `UserParam[1]`（索引 0 保留，不可访问）。可用元素数量取决于型号——大多数型号为 250，较小型号为 50。

## 示例

```text
AUserParam[1]=5      ; store a value in the first element
AUserParam[1]       ; read the first element
AUserParam[250]=0    ; highest usable index on a 250-element model
```

## 另请参阅

- [UserParamD](UserParamD.md) — 64 位双精度浮点变体
- [UserParamF](UserParamF.md) — 32 位单精度浮点变体
- [UserParamLL](UserParamLL.md) — long-long（64 位有符号整数）变体
- [GenData](GenData.md) — 非轴通用存储（推荐用于用户程序）
