# ECAMCycles

**Definition:**

ECAMCycles is used to define the number of occurrences of repeating/cyclical cam pattern. It is an array of size 10, where each element corresponds to a cam pattern.

| Value | ECAM properties |
|----|----|
| -2147483648 | Endless ECAM without starting nor ending segments |
| 2147483647 | Endless ECAM with only starting segment |
| \> 0 | ECAM with starting and ending segments, as well as ECAMCycles number of occurrences of cyclical patterns. |
| \< 0 | ECAM with starting and ending segments, as well as 2\*ECAMCycles number of occurrences of repeating patterns |

**Note:**

ECAMCycles describes the number of occurrences of the same pattern rather than repetition number. That is, if ECAMCycles = 1, it indicates that there is no repetition on the cam pattern, where ECAMStartCyc and ECAMEndCyc will not matter since the pattern within such range is already encapsulated by ECAMStart and ECAMEnd. In summary, a b s ( E C A M C y c l e s ) must be more than 1.

Please refer to the figures in [Motion mode – Electronic cam (ECAM)](../../../02-keywords/10-motion/08-motion-mode-electronic-cam-ecam/00-overview.md) for more information on the patterning logics.
