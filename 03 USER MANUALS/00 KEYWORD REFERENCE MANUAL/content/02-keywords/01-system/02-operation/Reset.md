---
keyword: Reset
summary: Performs a software power cycle; flash parameters are reloaded on restart.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 234
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
# Reset

Performs a software power cycle; flash parameters are reloaded on restart.

## Overview

`Reset` performs a software power-cycle of the controller. On restart, the parameters stored in flash are loaded, overriding any unsaved changes in volatile memory. Use it to apply settings that only take effect at startup (for example after a [Save](Save.md)), or to return the controller to its saved state. `Reset` is a **command** (no value) and cannot be issued while the motor is on or in motion.

## How it works

`Reset` is a controlled, graceful restart — it is not the same as cutting power, but it brings the firmware back through its full power-up path:

1. **Acknowledge first.** The controller sends the normal command acknowledgement *before* resetting, and then waits about one to two seconds so the reply (including any in-flight serial output) is fully transmitted before the processor restarts. A host therefore receives a confirmation, then loses the link briefly while the controller reboots.
2. **Quiesce hardware.** The serial bus is closed and the FPGA is reset, so the drive outputs are taken to a safe state rather than being left in whatever condition they were in. The I/O pins are returned to the mode the boot program expects.
3. **Restart.** Interrupts are disabled and execution jumps to the firmware's start-up entry point — the same point reached after a hardware reset.

On the subsequent start-up the firmware re-initializes, runs [Load](Load.md) to restore the saved parameters, and — if [AutoExec](AutoExec.md) is set and a user program is present — begins running that program. Because flash is reloaded, any unsaved edits are discarded; run [Save](Save.md) first if you want your current settings to survive the reset.

## Examples

```text
AReset               ; software power cycle (motor must be off)
```

## See also

- [Save](Save.md) — persist parameters before resetting
- [Load](Load.md) — reload from flash without a power cycle
- [AutoExec](AutoExec.md) — auto-start the user program after reset
