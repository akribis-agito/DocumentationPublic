---
keyword: PowerSupply
summary: Declares the drive's power-supply type so protections behave correctly.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 401
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 3
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# PowerSupply

Declares the drive's power-supply type so protections behave correctly.

## Overview

`PowerSupply` tells the amplifier what type of power feeds it, so that the AC-phase-missing protections check the correct input pins. Select the value matching your hardware (typically via the PCSuite configuration page). It cannot be changed while the motor is on or in motion.

| Value | Supply type |
|-------|-------------|
| 1 | Single-phase AC |
| 2 | DC — low-voltage supply |
| 3 | Three-phase AC |

## How it works

`PowerSupply` selects which power-input phases the drive monitors for "phase missing":

- **Three-phase:** both the A&ndash;C and B&ndash;C phase-missing flags are checked. If either is set, the axis is disabled and [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1054 (at least one required phase of the AC power inputs was cut off).
- **Single-phase:** only the B&ndash;C phase-missing flag is checked (raises the same fault code 1054).
- **DC:** the AC-phase checks are not applied.

`PowerSupply` also feeds the protection-mask logic: when [ProtectMask](../01-general-protection/ProtectMask.md) (or `PowerSupply`) changes, the drive re-derives the hardware fault-enable word and gates the AC-power-phase bits according to the declared supply type, so phases that the supply does not use are not flagged as missing. (On standalone AG100 drives this is done with dedicated power-phase mask bits; on Central-i the enable word is sent to the remote amplifier.)

### Edge cases

- **Motor off / motor on:** the keyword is gated `ok_in_motion: false`, `ok_motor_on: false` — change it only with the motor disabled and not in motion. The re-derivation of the protection-enable word happens on the next write.
- **Mismatched declaration:** declaring `PowerSupply = 2` (DC) on hardware actually wired for AC suppresses the AC-phase-missing fault — your protection is effectively disabled. Always declare the actual supply type.
- **Effect on [HWProtectBits](../01-general-protection/HWProtectBits.md):** unused-phase bits are not just masked from tripping — they are gated out of the live `HWProtectBits` report itself on Central-i.
- **Three-phase pin set:** the firmware checks both A–C and B–C phases; either one missing raises [ConFlt](../../07-status-and-faults/ConFlt.md) code 1054 (one or more required AC phases cut off).
- **Range overflow:** writes outside `1…3` are clamped to the keyword `range`.

## Examples

```text
APowerSupply=3       ; three-phase AC supply
```

## See also

- [ProtectMask](../01-general-protection/ProtectMask.md) — the power-phase protections it gates
- [HWProtectBits](../01-general-protection/HWProtectBits.md) — reports the phase-missing bits
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault 1054 on a missing AC phase
- [MaxVBus](MaxVBus.md) / [MinVBus](MinVBus.md) — bus-voltage limits
