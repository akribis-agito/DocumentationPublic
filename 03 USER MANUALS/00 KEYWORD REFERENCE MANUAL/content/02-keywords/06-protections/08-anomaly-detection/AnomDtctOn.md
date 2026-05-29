---
keyword: AnomDtctOn
summary: Enables or disables anomaly (collision) detection on the axis.
availability:
  standalone: []
  central-i:
  - v5
can_code: 778
attributes:
  access: rw
  scope: axis
  flash: true
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
# AnomDtctOn

Enables or disables anomaly (collision) detection on the axis.

## Overview

`AnomDtctOn` is the master switch for the anomaly-detection feature. Set it to `1` to arm the detector and `0` to turn it off. While armed, the controller filters the configured monitored signal every control cycle and checks it against the expected band held in [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md). When the signal leaves the band the axis is stopped or tripped (see [AnomDtctCnfg](AnomDtctCnfg.md)).

Configure the detector — monitored source, filter, limit tables — before arming it. See the [category overview](00-overview.md) for the full pipeline.

This keyword is available from v5 (central-i).

## How it works

| Value | Meaning |
| --- | --- |
| 0 | Detection off. The detector returns to idle. |
| 1 | Detection armed. After the next motion begins the detector becomes active and starts comparing the filtered signal against the band. |

Arming does not begin checking immediately. The detector first waits for motion to start; only once a motion is under way does it become active and track along the limit tables. The progression is reported by [AnomDtctSt](AnomDtctSt.md) element 1 (state). Detection runs only while the motor is on.

If the detector trips, the axis is either brought to a controlled stop or disabled with fault code 1067 (anomaly/collision detected) on [ConFlt](../../07-status-and-faults/ConFlt.md), depending on the stop mode in [AnomDtctCnfg](AnomDtctCnfg.md).

## Examples

```text
AAnomDtctOn[1]=1     ; arm anomaly detection on axis A
AAnomDtctOn[1]=0     ; disable it
AAnomDtctOn[1]       ; read the current enable state
```

## See also

- [AnomDtctCnfg](AnomDtctCnfg.md) — monitored source, filter pole, and stop behavior
- [AnomDtctSt](AnomDtctSt.md) — live detector state and filtered value
- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) — the expected band
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1067 raised on a trip
