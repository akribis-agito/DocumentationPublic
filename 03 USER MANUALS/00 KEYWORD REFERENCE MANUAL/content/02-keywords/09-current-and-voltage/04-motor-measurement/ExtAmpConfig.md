---
keyword: ExtAmpConfig
summary: Sets the external amplifier’s current-feedback scale and phase-current offsets.
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 866
availability:
- controller
- ci-master
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -4000.0
  - 4000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ExtAmpConfig

On a Central-i master with an ADP03, ADP04 or ADP05 external amplifier interface, use `ExtAmpConfig` on the axis connected to that remote. The five floating-point settings are saved with the axis parameters.

| Index | Setting | Units | Default |
| --- | --- | --- | --- |
| 1 | Scale applied to both phase-current feedback readings | Scale factor | −1.049041748046875 on remote initialization |
| 2 | Phase A (Ia) command offset | mA | 0 |
| 3 | Phase B (Ib) command offset | mA | 0 |
| 4 | Phase A (Ia) feedback offset | mA | 0 |
| 5 | Phase B (Ib) feedback offset | mA | 0 |

The parameter table initializes all five elements to zero. When a supported remote is initialized, a zero in element 1 takes the scale shown above. A stored nonzero scale is retained. A negative scale reverses the feedback polarity.

For the digital-SPI amplifier, the command path adds the phase’s offset before scaling by `32768 / AAmpFullScale`. For example, at 8 counts/mA, a 1,000 mA Ia command with `ExtAmpConfig[2]=250` produces DAC code 42,768. The feedback path scales the centered current-sense reading and subtracts the corresponding feedback offset.

Read `AExtAmpConfig[1]` for the scale on axis A or `AExtCurrCmdVal[1]` for the transmitted phase A DAC code. [ExtCurrCmdVal](ExtCurrCmdVal.md) · [AAmpFullScale](../../02-motor-and-amplifier/AAmpFullScale.md)
