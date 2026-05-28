---
keyword: VelFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 108
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
# VelFFW

Velocity feedforward gain, applied to the first derivative of the position reference.

## Overview

`VelFFW` is the velocity feedforward gain. It multiplies the velocity reference [dPosRef](../../../02-keywords/10-motion/01-kinematics-status/dPosRef.md) (the filtered first time-derivative of the position reference) and adds the result, ahead of feedback action, into the current reference that drives the current loop. Acting on the reference velocity, it compensates the velocity-proportional (damping/friction) term so the controller does not have to wait for a following error to build before commanding the force needed to maintain speed.

`VelFFW` adds into the **current reference** alongside the acceleration feedforward [AccFFW](AccFFW.md). It is a distinct mechanism from the velocity feedforward into the velocity-loop reference [VelRef](../../../02-keywords/10-motion/01-kinematics-status/VelRef.md), which is scaled by [VelTrackFact](../04-velocity-control/VelTrackFact.md).

Velocity feedforward is applied only in position operation mode ([OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 3). It has no effect in velocity, force or current operation modes.

`VelFFW` is an array used for gain scheduling. With no gain scheduling, the first element `VelFFW[1]` is the active value. See [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) for which array elements are selected under each scheduling method.

## How it works

Each control cycle the velocity feedforward term is the reference velocity [dPosRef](../../../02-keywords/10-motion/01-kinematics-status/dPosRef.md) scaled by `VelFFW` and a fixed gain scaling of 1/2¹⁶ (= 1.52587890625 × 10⁻⁵):

$$
VelTerm = dPosRef \times VelFFW \times \frac{1}{2^{16}}
$$

The velocity term is summed with the acceleration feedforward term (see [AccFFW](AccFFW.md)) to form the combined feedforward output. That output optionally passes through the feedforward filter ([FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md)) and is then added to the velocity-loop output to form the current reference [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md):

$$
CurrRefCtrl = (\text{velocity-loop output}) + (\text{filtered feedforward output})
$$

During the segment transitions of coordinated/vector motion the feedforward output is momentarily forced to zero to avoid current spikes from limited transition precision.

### Scaling, range and default

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit integer | 32-bit float |
| Range | 0 to 50000 | 0 to 1000000000 |
| Default | 0 | 0 |
| Gain scaling | 1/2¹⁶ (1.52587890625 × 10⁻⁵) | 1/2¹⁶ (1.52587890625 × 10⁻⁵) |

With the default value `0`, velocity feedforward is off.

## Examples

```text
AVelFFW[1]=65536     ; set velocity feedforward gain (first array element)
AVelFFW[1]           ; read back the gain
```

### Worked example: contribution at a constant slew

With `VelFFW = 65536` (a unit-effective gain after the internal 1/2^16 scaling) and a reference velocity `dPosRef = 50000` (user velocity units), the velocity feedforward term contributed to the current reference is:

`VelTerm = 50000 x 65536 x (1 / 65536) = 50000` (current units)

The same `VelTerm` is added whether the position loop has any error or not, so the steady current required to sustain the slew is supplied by the feedforward and the velocity loop only acts on the residual.

## See also

- [AccFFW](AccFFW.md) — acceleration feedforward gain (summed with the velocity term)
- [dPosRef](../../../02-keywords/10-motion/01-kinematics-status/dPosRef.md) — velocity reference this gain multiplies
- [FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md) — feedforward filter applied to the combined feedforward output
- [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) — current reference the feedforward adds into
- [VelTrackFact](../04-velocity-control/VelTrackFact.md) — velocity feedforward into the velocity-loop reference (a different path)
- [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) — gain-scheduling selection of array elements
