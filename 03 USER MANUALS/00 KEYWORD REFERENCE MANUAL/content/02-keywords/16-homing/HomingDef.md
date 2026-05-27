---
keyword: HomingDef
summary: Array defining up to 15 homing steps, each an instruction plus its parameters.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 341
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 201
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
# HomingDef

Array defining up to 15 homing steps, each an instruction plus its parameters.

## Overview

`HomingDef` defines the built-in homing process: up to 15 steps, each an instruction plus the parameters for that instruction. The ones digit of the array index selects the configuration element within a step; the tens and hundreds digits select the step. So `HomingDef[1–10]` configures step 1, `HomingDef[11–20]` configures step 2, and so on. The first element of each step's set (`HomingDef[1, 11, …, 141]`) is the instruction; the remaining elements are that instruction's parameters.

`HomingDef` is read and executed when [HomingOn](HomingOn.md) is set to `1`; progress and any error are reported by [HomingStat](HomingStat.md) and [HomingStep](HomingStep.md). It is an axis-scoped array saved to flash. The homing process must terminate with an "End homing" instruction (`0`); reaching the last defined step without one aborts with a "too many steps" error.

## How it works

The instruction stored in the first element of each step (`HomingDef[1, 11, …, 141]`) selects what that step does:

| Value | Instruction |
|---|---|
| 0 | End homing. |
| 1 | Jog to limit. |
| 2 | Check if axis is out of limit |
| 3 | Relative point to point (PTP) motion |
| 4 | Jog to index |
| 5 | Move to index position |
| 6 | Set position |
| 7 | Wait N controller cycles |
| 8 | Enable (or disable) the motor |
| 9 | Move to hard stop (detected by motor stuck) |
| 10 | Move to hard stop (detected by high position error) |
| 11 | Jog until a change in the Home discrete input |
| 12 | Absolute point to point (PTP) motion |
| 13 | Set position software limits (RevPLim and FwdPLim parameters) |

The remaining elements of each step (`HomingDef[2, 12, …, 142]`, `HomingDef[3, 13, …, 143]`, etc.) hold the parameters related to the step's instruction.

The following tables detail the parameters for each instruction.

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 0 | End homing. This must be the last step. The homing process will stop. Reaching this step means that the homing is completed successfully. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 1 | Jog to limit. Move in jog mode with kinematics defined below. Complete successfully when the motion stops upon limit switch detection. |
| HomingDef[2, 12, …, 142] | Jog speed (the sign is the direction and determines which limit to look for). |
| HomingDef[3, 13, …, 143] | Jog acceleration/deceleration. |
| HomingDef[4, 14, …, 144] | Jog emergency deceleration. |
| HomingDef[5, 15, …, 145] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 2 | Check if axis is out of limit. Check if activation status of both RLS and FLS. If one of them is activated, terminate the homing process with a specific error code. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 3 | Relative point to point (PTP) motion. Move with the provided kinematics for a given relative distance. |
| HomingDef[2, 12, …, 142] | Maximum speed. |
| HomingDef[3, 13, …, 143] | Maximum acceleration/deceleration. |
| HomingDef[4, 14, …, 144] | Relative distance (positive or negative). |
| HomingDef[5, 15, …, 145] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 4 | Jog to index. Jog with the provided kinematics until index is detected. The jogging speed should be low enough to ensure that the index is detected. Recommended values are smaller than 8000 counts/s. |
| HomingDef[2, 12, …, 142] | Jog speed (the sign is the direction). |
| HomingDef[3, 13, …, 143] | Jog acceleration/deceleration. |
| HomingDef[4, 14, …, 144] | Jog emergency deceleration. |
| HomingDef[5, 15, …, 145] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 5 | Move to index position Move (using the provided kinematics) to the last recorded index position. |
| HomingDef[2, 12, …, 142] | Maximum speed. |
| HomingDef[3, 13, …, 143] | Maximum acceleration/deceleration. |
| HomingDef[4, 14, …, 144] | Emergency deceleration. |
| HomingDef[5, 15, …, 145] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 6 | Set position. Set the current position to the provided value. **Note:** this step does nothing if the conditions for [SetPosition](../10-motion/03-kinematics-configuration/SetPosition.md) are not met — refer to that keyword's page. |
| HomingDef[2, 12, …, 142] | New position value at current position. |

| HomingDef\[Index\] | Value descriptions |
|----|----|
| HomingDef\[1, 11, …, 141\] = 7 | Wait N controller cycles. |
| HomingDef\[2, 12, …, 142\] | Number of controller cycles to wait before advancing to next homing step. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 8 | Enable (or disable) the motor. |
| HomingDef[2, 12, …, 142] | 0 to disable the motor. 1 to enable the motor. |
| HomingDef[3, 13, …, 143] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 9 | Move to hard stop (detected by motor stuck). Move with the provided kinematics until hard stop is detected (defined by motor-stuck parameters). Motor stuck is detected when the absolute velocity is lower than the given velocity threshold and the absolute current is higher than the given motor-current threshold, for a consecutive period of the given stuck time. Once motor stuck is detected, the motor position is set to the given "position to set" value. The sign of the maximum-speed parameter defines the direction of motion. **Note:** this step does nothing if the conditions for [SetPosition](../10-motion/03-kinematics-configuration/SetPosition.md) are not met. |
| HomingDef[2, 12, …, 142] | Maximum speed. |
| HomingDef[3, 13, …, 143] | Maximum acceleration/deceleration. |
| HomingDef[4, 14, …, 144] | Emergency deceleration. |
| HomingDef[5, 15, …, 145] | Velocity threshold to define motor stuck. |
| HomingDef[6, 16, …, 146] | Motor current threshold [in mA] to define motor stuck. |
| HomingDef[7, 17, …, 147] | Stuck time [number of controller cycle]. |
| HomingDef[8, 18, …, 148] | New position value to set when hard stop is detected. |
| HomingDef[9, 19, …, 149] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 10 | Move to hard stop (detected by high position error). Move with the provided kinematics until hard stop is detected (defined by position-error parameters). Hard stop is detected when the absolute position error is higher than the given maximal position-error threshold. Once hard stop is detected, the motor position is set to the given "position to set" value. The sign of the maximum-speed parameter defines the direction of motion. **Note:** this step does nothing if the conditions for [SetPosition](../10-motion/03-kinematics-configuration/SetPosition.md) are not met. |
| HomingDef[2, 12, …, 142] | Maximum speed. |
| HomingDef[3, 13, …, 143] | Maximum acceleration/deceleration. |
| HomingDef[4, 14, …, 144] | Emergency deceleration. |
| HomingDef[5, 15, …, 145] | Maximal position error threshold. |
| HomingDef[6, 16, …, 146] | New position value to set when hard stop is detected. |
| HomingDef[7, 17, …, 147] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 11 | Jog until a change in the Home discrete input Move with the provided kinematics until a change in the Home discrete input is detected. Upon detection, stop the motion. The sign of the given maximum speed parameter and the state of the Home discrete input defines the direction of the motion. If the Home discrete input is "0", the sign of the maximum speed parameter is the direction of the motion. If the Home is "1", the direction is inverted. |
| HomingDef[2, 12, …, 142] | Maximum speed. |
| HomingDef[3, 13, …, 143] | Maximum acceleration/deceleration. |
| HomingDef[4, 14, …, 144] | Emergency deceleration. |
| HomingDef[5, 15, …, 145] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 12 | Absolute point to point (PTP) motion Move with the provided kinematics to a given absolute target position. |
| HomingDef[2, 12, …, 142] | Maximum speed. |
| HomingDef[3, 13, …, 143] | Maximum acceleration/deceleration. |
| HomingDef[4, 14, …, 144] | Absolute target position. |
| HomingDef[5, 15, …, 145] | Timeout for homing step [number of controller cycle]. |

| HomingDef[Index] | Value descriptions |
|---|---|
| HomingDef[1, 11, …, 141] = 13 | Set position software limits (RevPLim and FwdPLim parameters). Provides the means to set the values of reverse software position limit (RevPLim) and forward software position limit (FwdPLim). |
| HomingDef[2, 12, …, 142] | 1 to set RevPLim. 0 to ignore setting RevPLim. |
| HomingDef[3, 13, …, 143] | New value of RevPLim. |
| HomingDef[4, 14, …, 144] | 1 to set FwdPLim. 0 to ignore setting FwdPLim. |
| HomingDef[5, 15, …, 145] | New value of FwdPLim. |

**Example 1**:

![image74.emf](../../assets/image74.emf)

## Examples

```text
AHomingDef[1]=1      ; step 1 instruction: jog to limit
AHomingDef[2]=-50000 ; step 1 jog speed (negative = toward reverse limit)
AHomingDef[11]=0     ; step 2 instruction: end homing
AHomingDef[1]       ; read the instruction of step 1
```

## See also

- [HomingOn](HomingOn.md) — starts the process defined by this array
- [HomingStat](HomingStat.md) — reports progress and abort reasons for these steps
- [HomingStep](HomingStep.md) — index of the last completed step
- [SetPosition](../10-motion/03-kinematics-configuration/SetPosition.md) — referenced by the "set position" and hard-stop steps
- [RevPLim](../06-protections/03-motion/position-limit-protection/RevPLim.md) / [FwdPLim](../06-protections/03-motion/position-limit-protection/FwdPLim.md) — software limits set by instruction 13
