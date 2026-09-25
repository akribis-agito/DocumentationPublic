---
keyword: MinVBus
summary: 允许的最小母线电压；降至或低于它将立即禁用轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 89
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
  - 11000
  - 90000
  default: 11000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MinVBus

允许的最小母线电压；降至或低于它将立即禁用轴。

## 概述

`MinVBus` 是允许的最小母线电压，单位为 mV。如果实际母线电压降至或低于该限值，则轴被禁用并触发故障。这可防范掉电 / 供电丢失情况。

## 工作原理

在每次周期性母线电压检查时，驱动器将 `VBus` 与 `MinVBus` 比较：

- 如果在电机使能时 `VBus ≤ MinVBus`，则轴被禁用，且 [ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1009（母线电压过低）。同样的条件也会阻止 [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) 请求：在 `VBus ≤ MinVBus` 期间，驱动器拒绝使能轴并返回故障码 1009。
- 当 `VBus` 从上方接近限值时，会在 [StatReg](../../07-status-and-faults/StatReg.md)（第 7–8 位）中报告多级欠压告警，分段为 `MinVBus` 的 1.12 / 1.08 / 1.04 倍（低 / 中 / 高）；在等于或低于 `MinVBus` 时，置位第 4 位（欠 MinVBus）。

> **注意：** 与过压跳闸不同，欠压跳闸是**立即**的——它*不*使用 [MaxVBusTime](MaxVBusTime.md) 延迟。

> **示例演算：** 在 `MinVBus = 18000`（18 V）的情况下，如果 `VBus` 在下一次母线检查时瞬间降至 17 V，则轴被禁用并 `ConFlt = 1009`。即使是单个低于 `MinVBus` 的采样也会跳闸；没有消抖或时间窗口。如需了解相对于过压分段和 `MaxVBusAbs` 上限的类别级视图，请参见[母线电压保护分段](00-overview.md)。

### 边界情况

- **电机失能：** 无论 `MotorOn` 如何，欠压*状态*（及多级告警）仍会更新，但禁用性跳闸仅在电机使能时才触发。当轴已失能时，欠压条件本身不会触发故障；相反，它会阻止轴被重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) 请求被以故障 1009 拒绝），直到供电恢复。
- **模式依赖性：** 无论运行模式如何，跳闸均会运行。
- **无延迟：** `MaxVBusTime` 仅用于过压路径；欠压始终为立即。
- **范围溢出：** 超出关键字 `range` 的写入将被钳位到该范围。
- **取值范围因驱动器系列而异。** 上方显示的 `range` 由单一固件配置解析得出，对应
  AGD200 / AGD301（48 V 级）：`11000…90000` mV。高压驱动器使用不同的范围：

  | 系列 | `MinVBus` 范围 (mV) | 默认值 |
  |---|---|---|
  | AGD200 / AGD301、AGD101-EC（48 V 级） | 11000…90000 | 11000 |
  | AGD155 / AGA155 / AGD155-EC、AGD156-EC（高压） | 100000…340000 | 100000 |

  请向驱动器查询实际限值，不要臆断；上表为各系列固件的编译期范围。
- **清除故障：** ConFlt 码 1009 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1，在供电恢复后）时或通过写入 `AConFlt=0` 清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 条目则保留。
- **HWProtectBits / ProtectMask：** 欠压跳闸不可通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽。

## 示例

```text
AMinVBus=18000       ; 18 V minimum bus voltage (mV)
```

## 另请参阅

- [MaxVBus](MaxVBus.md) — 最大母线电压
- [MaxVBusTime](MaxVBusTime.md) — 延迟（仅过压路径；此处不适用）
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 跳闸时触发的故障 1009
- [StatReg](../../07-status-and-faults/StatReg.md) — 第 4 位（欠 MinVBus）与第 7–8 位（VBus 告警）
