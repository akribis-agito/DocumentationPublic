---
keyword: HomeStat
summary: 只读位域，报告轴的回零状态。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 111
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
---
# HomeStat

轴的原点数字量输入的只读状态。

## 概述

尽管名称如此，`HomeStat` *并非*回零过程的状态字。它报告已分配 **Home** 功能的数字量输入的当前逻辑状态：原点输入有效时为 `1`，无效时为 `0`。回零*过程*由 [HomingStat](HomingStat.md)（各步骤状态及错误码）和 [HomingStep](HomingStep.md)（当前步骤）单独跟踪。

`HomeStat` 在每次采样原点输入时更新。任一方向的跳变（0→1 或 1→0）均会触发内部单周期的"原点变化"脉冲；回零引擎和 [StopOnHome](StopOnHome.md) 正是对这一脉冲作出响应——详见"工作原理"。该参数为轴相关只读变量，不保存至闪存。

## 工作原理

当某输入被配置为 Home 功能后，控制器对其进行采样，并将 `HomeStat` 维护为该输入经消抖后的电平。电平发生任何变化时均会触发内部单周期的"原点变化"脉冲；该脉冲用于：

- [StopOnHome](StopOnHome.md) 机制据此停止运动，以及
- [HomingDef](HomingDef.md) 中"点动直至原点数字量输入发生变化"回零步骤（指令 `11`）等待该脉冲以完成步骤。

步骤 `11` 的逻辑还会在运动开始时读取 `HomeStat` 以判断方向：若 `HomeStat` 为 `0`，则按配置的点动速度原方向运动；若 `HomeStat` 为 `1`，则方向取反，使轴始终向原点标志的边缘运动。

| HomeStat | 含义 |
|---|---|
| 0 | 原点输入未有效。 |
| 1 | 原点输入已有效。 |

若无输入被分配 Home 功能，`HomeStat` 保持默认值且不会改变。

## 示例

```text
AHomeStat           ; 0 = 原点输入未有效，1 = 已有效
```

## 另请参阅

- [StopOnHome](StopOnHome.md) — 在该输入发生变化时停止运动
- [HomingStat](HomingStat.md) — 实际的回零过程状态及错误码
- [HomingStep](HomingStep.md) — 当前回零步骤
- [HomingDef](HomingDef.md) — 步骤 11 点动直至该输入发生变化
- [HomingOn](HomingOn.md) — 启动回零过程
