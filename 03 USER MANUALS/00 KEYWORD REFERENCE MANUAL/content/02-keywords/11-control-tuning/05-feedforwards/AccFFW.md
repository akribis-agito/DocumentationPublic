---
keyword: AccFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 101
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 50000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 0
    - 1000000000
---
# AccFFW

Acceleration feedforward gain, applied to the second derivative of the position reference.

## Overview

`AccFFW` is the acceleration feedforward gain. It multiplies the acceleration of the post-processed position reference (the second time-derivative of the shaped/filtered reference) and adds the result, ahead of feedback action, into the current reference that drives the current loop. Acting on the reference acceleration, it compensates the inertial (mass) term of the load so the controller does not have to wait for a following error to build before commanding the required accelerating force.

Acceleration feedforward is applied only in position operation mode ([OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 3). It has no effect in velocity, force or current operation modes.

`AccFFW` is an array used for gain scheduling. With no gain scheduling, the first element `AccFFW[1]` is the active value. See [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) for which array elements are selected under each scheduling method.

## How it works

Each control cycle, the reference acceleration is formed as the second difference of the post-processed (shaped and filtered) position reference — the same reference signal the position loop uses:

$$
a_{\text{ref}} = \text{ref}_{k} - 2 \cdot \text{ref}_{k-1} + \text{ref}_{k-2}
$$

The acceleration feedforward term is this reference acceleration scaled by `AccFFW` and a fixed gain scaling of $1/2^{8}$ (= 3.90625 × 10⁻³):

$$
\text{AccTerm} = \frac{a_{\text{ref}} \cdot \text{AccFFW}}{2^{8}}
$$

The acceleration term is summed with the velocity feedforward term (see [VelFFW](VelFFW.md)) to form the combined feedforward output. That output optionally passes through the feedforward filter ([FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md), central-i v5) and is then added to the velocity-loop output to form the current reference [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md):

$$
\text{CurrRefCtrl} = (\text{velocity-loop output}) + (\text{filtered feedforward output})
$$

During the segment transitions of coordinated/vector motion the feedforward output is momentarily forced to zero to avoid current spikes from limited transition precision.

### Scaling, range and default

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit integer | 32-bit float |
| Range | 0 to 50000 | 0 to 1000000000 |
| Default | 0 | 0 |
| Gain scaling | 1/2⁸ (3.90625 × 10⁻³) | 1/2⁸ (3.90625 × 10⁻³) |

With the default value `0`, acceleration feedforward is off.

## Examples

```text
AAccFFW[1]=2560      ; set acceleration feedforward gain (first array element)
AAccFFW[1]           ; read back the gain
```

### Worked example: contribution at a peak reference acceleration

With `AccFFW = 2560` (v4 integer) and a reference acceleration of `a_ref = 1000` (user units/s² per cycle, as the second difference of the reference), the acceleration feedforward term contributed to the current reference is:

`AccTerm = 1000 x 2560 x (1 / 256) = 10000` (current units)

The feedforward injects this current ahead of the loop, so the velocity loop does not have to develop a following error to produce the accelerating current.

### Walk-through: pair acceleration and velocity feedforwards

`AccFFW` and [VelFFW](VelFFW.md) are summed at the same point in the loop (the combined feedforward output added to the velocity-loop output to form the current reference). They are usually configured together.

1. **Enable both feedforwards on set 1** (no scheduling). Begin with both zero, then write the value you have computed or measured:

   ```text
   AAccFFW[1]=2560
   AVelFFW[1]=65536
   ```

2. **Optionally apply the feedforward filter** to smooth the combined feedforward output (helpful if the reference is quantised or noisy):

   ```text
   AFFFiltDef[1]=1; AFFFiltDef[2]=100000   ; first-order low-pass at 1 kHz
   AFFFiltOn[1]=1
   ACalcFilters
   ```

3. **Run a profiled move** and read the loop-side current reference [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) (v5) to see the feedforward contribution riding on top of the velocity-PI output. During the constant-acceleration phase the `AccFFW` term dominates; during the constant-velocity phase the `VelFFW` term does.

4. **Watch [StatReg](../../../02-keywords/07-status-and-faults/StatReg.md) bit 21** (current saturation). A correctly sized feedforward pair reduces the following error that the position/velocity loops have to develop, so the current command is less likely to saturate during the acceleration phase.

## See also

- [VelFFW](VelFFW.md) — velocity feedforward gain (summed with the acceleration term)
- [FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md) — feedforward filter applied to the combined feedforward output
- [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) — current reference the feedforward adds into
- [PosGain](../03-position-control/PosGain.md) — position-loop gain whose error this feedforward helps suppress
- [VelTrackFact](../04-velocity-control/VelTrackFact.md) — velocity feedforward into the velocity-loop reference (a parallel path)
- [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) — gain-scheduling selection of array elements
