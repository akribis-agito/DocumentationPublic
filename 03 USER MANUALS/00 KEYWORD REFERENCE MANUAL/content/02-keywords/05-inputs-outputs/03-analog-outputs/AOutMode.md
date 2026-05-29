---
keyword: AOutMode
summary: Selects direct command mode or parameter-monitoring mode for each analog output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 220
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
---
# AOutMode

Selects direct command mode or parameter-monitoring mode for each analog output.

## Overview

`AOutMode` sets whether an analog output is in **direct command mode** or **monitoring mode**. The array index is the analog-output number (1-based: `AOutMode[1]` is analog output 1, `AOutMode[2]` is analog output 2). The value is not a fixed enumeration — apart from `0`, any value is interpreted as a **Complex CAN code (CCC)** identifying the parameter to emulate.

| Value | Mode |
|-------|------|
| 0 | Direct command mode — the output follows [AOutPort](AOutPort.md) |
| CCC | Monitoring mode — the output emulates the parameter whose Complex CAN code (CCC) is given |

In monitoring mode the emulated parameter is treated as millivolts, scaled by [AOutShifts](AOutShifts.md) and offset by [AOutOffset](AOutOffset.md). See the [analog-output overview](00-overview.md).

## How it works

Writing `AOutMode[Index]` does two things:

1. **Sets the per-output direct/monitor flag.** The output is forced into direct mode when the value is `0`, or when the related amplifier is an analog-current-command / built-in-linear type (in which case the DAC is driving the amplifier current command regardless). Otherwise the output is placed in monitoring mode.

2. **Resolves the CCC to a parameter.** The Complex CAN code packs three things — a CAN keyword code, an axis selector, and an array index — which are unpacked and validated (keyword code, axis, array index, and that the target is a parameter). The output then tracks that parameter. If the CCC is invalid, the output rests at 0 mV.

Each control cycle, for an output in monitoring mode, the monitored parameter is read, shifted by [AOutShifts](AOutShifts.md), offset by [AOutOffset](AOutOffset.md), converted to a DAC code and clamped:

$$
\text{DAC code} = \big((\text{parameter} \ll \text{AOutShifts}) + \text{AOutOffset}\big) \cdot \text{(mV-to-DAC factor)}
$$

(A negative `AOutShifts` shifts right instead.) Because the emulated parameter is treated as millivolts, choose `AOutShifts` so the parameter's internal range maps usefully onto ±11905 mV.

Each analog-output index maps to a fixed DAC channel: index 1 → DAC A, index 2 → DAC B, index 3 → C, index 4 → D.

## Examples

```text
AAOutMode[1]=0       ; direct command mode (output follows AOutPort[1])
AAOutMode[1]=<CCC>   ; monitor a parameter (use its Complex CAN code)
AAOutMode[1]          ; read back the configured mode
```

### Edge cases

- **Index 0** — invalid; valid indices are `AOutMode[1]`–`AOutMode[4]`. `AOutMode[0]` does not exist.
- **Invalid CCC** — if the Complex CAN code fails validation (unknown keyword, bad axis, out-of-range array index, or the target is a function rather than a parameter), the output is forced to `0 mV` rather than tracking a stale or undefined value.
- **Forced direct mode** — if the amplifier is an analog-current-command or built-in-linear type, the DAC drives the amplifier current command regardless of `AOutMode`; setting a CCC has no effect in that case.
- **Wrong scaling** — in monitoring mode, the monitored parameter is treated as millivolts; without an appropriate [AOutShifts](AOutShifts.md) ([AOutGain](AOutGain.md) on v5) the output saturates.
- **Mode independence** — `AOutMode` itself takes effect immediately and is independent of [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) and `MotorOn`. The monitored parameter may be one that is only meaningful in certain modes (e.g. monitoring `VelRef` while in current mode shows whatever the velocity loop holds, not active control).
- **Save** — flash-saveable; reloaded at boot.
- **Platform** — code path is the same on standalone v4, central-i v4 and central-i v5; the v5 difference is in the scaler ([AOutGain](AOutGain.md) instead of [AOutShifts](AOutShifts.md)).

## See also

- [AOutPort](AOutPort.md) — commanded value (used only when this is `0`)
- [AOutShifts](AOutShifts.md) — power-of-two scaling applied to the monitored parameter
- [AOutOffset](AOutOffset.md) — output offset, added before the DAC conversion
- [analog-output overview](00-overview.md) — full signal path
