---
keyword: Load
summary: Reloads all parameters from flash into volatile memory, discarding unsaved changes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 233
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Load

Reloads all parameters from flash into volatile memory, discarding unsaved changes.

## Overview

`Load` retrieves all flash-saveable parameters from non-volatile (flash) memory into the active (volatile) parameter table. The controller performs this once automatically at power-up; issuing `Load` manually repeats it **without** a power cycle.

`Load` overwrites every unsaved change in volatile memory. This makes it the quick way to recover from a bad, unsaved configuration: `Load` reverts the controller to the last known-good parameters stored in flash. Whether a given parameter participates is determined by its `flash` attribute (shown in each keyword's Quick Facts). It is a **command** (no value) and is **not allowed while the motor is enabled or in motion**.

## How it works

`Load` is the inverse of [Save](Save.md) and tolerates differences between the firmware that wrote the flash and the firmware reading it:

1. **Verify checksum.** The whole parameter area is summed and compared against the additive checksum stored by `Save`. On mismatch `Load` reports a checksum error and the parameters are instead initialized to their defaults (handled by the power-up path).
2. **Replay records.** Starting at the beginning of the parameter area, `Load` reads each record's CAN code (and packed axis number), element count, and values, then writes the values back into the matching live parameter — but only if that keyword is still `flash`-attributed in the current firmware. It stops at the last-CAN-code marker written by `Save`, or earlier if it reaches erased (`0xFFFF`) flash.
3. **Reconcile layout.** Per-parameter mismatches between flash and the running firmware are handled gracefully and logged to the [error log](../../07-status-and-faults/ErrLog.md) as warnings rather than hard errors:
   - **Array grew** — extra elements are filled with their default values.
   - **Array shrank** — surplus stored elements are skipped.
   - **Axis count decreased** — records for axes that no longer exist are skipped.
4. **Range-check.** Every loaded value is checked against its min/max limits; out-of-range values are replaced with the parameter default (and a warning is logged).
5. **Re-derive state.** After loading, the firmware re-runs each parameter's "special" initialization, marks the loop filters as modified, and recalculates the filters for every axis, so derived internal state matches the freshly loaded values.

The parameter checksum ([ParamCS](../01-status/ParamCS.md)) is recomputed during the load, so it reflects what was actually restored.

## Edge cases

- **Motor on / in motion.** Rejected — the interpreter returns an error. Stop the axis and disable the motor first; the same restriction applies at power-up if the firmware was somehow asked to reload during operation.
- **Checksum mismatch.** Reported as an error and every flash-saveable parameter is reset to its default rather than half-loaded.
- **Firmware upgrade (different parameter layout).** Per-parameter mismatches (array grew/shrank, axis count decreased) are handled gracefully and noted as warnings in [ErrLog](../../07-status-and-faults/ErrLog.md). A parameter that no longer has the `flash` attribute in the new firmware is simply skipped on load.
- **Central-i disconnect.** `Load` restores the master's own parameters; it does not push them to remote units. Per-port settings ([CIDeviceType](../05-central-i/CIDeviceType.md), [CILinkConfig](../05-central-i/CILinkConfig.md), …) take effect on the next [CIConnect](../05-central-i/CIConnect.md).

## Examples

```text
ALoad                ; reload all flash-saved parameters, discarding unsaved edits
```

## See also

- [Save](Save.md) — write parameters to flash (the records and checksum `Load` reads)
- [LoadUser](LoadUser.md) — restore the separate user parameter set instead
- [Reset](Reset.md) — software power cycle (also reloads from flash)
- [ParamCS](../01-status/ParamCS.md) — parameter checksum recomputed by this command
