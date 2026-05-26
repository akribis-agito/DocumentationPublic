---
keyword: RecTrigsLogic
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 518
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigsLogic

**Condition:**

RecTrigsLogic is only applicable for parallel (logical) trigger detection (RecTrigsMode = 1).

**Definition:**

RecTrigsLogic defines how multiple trigger conditions are logically joined to form the overall logic condition for parallel trigger detection. Each index will join a different set of triggers.

| Index | Scope no. | Logic between |
|---|---|---|
| 1 | 1 (First) | Trigger 1 and trigger 2 |
| 2 | 1 (First) | Trigger 2 and trigger 3 |
| 3 | 2 (Second) | Trigger 1 and trigger 2 |
| 4 | 2 (Second) | Trigger 2 and trigger 3 |

The value of RecTrigsLogic determines the logical operator used.

| Value | Logical operator |
|-------|------------------|
| 1     | && (AND)         |
| 2     | \|\| (OR)        |

**Note:**

Logical operators (AND, OR) are left-associative (operation is performed from left to right).

**Example:**

If RecTrigsLogic\[1\] = 1 and RecTrigsLogics\[2\] = 2, the overall trigger logic condition for the first scope is

$$
(Trigger\ 1)\ \&\&\ (Trigger\ 2)\ ||\ (Trigger\ 3)
$$

The overall trigger will occur only if either

1.  trigger 1 and trigger 2 are activated, or

2.  trigger 3 is activated
