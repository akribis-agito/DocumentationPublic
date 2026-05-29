---
keyword: PIVNoiseDtct
summary: "Enables run-time detection of excessive noise or jitter in the position/velocity loops while the axis is held at standstill."
availability:
  standalone: []
  central-i:
  - v5
can_code: 797
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PIVNoiseDtct

Enables run-time detection of excessive noise or jitter in the position/velocity loops while the axis is held at standstill.

## Overview

`PIVNoiseDtct` turns the PIV (position/velocity) noise detector on or off. When enabled, the controller watches how much the current reference produced by the position/velocity loops swings while the axis is being commanded to hold still. At a genuine standstill that reference should be quiet, so a large swing indicates noise or jitter feeding through the loops (for example from a noisy feedback signal or over-aggressive gains). If the swing is too large the controller turns the motor off and logs a fault.

| Value | Meaning |
|---|---|
| 0 | Detector disabled (default). |
| 1 | Detector enabled. |

This keyword is available from v5 (central-i) only.

## How it works

While the detector is enabled and the motor is on, the controller computes the spread (variance) of the current reference over a sliding window whose length is set by [PIVNoiseWSize](PIVNoiseWSize.md). The measurement is only evaluated when the axis is at a commanded standstill: the position reference must be unchanging and no signal injection may be active. The detector waits until the axis has been continuously at standstill for longer than the window (about one and a half window lengths) before it acts on the statistic, so the window holds only at-rest data and a normal move does not cause a false trip.

When the spread exceeds the threshold set by [PIVNoiseSTD](PIVNoiseSTD.md) (a percentage of the peak current limit, [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)), the controller turns the motor off and logs fault code 1072 (high noise/jitter detected), reported in [ConFlt](../../07-status-and-faults/ConFlt.md).

Enabling the detector takes effect when the motor is on; the statistics window and the standstill counter are cleared at that point. Setting the keyword back to 0 disables detection immediately. Because the detector can be turned on and off at any time, this keyword can be written while the axis is in motion and while the motor is on. The live statistic and active threshold can be read from [PIVNoiseStat](PIVNoiseStat.md).

## Examples

```text
APIVNoiseWSize=30     ; 30 ms statistics window
APIVNoiseSTD=2        ; threshold 2% of peak current limit
APIVNoiseDtct=1       ; enable the PIV noise detector
APIVNoiseDtct[1]      ; read back the enable state
```

## See also

- [PIVNoiseSTD](PIVNoiseSTD.md) — PIV noise spread threshold
- [PIVNoiseWSize](PIVNoiseWSize.md) — statistics window size
- [PIVNoiseStat](PIVNoiseStat.md) — PIV noise detector status array
- [ConFlt](../../07-status-and-faults/ConFlt.md) — controller fault code (1072 on detection)
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — peak current limit the threshold is scaled to
