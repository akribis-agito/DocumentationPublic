---
keyword: ExtClearFault
summary: Requests a one-cycle fault-clear command on the connected ADP05 external amplifier.
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 906
availability:
- controller
- ci-master
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ExtClearFault

With motion stopped and the motor off, enter `AExtClearFault` to request a fault clear on the ADP05 (AGL105) amplifier connected to axis A. Substitute the drive axis letter as needed.

The controller acknowledges the command when it queues the request in the axis command word. The control interrupt sends the clear-fault bit to the remote for one cycle, then clears it. Check the amplifier’s fault status after the request to determine whether the fault cleared.

This command takes no arguments. The current-feedback scale and offsets for Central-i ADP03, ADP04 and ADP05 interfaces are described under [ExtAmpConfig](ExtAmpConfig.md).
