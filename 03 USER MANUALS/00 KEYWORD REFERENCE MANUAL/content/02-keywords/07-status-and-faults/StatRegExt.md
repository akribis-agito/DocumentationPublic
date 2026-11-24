---
keyword: StatRegExt
summary: Read-only axis status word reporting when adaptive DC-bus compensation reaches its upper limit.
availability:
- controller
- ci-master
can_code: 966
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
last_updated: '2026-11-24'
doc_revision: '2026.11'
---
# StatRegExt

`StatRegExt` reports conditions from the most recent current-loop pass for the selected axis. Read it while the motor is running or select it as a recorder channel.

| Bit | When the bit is 1 |
| --- | --- |
| 0 | The brushless current loop applied the maximum adaptive DC-bus ratio of 1.2 to the axis voltage command. |
| 1–31 | Reserved. |

Bit 0 clears on a pass that uses a lower ratio, disables or bypasses compensation, or turns the motor off. It tracks the applied compensation independently of the voltage-output saturation in [StatReg](StatReg.md). On a shared-bus controller the axes use the same bus measurement, and each axis reports whether its own loop applied the ceiling.

For axis A, read `AStatRegExt` and test bit 0 with `AStatRegExt & 1`. Record it alongside [VBusRatio](../09-current-and-voltage/01-system-variables/VBusRatio.md) and [AdVBusEn](../09-current-and-voltage/01-system-variables/AdVBusEn.md) to see when the compensator reaches its limit. On older firmware, check that the controller exposes `StatRegExt` before requesting it.
