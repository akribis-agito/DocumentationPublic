---
keyword: Force
summary: Force feedback obtained from the analog input.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 582
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
overrides:
  central-i.v5:
    data_type: float32
---
# Force

Force feedback obtained from the analog input.

## Overview

`Force` is the force feedback obtained from the analog input. It takes the value of the filtered analog source linked to the force-feedback function (the analog port configured via [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)). It is the measured quantity that the force loop drives toward [ForceRef](ForceRef.md), with the difference reported as [ForceErr](ForceErr.md).

## How it works

Every control cycle the controller copies the filtered analog force-feedback channel into `Force`. `Force` is updated continuously regardless of the active [OperationMode](../01-general-keywords/OperationMode.md), so it can be read for monitoring even outside force mode.

This same conditioned filtered-analog reading is what the force loop uses as feedback: each cycle the loop forms `ForceErr = ForceRef - Force`, so the value shown by `Force` is exactly the quantity subtracted from the reference. The same reading is also compared against [ForceAInTh](ForceAInTh.md) for the analog (condition B) automatic entry into force mode. `Force` is the integer display copy of that internal reading (rounded for reporting); the loop and the threshold engine act on the underlying value.

If force operation mode is entered while no analog input has been assigned the force-feedback function, the force loop cannot run: [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1046 (no force feedback) and the motor is turned off. Assign the feedback channel with [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) before commanding force mode.

## Examples

```text
AForce              ; read the force feedback
```

### Edge cases

- **No analog force feedback configured** — `Force` reads `0`. Entering force mode in this state fails with [ConFlt](../../07-status-and-faults/ConFlt.md) = `1046` (no force feedback) and the motor is disabled.
- **Wrong mode** — `Force` is sampled every cycle regardless of [OperationMode](../01-general-keywords/OperationMode.md); the value is the live conditioned analog reading even outside force mode.
- **Motor off** — sampling continues; useful for monitoring the cell with the servo off.
- **Read-only** — writes are rejected.

## See also

- [ForceRef](ForceRef.md) — filtered force reference the loop tracks
- [ForceErr](ForceErr.md) — ForceRef minus Force
- [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) — configures the analog force-feedback input (required for force mode)
