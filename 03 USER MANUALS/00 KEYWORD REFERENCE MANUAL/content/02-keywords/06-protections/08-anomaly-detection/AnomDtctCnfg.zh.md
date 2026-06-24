---
keyword: AnomDtctCnfg
summary: '异常检测的配置数组：监测源、滤波器极点、停止行为和运动选择。'
availability:
  standalone: []
  central-i:
  - v5
can_code: 779
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 13
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AnomDtctCnfg

异常检测的配置数组：监测源、滤波器极点、停止行为和运动选择。

## 概述

`AnomDtctCnfg` 保存定义异常检测器行为的设置：它监视哪个信号、如何对该信号进行滤波、检测到异常时采取何种动作，以及在重复序列中限值表适用于哪个运动。在使用 [AnomDtctOn](AnomDtctOn.md) 使能检测器之前，请先配置这些项目。

该数组是 1-indexed；最高可用索引为 12（索引 0 为保留）。范围内并非每个索引都承载设置——下面列出实际使用中的元素。

该关键字自 v5（central-i）起可用。

## 工作原理

| 索引 | 元素 |
| --- | --- |
| 1 | **监测源。** 要监视的信号的复合 CAN code（例如电流或力的读数）。控制器将该 code 解析为实时值，并在每个控制周期将其送入检测器。参见 [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md)。 |
| 2 | **滤波器极点频率**，单位 Hz。设置施加于监测信号的二阶低通滤波器的截止频率。若保持为 `0` 或更低，则默认为 200 Hz。写入此元素会立即重新计算滤波器。 |
| 10 | **检测到时的停止行为。** `0` = 禁用轴并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 上置故障码 1067；`1` = 改为执行受控停止而非触发故障。 |
| 11 | **运动情形**（保留）。存在于配置数组中，但本参考所参照的固件中检测器未对其采取动作。 |
| 12 | **运动序列。** 选择检测器跟踪哪个被监测运动模式。检测器在每次新运动开始时逐步遍历所选序列中的各运动，并对每个运动应用 [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) 表中的匹配区段。参见下面的取值表。 |

索引 3 至 9 在本参考所参照的固件中未被检测器使用。

元素 12 中的运动序列值选择单个被监测运动或一连串运动。随着每次后续运动开始，检测器推进到链中的下一个运动，并在序列结束时回绕至链的起点：

| 取值 | 运动序列 |
| --- | --- |
| 0 | 仅运动 0（默认） |
| 1 | 仅运动 1 |
| 2 | 仅运动 2 |
| 3 | 仅运动 3 |
| 4 | 运动 0 然后 1 |
| 5 | 运动 0、1、2 |
| 6 | 运动 0、1、2、3 |

有意义的范围为 0–6；默认值为 0（跟踪单个运动 0）。

监测信号在每个控制周期采样一次、滤波，并在 [AnomDtctSt](AnomDtctSt.md) 元素 2 中报告。当前运动的预期分段取自上/下限值表，每经过 [AnomDtctGap](AnomDtctGap.md) 个周期，针对该运动推进一个表点。

## 示例

```text
AAnomDtctCnfg[1]=<complex CAN code of monitored signal>   ; choose the source
AAnomDtctCnfg[2]=150     ; filter pole at 150 Hz
AAnomDtctCnfg[10]=1      ; controlled stop on detection (no fault)
AAnomDtctCnfg[12]=1      ; track single motion 1 only
AAnomDtctCnfg[2]         ; read the configured filter pole
```

## 另请参阅

- [AnomDtctOn](AnomDtctOn.md) — 配置后使能检测器
- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) — 预期分段表
- [AnomDtctGap](AnomDtctGap.md) — 每个限值表点对应的周期数
- [AnomDtctSt](AnomDtctSt.md) — 滤波后的值和检测器状态
- [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) — 如何寻址源信号
