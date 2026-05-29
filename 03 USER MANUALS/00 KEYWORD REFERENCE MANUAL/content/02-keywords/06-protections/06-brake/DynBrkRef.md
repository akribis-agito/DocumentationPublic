---
keyword: DynBrkRef
summary: Sets the maximum strength (shorting duty-cycle ceiling) of dynamic braking.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 404
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
  scaling: 2.288
  implemented: final
overrides: {}
---
# DynBrkRef

Sets the maximum strength of dynamic braking — the ceiling on the phase-shorting duty cycle.

## Overview

When [dynamic braking](Dynamicbrake.md) engages, the axis shorts the motor phases with a variable duty cycle: higher duty cycle means stronger braking. `DynBrkRef` sets the **upper limit** of that duty cycle — the strongest braking the axis is allowed to apply. The axis automatically scales the actual duty cycle down from this ceiling as the braking current approaches the current limit, so `DynBrkRef` is a maximum, not a fixed level.

The value is expressed as braking strength where **1000 corresponds to the maximum (100%) shorting duty cycle**. Smaller values cap the braking proportionally weaker; 0 disables braking even when [DynBrakeOn](DynBrakeOn.md) is set.

## How it works

While the dynamic brake is engaged, the axis recomputes the shorting duty cycle each control cycle from the headroom remaining below the current limit:

$$
\text{duty} = \frac{\text{PeakCL}_{limited} - |\text{MotorCurr}|}{\text{PeakCL}_{limited}} \times \text{DynBrkRef} \times scaler
$$

- The result is clamped to the range `[0, DynBrkRef]`, so as the braking current rises toward the [PeakCL](../02-current-and-voltage/PeakCL.md)/[ContCL](../02-current-and-voltage/ContCL.md) limit the applied duty cycle automatically backs off to keep the current within limits.
- `scaler` is a fixed soft-start ramp (starting low and stepping up to full over a few cycles), so braking engages gradually rather than as a step. This ramp is not user-configurable.
- **Bus-voltage protection:** if the bus voltage reaches its ceiling ([MaxVBus](../02-current-and-voltage/MaxVBus.md) held for [MaxVBusTime](../02-current-and-voltage/MaxVBusTime.md), or the absolute limit [MaxVBusAbs](../02-current-and-voltage/MaxVBusAbs.md)), the duty cycle is forced to 0 to avoid pumping more regenerated energy onto an already-high bus.

So `DynBrkRef` is the strongest-braking ceiling that the headroom formula scales down from. Setting it higher gives stronger braking up to the current limit; the controller will not exceed the current limit regardless of the value.

> **No separate engagement-speed setting:** the soft-start "speed" with which braking ramps up is fixed in firmware and is not exposed as a keyword. Only the braking-strength ceiling (`DynBrkRef`) and the enable switch ([DynBrakeOn](DynBrakeOn.md)) are user-configurable.

## Examples

```text
ADynBrakeOn=1
ADynBrkRef=1000         ; allow full-strength braking (100% duty ceiling)
ADynBrkRef             ; read back the configured ceiling
ADynBrkRef=500          ; cap braking at roughly half strength
```

## See also

- [Dynamic brake](Dynamicbrake.md) — overview of the dynamic-braking mechanism
- [DynBrakeOn](DynBrakeOn.md) — enables dynamic braking
- [PeakCL](../02-current-and-voltage/PeakCL.md) / [ContCL](../02-current-and-voltage/ContCL.md) — current limits that bound the braking
- [MaxVBus](../02-current-and-voltage/MaxVBus.md) / [MaxVBusAbs](../02-current-and-voltage/MaxVBusAbs.md) — bus-voltage ceilings that force the duty cycle to 0
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 28 reports dynamic brake active
