# AutoGMode

**Definition:**

AutoGMode selects the operating mode of the automatic gain tuning algorithm. The mode controls whether the algorithm computes the inertia ratio itself or uses the value you supply in AutoGJratUs, and whether the resulting gains are applied automatically (full auto) or left for you to apply later with the AutoGCopy keyword (semi auto). Range 0 to 5; default 1. It is an axis-related parameter saved to flash and can be changed at any time.

| Value | Meaning |
|-------|---------|
| 0 | Manual: the algorithm runs but no parameters are computed. |
| 1 | Compute the inertia ratio and gains and apply them automatically (full auto). |
| 2 | Compute the inertia ratio and gains but do not apply them; apply later with AutoGCopy (semi auto). |
| 3 | Use the user-supplied inertia ratio from AutoGJratUs and apply the gains automatically (full auto). |
| 4 | Use the user-supplied inertia ratio from AutoGJratUs but do not apply the gains; apply later with AutoGCopy (semi auto). |
| 5 | Compute the estimated-to-user inertia-ratio gain, validate it, and use it in the control loop. |

**See also:**

[AutoGOn](AutoGOn.md), [AutoGStatus](AutoGStatus.md), [AutoGNumSet](AutoGNumSet.md)
