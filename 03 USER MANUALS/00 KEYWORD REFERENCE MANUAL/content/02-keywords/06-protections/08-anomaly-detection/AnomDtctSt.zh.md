---
keyword: AnomDtctSt
summary: 只读状态数组，报告检测器状态、滤波后信号值、当前生效分段以及当前生效运动。
availability:
  standalone: []
  central-i:
  - v5
can_code: 780
attributes:
  access: ro
  scope: axis
  flash: true
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
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# AnomDtctSt

只读状态数组，报告检测器状态、滤波后信号值、当前生效分段以及当前生效运动。

## 概述

`AnomDtctSt` 报告异常检测器当前正在执行的操作。它是该功能的主要诊断手段：它告诉你检测器是处于空闲、等待、正在检查还是已跳闸状态，并给出滤波后的信号值以及当前用于比较的分段。可用它来整定 [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) 限值表，并确认检测器正在跟踪你预期的运动。

该数组为只读。它由控制器更新，你无法对其写入。

该关键字自 v5（central-i）起可用。

## 工作原理

该数组为 1 索引（索引 0 为保留）。可用的元素为：

| 索引 | 元素 |
| --- | --- |
| 1 | 检测器的**状态**（见下方状态表）。 |
| 2 | **滤波后信号值** —— 经过低通滤波器后的被监测信号，即实际用于与分段比较的值。 |
| 3 | **当前生效下限** —— 在运动的当前位置上生效的 [AnomDtctLL](AnomDtctLL.md) 值。 |
| 4 | **当前生效上限** —— 在运动的当前位置上生效的 [AnomDtctUL](AnomDtctUL.md) 值。 |
| 5 | **当前生效运动** —— 检测器当前正在跟踪的被监测运动（0–3）。 |

元素 1 中报告的状态值：

| 值 | 含义 |
| --- | --- |
| 0 | 空闲。检测已关闭（[AnomDtctOn](AnomDtctOn.md) = 0）。 |
| 1 | 等待运动。检测已置位，但尚未有运动开始。 |
| 2 | 激活。检测器正在跟踪运动，并将滤波后信号与分段进行比较。 |
| 3 | 检测到异常。滤波后信号离开了分段。视 [AnomDtctCnfg](AnomDtctCnfg.md) 中的停止模式而定，轴要么被受控停止（不记录故障），要么电机被关闭并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 上触发故障码 1067。 |

另定义了一个保留状态值（4）用于挂起状态，但在本参考所参阅的固件中，检测器不会进入该状态。

当元素 1 报告为 3 时，检查元素 2、3 和 4 以了解信号超出分段的幅度及方向，并检查元素 5 以确认当时正在检查的是哪个运动。

## 示例

```text
AAnomDtctSt[1]     ; read the detector state
AAnomDtctSt[2]     ; read the filtered monitored value
AAnomDtctSt[3]     ; active lower limit
AAnomDtctSt[4]     ; active upper limit
AAnomDtctSt[5]     ; active monitored motion
```

## 参见

- [AnomDtctOn](AnomDtctOn.md) —— 置位或禁用检测器
- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) —— 当前生效限值来源的分段
- [AnomDtctCnfg](AnomDtctCnfg.md) —— 被监测源与停止行为
- [ConFlt](../../07-status-and-faults/ConFlt.md) —— 跳闸时触发的故障码 1067
