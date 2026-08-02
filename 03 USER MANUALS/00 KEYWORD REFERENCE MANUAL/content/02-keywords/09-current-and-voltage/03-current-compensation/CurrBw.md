---
keyword: CurrBw
summary: Current-loop bandwidth in Hz, used to normalise the field-weakening gains.
availability:
  standalone: []
  central-i:
  - v5
can_code: 877
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 500
  - 8000
  default: 1000
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# CurrBw

Current-loop bandwidth in Hz, used to normalise the field-weakening gains.

## Overview

`CurrBw` tells the drive how fast the current loop is. It does not *set* the current-loop bandwidth — that follows from [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) and [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) — it *declares* it, so that the field-weakening gains can be normalised and behave comparably across machines with very different electrical time constants.

## How it works

The drive divides the field-weakening loop gains by a factor derived from `CurrBw`, so that a given [FieldWeakKi](FieldWeakKi.md) produces a similar closed-loop response whether the current loop runs at 500 Hz or 2 kHz.

> **Important:** set `CurrBw` to the bandwidth the current loop **actually** achieves, not the value you would like. If the declared figure is wrong the field-weakening gains are normalised against a loop that does not exist, and their behaviour will not match the values you set.

### Determining the achieved bandwidth

For a PI current loop tuned to cancel the winding pole, the closed-loop bandwidth is set by the gains and the motor's per-phase resistance and inductance. Confirm it by commanding a current step and measuring the rise time: bandwidth in Hz is approximately `1 / (2π × rise time)`.

> **Note:** data-sheet resistance and inductance are usually quoted **line-to-line**. The per-phase values are half of those. Using the line-to-line figures directly gives a bandwidth estimate that is wrong by a factor of two.

### Edge cases

- **Range:** writes outside `500…8000` Hz are clamped.
- **Voltage limiting:** the achievable current-loop bandwidth falls as speed rises, because back-EMF consumes the bus. `CurrBw` is a single declared figure and does not model that.

## Examples

```text
ACurrBw=1000          ; current loop achieves roughly 1 kHz
```

## See also

- [FieldWeakKp](FieldWeakKp.md), [FieldWeakKi](FieldWeakKi.md) — the gains this normalises
