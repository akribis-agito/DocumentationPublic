---
keyword: VecPosFDef
summary: 定义应用于向量参考输出的位置滤波器系数的数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 647
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: false
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
# VecPosFDef

定义应用于向量参考输出的位置滤波器系数的数组。

## 概述

`VecPosFDef` 是一个 6 元素数组，用于定义应用于协调向量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）参考的位置滤波器。它描述了在合成向量位置参考被分配到各成员轴之前对其进行平滑处理的滤波器，从而减少传递到机械结构的急动度。该滤波器仅在 [VecPosFOn](VecPosFOn.md) 使能时生效。该参数为轴相关数组，保存至闪存，运动过程中不可更改。

## 工作原理

该数组使用控制器标准的可自定义位置滤波器定义：元素 [1] 选择滤波器**类型**，元素 [2]-[5] 为该类型提供最多四个**参数**。类型 `0`（默认值）表示无滤波器，参考值直接通过。当选择某种滤波器类型且 [VecPosFOn](VecPosFOn.md) = 1 时，控制器在向量运动开始时根据这些参数推导工作系数，并对合成路径参考施加二阶（双二次型）平滑滤波器。控制器上其他可自定义位置滤波器也使用相同的定义约定。

由于滤波器作用于组主轴（编号最低的成员轴——参见 [VecMemberAxes](VecMemberAxes.md)）的合成路径，请在主轴上进行定义。定义在运动开始时进行检验：类型与参数的无效组合将导致运动被拒绝，因此请在通过 [VecPosFOn](VecPosFOn.md) 使能滤波器之前验证各参数值。

## 示例

```text
AVecPosFDef[1]=0     ; 元素 1 = 滤波器类型（0 = 无滤波器，默认）
AVecPosFDef[1]       ; 读取滤波器类型元素
AVecPosFDef[2]       ; 读取第一个滤波器参数
```

## 另请参阅

- [VecPosFOn](VecPosFOn.md) — 使能/禁用此位置滤波器
- [VecMemberAxes](VecMemberAxes.md) — 定义分组及其主轴
- [VecSpeed](VecSpeed.md) — 指令合成速度
