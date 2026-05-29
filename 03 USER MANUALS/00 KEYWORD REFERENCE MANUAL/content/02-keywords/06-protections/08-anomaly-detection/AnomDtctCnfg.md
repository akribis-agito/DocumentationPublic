---
keyword: AnomDtctCnfg
summary: "Configuration array for anomaly detection: monitored source, filter pole, stop behavior, and motion selection."
availability:
  standalone: []
  central-i:
  - v5
can_code: 779
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 13
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
# AnomDtctCnfg

Configuration array for anomaly detection: monitored source, filter pole, stop behavior, and motion selection.

## Overview

`AnomDtctCnfg` holds the settings that define how the anomaly detector behaves: which signal it watches, how that signal is filtered, what it does when an anomaly is found, and which motion in a repeating sequence the limit tables apply to. Configure these elements before arming the detector with [AnomDtctOn](AnomDtctOn.md).

The array is 1-indexed; the highest usable index is 12 (index 0 is reserved). Not every index in the range carries a setting — the elements in active use are listed below.

This keyword is available from v5 (central-i).

## How it works

| Index | Element |
| --- | --- |
| 1 | **Monitored source.** The complex CAN code of the signal to watch (for example a current or force reading). The controller resolves this code to the live value and feeds it into the detector each control cycle. See [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md). |
| 2 | **Filter pole frequency**, in Hz. Sets the cut-off of the second-order low-pass filter applied to the monitored signal. If left at or below `0` it defaults to 200 Hz. Writing this element recalculates the filter immediately. |
| 10 | **Stop behavior on detection.** `0` = disable the axis with fault code 1067 on [ConFlt](../../07-status-and-faults/ConFlt.md); `1` = command a controlled stop instead of tripping a fault. |
| 11 | **Motion case** (reserved). Present in the configuration array but not acted on by the detector in the firmware consulted for this reference. |
| 12 | **Motion sequence.** Selects which monitored-motion pattern the detector tracks. The detector steps through the motions in the selected sequence as successive point-to-point moves complete, and applies the matching section of the [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) tables to each. |

Indices 3 through 9 are not used by the detector in the firmware consulted for this reference.

The monitored signal is sampled once per control cycle, filtered, and reported in [AnomDtctSt](AnomDtctSt.md) element 2. The expected band for the active motion is taken from the upper/lower limit tables, advancing one table point every [AnomDtctGap](AnomDtctGap.md) cycles for that motion.

## Examples

```text
AAnomDtctCnfg[1]=<complex CAN code of monitored signal>   ; choose the source
AAnomDtctCnfg[2]=150     ; filter pole at 150 Hz
AAnomDtctCnfg[10]=1      ; controlled stop on detection (no fault)
AAnomDtctCnfg[12]=1      ; select motion sequence 1
AAnomDtctCnfg[2]         ; read the configured filter pole
```

## See also

- [AnomDtctOn](AnomDtctOn.md) — arm the detector after configuring
- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) — the expected band tables
- [AnomDtctGap](AnomDtctGap.md) — cycles per limit-table point
- [AnomDtctSt](AnomDtctSt.md) — filtered value and detector state
- [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) — how a source signal is addressed
