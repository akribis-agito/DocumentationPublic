---
keyword: ComtStatus
summary: Read-only array reporting the actual commutation (phasing) status of the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 143
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
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
overrides:
  central-i.v5:
    array_size: 4
last_updated: '2026-07-29'
doc_revision: '2026.06'
---
# ComtStatus

Read-only array reporting the actual commutation (phasing) status of the axis.

## Overview

`ComtStatus` is a read-only array that reports the actual commutation status of the axis. It is used to monitor the commutation process configured by [ComtMode](ComtMode.md) and to diagnose failures: a positive value of 100 indicates a successfully finished commutation, intermediate values indicate progress, and negative values are error codes. Being read-only and not flash-saved, it can be read at any time, including while the motor is on or in motion. The resulting electrical angle is reported by [ComtAng](ComtAng.md).

When the phasing status reaches `100` (finished) the commutation-complete bit of [StatReg](../07-status-and-faults/StatReg.md) (bit 0) is set. For the Hall-start switching methods (`ComtMode[1]=3` or `4`), the bit is set once a usable rough Hall angle is established (status `300`/`400`) and stays set through refinement to `100`, so the axis can already run. Status `200` (commutation not required) also sets the bit. The bit stays cleared only before any usable angle is available (status `0`/`1`) or when commutation has failed (a negative status), in which case normal motion is blocked.

## How it works

The array holds the following elements (1-indexed):

| Index | Description |
|---|---|
| `[1]` | Phasing status. Default 0. See the value table below. |
| `[2]` | Number of consecutive successful jumps during the "jump to zero" search method (`ComtMode[1]=0`). Default 0; the search completes after 3 consecutive in-range jumps. |
| `[3]` | Bidirectional-search state (central-i v5 only). Reports the progress of a bidirectional commutation search: `0` unused, `1` armed, `2` first direction finished, `3` both directions finished. This index does not exist on v4/standalone. |

`ComtStatus[1]` (phasing status) values:

| Value | Commutation status |
|---|---|
| 0 | Required and not executed yet. |
| 1 | Commutation in progress. |
| 100 | Successfully finished. |
| 200 | Commutation is not required (e.g. DC, voice coil or stepper motors). |
| 300 | Rough commutation is done, waiting for index pulse for fine commutation adjustment. |
| 400 | Rough commutation is done. Waiting for Hall sequence change for fine commutation adjustment. |
| 500 | Learn process changed parameters (recommended to save to flash). |
| 600 | Burn-in mode is activated. |
| -1 | Unexpected motor off. Motor off occurred during commutation. |
| -2 | Illegal commutation method selected. |
| -3 | "Jump to zero" commutation failed. Please check motor, encoder and commutation parameters (such as voltage and accuracy). |
| -4 | Encoder error is detected. Commutation is required. |
| -5 | Parameter is modified. Commutation is required. |
| -6 | Amplifier power cycle is required. |
| -7 | Illegal halls sequence detected. |
| -8 | Central-I failure during commutation process. |
| -9, -10, -11, -12 | Illegal halls sequence is detected during learn process. |
| -14 | Commutation failed: incorrect direction detected during the search (central-i v5 only). |
| -15 | Commutation failed: a hard stop was reached during the search (central-i v5 only). |
| -16 | Commutation failed: no Hall transition was found during fine Hall learning (central-i v5 only). |
| -17 | Commutation refused: phasing would drive voltage directly into an external amplifier, which is not allowed. The axis is turned off (central-i v5 only). |

The illegal-Hall errors (`-7`, `-9` … `-12`) are raised when [HallsValue](HallsValue.md) reads `0` or `7` (the two combinations outside the legal range 1–6), or when the observed Hall sequence does not match the expected order.

### External-amplifier phasing refusal (status `-17`)

The "jump to zero" (`ComtMode[1]=0`) and minimal-jumps search (`ComtMode[1]=5`) commutation methods find the electrical angle by driving phase voltage (`Va`/`Vb`/`Vc`) directly — see [ComtMode](ComtMode.md). That voltage cannot be sent into an external amplifier, so on an axis configured for one, with commutation left in its default voltage domain (i.e. not switched to an explicit current domain), the controller refuses to phase: it sets `ComtStatus[1]` to `-17` and turns the motor off.

For minimal-jumps search this is the final status. For "jump to zero", the refusal happens inside the same control cycle as the method's own end-of-jump check, which then finds the motor already off and immediately overwrites the status to `-1` (unexpected motor off) — so on this method `-17` is transient and what actually persists is `-1` with the motor off. Either way the outcome is the same: phasing is refused and the motor stays off.

### Burn-in mode (status `600`)

While burn-in motion is active (see [BurnInMode](../../03-special-features/burn-in/BurnInMode.md)) the phasing status reads `600`. In this mode the controller drives a *virtual* commutation for a brushless motor: the electrical angle is advanced at a fixed electrical frequency (set by [BurnInFreq](../../03-special-features/burn-in/BurnInFreq.md)), with no position feedback. The commutation-complete bit of [StatReg](../07-status-and-faults/StatReg.md) (bit 0) is set so the axis can run during the test. When burn-in mode is turned off, because the motor may have moved while its angle was driven open-loop, the phasing status becomes `-5` (parameter modified — commutation is required), so a fresh commutation must run before normal motion resumes.

## Examples

```text
AComtStatus[1]      ; query the phasing status
AComtStatus[2]      ; consecutive successful jumps ("jump to zero" search method)
```

## See also

- [ComtMode](ComtMode.md) — commutation settings driving this status
- [ComtAng](ComtAng.md) — instantaneous commutation angle
- [HallsValue](HallsValue.md) — current raw Hall sensor state (related to illegal-Hall-sequence errors)
- [StatReg](../07-status-and-faults/StatReg.md) — bit 0 reports commutation complete
