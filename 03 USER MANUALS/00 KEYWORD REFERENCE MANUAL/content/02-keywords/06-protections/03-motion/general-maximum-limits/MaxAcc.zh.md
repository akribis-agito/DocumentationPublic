---
keyword: MaxAcc
summary: 允许的最大加速度/减速度，在运动开始前进行检查。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 81
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    access: rw
    data_type: float32
    ok_in_motion: true
    ok_motor_on: true
    units: user
    range:
    - 100.0
    - 686700000000.0
    default: 10000000
    implemented: final
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MaxAcc

允许的最大加速度/减速度，在运动开始前进行检查。

## 概述

`MaxAcc` 用作允许的最大加速度/减速度。其行为在不同固件变体之间差异显著。

## 工作原理

在 **standalone / v4** 上，`MaxAcc` **未作为强制限值实现**。关键字表将其标记为 `implemented: partial`，访问标志为 `0`（用户不可写）；存储值从不被运动规划器、控制环或指令校验读取。换言之，在此变体上设置它没有任何效果。协调（CNC）运动的逐轴加速度限制由独立的 CNC 机制处理，而非由此关键字处理。

> 诚实说明：此关键字的 frontmatter 反映了这一点——standalone/v4 上为 `implemented: partial` 且 `access: 0`。请勿依赖 `MaxAcc` 在这些变体上钳位或拒绝运动。

## 版本间变化

在 **central-i v5** 上，`MaxAcc` 成为可写的强制限值，在运动开始时进行检查。如果运动的指令加速度或减速度将超过 `MaxAcc`，控制器拒绝开始该移动，`Begin` 以错误 324 被拒绝（与 [MaxVel](MaxVel.md) 以错误 271 对指令 Speed 进行门控的方式类似）。该运动开始检查适用于点到点和点动式规划移动；它不适用于间接模式（齿轮、脉冲方向、eCam、操纵杆、CNC），在这些模式中加速度/减速度由外部输入或主轴驱动，不受 `MaxAcc` 管控。不存在运行时加速度钳位或跳闸——`MaxAcc` 仅对移动的开始进行门控。

## 示例

```text
AMaxAcc[1]=2000000    ; central-i v5: max accel/decel (user units). No effect on standalone/v4.
AMaxAcc[1]            ; read back
```

## 另请参阅

- [MaxVel](MaxVel.md) — 速度限值（饱和 + 超速跳闸）
