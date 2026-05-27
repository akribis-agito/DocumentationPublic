---
keyword: ContCL
summary: Continuous current limit used in the I²t power-limitation scheme.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 51
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
  - 10
  - 32000
  default: 32000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# ContCL

Continuous current limit used in the I²t power-limitation scheme.

## Overview

`ContCL` is the continuous current limit of the amplifier (in mA). Together with [PeakCL](PeakCL.md) (the peak limit) and [PeakTime](PeakTime.md) (the time allowed at peak), it defines the **I²t** scheme that lets the drive deliver brief bursts of peak current while protecting the motor and amplifier from sustained overheating.

## How it works

![I²t tripping mechanism](I2t-tripping-mechanism.svg)

The I²t scheme runs a first-order low-pass filter on the squared motor current — emulating the heating/cooling of the motor like charging a capacitor. The filtered value, $I_{filt}^{2}$, represents the equivalent continuous power. The drive may run up to `PeakCL`; once $I_{filt}^{2}$ rises above `ContCL²`, the limitation engages and the current is held down at the continuous level until the motor "cools".

### Filter time constant

When any of `ContCL`, `PeakCL` or `PeakTime` changes, the firmware recomputes the filter constant so that a step from zero up to `PeakCL` reaches `ContCL²` after exactly `PeakTime`:

$$
\frac{1}{\tau} = \frac{\ln\!\left(1 - \dfrac{ContCL^{2}}{PeakCL^{2}}\right)}{-\,PeakTime \times 0.001}
$$

(`PeakTime` is in ms.) The discrete filter is then run every control cycle on `MotorCurr²`.

### Engage / release (hysteresis)

| Condition | Action |
|-----------|--------|
| $I_{filt}^{2} > ContCL^{2}$ | I²t limitation engages |
| $I_{filt}^{2} < 0.90 \times ContCL^{2}$ | I²t limitation releases |

The 10 % hysteresis prevents rapid chattering at the threshold. While the limitation is engaged, the effective peak limit used by the current-command saturation (`gfLimitedPeakCL`) is lowered from `PeakCL` to the effective continuous value, and [StatReg](../../07-status-and-faults/StatReg.md) bit 25 ("power limit") is set.

### Limitation vs. fault

By default the I²t event is a *current limitation* (the command is clamped to the continuous level). If the current loop is **not** active, or if you set the relevant bit of `ControlMode` (the "I²t makes fault" option), the event instead **disables the axis** and raises [ConFlt](../../07-status-and-faults/ConFlt.md) = `1044` (`CON_FLT_MOTOR_I2T`, "Motor current over I2T").

> **Note:** if `ContCL` is set equal to or higher than `PeakCL`, the controller internally uses an effective continuous limit of `PeakCL / 2`. The stored `ContCL` value is not changed automatically, and an entry is logged to `ErrLog`.

## Changes between versions

In **v4** `ContCL` is a 32-bit integer; in **v5** (central-i only) it is a 32-bit float (`float32`). The I²t mechanism is unchanged.

## Examples

```text
AContCL=16000        ; continuous current limit (mA)
```

## See also

- [PeakCL](PeakCL.md) — peak current limit (and I²t upper bound)
- [PeakTime](PeakTime.md) — time allowed at peak current (sets τ)
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 25 flags active I²t power limitation
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault 1044 when I²t is configured to trip
