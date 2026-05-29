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
\frac{1}{\tau} = \frac{\ln\!\left(1 - \dfrac{\text{ContCL}^{2}}{\text{PeakCL}^{2}}\right)}{-\,\text{PeakTime} \times 0.001}
$$

(`PeakTime` is in ms.) The discrete filter is then run every control cycle on `MotorCurr²`.

![I-squared filtered response charging from zero toward PeakCL squared and reaching ContCL squared exactly at PeakTime; the engage and release thresholds are marked](i2t-curve.svg)

### Engage / release (hysteresis)

| Condition | Action |
|-----------|--------|
| $I_{filt}^{2} > \text{ContCL}^{2}$ | I²t limitation engages |
| $I_{filt}^{2} < 0.90 \times \text{ContCL}^{2}$ | I²t limitation releases |

The 10 % hysteresis prevents rapid chattering at the threshold. While the limitation is engaged, the effective peak limit used by the current-command saturation is lowered from `PeakCL` to the effective continuous value, and [StatReg](../../07-status-and-faults/StatReg.md) bit 25 ("power limit") is set.

### Limitation vs. fault

By default the I²t event is a *current limitation* (the command is clamped to the continuous level). If the current loop is **not** active, or if you set the relevant bit of `ControlMode` (the "I²t makes fault" option), the event instead **disables the axis** and [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1044 (motor current over I²t).

> **Note:** if `ContCL` is set equal to or higher than `PeakCL`, the controller internally uses an effective continuous limit of `PeakCL / 2`. The stored `ContCL` value is not changed automatically, and an entry is logged to [ErrLog](../../07-status-and-faults/ErrLog.md).

### Edge cases

- **Motor off:** the I²t filter and the engagement check continue to run; the filter input is normally the live `MotorCurr` so the filtered value decays back toward 0 once current ceases.
- **Mode dependency:** I²t works whenever the current loop is active (or when an external amplifier follows `CurrRef`). With no current loop active and no external-amplifier following, the I²t event raises a fault rather than limiting (because there is no command path to clamp).
- **Engage / release hysteresis:** engages at $I_{filt}^{2} > \text{ContCL}^{2}$, releases at $I_{filt}^{2} < 0.90 \times \text{ContCL}^{2}$ (10 % hysteresis prevents chatter).
- **`ContCL ≥ PeakCL`:** the effective continuous limit is silently set to `PeakCL / 2` — a misconfiguration, not a feature. Confirm with [ErrLog](../../07-status-and-faults/ErrLog.md) and correct `ContCL` and [PeakCL](PeakCL.md).
- **Range overflow:** writes outside `10…32000` (v4) are clamped to the keyword `range`.
- **Clearing the fault (when configured to trip):** ConFlt code 1044 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the I²t trip is not maskable through [ProtectMask](../01-general-protection/ProtectMask.md).

## Changes between versions

In **v4** `ContCL` is a 32-bit integer; in **v5** (central-i only) it is a 32-bit float (`float32`). The I²t mechanism is unchanged.

## Examples

```text
AContCL=16000        ; continuous current limit (mA)
```

### Walk-through: configure the I&#178;t scheme and watch it engage

A full I&#178;t setup is three keywords; check the engagement on a sustained-load move:

```text
APeakCL=4000          ; peak current limit (mA)
AContCL=2000          ; continuous limit (mA)
APeakTime=1000        ; allowed time at PeakCL before engage (ms)
```

When the motor is held at or near `PeakCL` (e.g. accelerating a heavy load), I&#178;_filt climbs toward `PeakCL&#178;` and crosses `ContCL&#178;` after approximately `PeakTime`. From that instant the [PeakCL](PeakCL.md) clamp drops to the continuous level and:

```text
AStatReg                      ; bit 25 (power limit) set while engaged
                              ; bit 21 (current saturation) set while CurrRef is being clamped
```

The limitation releases once `I²_filt` drops below `0.90 × ContCL²` (10% hysteresis). If `ControlMode` is configured for "I&#178;t makes fault" (or the current loop is not active), the same crossing instead disables the axis with `AConFlt = 1044` and the move ends with `AMotionReason = 8`.

## See also

- [PeakCL](PeakCL.md) — peak current limit (and I²t upper bound)
- [PeakTime](PeakTime.md) — time allowed at peak current (sets τ)
- [CurrLimMode](CurrLimMode.md) — controls how the saturated current command interacts with `PeakCL`
- [MaxMotorCurr](MaxMotorCurr.md) — instantaneous over-current trip (separate from I²t)
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 25 flags active I²t power limitation, bit 21 flags current saturation
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault 1044 when I²t is configured to trip
