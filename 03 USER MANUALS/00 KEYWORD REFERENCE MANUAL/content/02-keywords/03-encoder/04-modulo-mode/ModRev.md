---
keyword: ModRev
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 70
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: user
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ModRev

**Definition:**

ModRev defines divisor used in modulo operation, as explained below.

| ModRev value | Descriptions |
|:--:|:--:|
| 
$$
0
$$ | Modulo operation is disabled. |
| 
$$
\geq 0
$$ | Modulo operation is enabled, with feedback wrapped to the range of $\lbrack 0,\ ModRev - 1\rbrack$ |

When the feedback (generally, Pos) undergoes modulo operation, position reference (PosRef) and target position (AbsTrgt) will undergo modulo operation as well to ensure continuity in position control. Modulo operation also applies to

1.  position before mapping (PosBeforeMap)

2.  pulse-direction position (PDPos)

3.  gear motion position (MasterPos)

**Example:**

| Modulo operation input (after error mapping) | ModRev value | Modulo operation output |
|:--:|:--:|:--:|
| 3050 | 3000 | 50 |
| 3000 | 3000 | 0 |
| 0 | 3000 | 0 |
| -40 | 3000 | 2960 |
