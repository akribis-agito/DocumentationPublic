---
keyword: MaxPWM
summary: Limits the maximum PWM duty cycle (and thus the maximum voltage to the motor).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 91
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 1470
  default: null
  scaling: 1.144
  implemented: final
overrides:
  central-i.v4:
    scaling: 1.526
  central-i.v5:
    scaling: 1.526
---
# MaxPWM

Limits the maximum PWM duty cycle (and thus the maximum voltage to the motor).

## Overview

For PWM amplifiers, `MaxPWM` limits the maximum duty cycle of the PWM drive — and therefore the maximum voltage applied to the motor. The units are **0.1%**: `1000` represents 100% duty cycle, and `0` represents 0%.

## How it works

`MaxPWM` is applied as the saturation limit on the output voltages inside the current loop, in two ways:

- **Vector magnitude.** For brushless motors the firmware limits the magnitude of the output voltage vector so that $\sqrt{V_q^{2}+V_d^{2}} \le \text{MaxPWM}$ (using a precomputed `MaxPWM²`). If the enhanced-speed-range option is enabled in `ControlMode`, the squared budget is scaled by $\frac{4}{3}$ (space-vector over-modulation).
- **Per-phase clamp.** Each phase output (`Va`, `Vb`, `Vc`) is independently clamped to ±`MaxPWM`.

Whenever the output voltage is clamped, the firmware records a saturation factor and sets [StatReg](../../07-status-and-faults/StatReg.md) bit 22 (voltage saturation). `MaxPWM` is a *limit*, not a trip — exceeding the demand simply saturates the output; it does not raise a [ConFlt](../../07-status-and-faults/ConFlt.md) fault.

### Edge cases

- **Motor off:** the saturation does not actively clamp (no phase voltages are being driven), but the limit takes effect immediately on the next motor-on.
- **Mode dependency:** the per-phase clamp applies whenever the current loop produces phase outputs (servo or stepper internal amplifier).
- **External amplifier:** `MaxPWM` has no effect when the drive is configured for an external amplifier (analog current or analog velocity command — the phase outputs are not driven by the internal current loop).
- **Range overflow:** writes outside `0…1470` (0.1 % units, i.e. up to ~147 %) are clamped to the keyword `range`. Note the keyword units are 0.1 %, not %: `1000` = 100 %.
- **HWProtectBits / ProtectMask:** voltage saturation is not a trip and not maskable.

## Examples

With a 48 V bus and default `MaxPWM = 900`, to cap the output at 30% duty cycle (14.4 V) set:

```text
AMaxPWM=300          ; limit to 30% duty cycle (~14.4 V on a 48 V bus)
```

## See also

- [MaxVBus](MaxVBus.md) / [MinVBus](MinVBus.md) — bus-voltage limits
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 22 flags voltage saturation
