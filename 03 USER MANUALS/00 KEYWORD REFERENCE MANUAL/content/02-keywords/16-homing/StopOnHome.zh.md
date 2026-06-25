---
keyword: StopOnHome
summary: 当原点数字量输入状态变化时，自动停止轴运动。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 169
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# StopOnHome

当原点数字量输入状态变化时，自动停止轴运动。

## 概述

`StopOnHome` 用于使能原点开关停止功能。设置为非零值时，当点动过程中原点数字量输入*发生状态变化*，轴自动请求停止。该参数通常用于参考原点开关的回零过程——参见 [HomingDef](HomingDef.md) 中的"点动直至原点离散量输入状态变化"步骤——其工作方式与 [StopOnIndex](StopOnIndex.md) 类似（`StopOnIndex` 在编码器索引脉冲时停止）。该参数为轴作用域，不保存至闪存，可随时修改。

## 工作原理

`StopOnHome` 仅在点动或速度控制运动期间由运动规划器进行评估。每个控制周期，若 `StopOnHome` 为非零值且原点输入刚发生状态变化（由 [HomeStat](HomeStat.md) 衍生的内部单周期"原点变化"脉冲），运动规划器将：

1. 置位停止请求位，使运动减速至停止；
2. 将运动结束原因设置为"原点变化"（由 [MotionReason](../10-motion/05-motion-status/MotionReason.md) 报告，值为 16）；
3. 将 `StopOnHome` 清零至 `0`。

由于固件会自动清零，`StopOnHome` 属于一次性使能：读回 `0` 即可确认停止已触发，然后等待 [MotionStat](../10-motion/05-motion-status/MotionStat.md) 显示轴已不再运动。回零引擎在步骤 11 内部设置并依赖该标志；在回零之外，也可手动置位以实现自定义的点动至原点运动。

> 注意：触发条件为原点输入电平的*变化*，而非特定电平。"点动直至原点离散量输入状态变化"回零步骤使用 [HomeStat](HomeStat.md) 选择初始点动方向，从而确保运动总能穿越原点标志边沿。

## 示例

```text
AStopOnHome=1        ; 使能在下一次原点输入状态变化时停止
AStopOnHome         ; 0 = 已禁用 / 已触发，1 = 已使能
```

## 另请参阅

- [StopOnIndex](StopOnIndex.md) — 在编码器索引脉冲时停止的等效功能
- [HomeStat](HomeStat.md) — 该标志所响应的原点输入状态
- [MotionReason](../10-motion/05-motion-status/MotionReason.md) — 报告"原点变化"运动结束原因
- [HomingDef](HomingDef.md) — 回零步骤 11 点动至原点输入状态变化
