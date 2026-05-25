# MaxPhaseCurr

**Definition:**

MaxPhaseCurr defines the maximum allowable motor phase current in mA. If absolute value of any phase current exceeds MaxPhaseCurr for more than 0.25ms, axis is disabled, and an error code is thrown to ConFlt.

**Note:**

For single-phase motor/voice-coil, MotorCurr is monitored. For three-phase motor, Ia, Ib and Ic are monitored. Ic is inferred from Ia and Ib.
