# AOutShifts

<!-- Imported from the 2021 PDF reference. Verify against current firmware
     behavior and update with the latest semantics. -->

AOutShifts divides or multiplies the monitored parameter (refer to [AOutMode](AOutMode.md)) to obtain a better dynamic range. `AOutShifts[1]` is applied to the value on Analog Output 1 and `AOutShifts[2]` is applied to the value on Analog Output 2.

A negative value in AOutShifts will cause a shift right by the value of AOutShifts. This is the same as dividing the output value by $2^{|\text{AOutShifts}|}$.

A positive value of AOutShifts will cause a shift left by the value of AOutShifts. This is the same as multiplying the output value by $2^{\text{AOutShifts}}$.

$$
\text{Analog output [mV]} = \text{Monitored parameter [internal units]} \times 2^{\text{AOutShifts}}
$$
