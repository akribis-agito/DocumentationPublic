---
keyword: ExtClearFault
summary: Send a fault-clear pulse to the external amplifier on a Central-i ADP05 axis.
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
last_updated: '2026-11-24'
doc_revision: '2026.11'
---
# ExtClearFault

Send a fault-clear pulse to the external amplifier on a Central-i ADP05 axis.

Stop the axis and turn the motor off before issuing this command. It takes no arguments. For axis A, enter the following command.

```text
AExtClearFault
```

The controller acknowledges the request and sets the fault-clear bit for one Central-i control cycle on the ADP05. Check the amplifier’s fault indication to confirm that the fault cleared.
