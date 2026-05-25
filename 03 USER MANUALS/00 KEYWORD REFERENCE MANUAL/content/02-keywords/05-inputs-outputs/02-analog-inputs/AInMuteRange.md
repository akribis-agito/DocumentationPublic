# AInMuteRange

AInMuteRange defines the second analog deadband value in millivolts. The array index corresponds to the index of the analog input (i.e.: AInMuteRange\[2\] refers to analog input 2).

The following table shows the input-output relation for this deadband adjustment block.

| abs(Input)     | Output |
|----------------|--------|
| ≤AInMuteRange  | 0      |
| \>AInMuteRange | Input  |
