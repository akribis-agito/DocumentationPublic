---
keyword: RecTrigForce
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 252
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigForce

**Definition:**

RecTrigForce will overrule the trigger detection and force the recording to continue. Forced trigger will occur regardless of whether RecTrigForce is called while pre-trigger data is filled, or while the scope is waiting trigger (after filling pre-trigger data).

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

For example, RecTrigForce\[1\] will force-trigger the first scope.

<span class="anchor" id="_RecTrigMask"></span>
