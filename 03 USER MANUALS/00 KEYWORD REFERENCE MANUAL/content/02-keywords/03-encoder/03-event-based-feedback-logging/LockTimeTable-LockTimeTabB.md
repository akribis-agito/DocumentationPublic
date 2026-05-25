# LockTimeTable/LockTimeTabB

**Definition:**

LockTimeTable and LockTimeTabB store the time when the digital event is triggered. The time is stored in terms of number of controller cycle elapsed since feedback logging is enabled from the disabled state.

LockTimeTable and LockTimeTabB are populated based on the LockCntr, as shown.

| Condition | Array used | Corresponding index for the array |
|:--:|:--:|:--:|
| 
$$
1 \leq LockCntr \leq 65000
$$ | LockTimeTable | 
$$
LockCntr
$$ |
| 
$$
65001 \leq LockCntr \leq 130000
$$ | LockTimeTabB | 
$$
LockCntr - 65000
$$ |

**Example:**

When an event triggers feedback logging and LockCntr turns 70000, LockTimeTabB\[5000\] will be used to store the logging time.
