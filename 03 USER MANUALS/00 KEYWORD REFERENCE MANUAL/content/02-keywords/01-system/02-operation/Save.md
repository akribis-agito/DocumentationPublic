---
keyword: Save
summary: Writes all flash-saveable parameters from volatile memory to flash.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 232
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
# Save

Writes all flash-saveable parameters from volatile memory to flash.

## Overview

`Save` persists parameters to non-volatile (flash) memory. It first erases the dedicated parameter area in flash, then walks the keyword table and copies every flash-saveable parameter from volatile (RAM) memory into it — so the stored set always reflects the controller's current configuration. Settings that are not saved are lost on the next power cycle or [Load](Load.md).

`Save` is a **command** (it takes no value). It is **not allowed while the motor is enabled or in motion** — the interpreter rejects it with an error in those states, and the operation blocks the main loop for the duration of the write. Whether a given parameter is included depends on its `flash` attribute (shown in each keyword's Quick Facts); read-only and live-status keywords are not saved.

## How it works

`Save` runs in three phases:

1. **Erase.** The parameter blocks in flash are erased first. If the erase or any subsequent program step fails, `Save` aborts and returns an error rather than leaving a partial set.
2. **Write records.** The firmware scans the keyword table by CAN code. For each parameter whose `flash` attribute is set, it writes a self-describing record so the data can be re-read correctly even if a future firmware revision changes the parameter's size or axis layout. For axis-related parameters the record is repeated once per axis. Each record is:

   | Field | Size | Contents |
   |-------|------|----------|
   | CAN code | 1 word | Parameter's CAN code, with the axis number packed into the upper bits |
   | Element count | 1 word | Number of array members (1 for a scalar) |
   | Value(s) | 2 words each | The 32-bit value of each element |

   While writing, a running **parameter checksum** is accumulated over the values (the [ParamCS](../01-status/ParamCS.md) words). Three checksum variants are kept so a host can compare configuration while ignoring volatile identity fields such as the network IP/MAC address.
3. **Finalize.** After the last parameter, `Save` writes a marker recording the last CAN code stored (used by [Load](Load.md) to know where the saved set ends) and a whole-area additive checksum that `Load` re-verifies on every restore. If flash fills before the table is exhausted, `Save` returns a "flash full" error.

Because the operation can take a noticeable time, the firmware refreshes the watchdog and signals progress on the status LED while it runs. On central-i the command is acknowledged immediately — an early empty reply tells the host the operation has begun — and, because the long flash write blocks the loop that normally feeds the watchdog, the firmware pre-loads the background watchdog feed for roughly 120 seconds. A host should therefore allow up to about that long for the final OK/error reply before treating `Save` as hung. Index 0 of every array is deliberately excluded from the checksum and from host upload (arrays are 1-indexed).

## Examples

```text
ASave                ; persist current parameters to flash (motor must be off)
```

### Walk-through: save the current config and restart

Persist your edits to flash, restart the controller, and confirm the saved set is what came back. The motor must be off throughout.

```text
AMotorOn=0           ; ensure the motor is off (Save is rejected otherwise)
AParamCS[1]          ; (optional) note the pre-save checksum for comparison
ASave                ; persist all flash-saveable parameters to flash
AParamCS[1]          ; checksum after save — reflects what was written
AReset               ; software power cycle; firmware auto-runs Load on restart
                     ; ... reconnect, then ...
AParamCS[1]          ; same value as the post-save checksum — confirms a clean restore
```

If `ParamCS[1]` before and after `Reset` matches the post-`Save` value, the parameters you saved are the parameters running on the controller. To compare functional configuration across units while ignoring the per-unit network identity, use `ParamCS[1]`; to verify an exact match including IP and MAC, use `ParamCS[3]`.

## Edge cases

- **Motor on / in motion.** Rejected — the interpreter returns an error and nothing is written. Stop the axis and disable the motor first.
- **Flash error.** A failed erase returns error 27 and a failed write returns error 28; in either case `Save` aborts rather than leaving a partial set.
- **Flash-board / build mismatch.** If the flash-chip layout the firmware was built for does not match the board it is running on, `Save` refuses before writing anything and returns error 251 or 252 (single-flash vs double-flash board mismatch, build-dependent). This guards against writing the parameter area with the wrong flash geometry.
- **Flash full.** If the parameter set exceeds the reserved flash space `Save` returns a "flash full" error (29) after writing what fits; on the next [Load](Load.md) only the records actually written are restored, and missing parameters revert to their defaults.
- **Power loss mid-Save.** Because `Save` erases the area first, a power loss before the final checksum/marker is written leaves the area incomplete; on the next power-up [Load](Load.md) sees a checksum mismatch and the firmware initialises all parameters to their defaults (rather than loading a partial set).
- **Central-i disconnect.** The save operates on the master's own parameters and is unaffected by the link state to any remote unit.

## See also

- [Load](Load.md) — reload parameters from flash (and re-verify the checksum written here)
- [SaveUser](SaveUser.md) — save to a separate user area instead of the main set
- [Reset](Reset.md) — software power cycle; reloads the saved set on restart
- [ParamCS](../01-status/ParamCS.md) — the parameter checksum this command computes
