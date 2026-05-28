# Dual-loop gantry control

In dual-loop gantry control the controller closes the linear position loop on a separate load-side feedback rather than on the two main motor encoders. The load feedback is selected by the [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) pointer, while the two main motor encoders are kept for the inner velocity loop and the yaw (differential) loop.

![Dual-loop gantry feedback arrangement: load feedback for the linear loop, motor encoders for the inner velocity and yaw loops](gantry-dual-loop.svg)

In the table below the feedback selected by [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) is denoted "encoder C". The table compares how each feedback and velocity term is sourced under the three control structures.

| Feedback keywords | Default control | Dual-loop control | Pseudo dual-loop control |
|---|---|---|---|
| Gantry feedback (GantryFdbk) <br>If applicable | From 2 main encoders <br>Unit: Main encoder count | From encoder C <br>Unit: Encoder C count | From 2 main encoders <br>Unit: Encoder C count |
| Gantry auxiliary feedback (GantryAuxFdbk) <br>If applicable | - | From 2 main encoders <br>Unit: Main encoder count | From 2 main encoders <br>Unit: Main encoder count |
| Velocity (GantryVel) | Derivative of Pos <br>Unit: Main encoder count / s | If DualLoopFact ≥ 65536, <br>Derivative of GantryAuxFdbk * (DualLoopFact / 65536) <br>Unit: Encoder C count / s <br>If DualLoopFact < 65536, <br>Derivative of GantryAuxFdbk <br>Unit: Main encoder count / s | If DualLoopFact ≥ 65536, <br>Derivative of GantryAuxFdbk * (DualLoopFact / 65536) <br>Unit: Encoder C count / s <br>If DualLoopFact < 65536, <br>Derivative of GantryAuxFdbk <br>Unit: Main encoder count / s |
| Auxiliary velocity (GantryAuxVel) | - | Derivative of GantryAuxFdbk <br>Unit: Main encoder count / s | Derivative of GantryAuxFdbk <br>Unit: Main encoder count / s |
