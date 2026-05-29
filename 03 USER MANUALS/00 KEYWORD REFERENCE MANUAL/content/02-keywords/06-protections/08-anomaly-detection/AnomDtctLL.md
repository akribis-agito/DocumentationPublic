---
keyword: AnomDtctLL
summary: Lower-limit table defining the bottom of the expected band the filtered signal is checked against, per monitored motion.
availability:
  standalone: []
  central-i:
  - v5
can_code: 777
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 1025
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
overrides: {}
---
# AnomDtctLL

Lower-limit table defining the bottom of the expected band the filtered signal is checked against, per monitored motion.

## Overview

`AnomDtctLL` is the lower boundary of the expected band for anomaly detection. Together with the upper-limit table [AnomDtctUL](AnomDtctUL.md) it describes the normal shape of a monitored signal as a motion progresses. When the filtered monitored signal falls below the lower limit in force at that point of the motion, the detector trips (see [AnomDtctCnfg](AnomDtctCnfg.md) for the stop behavior).

The table is large because it stores a full profile for each of several monitored motions, sampled point by point along each motion.

This keyword is available from v5 (central-i).

## How it works

The table is divided into one block per monitored motion (up to four motions). Each block holds up to 256 points. As the motion progresses, the detector advances one point at a time; [AnomDtctGap](AnomDtctGap.md) sets how many control cycles each point is held before moving to the next. The comparison begins at the **second** slot of each motion's block and advances one slot per gap window — the first slot of each block (index 1, 257, 513, 769) holds a value but is never compared against the signal.

The array is 1-indexed (index 0 is reserved); the highest usable index is one less than the frontmatter `array_size`. The blocks are laid out consecutively, matching [AnomDtctUL](AnomDtctUL.md) (the index ranges below show where values are *stored*):

| Index range | Monitored motion |
| --- | --- |
| 1 – 256 | motion 0 |
| 257 – 512 | motion 1 |
| 513 – 768 | motion 2 |
| 769 – 1024 | motion 3 |

The value at each index is compared in the native units of the selected monitored signal (`AnomDtctLL` itself carries no unit conversion). The current motion's active lower limit is mirrored to [AnomDtctSt](AnomDtctSt.md) element 3 so you can read what the detector is comparing against.

Populate the table with a lower envelope that sits comfortably below the signal seen during a known-good motion, leaving margin for normal cycle-to-cycle variation. The upper envelope goes in [AnomDtctUL](AnomDtctUL.md). The detector reports an anomaly when the filtered value is outside the band on either side.

## Examples

```text
AAnomDtctLL[1]=-12000    ; first stored slot of motion 0 (not compared; the walk starts at index 2)
AAnomDtctLL[2]=-12500    ; first compared lower-limit point of motion 0
AAnomDtctLL[257]=-8000   ; first stored slot of motion 1's block (not compared; comparison starts at index 258)
AAnomDtctLL[2]           ; read the first compared lower-limit point
```

## See also

- [AnomDtctUL](AnomDtctUL.md) — upper boundary of the band
- [AnomDtctGap](AnomDtctGap.md) — control cycles spanned by each table point
- [AnomDtctCnfg](AnomDtctCnfg.md) — monitored source and motion selection
- [AnomDtctSt](AnomDtctSt.md) — active limits and filtered value
