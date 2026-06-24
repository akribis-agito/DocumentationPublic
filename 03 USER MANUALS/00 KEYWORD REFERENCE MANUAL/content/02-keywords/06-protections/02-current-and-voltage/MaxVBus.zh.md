---
keyword: MaxVBus
summary: 允许的最大母线电压；持续超限将禁用轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 92
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 12000
  - 95000
  default: 95000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# MaxVBus

允许的最大母线电压；持续超限将禁用轴。

## 概述

`MaxVBus` 是允许的最大母线电压，单位为 mV。如果实际母线电压超过该限值的时间超过 [MaxVBusTime](MaxVBusTime.md)，则轴被禁用并触发故障。如需瞬时（无延迟）过压上限，请参见 [MaxVBusAbs](MaxVBusAbs.md)。

## 工作原理

母线电压（`VBus`）会被周期性检查（每第 16 个控制周期检查一次）。每次检查时：

- 如果 `VBus ≥ MaxVBus`，则累加过压计时器（并置位 [StatReg](../../07-status-and-faults/StatReg.md) 第 3 位）；否则计时器复位为 0。
- 当计时器在仍处于超限状态下达到 [MaxVBusTime](MaxVBusTime.md) 时，轴被禁用，且 [ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1008（母线电压过高）。

这种带时间窗口的跳闸可容忍短暂的过压瞬变（例如再生尖峰）。若在 `MaxVBusTime` 经过之前短暂偏移即回落到 `MaxVBus` 以下，则计时器复位且*不*跳闸——只有持续超限才会跳闸：

![Timeline showing VBus rising above MaxVBus, the over-voltage timer accumulating, and the trip firing when the timer reaches MaxVBusTime with the axis still over the limit](maxvbus-time-window.svg)

为告警目的，当 `VBus` 接近限值时，驱动器还会在 [StatReg](../../07-status-and-faults/StatReg.md)（第 7–8 位）中报告多级 VBus 告警，分段为 `MaxVBus` 的 0.88 / 0.92 / 0.96 倍（低 / 中 / 高）。

### 边界情况

- **电机失能：** 母线电压告警及其计时器继续运行（[StatReg](../../07-status-and-faults/StatReg.md) 的过 VBus 与告警位仍会更新），但禁用性跳闸本身仅在电机使能时才触发——跳闸路径以轴处于使能状态为门控条件。
- **模式依赖性：** 无论运行模式如何，跳闸均会运行。
- **`MaxVBusTime = 0`：** 在第一次检测到母线电压高于 `MaxVBus` 的检查时即跳闸，实际上为瞬时（速度与 [MaxVBusAbs](MaxVBusAbs.md) 相同，但使用 `MaxVBus` 作为阈值）。
- **计时器分辨率与阈值：** 过压计时器每次推进一个母线检查周期（母线电压每第 16 个控制周期检查一次），并在 [MaxVBusTime](MaxVBusTime.md) 处饱和。计时器累加与 [StatReg](../../07-status-and-faults/StatReg.md) 过 VBus 告警使用 `VBus ≥ MaxVBus`，而禁用性跳闸使用严格的 `VBus > MaxVBus`，且仅在计时器达到 `MaxVBusTime` 后才触发。`MaxVBusTime` 以毫秒输入并在内部转换为采样数，因此在标准（16 kHz）产品上，有效计时器分辨率为一个母线检查周期（约 1 ms）。
- **范围溢出：** 超出 `12000…95000`（mV）的写入将以超范围错误被拒绝；所存储的值保持不变。请将 `MaxVBus` 设在 [MaxVBusAbs](MaxVBusAbs.md) 以下，以便定时分段在正常再生瞬变时先起作用。
- **清除故障：** ConFlt 码 1008 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）时或通过写入 `AConFlt=0` 清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 条目则保留。
- **HWProtectBits / ProtectMask：** 母线电压跳闸不可通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽。

> **示例演算：** 在 `MaxVBus = 80000`（80 V）与 `MaxVBusTime = 200`（ms）的情况下，如果 `VBus` 升至 82 V 并保持 250 ms，则计时器在仍超限时达到 200 ms，轴被禁用并 `ConFlt = 1008`。若再生尖峰短暂达到 82 V 持续 50 ms 后回落至 70 V，则计时器复位且不跳闸——但只要其超过 [MaxVBusAbs](MaxVBusAbs.md)，就会*立即*跳闸（无延迟）。

## 示例

```text
AMaxVBus=80000       ; 80 V maximum bus voltage (mV)
```

### 操作演练：布置母线电压保护分段

设置三个母线电压限值，使定时上限与瞬时上限正确叠置，并使欠压跳闸捕捉到掉电情况：

```text
AMinVBus=18000        ; 18 V brown-out floor (immediate trip)
AMaxVBus=80000        ; 80 V timed ceiling
AMaxVBusTime=200      ; 200 ms window for sustained over-voltage
AMaxVBusAbs=90000     ; 90 V hard backstop (immediate trip)
```

运行最坏情况的再生场景（重负载的快速减速），并观察告警分段与跳闸码：

```text
AStatReg                       ; bit 3 set while over MaxVBus (timer running)
                               ; bits 7-8 give the 4-level warning (0.88 / 0.92 / 0.96 of MaxVBus)
AConFlt                        ; 1008 timed over-voltage, 1023 absolute over-voltage, 1009 under-voltage
```

如果在母线上观察到 90 V 再生尖峰，请提高 `MaxVBusAbs` 或降低减速度，使尖峰保持在定时分段之内；如果定时跳闸（1008）反复触发，只有在确认电源和制动电阻能够吸收再生能量后，才延长 `MaxVBusTime`。

## 另请参阅

- [MinVBus](MinVBus.md) — 最小母线电压
- [MaxVBusTime](MaxVBusTime.md) — 跳闸前的超范围时间
- [MaxVBusAbs](MaxVBusAbs.md) — 瞬时过压跳闸
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 跳闸时触发的故障 1008
- [StatReg](../../07-status-and-faults/StatReg.md) — 第 3 位（过 MaxVBus）与第 7–8 位（VBus 告警）
