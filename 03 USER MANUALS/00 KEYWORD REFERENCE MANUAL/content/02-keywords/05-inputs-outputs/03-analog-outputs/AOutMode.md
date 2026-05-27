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
  scope: axis
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
overrides: {}
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

Writing `AOutMode[Index]` runs the special function `SpAOutMode` (`SpecialFuncs.c:4866`), which does two things:

1. **Sets the per-output direct/monitor flag** `gsUseAOutPort[]`. The output is forced into direct mode (flag = 1) when the value is `0`, or when the related amplifier is an analog-current-command / built-in-linear type (in which case the DAC is driving the amplifier current command regardless). Otherwise the flag is cleared (flag = 0) and the output is in monitoring mode (`SpecialFuncs.c:4877`–`4883`).

2. **Resolves the CCC to a parameter pointer.** The Complex CAN code packs three things — a CAN keyword code, an axis selector, and an array index — which `ComplexCANToTokens` unpacks (`SpecialFuncs.c:4886`). The firmware then validates the keyword code, axis, array index and that the target is a parameter, and stores the address of that parameter's global into the analog-output pointer (e.g. `glpAnalogOutput1VariablePointer`). If the CCC is invalid, the pointer is aimed at a constant zero so the output rests at 0 mV (`SpecialFuncs.c:4889`–`4932`).

Each control cycle, for an output in monitoring mode (`gsUseAOutPort == 0`), the interrupt reads the pointed-to parameter, shifts it by [AOutShifts](AOutShifts.md), adds [AOutOffset](AOutOffset.md), converts to a DAC code and clamps it (`AG300_CTL01ControlInterrupt.c:12407`–`12426`):

$$
\text{DAC code} = \big((\text{parameter} \ll \text{AOutShifts}) + \text{AOutOffset}\big) \times \text{AOUT\_VALUE\_TO\_MV}
$$

(A negative `AOutShifts` shifts right instead.) Because the emulated parameter is treated as millivolts, choose `AOutShifts` so the parameter's internal range maps usefully onto ±11905 mV.

Each analog-output index maps to a fixed DAC channel: index 1 → DAC A, index 2 → DAC B, index 3 → C, index 4 → D.

## Examples

```text
AAOutMode[1]=0       ; direct command mode (output follows AOutPort[1])
AAOutMode[1]=<CCC>   ; monitor a parameter (use its Complex CAN code)
AAOutMode[1]          ; read back the configured mode
```

## See also

- [AOutPort](AOutPort.md) — commanded value (used only when this is `0`)
- [AOutShifts](AOutShifts.md) — power-of-two scaling applied to the monitored parameter
- [AOutOffset](AOutOffset.md) — output offset, added before the DAC conversion
- [analog-output overview](00-overview.md) — full signal path
