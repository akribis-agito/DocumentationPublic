---
keyword: InitFifoParams
summary: Initialises the addressed EtherCAT axis’s FIFO tracking state from its current cyclic targets.
last_updated: '2026-11-23'
doc_revision: '2026.11'
can_code: 896
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
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InitFifoParams

Calling `InitFifoParams` copies the incoming position and torque targets into the addressed axis’s FIFO tracking state. The command also clears its position, velocity and current tracking offsets. In linear interpolation mode, firmware seeds the interpolator according to the current EtherCAT mode of operation. [FIFOPosType](FIFOPosType.md) · [FIFOPosTrgt](FIFOPosTrgt.md) · [FIFOTorqueTrgt](FIFOTorqueTrgt.md)

On firmware containing PR #2680, `AInitFifoParams` and `AInitFifoParms` invoke the same command on axis A. Use the canonical name `InitFifoParams` in tools that select keywords from the controller’s About list. Its CAN code is 896. [Firmware PR #2680](https://github.com/akribis-agito/Firmware-Main/pull/2680)
