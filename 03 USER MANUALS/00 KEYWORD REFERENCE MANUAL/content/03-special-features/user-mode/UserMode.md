---
keyword: UserMode
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 77
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# UserMode

UserMode is a parameter used to activate special algorithms within the controller. These
algorithms are for the most part custom made for dedicated purposes.
By assigning a very specific value to UserMode, the user can activate a pre-defined algorithm
that was included in the controller software for this user needs.
Relevant customers will be informed about possible and relevant values of UserMode to activate
their special algorithms.
All other customers are advised to keep this parameter as 0, to avoid accidental operation of a
non-documented special and application dedicated feature.
