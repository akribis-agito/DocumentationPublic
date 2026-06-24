---
keyword: MaxVBusAbs
summary: 绝对母线电压上限；超过它将立即禁用轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 94
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MaxVBusAbs

绝对母线电压上限；超过它将立即禁用轴。

## 概述

`MaxVBusAbs` 是允许的绝对最大母线电压，单位为 mV。如果母线电压超过 `MaxVBusAbs`，则轴被**瞬时**禁用——没有时间窗口。这是 [MaxVBus](MaxVBus.md) 的无延迟对应项，后者可容忍超限最长达 [MaxVBusTime](MaxVBusTime.md)。

## 工作原理

在每次周期性母线电压检查时，驱动器将 `VBus` 直接与 `MaxVBusAbs` 比较：

- 如果 `VBus > MaxVBusAbs`，则轴被立即禁用，且 [ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1023（母线电压过高——超过绝对限值）。
- 如果 `VBus ≥ MaxVBusAbs`，则置位 [StatReg](../../07-status-and-faults/StatReg.md) 第 6 位（过 MaxVBusAbs）作为状态指示。

由于不涉及计时器，请将 `MaxVBusAbs` 设在 [MaxVBus](MaxVBus.md) 以上，以便带时间窗口的限值在正常瞬变时先起作用，而 `MaxVBusAbs` 作为硬性后备。

> **示例演算：** 在 `MaxVBus = 80000`（80 V）、`MaxVBusTime = 200`（ms）与 `MaxVBusAbs = 90000`（90 V）的情况下，达到 82 V 的再生尖峰可被容忍最长 200 ms（仅在此之后 `ConFlt = 1008`）。达到 91 V 的尖峰会在下一次母线检查时立即跳闸并 `ConFlt = 1023`，与 `MaxVBusTime` 无关。

### 边界情况

- **电机失能：** 过 `MaxVBusAbs` 状态指示（[StatReg](../../07-status-and-faults/StatReg.md) 第 6 位）继续更新，但禁用性跳闸本身仅在电机使能时才触发——跳闸路径以轴处于使能状态为门控条件，与 [MaxVBus](MaxVBus.md) 相同。
- **模式依赖性：** 无论运行模式如何，跳闸均会运行。
- **无延迟：** 此处不适用 `MaxVBusTime`——`MaxVBusAbs` 是无条件的，并在下一次母线检查时起作用。
- **范围溢出：** 超出 `12000…95000`（mV）的写入将以超范围错误被拒绝；所存储的值保持不变。请设在 [MaxVBus](MaxVBus.md) 以上，以便定时分段先起作用。
- **清除故障：** ConFlt 码 1023 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）时或通过写入 `AConFlt=0` 清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 条目则保留。
- **HWProtectBits / ProtectMask：** 绝对过压跳闸不可通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽。

## 示例

```text
AMaxVBusAbs=90000    ; instantaneous over-voltage ceiling (mV)
```

## 另请参阅

- [MaxVBus](MaxVBus.md) — 带时间延迟的过压限值
- [MaxVBusTime](MaxVBusTime.md) — MaxVBus 所用的延迟（MinVBus 或 MaxVBusAbs 不使用）
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 跳闸时触发的故障 1023
- [StatReg](../../07-status-and-faults/StatReg.md) — 第 6 位标记过 MaxVBusAbs
