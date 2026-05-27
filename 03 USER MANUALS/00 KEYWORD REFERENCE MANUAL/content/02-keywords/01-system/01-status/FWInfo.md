---
keyword: FWInfo
summary: Read-only command returning firmware version and build information.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 312
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FWInfo

Read-only command returning firmware version and build information.

## Overview

`FWInfo` is a read-only command (a function) that returns the firmware build-information block for the controller. Host software uses it to identify the firmware build currently running on the device — for example to confirm a unit is on the expected release before commissioning, or to capture the build for a support report. For the numeric firmware/FPGA version, read [Identity](Identity.md) instead; `FWInfo` returns the human-readable build description.

## How it works

The build information is stored in a fixed constant block in flash that is written when the firmware HEX image is downloaded. The block holds **four free-text lines of up to 64 characters each**, used to describe the build — typically a short note about what changed in the release and the FPGA version the firmware is meant to be paired with. `FWInfo` streams these four lines back to the host, then appends the **firmware checksum** as a final text field, then a terminator. Each stored line is NUL-terminated; the firmware replaces the terminator and any trailing bytes with spaces so the host (Agito PCSuite) receives fixed-width, printable text. The reply uses the same string protocol as `ProgInfo`.

Because the four lines are arbitrary build text, their exact content changes with every firmware build; treat them as an opaque human-readable description rather than a parseable structure.

## Examples

```text
AFWInfo             ; return the firmware build-info lines and checksum
```

## See also

- [Identity](Identity.md) — numeric firmware/FPGA version and feature flags
- [About](About.md) — full parameter dump (Agito PCSuite internal use)
- [UnitStat](UnitStat.md) — flags a firmware/FPGA image mismatch
