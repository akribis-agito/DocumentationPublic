# LockValTable/LockValTabB

**Definition:**

LockValTable and LockValTabB store the feedback position when the digital event is triggered (i.e. LockVal).

LockValTable and LockValTabB are populated based on the LockCntr, as shown.

| Condition | Array used | Corresponding index for the array |
|:--:|:--:|:--:|
| 
$$
1 \leq LockCntr \leq 65000
$$ | LockValTable | 
$$
LockCntr
$$ |
| 
$$
65001 \leq LockCntr \leq 130000
$$ | LockValTabB | 
$$
LockCntr - 65000
$$ |

**Example:**

When an event triggers feedback logging and LockCntr turns 71000, LockValTabB\[6000\] will be used to store the updated LockVal.
