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

The non-fault rejection codes are controller error numbers; the rest are controller fault codes. Representative values:

| Value | Meaning |
|---|---|
| 1 | **All checks passed** — enabling would currently succeed. |
| 31 | Commutation / auto-phasing has not been done yet. |
| 86 | Inrush charge relay has not closed yet. |
| 87 | The last [CalcFilters](../../11-control-tuning/01-general-keywords/CalcFilters.md) failed. |
| 102 | Loop filters were changed without re-running [CalcFilters](../../11-control-tuning/01-general-keywords/CalcFilters.md). |
| 159 | Central-i port is not active/connected. |
| 175 | The Central-i device is not an amplifier. |
| 186 | Remote amplifier relay is still open. |
| 241 | Sum of [ContCL](../../06-protections/02-current-and-voltage/ContCL.md) across axes exceeds the hardware limit. |
| 244 | A faulty FPGA was detected. |
| 245 / 250 / 268 | FPGA version does not match the firmware. |
| ≥ 1000 | A standing controller fault would block enabling (STO, encoder error, over-current, bus voltage, over-temperature, …). See [Controller error codes](../../../04-error-codes/controller-error-codes.md). |

The list is not exhaustive — some protections may not be analysed by `CanMotorOn`, and because checks run in a fixed order only the **first** failure is reported.

## Examples

```text
ACanMotorOn         ; run the checks
ACanMotorOnRes      ; 1 = would enable; 31 = needs commutation; >=1000 = standing fault
```

### Edge cases

- **No CanMotorOn run** — at power-up `CanMotorOnRes = 0`. **`0` is not "success"** — only `1` indicates all checks would pass; treat `0` as "unknown" until `CanMotorOn` has been called.
- **Stale result** — the value reflects the **last** `CanMotorOn` call; conditions can change between the check and a `MotorOn = 1`.
- **Motor on / simulation / PD amp** — the firmware short-circuits to `1` in these cases without running the full chain; do not rely on it as a real check while the motor is on.
- **First failure only** — only the first failing check is reported; clearing one reason may reveal another on the next `CanMotorOn` call.
- **Read-only** — writes are rejected.
- **Save** — not flash-saveable.

## See also

- [CanMotorOn](CanMotorOn.md) — command that produces this result
- [MotorOn](MotorOn.md) — the keyword that actually enables the motor
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault codes (≥ 1000) echoed here
- [Controller error codes](../../../04-error-codes/controller-error-codes.md) — full code list
