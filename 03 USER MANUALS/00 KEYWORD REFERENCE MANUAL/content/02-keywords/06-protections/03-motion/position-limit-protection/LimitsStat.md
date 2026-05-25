# LimitsStat

**Definition:**

LimitsStat reflects the current status of the limit switches. If the bit is set ("1"), limit is activated. If the bit is cleared ("0"), limit is not activated.

| LimitsStat, Bit # | 0 | 1 | 2-31 |
|---|---|---|---|
| Axis | RLS (Reverse Limit Switch) | FLS (Forward Limit Switch) | Unused |

**Example:**

LimitsStat == 1 indicate that RLS is active.

LimitsStat == 2 indicate that FLS is active.
