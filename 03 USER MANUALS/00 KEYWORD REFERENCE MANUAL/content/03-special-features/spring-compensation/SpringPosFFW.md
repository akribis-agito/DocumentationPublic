---
keyword: SpringPosFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 595
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
  - -100000
  - 100000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# SpringPosFFW

**Definition:**

SpringPosFFW sets the position feedforward gain that scales the position-dependent spring correction current added to the control output. It is an axis-related parameter saved to flash and can be changed at any time.

The active spring compensation is a linear (position-proportional plus constant) model, not a lookup table. While [SpringOn](SpringOn.md) is nonzero and the position reference lies inside the band [SpringPLow](SpringPLow.md) to [SpringPHigh](SpringPHigh.md), a compensation current is added to the axis current reference at the output of the velocity loop (just ahead of the current/torque loop):

$$ I_{spring} = (P_{ref} - \text{SpringPLow}) \cdot \text{SpringPosFFW} \cdot 0.001 + \text{SpringCurrFFW} \cdot 0.001 \;\; [\text{mA}] $$

where $P_{ref}$ is the shaped, filtered position reference (the commanded profile, not the measured feedback position), SpringPosFFW is in microamps per position count, and SpringCurrFFW is in microamps. SpringPLow and the position reference are entered in user units and converted internally to position counts. The added current is summed into the current reference (in mA) and is therefore still subject to the normal current and torque limits applied downstream. Outside the band no spring current is added at all.

**See also:**

[SpringOn](SpringOn.md), [SpringCurrFFW](SpringCurrFFW.md), [SpringTable](SpringTable.md)
