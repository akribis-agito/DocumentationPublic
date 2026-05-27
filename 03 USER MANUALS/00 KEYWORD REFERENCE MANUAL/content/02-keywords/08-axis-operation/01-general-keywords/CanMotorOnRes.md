---
keyword: CanMotorOnRes
summary: Result code from the last CanMotorOn enable attempt.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 413
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CanMotorOnRes

Result code from the last CanMotorOn enable attempt.

## Overview

`CanMotorOnRes` is a read-only status variable that holds the result of the last [CanMotorOn](CanMotorOn.md) command. It is axis-related and is not saved to flash.

The value `1` means **all pre-checks passed** — enabling the axis (with `MotorOn = 1`) would currently be accepted. Any **other** value is the code of the first failed check. The codes come from two pools: the controller's interpreter error numbers (the small "not allowed…" / hardware codes below) and the controller [fault codes](../../07-status-and-faults/ConFlt.md) (the 1000-based [Controller error codes](../../../04-error-codes/controller-error-codes.md)) when a standing protection would block the enable.

> Note: although the parameter table lists the range as `0…1`, the live value can hold any of the reason codes below. `1` is the only "all clear" value — do not treat `0` as success.

## How it works

`CanMotorOn()` writes this variable. The non-fault rejection codes are interpreter error numbers (`AG300_CTL01Interpreter.h`); the rest are `CON_FLT_*` controller fault codes. Representative values:

| Value | Internal name | Meaning |
|---|---|---|
| 1 | — | **All checks passed** — enabling would currently succeed. |
| 31 | `NOT_ALLOWED_BEFORE_COMMUTATION` | Commutation / auto-phasing has not been done yet. |
| 86 | `NOT_ALLOWED_WHILE_INRUSH_RESISTOR_ACTIVE` | Inrush charge relay has not closed yet. |
| 87 | `NOT_ALLOWED_IF_CALC_FILTERS_FAILED` | The last `CalcFilters` failed. |
| 102 | `NOT_ALLOWED_IF_FILTERS_MODIFIED` | Loop filters were changed without re-running `CalcFilters`. |
| 159 | `CI_PORT_NOT_ACTIVE` | Central-i port is not active/connected. |
| 175 | `CI_DEVICE_NOT_AMPLIFIER` | The Central-i device is not an amplifier. |
| 186 | `CI_DEVICE_RELAY_OFF` | Remote amplifier relay is still open. |
| 241 | `DRV02_TOO_HIGH_OVERALL_CURRENT` | Sum of `ContCL` across axes exceeds the hardware limit. |
| 244 | `FAULTY_FPGA` | A faulty FPGA was detected. |
| 245 / 250 / 268 | `AG100_FPGA_FW_DONOT_MATCH` / `AGD301_FPGA_FW_DONOT_MATCH` / `DYNBRK_FPGA_FW_DONOT_MATCH` | FPGA version does not match the firmware. |
| ≥ 1000 | `CON_FLT_*` | A standing controller fault would block enabling (STO, encoder error, over-current, bus voltage, over-temperature, …). See [Controller error codes](../../../04-error-codes/controller-error-codes.md). |

The list is not exhaustive — the firmware comments note that some protections may not be analysed by `CanMotorOn`, and because checks run in a fixed order only the **first** failure is reported.

## Examples

```text
ACanMotorOn         ; run the checks
ACanMotorOnRes      ; 1 = would enable; 31 = needs commutation; >=1000 = standing fault
```

## See also

- [CanMotorOn](CanMotorOn.md) — command that produces this result
- [MotorOn](MotorOn.md) — the keyword that actually enables the motor
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault codes (≥ 1000) echoed here
- [Controller error codes](../../../04-error-codes/controller-error-codes.md) — full code list
