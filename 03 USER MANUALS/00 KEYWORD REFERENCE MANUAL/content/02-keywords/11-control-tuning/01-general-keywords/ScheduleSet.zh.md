---
keyword: ScheduleSet
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 261
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
  - 1
  - 5
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 当前使用的整定增益组编号，范围为 1–5。
---
# ScheduleSet

当前使用的整定增益组编号，范围为 1–5。

## 概述

`ScheduleSet` 报告五个增益组中哪一个处于激活状态。激活的增益组决定 [ScheduleGains](ScheduleGains.md) 中发布的值以及控制环应用的值。在手动调度模式下，该关键字也可写，用户可直接选择增益组。

## 工作原理

`ScheduleSet` 的确定方式取决于 [ScheduleMode](ScheduleMode.md)：

- **无调度（`ScheduleMode = 0`）：** 保持为 1。
- **手动（`ScheduleMode = 1`）：** 由用户设置——可通过通信写入 `ScheduleSet`，或者，若数字量输入被分配了控制组切换功能，则由输入电平决定（低电平 → 1，高电平 → 2）。
- **自动模式（`ScheduleMode` ≥ 2）：** 控制器每个调度周期根据激活规则（运动/时间、到位状态、速度/位置/温度分段、PD 脉冲或 CNC 段）更新该值。在这些模式下，该值反映规则结果，不应由用户写入。

`ScheduleSet` 在上电时以及调度禁用时（`ScheduleMode = 0`）复位为 1。当调度模式的龙门配对与当前龙门状态不匹配时，使用默认增益组 1（参见 [ScheduleGntry](ScheduleGntry.md)）。

在插值速度/位置模式（`ScheduleMode = 9` 或 `10`）下，值为 `-1` 表示配置错误：四个分段阈值未严格递增，调度已被禁用，当前使用增益组 1。

## 示例

```text
AScheduleMode=1; AScheduleSet=3      ; manual mode, then select gain set 3
AScheduleSet                            ; read the active gain-set number
```

### 示例详解：检测插值模式配置错误

以 `ScheduleMode = 9`（速度，插值）为例，但 `ScheduleVel = [10000, 50000, 50000, 200000, ...]`（第三个阈值不大于第二个），控制器无法正常插值。读取 `ScheduleSet` 返回 `-1`，控制环回退至增益组 1。每当 `ScheduleVel`、`SchedulePos` 或 `ScheduleMode` 被写入时，阈值重新验证，因此写入严格递增的阈值即可清除该错误。

## 另请参阅

- [ScheduleMode](ScheduleMode.md) — 增益组的选择方式
- [ScheduleGains](ScheduleGains.md) — 激活增益组的增益值
