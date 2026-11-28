---
keyword: RecTrigPos
summary: Percentage of RecLength captured before the trigger (pre-trigger data).
availability:
- controller
- ci-master
can_code: 247
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  agc300-et:
    array_size: 2
  agd200-et-2d01:
    array_size: 2
  agd200-et-2d02:
    array_size: 2
  agd200-et-2d05:
    array_size: 2
  agd200-et-2d05-71:
    array_size: 2
  agd155-af-2a06:
    array_size: 2
  agd155-af-2a10:
    array_size: 2
  agd155-ec:
    array_size: 2
  agd155-ec-var34:
    array_size: 2
  agd155-ec-var34-3:
    array_size: 2
  agd156-ec:
    array_size: 2
  agd101-ec-34a:
    array_size: 2
  agd101-ec-17a:
    array_size: 2
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# RecTrigPos

Percentage of RecLength captured before the trigger (pre-trigger data).

## Overview

`RecTrigPos` defines the percentage of data points, out of [RecLength](RecLength.md), to capture before the trigger condition(s) activate. It is normally used during debugging to allow monitoring of the data leading up to the trigger event. Each array index selects a scope. Valid values are 0 to 100; [RecStart](RecStart.md) rejects the request with error 71 if the value is outside this range.

![RecTrigPos splits RecLength into a pre-trigger portion (RecTrigPos percent of RecLength) that captures the samples leading up to the trigger, and a post-trigger portion (the remainder) that captures the samples after the trigger fires](rectrigpos-buffer.svg)

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## Examples

```text
ARecTrigPos[1]=10    ; reserve 10% of RecLength for pre-trigger data
ARecTrigPos[1]      ; query the first scope pre-trigger percentage
```

If `RecLength[1] = 16384` and `RecTrigPos[1] = 10`, the first scope will have 1638 pre-trigger data points and 14746 post-trigger data points. The recorder rounds the pre-trigger count to the nearest whole sample per channel, rounding a half sample up.

With `RecLength[1] = 205` and `RecTrigPos[1] = 20`, each channel retains 41 samples before the trigger. The sample that satisfies the trigger is sample 42 and starts the remaining 164 samples. At 0% the triggering sample comes first. At 100% every retained sample precedes it. These positions apply to configured triggers on firmware containing the recorder correction. [Ring header fields](RecDataA-RecDataB.md) · [Firmware change #2675](https://github.com/akribis-agito/Firmware-Main/pull/2675)

## See also

- [RecLength](RecLength.md) — total data points per parameter
- [RecStat](RecStat.md) — reports when pre-trigger data is filled
- [RecTrigTyp](RecTrigTyp.md) — trigger activation type
