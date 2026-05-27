---
keyword: AOutOffset
summary: Offset (mV) added to the analog output, used to calibrate/zero it.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 227
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
  - -500
  - 500
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AOutOffset

Offset (mV) added to the analog output, used to calibrate/zero it.

## Overview

`AOutOffset` adds a fixed offset, in millivolts, to the analog output — the final stage of the [analog-output signal path](00-overview.md), applied after scaling. The array index is the analog-output number (e.g. `AOutOffset[2]` is analog output 2). Use it to calibrate or zero the output of a channel.

## Examples

```text
AAOutOffset[1]=-12   ; trim analog output 1 by -12 mV to zero it
```

## See also

- [AOutPort](AOutPort.md) — commanded value (direct mode)
- [AOutShifts](AOutShifts.md) — scaling (monitoring mode)
