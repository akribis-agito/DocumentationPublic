---
keyword: HomingStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 342
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomingStat

HomingStat reports the status of homing.

| HomingStat | Descriptions |
|----|----|
| 0 | No homing was done after power on or reset |
| Positive value (not 100) | Homing is in process. HomingStat value reflects the number of the currently processed step in the homing process. |
| -1 | The homing process failed and aborted due to wrong parameter at HomingDef array (the parameters related to each homing step are checked at the beginning of each step). |
| -2 | The homing process failed and aborted due to timeout during one of the homing steps. |
| -3 | The homing process failed and aborted due to unexpected motor off. During one of the homing steps, the axis was disabled due to some fault (reflected at the value of ConFlt) and the step could not be completed. |
| -4 | The homing process failed and aborted due to wrong motion reason. This means that the homing step which expects a given reason for end of motion (RLS, index, reached target…) encounters a different reason for end of motion. |
| -5 | The homing process failed and aborted due to wrong step type. This means that the homing process reached a step whose type (as defined in the HomingDef array) is not recognized. |
| -6 | The homing process failed and aborted due to axis in motion when starting a new step. |
| -7 | The homing process failed and aborted due to too many steps. This error will happen if the homing process reaches the last step defined in the HomingDef array, but the step’s instruction is not “End homing”. |
| -8 | The homing process failed and aborted due to unexpected limit. This error is relevant only when step’s instruction is “Check if axis is out of limit”. |
| 100 | The homing process has been successfully completed. |
