---
keyword: ForceFFWP
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 599
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    can_code: 607
---
# ForceFFWP

Position-wise force feedforward gain (force-over-PIV control only).

## Overview

`ForceFFWP` is the position-wise force feedforward gain. It is used **only** in force-over-PIV control ([ForcePIVOn](ForcePIVOn.md) = 1); in standard force control (`ForcePIVOn = 0`) it has no effect.

In force-over-PIV mode it multiplies the change in the filtered force reference relative to its value at the moment force operation mode was entered, and the result is added to the force PID output before that sum is converted to a position reference:

$$
\text{ForceFFWP term} = \text{ForceFFWP} \cdot (\text{ForceRef} - \text{ForceRef}_{\text{entry}})
$$

Here `ForceRef` is the filtered reference [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) and `ForceRef_entry` is the internally recorded filtered reference captured at the instant force mode was entered. The gain is applied with an internal scaling of 1.0 (used as entered).

Value range is `0` to `2147483647`; the default is `0`. The keyword is stored in flash and may be changed while the motor is on and in motion.

## How it works

In force-over-PIV control the force loop is the outermost loop and produces a position reference for the inner position/velocity cascade. The force PID output (P + I + D) is summed with this `ForceFFWP` feedforward term; the sum is scaled by the controller sampling time and added to the entry position to form the position reference, which is then saturated at the software position limits. Referencing the feedforward to the entry-time force value keeps the contribution zero at the moment of mode entry, so the switch into force mode is bumpless.

### Loop math

Writing $T_s$ for the controller sampling time, $\text{Pos}_{\text{entry}}$ for the position captured when force mode was entered, and $\text{ForceRef}_{\text{entry}}$ for the filtered force reference captured at that same instant, the generated position reference is:

$$
\text{PosRef} = \text{Pos}_{\text{entry}} + T_s \cdot \Big( (P+I+D) + \text{ForceFFWP} \cdot (\text{ForceRef} - \text{ForceRef}_{\text{entry}}) \Big)
$$

followed by saturation at [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) and [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md). The bracketed sum is multiplied by $T_s$ and added to the fixed entry position $\text{Pos}_{\text{entry}}$ — recomputed from scratch each cycle, not accumulated onto the previous reference — so a sustained force-loop output holds the position reference at a fixed offset from the entry position proportional to that output. At mode entry both the position-error and force-reference deviations are zero, so `PosRef` starts exactly at $\text{Pos}_{\text{entry}}$.

## Examples

```text
AForcePIVOn[1]=1        ; select force-over-PIV control
AForceFFWP[1]=500       ; set the position-wise force feedforward gain
AForceFFWP[1]           ; read the position-wise force feedforward gain
```

## See also

- [ForcePIVOn](ForcePIVOn.md) — must be 1 for ForceFFWP to take effect
- [ForceFFW](ForceFFW.md) — current-wise force feedforward
- [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) — filtered reference this gain acts on
- [Force control](00-overview.md) — force-loop structure overview
