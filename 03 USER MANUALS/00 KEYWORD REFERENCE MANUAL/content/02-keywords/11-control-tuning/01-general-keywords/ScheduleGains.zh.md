---
keyword: ScheduleGains
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 274
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 6
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
overrides:
  central-i.v5:
    array_size: 7
    data_type: float32
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 只读数组，报告增益调度选定当前激活增益组后，控制环正在使用的整定增益。
---
# ScheduleGains

只读数组，报告增益调度选定当前激活增益组后，控制环正在使用的整定增益。

## 概述

`ScheduleGains` 是该轴当前有效调度增益的实时读数。每个数组元素存储一个增益值。当增益调度切换增益组时——或在插值模式下在增益组之间混合时——这些是实际产生的值，也是控制环实际应用的值。

| 索引 | 增益 |
|---|---|
| 1 | 位置环比例增益 |
| 2 | 加速度前馈增益 |
| 3 | 速度环比例增益 |
| 4 | 速度环积分增益 |
| 5 | 速度前馈增益 |
| 6 | 位置环积分增益（仅限 central-i v5） |

索引 6（位置环积分增益）仅在 central-i v5 上存在，其中 [PosKi](../03-position-control/PosKi.md) 可用且可参与调度。在 v4 上仅报告索引 1–5。

## 工作原理

每个控制周期，控制器根据 [ScheduleMode](ScheduleMode.md) 选择的规则确定激活的增益组编号（[ScheduleSet](ScheduleSet.md)），然后从该组加载 `ScheduleGains`：

- 在步进模式下，调度增益元素（v4 上为五个，central-i v5 上为六个）从激活组索引处对应的增益数组复制——例如 `ScheduleGains[2]` = [AccFFW](../05-feedforwards/AccFFW.md)`[set]`。
- 在插值模式（速度范围或位置范围）下，每个元素通过在当前测量值两侧的两个增益组之间线性插值计算得出，因此报告值连续变化而非阶跃变化。
- 当轴使用龙门配对调度时，增益取自龙门整定数组而非标准数组（参见 [ScheduleGntry](ScheduleGntry.md)）。

在无调度（`ScheduleMode = 0`）时，激活组始终为 1，因此每个 `ScheduleGains` 元素等于其对应增益关键字的第一个元素——例如 `ScheduleGains[2]` = `AccFFW[1]`，`ScheduleGains[1]` = `PosGain[1]`。

## 示例

```text
AScheduleGains[3]      ; read the velocity-loop proportional gain currently applied
AScheduleGains[1]      ; read the position-loop proportional gain currently applied
```

### 示例详解：确认当前激活的调度增益组

以速度分段调度（`ScheduleMode = 4`）为例，配置 `PosGain[1..3] = 400, 400, 250`，假设轴处于静止状态，[ScheduleSet](ScheduleSet.md) 读数为 `1`，则 `ScheduleGains[1]` 读数为 `400`（= `PosGain[1]`）。在指令快速运动使速度进入第三速度分段后，`ScheduleSet` 读数为 `3`，`ScheduleGains[1]` 读数为 `250`（= `PosGain[3]`）。`ScheduleGains` 的变化证实控制器已实际切换运行增益，而不仅仅是增益组编号。

## 另请参阅

- [ScheduleSet](ScheduleSet.md) — 选定这些值的激活增益组编号
- [ScheduleMode](ScheduleMode.md) — 驱动选择的规则
- [PosGain](../03-position-control/PosGain.md) / [PosKi](../03-position-control/PosKi.md) / [VelGain](../04-velocity-control/VelGain.md) / [VelKi](../04-velocity-control/VelKi.md) / [VelFFW](../05-feedforwards/VelFFW.md) / [AccFFW](../05-feedforwards/AccFFW.md) — 源增益数组
