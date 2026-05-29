---
keyword: CanMotorOn
summary: Command that attempts to enable the motor after running pre-checks.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 129
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CanMotorOn

Command that attempts to enable the motor after running pre-checks.

## Overview

`CanMotorOn` is a command function that tests whether the axis *could* be enabled and reports the result in [CanMotorOnRes](CanMotorOnRes.md). It is an axis-related command and can be issued at any time.

Important: `CanMotorOn` does **not** turn the motor on. It runs the same pre-condition checks that `MotorOn = 1` would run, but instead of enabling it writes either `1` (all checks passed — enabling would succeed) or the error/fault code of the first failed check into [CanMotorOnRes](CanMotorOnRes.md). To actually enable the axis you still write [MotorOn](MotorOn.md) `= 1`. Use `CanMotorOn` first when you want to know *why* an enable would be refused without provoking an error response.

## How it works

`CanMotorOn` sets `CanMotorOnRes = 1` and then walks a single-pass chain of checks, breaking out at the first failure and storing that reason code:

1. The **same pre-conditions checked when enabling with [MotorOn](MotorOn.md)**, in the same order: FPGA / variant / full-scale health, Central-i port active and device is an amplifier with relay closed, overall current limit, **commutation complete**, inrush bypassed, CalcFilters succeeded, filters not modified.
2. Then the **interrupt-level protections** that would fault the axis even at standstill: hardware-protection conditions (STO1/STO2, encoder error, over-current, IPM fault, watchdog, 5 V faults, AC power phases), unknown encoder type, missing power supplies, bus over/under-voltage, logic over/under-voltage, board / IPM / motor over-temperature, and illegal modulo-with-input-shaping.

If the motor is already on, or `MotorType` = simulation, or the amplifier is a PD type, the result is left at `1`.

The check is a **snapshot**: time-dependent protections (e.g. a `MaxVBus` over-voltage that needs to persist) and anything that can only happen after enabling (position/velocity-error, stall, high current) are *not* covered, so `MotorOn = 1` can still fail or the axis can trip shortly after enabling even when `CanMotorOn` returned `1`.

## Examples

```text
ACanMotorOn          ; run the pre-checks (does not enable the motor)
ACanMotorOnRes       ; 1 = enabling would succeed, otherwise the reject/fault code
AMotorOn=1           ; actually enable the axis
```

## See also

- [CanMotorOnRes](CanMotorOnRes.md) — result code this command writes
- [MotorOn](MotorOn.md) — the keyword that actually enables/disables the motor
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault codes that `CanMotorOnRes` can echo back
- [StatReg](../../07-status-and-faults/StatReg.md) — commutation / filter status bits the checks read
