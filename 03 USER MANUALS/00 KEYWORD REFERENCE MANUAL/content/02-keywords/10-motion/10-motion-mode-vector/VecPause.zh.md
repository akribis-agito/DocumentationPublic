---
keyword: VecPause
summary: 通过将合成速度斜坡至零或从零斜坡恢复，暂停（1）或继续（0）向量运动。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 640
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
# VecPause

通过将合成速度斜坡至零或从零斜坡恢复，暂停（1）或继续（0）向量运动。

## 概述

`VecPause` 在不终止运动的情况下临时保持协调向量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）。值为 `1` 时，通过将指令合成速度强制为 0 来暂停运动，使分组沿路径减速直至停止。值为 `0` 时，运动正常继续；若之前处于暂停状态，则分组重新加速至 [VecSpeed](VecSpeed.md) 并沿同一路径继续运动。与终止运动的 [StopVec](StopVec.md) 不同，`VecPause` 允许同一运动从暂停处精确恢复。

该参数不保存至闪存，上电时取默认值 `0`。

## 工作原理

在**组主轴**（编号最低的成员轴——参见 [VecMemberAxes](VecMemberAxes.md)）上设置 `VecPause`，因为主轴运行整个分组的单一路径规划器。每个控制周期，规划器检查该标志：当其为 `1` 时，合成目标速度保持为零，分组报告 [VecMotionStat](VecMotionStat.md) = 2（已暂停）；当其返回 `0` 时，目标速度恢复至 [VecSpeed](VecSpeed.md)，[VecMotionStat](VecMotionStat.md) 返回 1（运动中）。沿路径的加减速遵循已配置的向量加减速斜坡，因此暂停和恢复是平滑的而非瞬时的。

暂停不会更改目标位置，因此所有成员轴在恢复后继续运动至原始终点。若分组被停止（例如由 [StopVec](StopVec.md) 停止），控制器会自动将 `VecPause` 清零，因为该运动已不可保持。

## 示例

```text
AVecPause=1          ; 在组主轴 A 上：暂停向量运动（沿路径减速至停止）
AVecPause=0          ; 继续向量运动（加速恢复至 VecSpeed）
```

## 另请参阅

- [StopVec](StopVec.md) — 终止（而非暂停）向量运动
- [VecSpeed](VecSpeed.md) — 暂停后恢复的目标速度
- [VecMotionStat](VecMotionStat.md) — 暂停期间报告值 2
- [VecMemberAxes](VecMemberAxes.md) — 定义分组及其主轴
