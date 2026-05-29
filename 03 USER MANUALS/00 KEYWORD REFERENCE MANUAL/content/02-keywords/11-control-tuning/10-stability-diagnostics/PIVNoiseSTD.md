---
keyword: PIVNoiseSTD
summary: PIV noise spread threshold for standstill noise/jitter detection, in percent of the peak current limit.
availability:
  standalone: []
  central-i:
  - v5
can_code: 798
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.01
  - 100.0
  default: 2.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PIVNoiseSTD

PIV noise spread threshold for standstill noise/jitter detection, in percent of the peak current limit.

## Overview

`PIVNoiseSTD` sets the spread (standard-deviation) threshold used by the PIV noise detector ([PIVNoiseDtct](PIVNoiseDtct.md)). It defines how much the current reference is allowed to swing while the axis is held at standstill before the swing is treated as excessive noise or jitter.

The value is a percentage of the axis peak current limit ([PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)). A larger value makes the detector tolerate more standstill noise; a smaller value makes it trip on a quieter signal.

This keyword is available from v5 (central-i) only.

## How it works

While the detector is enabled and the axis has been at a commanded standstill long enough to fill its window (see [PIVNoiseWSize](PIVNoiseWSize.md)), the controller compares the spread of the current reference against this threshold. The percentage is scaled against the peak current limit and squared internally (the comparison is made on a variance basis), so the effective level tracks [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) automatically.

When the measured spread exceeds the threshold, the controller turns the motor off and logs fault code 1072, visible in [ConFlt](../../07-status-and-faults/ConFlt.md).

The value is saved to flash and can be changed while the axis is in motion and while the motor is on; the new threshold is applied the next time the detector is (re)enabled with the motor on. The active threshold can be read back from element 2 of [PIVNoiseStat](PIVNoiseStat.md).

## Examples

```text
APIVNoiseSTD=2        ; threshold = 2% of peak current limit
APIVNoiseSTD=5        ; tolerate more standstill noise before flagging
APIVNoiseSTD[1]       ; read back the configured percentage
```

## See also

- [PIVNoiseDtct](PIVNoiseDtct.md) — enable the PIV noise detector
- [PIVNoiseWSize](PIVNoiseWSize.md) — statistics window size
- [PIVNoiseStat](PIVNoiseStat.md) — PIV noise detector status array
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — peak current limit the threshold is scaled to
