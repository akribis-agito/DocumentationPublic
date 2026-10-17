---
keyword: EncAbsErrTime
summary: 绝对式编码器错误/告警/CRC 状况在轴故障之前允许持续的控制周期数；-1 禁用监控。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 423
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
  - -1
  - 10000
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    implemented: partial
last_updated: '2026-10-17'
doc_revision: '2026.10'
language: zh-CN
---
# EncAbsErrTime

绝对式编码器错误/告警/CRC 状况在轴故障之前允许持续的控制周期数；-1 禁用监控。

## 概述

`EncAbsErrTime` 设置现有绝对式编码器错误处理策略对错误、告警或 CRC 状况的容忍时长。计数尚未超过阈值时，启用的错误处理使用位置外推；计数超过阈值且电机处于使能状态时，轴被关断，并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中记录对应代码。[EncStatReg](../01-general-settings/EncStatReg.md) 提供诊断信息，其当前值不一定是此处理策略所使用的依据。

它是按轴的参数，保存至闪存。该值是控制周期的计数（控制环以控制器固定的采样率运行，因此所容忍的时间为 `EncAbsErrTime` × 控制周期的周期时间）。有效范围为 `-1` 到 `10000`，默认值为 `-1`。它适用于使用串行绝对式编码器的轴（参见 [EncType](../01-general-settings/EncType-AuxEncType.md)）。

## 工作原理

每次执行现有绝对式编码器处理程序时，控制器处理该协议的错误策略输入：

| EncAbsErrTime | 行为 |
|---|---|
| -1 | 错误 / 告警 / CRC 监控被**禁用**：这些状况不计数，也不会使轴故障。 |
| 0 至 10000 | 持续的错误 / 告警 / CRC 状况会被计数；在计数期间，位置被外推以使运动继续，一旦计数超过此值，轴即故障。 |

两个可恢复的分组分别计数：

- **CRC 错误**（状态位 4）。到期时，[ConFlt](../../07-status-and-faults/ConFlt.md) 报告故障 `1069`。
- **错误 / 告警**（状态位 1，或位 3 处的告警状况）。到期时，[ConFlt](../../07-status-and-faults/ConFlt.md) 报告故障 `1068`。

一个干净的周期（无异常位）会复位计数器，因此只有持续时间超过 `EncAbsErrTime` 的*连续*状况才会产生故障——短暂的噪声毛刺通过外推被平滑度过。

现有的**主编码器保护**路径独立于 `EncAbsErrTime`，可产生 [ConFlt](../../07-status-and-faults/ConFlt.md) 故障 `1070`。在 Central-i 上，其物理含义取决于协议和 FPGA 镜像；位 0 不能统一解释为电缆断开。

## Central-i 已接受的位置与策略质量

在包含[已接受质量修复](https://github.com/akribis-agito/Firmware-Main/issues/1408)的 AGM800 和 AGM800-EC 固件中，活动的标准 AMP 主 BiSS-C、EnDat 和 Tamagawa 反馈使用通过 Central-i CRC1 检查、与主位置一起被接受的现有错误/告警/CRC 输入。通过 CRC1 的传输帧本身仍可能报告编码器错误。传输解码被拒绝或跳过时，已接受的位置及其策略质量均保持不变。

[EncStatReg](../01-general-settings/EncStatReg.md) 继续报告当前解码输入。因此，被拒绝的异常帧可以显示在诊断中，却不会为保留的正常样本启动编码器错误计数；被拒绝的正常帧可以清除诊断显示，却不会清除保留的异常样本所提供的策略依据。现有计数器仍按控制处理程序的执行次数计数，包括重复使用保留的异常质量，而不是按新回复数计数。`-1` 旁路、阈值及故障动作不变。

此归属规则不适用于本地控制器、辅助反馈、ADP05/AGFB、仿真或解析反馈源。复位后首个帧被接受之前，兼容性零值不代表反馈正常或已通过资格确认。初始化时序不变。此参数及清零的诊断寄存器均不能证明物理采样年龄或完整的 Tamagawa SF/ALMC 告警状态。

> [!caution]
> 设置 `-1` 会同时抑制错误、告警和 CRC 状况：在监控被禁用期间，它们都不会计入故障。**断开连接**状况独立于 `EncAbsErrTime`，且始终会被响应——`-1` 不会抑制断开连接故障。

> **可用性说明：** 在 Central-i v5 上，此关键字标记为部分实现。

## 示例

```text
AEncAbsErrTime=-1        ; disable error/warning/CRC monitoring (default)
AEncAbsErrTime=100       ; tolerate up to 100 control cycles of error/warning/CRC before faulting
AEncAbsErrTime           ; read the configured tolerance
```

## 另请参阅

- [EncStatReg](../01-general-settings/EncStatReg.md) — 当前编码器诊断及其与已接受策略质量的区别
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 故障寄存器；报告代码 1068 / 1069 / 1070
- [EncType](../01-general-settings/EncType-AuxEncType.md) — 反馈类型；此适用于串行绝对式编码器
