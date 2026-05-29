---
keyword: ForceMotorOn
summary: Enables the motor before commutation is done, for current-loop tuning only.
availability:
  standalone: []
  central-i:
  - v5
can_code: 829
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
# ForceMotorOn

Enables the motor before commutation is done, for current-loop tuning only.

## Overview

`ForceMotorOn` enables the motor **even though the axis has not been commutated (phased) yet**. Normally the controller refuses to enable an un-phased axis, and it will trip an enabled axis off the instant phasing is found to be missing, because driving an un-phased motor can inject DC current into a single winding. `ForceMotorOn` is the deliberate, guarded exception to that rule: it is intended for **current-loop tuning**, where you need the power stage live while the motor is held under current control before phasing has been performed.

Because it overrides a safety interlock, the enable is protected. Writing `ForceMotorOn` only takes effect when the write carries the specific reserved value **`555851`**; any other value is rejected with an error and the motor is not forced on. Reading `ForceMotorOn` returns the current state: `1` while the forced-on (un-phased) enable is active, `0` otherwise.

Available on central-i (v5).

## How it works

`ForceMotorOn` does not replace the normal enable path — it removes one specific pre-condition from it. When you write the reserved value:

1. If the axis is not yet phased, `ForceMotorOn` is set to `1` for that axis, and (if the axis is currently off) the controller runs the standard [MotorOn](MotorOn.md) enable sequence. All the other [MotorOn](MotorOn.md) pre-conditions and the post-enable steps are still performed exactly as usual — only the **commutation-done** requirement is waived (the same waiver used by production burn-in).
2. While `ForceMotorOn = 1`, the protection that disables an un-phased axis is held off, so the axis can stay enabled under current control without phasing.
3. If the axis belongs to a gantry pair and a member is not commutated, gantry control is dropped first so the force-on can proceed on the individual axis.

The waiver is strictly tied to the forced state. As soon as the motor turns off (by command or by any fault), `ForceMotorOn` returns to `0`, and the normal interlock is back in force: an enabled axis that is found to be un-phased while `ForceMotorOn = 0` is disabled automatically and a controller fault is recorded (read [ConFlt](../../07-status-and-faults/ConFlt.md) for the code — it reports a "no phasing detected" condition). To force the motor on again you must re-issue the reserved value.

`ForceMotorOn` does **not** bypass any of the other enable checks — hardware health, communication, inrush bypass, drained-bus and protection conditions all still apply, just as for [MotorOn](MotorOn.md). It only lets you operate the current loop before phasing; it is not a way to run position or velocity moves on an un-phased axis.

## Examples

Bring an un-phased axis live for current-loop tuning (current control mode):

```text
AOperationMode=1     ; current control mode (writable only while disabled)
AForceMotorOn=555851 ; enable the motor without phasing (reserved value required)
AForceMotorOn        ; expect 1 = forced on (un-phased)
AMotorOn             ; expect 1 = servo on
                     ; ... perform current-loop tuning ...
AMotorOn=0           ; disable; ForceMotorOn returns to 0 automatically
```

### Edge cases

- **Wrong write value** — any value other than `555851` is rejected with an error; the motor is not forced on.
- **Already phased** — if the axis is already commutated there is nothing to waive; the normal [MotorOn](MotorOn.md) path applies.
- **Other pre-conditions still fail** — the forced enable still runs the full [MotorOn](MotorOn.md) pre-check chain (hardware, communication, inrush, protections); a failure there still rejects the enable.
- **Auto-clear on motor off** — turning the motor off, or any fault that disables it, resets `ForceMotorOn` to `0`; the no-phasing protection then re-arms.
- **No-phasing trip** — if an enabled axis is found un-phased while `ForceMotorOn = 0`, it is disabled and [ConFlt](../../07-status-and-faults/ConFlt.md) records a no-phasing fault. See [MotorReason](../../07-status-and-faults/MotorReason.md).
- **Gantry** — gantry control is dropped for an un-phased pair before the force-on proceeds.
- **Intended use** — current-loop tuning only. Do not use it to attempt position/velocity motion on an un-phased motor.
- **Platform** — v5 central-i only.

## See also

- [MotorOn](MotorOn.md) — normal enable/disable; `ForceMotorOn` waives only its commutation-done pre-condition
- [CanMotorOn](CanMotorOn.md) / [CanMotorOnRes](CanMotorOnRes.md) — pre-check whether a normal enable would succeed
- [ConFlt](../../07-status-and-faults/ConFlt.md) — records the no-phasing fault when an un-phased axis is enabled without forcing
- [MotorReason](../../07-status-and-faults/MotorReason.md) — why the axis was last disabled
- [OperationMode](OperationMode.md) — select current control mode for current-loop tuning
