---
keyword: EncAbsErrTime
summary: Number of control cycles an absolute-encoder error/warning/CRC condition may persist before the axis faults; -1 disables monitoring.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 423
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
  - -1
  - 10000
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    implemented: partial
last_updated: '2026-10-17'
doc_revision: '2026.10'
---
# EncAbsErrTime

Number of control cycles an absolute-encoder error/warning/CRC condition may persist before the axis faults; -1 disables monitoring.

## Overview

`EncAbsErrTime` sets how long the existing absolute-encoder error policy tolerates an error, warning or CRC condition. Before the count exceeds the threshold, enabled handling uses position extrapolation. Once the count exceeds it, and the motor is on, the axis is taken off and the matching code is recorded in [ConFlt](../../07-status-and-faults/ConFlt.md). [EncStatReg](../01-general-settings/EncStatReg.md) reports diagnostics; its current value is not always the evidence used by this policy.

It is a per-axis parameter, saved to flash. The value is a count of control cycles (the loop runs at the controller's fixed sample rate, so the tolerated time is `EncAbsErrTime` × the control-cycle period). The valid range is `-1` to `10000`, and the default is `-1`. It applies to axes using a serial absolute encoder (see [EncType](../01-general-settings/EncType-AuxEncType.md)).

## How it works

Each invocation of the existing absolute-encoder handler processes the protocol's error-policy inputs:

| EncAbsErrTime | Behaviour |
|---|---|
| -1 | Error / warning / CRC monitoring is **disabled**: those conditions are not counted and do not fault the axis. |
| 0 to 10000 | A persisting error / warning / CRC condition is counted; while counting, the position is extrapolated so motion continues, and the axis faults once the count exceeds this value. |

The two recoverable groups are counted separately:

- **CRC errors** (status bit 4). On expiry, [ConFlt](../../07-status-and-faults/ConFlt.md) reports fault `1069`.
- **Error / warning** (status bit 1, or the warning condition at bit 3). On expiry, [ConFlt](../../07-status-and-faults/ConFlt.md) reports fault `1068`.

A clean cycle (no abnormal bit) resets the counters, so only a *continuous* condition lasting longer than `EncAbsErrTime` produces a fault — short noise glitches are ridden through by extrapolation.

The existing **main-encoder protection** path is separate from `EncAbsErrTime` and can produce [ConFlt](../../07-status-and-faults/ConFlt.md) fault `1070`. On Central-i its physical meaning depends on the protocol and FPGA image; bit 0 is not a universal cable-disconnect verdict.

## Central-i accepted position and policy quality

On AGM800 and AGM800-EC firmware containing the [accepted-quality repair](https://github.com/akribis-agito/Firmware-Main/issues/1408), active standard AMP main BiSS-C, EnDat and Tamagawa feedback uses the existing error/warning/CRC inputs accepted with the main position under the Central-i CRC1 check. A CRC1-accepted frame may itself report an encoder error. Rejected or skipped transport decoding retains both the accepted position and its policy quality.

[EncStatReg](../01-general-settings/EncStatReg.md) continues to report current decoded inputs. A rejected bad frame can therefore appear in diagnostics without starting encoder-error counting for a retained good sample; a rejected clean frame can clear diagnostics without clearing the policy evidence from a retained bad sample. Existing counters still count control-handler invocations, including repeated use of retained bad quality, rather than new replies. The `-1` bypass, thresholds and fault actions are unchanged.

This ownership rule does not apply to local controllers, auxiliary feedback, ADP05/AGFB, simulation or analytic feedback producers. Before the first accepted frame after a reset, zero compatibility values do not establish healthy or qualified feedback. Initialization timing is unchanged. Neither this parameter nor a clear diagnostic register establishes physical sample age or full Tamagawa SF/ALMC alarm state.

> [!caution]
> Setting `-1` suppresses the error, warning and CRC conditions together: while monitoring is disabled none of them counts toward a fault. The **disconnect** condition is independent of `EncAbsErrTime` and is always acted on — `-1` does not suppress a disconnect fault.

> **Availability note:** on Central-i v5 this keyword is marked partially implemented.

## Examples

```text
AEncAbsErrTime=-1        ; disable error/warning/CRC monitoring (default)
AEncAbsErrTime=100       ; tolerate up to 100 control cycles of error/warning/CRC before faulting
AEncAbsErrTime           ; read the configured tolerance
```

## See also

- [EncStatReg](../01-general-settings/EncStatReg.md) — current encoder diagnostics and their distinction from accepted policy quality
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault register; reports codes 1068 / 1069 / 1070
- [EncType](../01-general-settings/EncType-AuxEncType.md) — feedback type; this applies to the serial absolute encoder
