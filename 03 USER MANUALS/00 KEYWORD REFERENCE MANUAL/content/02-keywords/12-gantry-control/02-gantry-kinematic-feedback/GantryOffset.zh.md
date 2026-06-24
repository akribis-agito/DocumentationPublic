---
keyword: GantryOffset
summary: 只读初始 A/B 位置偏置，在龙门模式开启时捕获。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 653
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GantryOffset

只读初始 A/B 位置偏置，在龙门模式开启时捕获。

## 概述

`GantryOffset` 是一个只读参数。`AGantryOffset` 在用户将 `AGantryOn` 从 `0` 切换至 `1` 时计算一次。它捕获两端位置参考之间的初始差值，以便从差值（[GantryFdbk](GantryFdbk.md)）计算中去除该固有偏置。若不捕获此偏置，龙门模式接入瞬间两电机之间的差值将表现为较大的偏摆误差，控制器会尝试以阶跃方式强制横梁对齐；通过折入所捕获的偏置，偏摆反馈可从干净的零值开始（参阅 [GantryOn](../01-general-variables/GantryOn.md) 中的共模/差模说明）。只要龙门模式保持开启，该值保持不变，并在下次 `0`→`1` 跳变时重新计算。以用户单位报告；在 central-i v5 上为 64 位值。

## 工作原理

偏置在 `0 → 1` 跳变时捕获，取两个成员轴**经整形、滤波后**的位置参考之差（即经平滑/整形/滤波后，位置环实际跟随的值）：

```text
AGantryOffset = APosRef - BPosRef
```

随后在龙门开启期间每周期将其折入龙门反馈：

```text
AGantryFdbk = (APos + BPos + AGantryOffset) / 2
BGantryFdbk = (APos - BPos - AGantryOffset)
```

在主轴（`A`，或 v5 上的 `C`/`E`/`G`）以外的任何轴上读取 `GantryOffset` 无意义，始终返回 `0`。

## 示例

```text
AGantryOffset      ; 读取已捕获的 A/B 偏置
```

### 边界情况

- **龙门关闭**（[GantryOn](../01-general-variables/GantryOn.md) = 0）——偏置保持上次捕获的值（若龙门从未接合则为 `0`）；不重新计算。
- **每次接合时捕获**——每次 `0 → 1` 跳变重新捕获偏置。若龙门关闭期间负载发生漂移，下次接合时将捕获新的机械关系，偏摆环再次从零开始。
- **只读**——写入被拒绝。
- **错误轴**——仅主轴存储有意义；在其他轴上读取返回 `0`。
- **接合前的值**——`0 → 1` 跳变时捕获的偏置取自 [PosRef](../../10-motion/01-kinematics-status/PosRef.md)（经整形/滤波后的位置参考），而非 [Pos](../../10-motion/01-kinematics-status/Pos.md)，因此静止轴（参考等于反馈）得到 `Pos[A] - Pos[B]`；具有非零跟踪误差的运动轴则得到整形参考差值。
- **平台**——v5 将存储扩展为 64 位，并支持多个龙门对（[GantryOn](../01-general-variables/GantryOn.md) 在 A/C/E/G 轴上）。

## 另请参阅

- [GantryFdbk](GantryFdbk.md) — 应用本偏置的龙门反馈
- [GantryOn](../01-general-variables/GantryOn.md) — 在 0→1 跳变时捕获偏置
