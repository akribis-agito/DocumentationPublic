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

If force operation mode is entered while no analog input has been assigned the force-feedback function, the force loop cannot run: [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1046 (no force feedback) and the motor is turned off. Assign the feedback channel with [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) before commanding force mode.

## Examples

```text
AForce              ; read the force feedback
```

## See also

- [ForceRef](ForceRef.md) — filtered force reference the loop tracks
- [ForceErr](ForceErr.md) — ForceRef minus Force
- [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) — configures the analog force-feedback input (required for force mode)
