# Dual-loop gantry control

For gantry dual-loop control, rather than 2 main encoders and 1 auxiliary encoder, the controller will source from 2 main encoders and the value pointed by GantryFdbkSrc pointer.

We let GantryFdbkSrc will be denoted by encoder C. The following is the comparison of keywords/properties under different control structures.

| Feedback keywords | Default control | Dual-loop control | Pseudo dual-loop control |
|---|---|---|---|
| Gantry feedback (GantryFdbk) <br>If applicable | From 2 main encoders <br>Unit: Main encoder count | From encoder C <br>Unit: Encoder C count | From 2 main encoders <br>Unit: Encoder C count |
| Gantry auxiliary feedback (GantryAuxFdbk) <br>If applicable | - | From 2 main encoders <br>Unit: Main encoder count | From 2 main encoders <br>Unit: Main encoder count |
| Velocity (GantryVel) | Derivative of Pos <br>Unit: Main encoder count / s | If DualLoopFact ≥ 65536, <br>Derivative of GantryAuxFdbk * (DualLoopFact / 65536) <br>Unit: Encoder C count / s <br>If DualLoopFact < 65536, <br>Derivative of GantryAuxFdbk <br>Unit: Main encoder count / s | If DualLoopFact ≥ 65536, <br>Derivative of GantryAuxFdbk * (DualLoopFact / 65536) <br>Unit: Encoder C count / s <br>If DualLoopFact < 65536, <br>Derivative of GantryAuxFdbk <br>Unit: Main encoder count / s |
| Auxiliary velocity (GantryAuxVel) | - | Derivative of GantryAuxFdbk <br>Unit: Main encoder count / s | Derivative of GantryAuxFdbk <br>Unit: Main encoder count / s |
