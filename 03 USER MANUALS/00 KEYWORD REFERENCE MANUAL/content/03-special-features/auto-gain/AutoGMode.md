---
keyword: AutoGMode
summary: Selects the operating mode of the automatic gain tuning algorithm.
availability:
- controller
- ci-master
products:
- agc300-et
- agc301-et
- agc301-et-bioxtreme
- agd155-af-2a06
- agd155-af-2a10
- agd200-et-2d01
- agd200-et-2d02
- agd200-et-2d05
- agd200-et-2d05-71
- agd301-et-2d01
- agd301-et-2d02
- agd301-et-2d05
- agd301-et-2d09
can_code: 367
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
  - 5
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
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
| 5 | Compute the estimated-to-user inertia-ratio gain (estimated total inertia divided by user-supplied total inertia, in percent) and validate it. |

In modes 3, 4 and 5 the supplied AutoGJratUs is acted on only when it lies within the AutoGMinRat to AutoGMaxRat range; outside that range the gains are not computed and nothing is applied. When gains are applied (full-auto modes 1 and 3, or via AutoGCopy in semi-auto modes 2 and 4), only the parameters enabled in AutoGMask are written, and they are written into the control set selected by AutoGNumSet.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGStatus](AutoGStatus.md), [AutoGNumSet](AutoGNumSet.md)
