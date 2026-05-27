---
keyword: StatReg
summary: Read-only bitfield reporting general axis status and warnings.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 33
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# StatReg

Read-only bitfield reporting general axis status and warnings.

## Overview

`StatReg` reports the general statuses of an axis as a bitfield. It is an axis-scoped, read-only register that is not saved to flash, so it always reflects the live state of the axis. Some statuses are encoded across more than one bit (for example, warnings that have several severity levels), so a mask-and-shift is needed to extract an individual status.

Agito PCSuite uses the bit values of this register to drive the LEDs in its status panel. Warning statuses with four levels (none, low, medium, high) are shown as a multi-color LED (off, yellow, orange, red, respectively).

> **Documentation pending:** This keyword is marked `implemented: partial`. The complete bit-field map (bit offsets, masks, and the meaning of each status field) is not yet documented here. The notes below are the recommended follow-up checks for the warning statuses but are not yet mapped to specific bits. Use Agito PCSuite, which translates `StatReg` into named statuses, until the bit table is finalized.

## How it works

To extract a specific status, use the following formula:

$$
Status = (StatReg\ \&\ Bit\ mask) \gg Bit\ offset
$$

Recommended checks when a warning status is set:

1. Check whether protections MaxVBus and MinVBus are set appropriately.
2. Check if warning is due to voltage exceeding limits during deceleration phase.
3. Check if warning is due to voltage dropping below limits during acceleration phase. If yes, check that power supply can provide sufficient current or lower the profile acceleration.
4. Check motor, driver and power supply sizing to fulfill current requirement
5. Check if MaxPWM is limiting driver’s output
6. Check current loop tuning gains
7. Redo phasing with high current and voltage and/or under lower tolerance setting to improve force constant.
8. Check the ambient temperature around the driver.
9. Install fans to circulate hot air out of the control box.
10. Relocate the drive to a position with more air flow.
11. Velocity saturation (MaxVel)
12. Current saturation (PeakCL or ContCL)
13. Voltage saturation (Va or Vb or Vc reaches MaxPWM)
14. Check first for voltage saturations, as it will affect the current, velocity and position loops.
15. PosFiltOn or PosFiltDef
16. VelFiltOn or VelFiltDef
17. FFFiltOn or FFFiltDef
18. ForceFiltOn or ForceFiltDef
19. UPMDistFilter
20. AnomDtctCnfg[2]
21. UPMRptLevel
22. PlantModel

## Examples

```text
StatReg?            ; read the full axis status bitfield
```

## See also

- [ConFlt](ConFlt.md) — axis fault code (separate from these status/warning bits)
- [MaxVBus](../06-protections/02-current-and-voltage/MaxVBus.md) / [MinVBus](../06-protections/02-current-and-voltage/MinVBus.md) — bus-voltage limits referenced by the voltage warnings

**Note:**

Agito PCSuite uses the bits values of this status parameter to control the LEDs at its status panel. The warning statuses, which have 4 values (none, low, medium and high) are reflected as a multi-color LED at the PC Suite status panel (off, yellow, orange and red, respectively).
