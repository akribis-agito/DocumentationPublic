---
keyword: OneOverTOn
summary: Enables or disables the 1/T velocity measurement reported as Vel[4].
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 187
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# OneOverTOn

Enables or disables the 1/T velocity measurement reported as Vel[4].

## Overview

`OneOverTOn` enables (`= 1`) or disables (`= 0`) the 1/T velocity measurement reported as [Vel](Vel.md)`[4]`. The 1/T method gives a high-resolution velocity estimate at low speed by measuring the *time* taken to accumulate a fixed *number of encoder counts*, rather than counting how many counts occur in a fixed control sample. At low speeds the count-per-sample method is coarse (often only 0 or 1 count per sample), whereas timing a known displacement against a high-frequency timer remains precise.

It applies when a digital incremental encoder ([EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) `= 1`) is used. The measurement is further tuned by [OneOverTFreq](OneOverTFreq.md) (timer frequency) and [OneOverTGap](OneOverTGap.md) (count gap). When disabled on a standalone product, `Vel[4]` reports `0`.

## How it works

On standalone products the 1/T capture is performed by a dedicated quadrature-encoder timing unit, which is **always running** regardless of `OneOverTOn` — the unit continuously latches the timer count between encoder events.

`OneOverTOn` only gates the *calculation* of `Vel[4]` from that captured value, which is done once per control cycle in the second half of the cycle. The velocity computation involves a division, so when the feature is off the calculation is skipped (to save cycle time) and `Vel[4]` is reported as `0`.

The actual velocity is derived from the latched timer period; see [OneOverTFreq](OneOverTFreq.md) and [OneOverTGap](OneOverTGap.md) for the full equation and the sign/overflow handling.

| Value | Effect on standalone |
|-------|----------------------|
| `0` (default) | 1/T velocity calculation skipped; `Vel[4] = 0`. The capture timing unit still runs. |
| `1` | `Vel[4]` is computed each control interrupt from the captured 1/T timer period. |

## Examples

```text
AOneOverTOn=1        ; enable 1/T velocity measurement on axis A
AOneOverTOn=0        ; disable (Vel[4] reports 0 on standalone)
AOneOverTOn          ; read current value
```

After enabling, read the result with `AVel[4]` (the 1/T element of the velocity array).

## Changes between versions

On **standalone (v4)** products `OneOverTOn` gates the timing-unit-based `Vel[4]` calculation as described above.

On **Central-i (v5)** the 1/T velocity is computed in the remote amplifier and delivered to the master in the synchronous message; the master copies it into `Vel[4]` directly. That Central-i path is **not gated by `OneOverTOn`**, so on Central-i the keyword does not switch `Vel[4]` off the way it does on standalone. The companion tuning keywords [OneOverTFreq](OneOverTFreq.md), [OneOverTGap](OneOverTGap.md) and [OneOverTAuto](OneOverTAuto.md) are standalone-only.

## See also

- [Vel](Vel.md) — feedback velocity array (`Vel[4]` is the 1/T method)
- [OneOverTFreq](OneOverTFreq.md) — 1/T timer-frequency divider (resolution vs. overflow)
- [OneOverTGap](OneOverTGap.md) — encoder-count gap measured per 1/T sample
- [OneOverTAuto](OneOverTAuto.md) — reserved auto-tuning of frequency/gap (not implemented)
- [EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) — must be a digital incremental encoder
