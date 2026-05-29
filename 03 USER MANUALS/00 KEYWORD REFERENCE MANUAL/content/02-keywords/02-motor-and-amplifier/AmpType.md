---
keyword: AmpType
summary: Selects how the axis drives its motor — built-in amplifier or an external amplifier via analog/digital command.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 226
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
  - 0
  - 7
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    range:
    - 0
    - 8
---
# AmpType

Selects how the axis drives its motor — built-in amplifier or an external amplifier via analog/digital command.

## Overview

`AmpType` defines the amplifier mode used by the axis. Depending on the Agito product, an axis can drive its internal PWM amplifier directly or interface with an external amplifier through an analog or digital command. The choice determines which command signal the axis produces, and which related keywords apply — for example the external analog modes use [AAmpFullScale](AAmpFullScale.md) to scale the output. Contact Agito for the amplifier functionality available on each product.

Because `AmpType` is an axis-scope parameter saved to flash, it cannot be changed while the motor is on or in motion; set it during axis configuration (typically from the PCSuite setup page), then `Save`.

> [!note] Status: partial
> The frontmatter marks `AmpType` as `partial`. On v4 the firmware range is 0–7; v5 (central-i) extends it to 0–8. Selecting a value the product does not support is rejected at motor-on with controller fault [1053](../../04-error-codes/controller-error-codes.md) ("AmpType value not allowed for this product").

## How it works

`AmpType` decides whether the axis closes its **own current loop** or delegates it. For the **internally-commutated** modes — built-in PWM amplifier (0), linear adapter (7), and (v5) digital SPI (8) — the controller runs the full internal current/commutation loop and either drives the power stage directly (0) or emits the resulting phase-current references for an external power stage (7, 8). For the remaining modes the axis is flagged as **driven externally**: the internal current loop is skipped and the controller only emits a command signal (analog current, analog velocity, or pulse-direction) for the external amplifier to close the loop on.

Changing `AmpType` re-arms commutation **only for the internally-commutated modes** on a brushless motor: the [StatReg](../07-status-and-faults/StatReg.md) commutation bit is cleared and re-phasing is required before motor-on. For the externally-driven modes the axis is no longer treated as a brushless motor for commutation, so this re-arm is skipped.

| AmpType | Amplifier mode | Current loop |
|----|----|----|
| 0 | Built-in PWM amplifier — controller drives the power stage directly. | Internal |
| 1 | Reserved (was central-i). Do not use. | — |
| 2 | External amplifier, analog **current** command. The current reference ([CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md)) is scaled to an analog-output voltage via [AAmpFullScale](AAmpFullScale.md). | External |
| 3 | External amplifier, digital **pulse-direction (PD)** command. The controller outputs step/direction pulses; many checks (current loop, commutation) are bypassed. | External |
| 4 | Built-in **linear** amplifier (reserved product). The axis is driven externally: it skips the internal current loop and only emits an analog **current** command — the current reference scaled by [LAmpFullScale](LAmpFullScale.md) (same command path as mode 2). | External |
| 5 | External amplifier, analog **velocity** command. The velocity reference ([VelRef](../10-motion/01-kinematics-status/VelRef.md)) is scaled to an analog-output voltage via [AAmpFullScale](AAmpFullScale.md). | External |
| 7 | External **linear adapter**: the controller still runs its internal commutation/current loop and outputs the two phase-current references ([IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)) as analog voltages (scaled by [AAmpFullScale](AAmpFullScale.md)). | Internal |

In **v5 (central-i)** two more modes exist:

| AmpType | Amplifier mode | Current loop |
|----|----|----|
| 6 | Digital pulse-direction command with position feedback. Driven externally. | External |
| 8 | Digital SPI: the controller runs its internal commutation/current loop and outputs the two phase-current references ([IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)) as digital SPI codes — the digital counterpart of the analog linear adapter (mode 7). Because it stays internally commutated, commutation/auto-phasing and current-loop tuning apply as for a brushless motor. | Internal |

> [!note]
> Value 6 falls in the v4 0–7 range numerically but mode 6 is only available on v5; on v4, modes 6 and 8 are not available.

### Output scaling for the external modes

For the analog command modes (2, 5, and the linear adapter 7, and built-in linear 4) the analog-output voltage is the reference times a fixed factor `10000 / FullScale` (so full-scale reference → 10 000 mV = 10 V). The factor is recomputed whenever `AmpType`, [AAmpFullScale](AAmpFullScale.md), or [LAmpFullScale](LAmpFullScale.md) changes. When the motor is off, the analog output is forced to zero. See [AAmpFullScale](AAmpFullScale.md) for the per-mode units and worked example.

### Allowed values per remote unit (v5 central-i)

On v5 (central-i), the connection manager validates `AmpType` against the class of remote unit detected on the link:

| Remote-unit class | Allowed `AmpType` |
|---|---|
| Built-in amplifier unit | 0 (built-in PWM) |
| Analog / pulse-direction adapter | 2 (analog current), 3 (PD), 5 (analog velocity), 6 (PD with feedback) |
| Linear / digital-SPI adapter | 7 (linear adapter), 8 (digital SPI) |
| Remote I/O unit | any `AmpType` |

If the configured `AmpType` does not match the detected unit (or the unit type is unknown), the device is disconnected and its [CIStatus](../01-system/05-central-i/CIStatus.md) / [CIIdentity](../01-system/05-central-i/CIIdentity.md) are cleared. The v4 device set is narrower (it has no mode-6/8 and only one such adapter class mapping to mode 7).

## Examples

```text
AAmpType=0           ; use the built-in PWM amplifier
AAmpType=2           ; external amplifier, analog current-reference command
AAmpType            ; query the current amplifier mode
```

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Range | 0–7 | 0–8 |
| Added modes | — | 6 (PD with feedback), 8 (digital SPI phase-current) |

v5 is central-i only; on the standalone product `AmpType` keeps the v4 range 0–7.

## See also

- [AAmpFullScale](AAmpFullScale.md) — full-scale output scaling for the external analog modes (2, 5, 7; and 8 in v5)
- [LAmpFullScale](LAmpFullScale.md) — full-scale selection for the built-in linear amplifier (mode 4)
- [MotorType](MotorType.md) — type of motor connected to the amplifier
- [StatReg](../07-status-and-faults/StatReg.md) — commutation status bit (cleared when `AmpType` changes)
