---
keyword: BeginDInOn
summary: Enables a digital-input trigger that automatically issues Begin on the axis.
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

Enables a digital-input trigger that automatically issues `Begin` on the axis.

## Overview

`BeginDInOn` enables a hardware trigger so that a configured digital input automatically issues a [Begin](Begin.md) command, starting motion without a software command. When set to `1`, the rising edge of the selected digital input starts the move; when `0`, the trigger is disabled. The digital input state is read through the [DInPort-DInPortHigh](../../05-inputs-outputs/04-digital-inputs/DInPort-DInPortHigh.md) registers. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
BeginDInOn=1        ; enable digital-input start trigger
BeginDInOn=0        ; disable the trigger
BeginDInOn?         ; query state
```

## See also

- [Begin](Begin.md) — the command this trigger issues
- [DInPort-DInPortHigh](../../05-inputs-outputs/04-digital-inputs/DInPort-DInPortHigh.md) — digital input port status
