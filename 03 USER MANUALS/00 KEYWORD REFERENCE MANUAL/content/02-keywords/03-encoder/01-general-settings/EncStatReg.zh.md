---
keyword: EncStatReg
summary: 只读状态寄存器，报告绝对式编码器的健康位（断开、错误、告警、CRC）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 422
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
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# EncStatReg

只读状态寄存器，报告绝对式编码器的健康位（断开、错误、告警、CRC）。

## 概述

`EncStatReg` 是一个只读的、轴相关的位域，报告**串行绝对式编码器**的健康状态。控制器每个控制周期从编码器接口刷新它，并保留低位的健康位。它是通用轴状态寄存器 [StatReg](../../07-status-and-faults/StatReg.md) 的编码器专用配套寄存器：当其中某一位指示持续故障时，轴会被关闭，相应的代码出现在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中。

该寄存器仅对反馈为串行绝对式编码器的轴有意义（参见 [EncType](EncType-AuxEncType.md)）。对于增量式、Sin/Cos 或其他反馈类型，这些位保持清零。它不保存至闪存，始终反映实时状态。

## 工作原理

控制器每个周期读取编码器接口状态，仅保留最低五位（掩码 `0x1F`）；更高位不予反映。有意义的健康位为：

| Bit | Mask | 置位时的含义 |
|---|---|---|
| 0 | `0x00000001` | 编码器未响应 / 看起来已断开。 |
| 1 | `0x00000002` | 编码器错误位被置位（编码器报告的读头或栅尺问题）。 |
| 2 | `0x00000004` | 被报告但控制器不对其采取动作（含义取决于协议——参见下面的*按编码器协议的位布局*）。 |
| 3 | `0x00000008` | 编码器告警被置位（编码器报告的劣化但非致命的状况）。 |
| 4 | `0x00000010` | 编码器数据帧的 CRC 校验失败（链路上很可能有高噪声）。 |

位 2（掩码 `0x00000004`）被保留并对上位机可见，但控制器不对其进行故障处理测试——它绝不会仅因位 2 而关闭轴。其含义取决于协议，因此不要仅因位 2 是唯一置位的位就认为编码器正常。

编码器告警（位 3，掩码 `0x00000008`）与错误位分开发出信号，但在故障处理上与其一同处理。要确认编码器正常，应测试所有这些健康位均不存在，而非依赖任何单一位。

对于 BiSS-C 编码器，帧以一个 6 位 CRC 结尾。接口每个控制周期对接收到的数据字段及其两个错误/告警状态位重新计算 CRC，并将其与编码器发送的 CRC 进行比较；不匹配会置位 CRC 位（位 4）。由于该校验在每一帧上运行，间歇性置位的 CRC 位指向边缘性的链路完整性问题（电缆长度、屏蔽、接地或连接器噪声），而非永久性故障——请在错误计数达到 [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) 限值且轴被关闭之前予以清除。

这些位如何被处理取决于 [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md)，即异常状况超时：

- **断开（位 0，无 CRC）：** 若电机使能，轴会被立即关闭，[ConFlt](../../07-status-and-faults/ConFlt.md) 报告故障 `1070`。对于无刷电机，换相状态也会被作废（必须重新定相），因为在编码器断开期间电机可能已移动。
- **CRC 错误（位 4）：** 在该状况持续期间，控制器外推位置并对周期计数。若该状况持续时间超过 [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) 个周期且电机使能，轴会被关闭，[ConFlt](../../07-status-and-faults/ConFlt.md) 报告故障 `1069`。
- **错误或告警（位 1，或告警状况）：** 以相同方式针对同一超时处理；超时到期时 [ConFlt](../../07-status-and-faults/ConFlt.md) 报告故障 `1068`。
- 当不存在任何异常位时，错误计数器复位。

将 [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) 设为 `-1` 会禁用错误/告警/CRC 监控（这些位仍可能被报告，但不会触发故障）。断开处理独立于 `EncAbsErrTime`。

此监控仅在上电初始化窗口关闭后才开始。上电时获取的首个绝对读数用于初始化位置，期间不检查这些状态位，因此损坏的上电帧可能将位置初始化为错误的绝对值（参见 [EncAbsOff](EncAbsOff-AuxEncAbsOff.md)）。在依赖所初始化的位置之前，请在引导启动后的若干周期确认 `EncStatReg` 干净。

### 按编码器协议的位布局

无论编码器类型如何，控制器都读取相同的五个状态位，并应用一种固定的解释（位 0 = 断开，位 1 = 错误，位 3 = 告警，位 4 = CRC）。对于 **BiSS-C / SIN-COS** 编码器，编码器接口与该解释完全对应：

| Bit (mask) | BiSS-C / SIN-COS |
|---|---|
| 0 (`0x01`) | 已断开 / 无响应 |
| 1 (`0x02`) | 幅值错误 |
| 2 (`0x04`) | 频率错误 |
| 3 (`0x08`) | 系统错误 |
| 4 (`0x10`) | 帧 CRC 失败 |

对于其他绝对协议（EnDat 2.2、Tamagawa），编码器接口将其原生的错误和 CRC 状况映射到这相同的五个位上，但每个状况的确切位位置可能因编码器类型和硬件变体而异。不要假设某特定协议将其 CRC 或错误标志置于某特定位上。要进行与协议无关的监控，应测试*所有*低位均不存在，而非某特定位位置。

## 示例

```text
AEncStatReg          ; read the absolute-encoder status bits

; test a specific condition (host-side bit test)
; bit 4 (0x10) set  -> CRC errors are occurring
; bit 0 (0x01) set  -> encoder looks disconnected
```

## 另请参阅

- [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) — 将持续的错误/告警/CRC 状况转换为故障的超时
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — 在此监控开始之前获取的上电位置初始化
- [EncType](EncType-AuxEncType.md) — 反馈类型；这些位适用于串行绝对式编码器
- [StatReg](../../07-status-and-faults/StatReg.md) — 通用轴状态寄存器
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 故障寄存器；针对这些状况报告代码 1068 / 1069 / 1070
