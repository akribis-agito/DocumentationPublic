---
keyword: AutoGVelTh
summary: Sets the velocity threshold in user units per second below which motion data is excluded from the auto-gain identification process.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 352
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 5000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGVelTh

**Definition:**

AutoGVelTh sets the velocity threshold in user units per second below which motion data is excluded from the auto-gain identification process. A sample is skipped when the absolute velocity is below AutoGVelTh or the absolute acceleration is below AutoGAccTh, so both thresholds must be met for the sample to be collected. The default is 5000. It is an axis-related parameter expressed in user units, saved to flash, and can be changed at any time.

**See also:**

[AutoGAccTh](AutoGAccTh.md), [AutoGOn](AutoGOn.md), [AutoGMinLen](AutoGMinLen.md)
