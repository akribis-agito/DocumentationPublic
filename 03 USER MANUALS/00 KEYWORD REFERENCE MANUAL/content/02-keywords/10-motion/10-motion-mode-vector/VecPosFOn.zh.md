---
keyword: VecPosFOn
summary: 启用（1）由 VecPosFDef 定义的位置滤波器，作用于矢量参考输出。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 648
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# VecPosFOn

启用（1）由 VecPosFDef 定义的位置滤波器，作用于矢量参考输出。

## 概述

`VecPosFOn` 用于在协调矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）的参考上启用位置滤波器。设为 `1` 时，将应用 [VecPosFDef](VecPosFDef.md) 定义的滤波器，对合成矢量位置参考进行平滑处理，之后再将其分配给各成员轴；设为 `0`（默认值）时，参考不经任何滤波直接通过。对矢量参考进行平滑处理可减少传递至各成员轴机构的加加速度。该参数为轴相关参数，保存至闪存，且在轴运动期间不可修改。

## 工作原理

滤波器作用于由组主轴（编号最小的成员轴，参见 [VecMemberAxes](VecMemberAxes.md)）计算出的**合成路径**参考，因此应在主轴上配置并启用该滤波器。由于经过滤波的合成值将分发至各成员轴，启用该滤波器可同时对所有成员轴进行平滑处理，并保持协调路径的一致性。

使能标志在矢量运动启动时进行校验：若设为 `1`，控制器将检查 [VecPosFDef](VecPosFDef.md) 是否描述了有效的滤波器，若无效则拒绝该运动指令。应先配置 [VecPosFDef](VecPosFDef.md)，再将 `VecPosFOn` 设为 `1`。仅接受 `0`（关闭）和 `1`（开启）两个值。

## 示例

```text
AVecPosFOn=0         ; 轴 A 上的位置滤波器已禁用（默认）
AVecPosFOn=1         ; 对矢量参考应用 VecPosFDef 位置滤波器
```

## 另请参阅

- [VecPosFDef](VecPosFDef.md) — 启用时所应用的滤波器定义
- [VecMemberAxes](VecMemberAxes.md) — 定义组及其主轴
- [VecSpeed](VecSpeed.md) — 指令合成速度
