---
keyword: MapErrOffRamp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 454
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
  - 1
  - 2147483647
  default: 16384
  scaling: 1.0
  implemented: final
overrides: {}
summary: 映射误差偏置向其目标值收敛的速率。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MapErrOffRamp

映射误差偏置向其目标值收敛的速率。

## 概述

`MapErrOffRamp` 设置*已应用*偏置向 [MapErrOffset](MapErrOffset.md) 目标值收敛的变化速率。以变化速率方式逐步逼近偏置，而非以阶跃方式应用，可避免校正反馈中出现位置突跳。值越大，收敛越快。它不同于 [MapErrOnStep](MapErrOnStep.md)（后者控制整个修正的单独接入/退出斜坡），也不同于 [MapType](MapType.md)（后者启用映射）。

它是一个轴相关参数，保存至闪存，可在任何时候更改，包括运动期间。

## 工作原理

该速率以**编码器 counts 每秒**为单位。每个控制周期，控制器将已应用偏置向 [MapErrOffset](MapErrOffset.md) 目标值移动 `MapErrOffRamp × SampleTime` counts（即每周期 `MapErrOffRamp / (每秒采样数)` counts），并在将要过冲的那个周期精确钳位到目标值上。默认值 `16384` 等于一个采样率单位，因此在基本采样率下，偏置每秒移动约 16384 counts。设置较小的值可实现有意的、缓慢的微调；较大的值则接近阶跃。

## 示例

```text
AMapErrOffRamp=16384 ; default slew rate (~16384 counts/s at base rate)
AMapErrOffRamp       ; read the current slew rate
```

### 边界情况

- **超出范围**——超出 `1`–`2 147 483 647` 的值被拒绝；最小值为 `1`，以保证有进展。
- **映射关闭**（[MapType](MapType.md) = 0）——值已存储，但在映射接入之前不影响反馈。
- **仿真电机**——跳过映射；变化速率没有可观察的效果。
- **运动中**——允许；运动期间偏置继续按速率变化。
- **保存**——可保存至闪存。

## 另请参阅

- [MapErrOffset](MapErrOffset.md) — 本关键字向其逼近的目标偏置
- [MapErrOnStep](MapErrOnStep.md) — 整个修正的单独接入/退出斜坡
- [MapType](MapType.md) — 启用误差映射
- [Pos](../10-motion/01-kinematics-status/Pos.md) — 受偏置影响的校正反馈
