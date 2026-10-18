---
keyword: FricVelSrc
summary: 选择摩擦模型所用的速度（0 = dPosRef，1 = VelRef，2 = 速度反馈）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 927
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricVelSrc

选择摩擦模型所用的速度（0 = dPosRef，1 = VelRef，2 = 速度反馈）。

## 概述

`FricVelSrc` 选择驱动摩擦方法 1、2、3 和 5 的速度。适用于 AGM800 和 AGM800-EC（central-i v5）。

| `FricVelSrc` | 所用速度 |
|---|---|
| 0 | 轨迹规划器给出的位置参考导数（dPosRef） |
| 1 | 速度参考（[VelRef](../../02-keywords/10-motion/01-kinematics-status/VelRef.md)） |
| 2 | 速度反馈（默认） |

## 工作原理

三种来源的单位都是 counts/s，因此无论选择哪一种，同一组死区带和 Stribeck 速度都适用。参考值（0 或 1）信号干净、无噪声，并且在指令换向时准确换向；反馈值（2）跟随轴的实际运动。

速度模式下没有位置参考，因此无论 `FricVelSrc` 如何设置，该环节都使用 `VelRef`。LuGre（方法 4）和象限切换补偿始终使用速度反馈。粘性项（[FricViscous](FricViscous.md)）始终使用速度反馈。

## 示例

```text
AFricVelSrc=1      ; 用速度参考驱动摩擦模型
```

## 另请参阅

- [FricMethod](FricMethod.md)
- [摩擦前馈](00-overview.md)
