---
keyword: CurrPosErrTh
summary: Position-error threshold (condition B) to enter current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 337
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -327680
  - 327680
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrPosErrTh

Position-error threshold (condition B) to enter current mode.

## Overview

`CurrPosErrTh` is the threshold position error (`PosErr`) value used in the second condition check (condition B) to enter current operation mode. It is used only while the axis is in position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 3).

## How it works

| Value | Descriptions                                             |
|-------|----------------------------------------------------------|
| \< 0  | Second condition is fulfilled if `PosErr` < `CurrPosErrTh`. |
| 0     | Second condition is not fulfilled.                       |
| \> 0  | Second condition is fulfilled if `PosErr` > `CurrPosErrTh`. |

`CurrPosErrTh` is one of three interchangeable condition-B checks; the others are [CurrAInTh](CurrAInTh.md) (analog force feedback) and [CurrCurrTh](CurrCurrTh.md) (current reference). The firmware evaluates all armed condition-B checks each cycle and switches if **any** of them is satisfied (logical OR among B), provided the condition-A position gate has already passed.

Entry into current operation mode still requires the first condition check ([CurrPosTh](CurrPosTh.md) / [CurrPosThDir](CurrPosThDir.md)) to pass in the same cycle. When both conditions are met, the axis enters current mode and the firmware clears `CurrPosErrTh` to 0 (and clears [CurrPosThDir](CurrPosThDir.md)) to avoid undesired future switching; the user must reconfigure its value for the next switch. See [Current operation mode](00-overview.md) for the overview.

## Examples

```text
ACurrPosErrTh=5000   ; enter current mode when PosErr > 5000
ACurrPosErrTh=0      ; disable this condition
```

### Edge cases

- **Mode dependence** — although the condition-B threshold engine runs in both velocity ([OperationMode](../01-general-keywords/OperationMode.md) = 2) and position (`OperationMode` = 3) operation mode, `CurrPosErrTh` can only ever trigger in position mode. The position error (`PosErr`) is held at `0` in velocity mode (and outside position mode generally), so neither the `PosErr > value` nor the `PosErr < value` comparison can be satisfied there.
- **Zero value** — disables this condition (only condition A and the other condition-B keywords matter).
- **After trigger** — both `CurrPosErrTh` and [CurrPosThDir](CurrPosThDir.md) are cleared to `0` to prevent repeat triggers. Re-arm by writing both again.
- **Sign sensitivity** — a positive threshold fires on `PosErr > value`; a negative threshold fires on `PosErr < value`.
- **Motor off** — the threshold engine does not run.
- **Save** — flash-saveable.

## See also

- [Current operation mode](00-overview.md) — full mode-switching conditions
- [CurrAInTh](CurrAInTh.md) — alternative second condition (analog force feedback)
- [CurrCurrTh](CurrCurrTh.md) — alternative second condition (current reference)
