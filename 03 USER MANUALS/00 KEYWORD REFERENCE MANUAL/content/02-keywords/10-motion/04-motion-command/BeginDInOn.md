---
keyword: BeginDInOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 142
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BeginDInOn

**Definition:**

BeginDInOn configures a digital input line that, when asserted, automatically triggers a Begin command on the axis. Setting this parameter to a non-zero value enables the hardware trigger so that the rising edge of the selected digital input starts motion without a software command. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[Begin](Begin.md), [DInPort-DInPortHigh](../../05-inputs-outputs/04-digital-inputs/DInPort-DInPortHigh.md)
