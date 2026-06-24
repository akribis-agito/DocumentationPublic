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
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsErrTime

绝对式编码器错误/告警/CRC 状况在轴故障之前允许持续的控制周期数；-1 禁用监控。

## 概述

`EncAbsErrTime` 设置在控制器将可恢复的绝对式编码器问题视为故障之前对其容忍的时长。当某问题在 [EncStatReg](../01-general-settings/EncStatReg.md) 中被标记时，控制器会以外推位置使轴继续运行，最多持续这么多个控制周期；如果在此之后该状况仍然存在，且电机处于使能状态，则轴被关断，并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中记录对应的代码。

它是按轴的参数，保存至闪存。该值是控制周期的计数（控制环以控制器固定的采样率运行，因此所容忍的时间为 `EncAbsErrTime` × 控制周期的周期时间）。有效范围为 `-1` 到 `10000`，默认值为 `-1`。它适用于使用串行绝对式编码器的轴（参见 [EncType](../01-general-settings/EncType-AuxEncType.md)）。

## 工作原理

每个控制周期，控制器检查绝对式编码器的状态位（[EncStatReg](../01-general-settings/EncStatReg.md)）：

| EncAbsErrTime | Behaviour |
|---|---|
| -1 | 错误 / 告警 / CRC 监控被**禁用**：这些状况不计数，也不会使轴故障。 |
| 0 to 10000 | 持续的错误 / 告警 / CRC 状况会被计数；在计数期间，位置被外推以使运动继续，一旦计数超过此值，轴即故障。 |

两个可恢复的分组分别计数：

- **CRC 错误**（状态位 4）。到期时，[ConFlt](../../07-status-and-faults/ConFlt.md) 报告故障 `1069`。
- **错误 / 告警**（状态位 1，或位 3 处的告警状况）。到期时，[ConFlt](../../07-status-and-faults/ConFlt.md) 报告故障 `1068`。

一个干净的周期（无异常位）会复位计数器，因此只有持续时间超过 `EncAbsErrTime` 的*连续*状况才会产生故障——短暂的噪声毛刺通过外推被平滑度过。

真正的**断开连接**（状态位 0）单独处理，**不**受 `EncAbsErrTime` 管控：它会立即关断轴（[ConFlt](../../07-status-and-faults/ConFlt.md) 故障 `1070`）。

> [!caution]
> 设置 `-1` 会同时抑制错误、告警和 CRC 状况：在监控被禁用期间，它们都不会计入故障。**断开连接**状况独立于 `EncAbsErrTime`，且始终会被响应——`-1` 不会抑制断开连接故障。

> **可用性说明：** 在 Central-i v5 上，此关键字标记为部分实现。

## 示例

```text
AEncAbsErrTime=-1        ; disable error/warning/CRC monitoring (default)
AEncAbsErrTime=100       ; tolerate up to 100 control cycles of error/warning/CRC before faulting
AEncAbsErrTime           ; read the configured tolerance
```

## 参见

- [EncStatReg](../01-general-settings/EncStatReg.md) — 此超时所作用的编码器状态位
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 故障寄存器；报告代码 1068 / 1069 / 1070
- [EncType](../01-general-settings/EncType-AuxEncType.md) — 反馈类型；此适用于串行绝对式编码器
