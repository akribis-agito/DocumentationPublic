---
keyword: AutoGMinLen
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 355
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
  - 10
  - 100
  default: 15
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# AutoGMinLen

**Definition:**

AutoGMinLen sets the minimum number of collected motion samples that the auto-gain algorithm must gather in a motion direction/command region before that region is considered to have enough data for inertia identification. Samples are sorted into four regions by direction of motion and direction of command; once at least two of those four regions have each accumulated AutoGMinLen samples, the algorithm has enough data to compute an inertia-ratio estimate and updated gains. AutoGMaxLen sets the per-region upper limit on collected samples. Range 10 to 100; default 15. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGMaxLen](AutoGMaxLen.md), [AutoGAccTh](AutoGAccTh.md), [AutoGVelTh](AutoGVelTh.md)
