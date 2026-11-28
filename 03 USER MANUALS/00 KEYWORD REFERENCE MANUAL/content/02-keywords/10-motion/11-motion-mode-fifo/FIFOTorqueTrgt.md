---
keyword: FIFOTorqueTrgt
summary: Reads or writes the addressed EtherCAT axis’s FIFO torque target.
last_updated: '2026-11-23'
doc_revision: '2026.11'
can_code: 897
availability:
- controller
- ci-master
products:
- agd101-ec-17a
- agd101-ec-34a
- agd155-ec
- agd155-ec-var34
- agd155-ec-var34-3
- agd156-ec
- agm800-ec
attributes:
  access: rw
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
# FIFOTorqueTrgt

Read `FIFOTorqueTrgt` to inspect the working torque target in the axis’s EtherCAT FIFO tracking state. It is a signed 32-bit integer. A cyclic update from the EtherCAT master can replace a value entered at the terminal. Initialising the FIFO also reloads the torque target from the received cyclic data. [InitFifoParams](InitFifoParams.md)

On firmware containing PR #2680, `AFIFOTorqueTrgt` and `AFIFOTorqTrgt` read the same target on axis A. Use the canonical name `FIFOTorqueTrgt` in tools that select keywords from the controller’s About list. Its CAN code is 897. [Firmware PR #2680](https://github.com/akribis-agito/Firmware-Main/pull/2680)
