---
keyword: StallStat
summary: 只读步进失步（堵转）状态标志（0 = 无堵转，1 = 已堵转）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 514
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
# StallStat

只读步进失步（堵转）状态标志（0 = 无堵转，1 = 已堵转）。

## 概述

`StallStat` 是一个只读标志，报告步进失步（堵转）检测结果：`0` = 无堵转，`1` = 检测到堵转。它是由 [StallCfg](StallCfg.md) 使能的堵转保护组的状态输出。

## 工作原理

当 [StallCfg](StallCfg.md) 非零时，固件每个控制周期都会将实时度量值与阈值进行比较，并相应地设置 `StallStat`：

```text
if StallVal < StallTh
    StallStat = 1
    if StallCfg = 2 (motor-off mode)
        turn the axis off and log the stall fault
    set the StatReg stall bit (bit 31)
else
    clear the StatReg stall bit
    StallStat = 0
```

因此，无论是在仅告警模式（[StallCfg](StallCfg.md) = 1）还是电机关闭模式（[StallCfg](StallCfg.md) = 2）下，只要经滤波的度量值 [StallVal](StallVal.md) 降至计算得到的阈值 [StallTh](StallTh.md) 以下，`StallStat` 就会被设置。在检测处于激活状态时，它会跟踪 [StatReg](../../../07-status-and-faults/StatReg.md) 的 bit 31（`0x80000000`），该位在同一比较中被设置和清除。当度量值恢复至阈值以上时，该标志会自动清除。在检测禁用（[StallCfg](StallCfg.md) = 0）时，该标志不会更新；当电机失能时它会复位为 `0`。

### 边界情况

- **电机失能：** 检测模块不运行；`StallStat`、[StallVal](StallVal.md) 和 [StallTh](StallTh.md) 全部复位为 `0`。
- **非步进电机 / 外部驱动器：** 不生成度量值，因此无论 [StallCfg](StallCfg.md) 取值如何，`StallStat` 都保持为 `0`。
- **未整定的 [StallCnst](StallCnst.md)：** 在默认系数（两者均为 `0`）下，速度拟合项为 `0`，因此阈值输入仅剩 `−10000` 偏移，`StallTh` 滤波趋向一个负值。由于度量值 [StallVal](StallVal.md) 为非负值，`StallVal < StallTh` 永远不成立，`StallStat` 保持为 `0`——在针对电机/负载整定系数之前，永远不会标记任何堵转。
- **模式 2（电机关闭）：** 该轴以 [ConFlt](../../../07-status-and-faults/ConFlt.md) 代码 1065 被禁用。关闭电机会将 `StallStat` 复位为 `0`，但 [StatReg](../../../07-status-and-faults/StatReg.md) 堵转位（bit 31）在电机失能后会保留；它会在重新启动后、度量值高于阈值的第一个使能周期被清除。

## 示例

```text
AStallStat[1]         ; 0 = no stall, 1 = stall detected
```

## 另请参阅

- [StallCfg](StallCfg.md) — 使能检测并决定堵转是否也关闭电机
- [StallVal](StallVal.md) / [StallTh](StallTh.md) — 其比较结果设置此标志的度量值与阈值
- [StatReg](../../../07-status-and-faults/StatReg.md) — 堵转位（bit 31，`0x80000000`）镜像此标志
