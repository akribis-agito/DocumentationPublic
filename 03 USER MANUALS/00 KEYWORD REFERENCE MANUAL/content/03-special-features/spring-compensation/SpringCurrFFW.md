---
keyword: SpringCurrFFW
summary: Sets a constant, position-independent feedforward current, in microamps, that is added by the spring compensation.
availability:
- controller
- ci-master
can_code: 596
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
  - -16000000
  - 16000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -64000000
    - 64000000
  agc300-et:
    range:
    - -4000000
    - 4000000
  agc301-et:
    range:
    - -4000000
    - 4000000
  agc301-et-bioxtreme:
    range:
    - -4000000
    - 4000000
  agd200-et-2d01:
    range:
    - -4000000
    - 4000000
  agd200-et-2d02:
    range:
    - -8000000
    - 8000000
  agd301-et-2d01:
    range:
    - -4000000
    - 4000000
  agd301-et-2d02:
    range:
    - -8000000
    - 8000000
  agd301-et-2d09:
    range:
    - -25500000
    - 25500000
  agd155-af-2a06:
    range:
    - -25500000
    - 25500000
  agd155-af-2a10:
    range:
    - -28500000
    - 28500000
  agd155-ec:
    range:
    - -25500000
    - 25500000
  agd155-ec-var34:
    range:
    - -28500000
    - 28500000
  agd155-ec-var34-3:
    range:
    - -42500000
    - 42500000
  agd156-ec:
    range:
    - -12726000
    - 12726000
  agd101-ec-34a:
    range:
    - -28280000
    - 28280000
  agd101-ec-17a:
    range:
    - -14140000
    - 14140000
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# SpringCurrFFW

**Definition:**

SpringCurrFFW sets a constant, position-independent feedforward current, in microamps, that is added by the spring compensation. This bias current is applied whenever the position reference lies within the band defined by [SpringPLow](SpringPLow.md) and [SpringPHigh](SpringPHigh.md), and it does not vary with position; the position-proportional part of the spring compensation comes from [SpringPosFFW](SpringPosFFW.md). It is an axis-related parameter saved to flash and can be changed at any time.

The default is 0 (no constant bias). The allowed range spans from minus to plus the axis maximum current command (expressed in microamps, i.e. the maximum current command in mA scaled by 1000). The entered microamp value is scaled by 0.001 to convert it to milliamps before it is summed into the current reference, so it remains subject to the normal current and torque limits applied downstream.

**See also:**

[SpringOn](SpringOn.md), [SpringPosFFW](SpringPosFFW.md), [SpringTable](SpringTable.md)
