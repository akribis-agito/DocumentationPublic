# AInDB

AInDB defines the first analog deadband value in millivolts. The array index corresponds to the index of the analog input (i.e.: AInDB\[3\] refers to analog input 3).

The following table shows the input-output relation for this deadband adjustment block.

| abs(Input) | Output                     |
|------------|----------------------------|
| ≤AInDB     | 0                          |
| \>AInDB    | Input – Sign(Input)\*AInDB |

For example, if the dead band is 20mV, the output (in mV) as a function of the input (in mV) will look as follows.

```desmos-graph
left=-120; right=120; bottom=-90; top=90
height=300;
xAxisLabel=Input (mV)
yAxisLabel=Output (mV)
---
y=\{x>20:x-20,x<-20:x+20,0\}|blue
x=20|black|dashed
x=-20|black|dashed

```
