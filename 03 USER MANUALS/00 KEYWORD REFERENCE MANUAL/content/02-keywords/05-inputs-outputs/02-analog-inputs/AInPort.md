# AInPort

AInPort contains the processed and original readings of the analog inputs. The array length corresponds to twice the number of the analog inputs.

The first half of the array holds the readings after processing (filter, offset, first deadband, gain and second deadband). The second half of the array holds the original values of the analog inputs (after ADC) as shown below.

| Data | **Analog input 1** | **Analog input 2** | **Analog input 3** | **Analog input 4** |
|----|----|----|----|----|
| Processed input | AInPort\[1\] | AInPort\[2\] | AInPort\[3\] | AInPort\[4\] |
| Original input | AInPort\[5\] | AInPort\[6\] | AInPort\[7\] | AInPort\[8\] |
