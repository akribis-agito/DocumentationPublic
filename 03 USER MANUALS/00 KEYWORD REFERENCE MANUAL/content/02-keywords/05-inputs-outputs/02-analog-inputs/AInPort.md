---
keyword: AInPort
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 35
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 9
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
# AInPort

AInPort contains the processed and original readings of the analog inputs. The array length corresponds to twice the number of the analog inputs.

The first half of the array holds the readings after processing (filter, offset, first deadband, gain and second deadband). The second half of the array holds the original values of the analog inputs (after ADC) as shown below.

| Data | **Analog input 1** | **Analog input 2** | **Analog input 3** | **Analog input 4** |
|----|----|----|----|----|
| Processed input | AInPort\[1\] | AInPort\[2\] | AInPort\[3\] | AInPort\[4\] |
| Original input | AInPort\[5\] | AInPort\[6\] | AInPort\[7\] | AInPort\[8\] |
