---
keyword: MaxPWM
summary: Limits PWM voltage-command magnitude; AGD101 maximum is 900 (90%), other products use their reported limits.
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
  range: null
  default: null
  scaling: 1.144
  implemented: final
overrides:
  central-i.v4:
    scaling: 1.526
  central-i.v5:
    scaling: 1.526
last_updated: '2026-10-21'
doc_revision: '2026.10'
---
# MaxPWM

Limits the PWM voltage-command magnitude.

## Overview

`MaxPWM` limits the voltage command produced by the current loop. Its units are **0.1% of the PWM command range**: `900` means 90% of that range. This is a bipolar modulation limit, not a direct high-side switch duty percentage. On AGD101's centred up/down PWM, a positive phase command of 90% maps to an ideal high-side duty of 95% before dead time; zero phase command maps to 50% duty.

The generated Quick Facts distinguish legacy standalone/central-i version cells, not individual AGD101 variants. A universal numeric range is therefore left unresolved; the legacy standalone scaling of 1.144 is not the normal AGD101 C28388 scaling (3.125 ticks per keyword unit). Use the product-specific limit below and the controller’s reported metadata.

### AGD101 limit

For AGD101, the maximum accepted setting is **900 (90%)**. The existing 90% default is retained. Higher settings are rejected without changing the stored value. When loading a parameter image saved by older firmware, an AGD101 value above the new internal bound is replaced by the existing default through the normal load-range validation.

The limit reserves modulation headroom for low-side current-sampling validation. It does not enable oversampling or certify current-sense settling, noise, or timing. Internal values use whole PWM counter ticks, so scaling and readback have the normal counter quantization. The change applies to AGD101's current-rating variants; other products retain their own product-dependent bounds.

## How it works

For brushless vector control, the firmware limits the output voltage vector using a precomputed `MaxPWM²`. The enhanced-speed-range option in [ControlMode](../../09-current-and-voltage/02-motor-variables/ControlMode.md) changes that vector budget. Direct per-phase clamps to ±`MaxPWM` apply in current-control or vector-control bypass modes. Configurable dead-time compensation can also change the final phase commands; the keyword alone does not establish a guaranteed physical low-side conduction window.

Voltage saturation is reported in [StatReg](../../07-status-and-faults/StatReg.md) bit 22. `MaxPWM` limits the requested output; saturation does not itself raise a [ConFlt](../../07-status-and-faults/ConFlt.md) fault.

## Examples

```text
AMaxPWM=900          ; AGD101 maximum: 90% PWM voltage-command range
AMaxPWM=300          ; reduce the limit to 30% of the command range
```

`AMaxPWM=901` is outside the AGD101 range and is refused. Use the controller's reported keyword limits for other products.

## See also

- [MaxVBus](MaxVBus.md) / [MinVBus](MinVBus.md) — bus-voltage limits
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 22 flags voltage saturation
