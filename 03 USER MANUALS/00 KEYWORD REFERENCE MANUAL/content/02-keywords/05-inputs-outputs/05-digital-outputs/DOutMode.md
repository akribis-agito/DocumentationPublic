# DOutMode

**Definition:**

DOutMode assigns specific software functions to digital outputs. These functions are used to reflect selected controller statuses on the outputs.

Each index in DOutMode\[\] corresponds to an output (1-based index).

| Index | Corresponds to |
|-------|----------------|
| 1     | Output 1       |
| 2     | Output 2       |
| 3     | Output 3       |
| …     | …              |

The functionality is selected by lower 16 bits of Value. The list of functionalities is as per the table below.

**Note:**

Value (lower 16 bits) Function descriptions 0 General output – no function 1 Reserved 2 Motor on status Output bit will reflect the status of motor, with “1” and “0” representing enabled and disabled state, respectively. 3 In motion status Output bit is set if axis is in motion and cleared otherwise. 4 In acceleration status Output bit is set if axis is accelerating and cleared otherwise. Note This functionality is valid only for motion mode that uses the built-in profiler. For example, indirect Pulse/Direction mode uses this profiler, while direct Pulse/Direction mode does not. 5 In deceleration status Output bit is set if axis is decelerating and cleared otherwise. Note This functionality is valid only for motion mode that uses the built-in profiler. For example, indirect Pulse/Direction mode uses this profiler, while direct Pulse/Direction mode does not. 6 In constant speed status Output bit is set if axis is in constant speed motion phase and cleared otherwise. Note This functionality is valid only for motion mode that uses the built-in profiler. For example, indirect Pulse/Direction mode uses this profiler, while direct Pulse/Direction mode does not. 7 End of motion - not implemented 8 In target status Output bit is set if InTargetStat = 4 (in target) and cleared otherwise. 9 Fault/alarm status Output bit is set if ConFlt is non-zero (with faults) and cleared otherwise. 10 Warnings found in the last motion – not implemented 11 Current saturation in the last motion - not implemented 12 Limit active status Output bit is set if LimitsStat is non-zero and cleared otherwise. Non-zero LimitsStat indicates either or both reverse limit switch (RLS) and forward limit switch (FLS) is activated. 13 Out of travel range status Output bit is set if the position reference is higher than FwdPLim or smaller than RevPLim. It is cleared otherwise. 14 Regeneration active status Output bit is set if regeneration is activated and cleared otherwise. 15 Dynamic brake active status Output bit is set if dynamic braking is activated and cleared otherwise. 16 Motor brake active status Output bit is set if motor brake is activated and cleared otherwise. 17 Reserved 18 Reverse limit switch (RLS) active status Output bit is set if LimitsStat bit 0 is set and cleared otherwise. 19 Forward limit switch (FLS) active status Output bit is set if LimitsStat bit 1 is set and cleared otherwise. 20 Homing done status Output bit is set if HomingStat = 100 and cleared otherwise. 21 Force in target status Output bit is set if ForceInTrgtStat = 4 (in target) and cleared otherwise.

The axis, for which the function **applies to**, is selected by the Value (upper 16 bits).

| Axis | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value (upper 16 bit) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

**Example:**

If ADOutMode\[2\] = 65538 (binary 00000000 0000000<u>1</u> 00000000 000000<u>1</u>0):

6.  Index → 2 (Digital Output 2)

7.  Value (upper 16-bits) → 1 (Axis B)

8.  Value (lower 16-bits) → 2 (Motor On status)

Digital Output 2 (of Axis A) reflects Axis B Motor On status.
