# OpenLoopOn

**Definition:**

OpenLoopOn is used to open the control loop at a chosen point, as shown.

| OpenLoopOn | Descriptions |
|---|---|
| 0 | **No open loop** All control loops are closed. |
| 1 | **Current open loop** Control loops are cut-off/opened at the current reference input (just before the current loop). |
| 2 | **Voltage open loop** Control loops are cut-off/opened at the voltage reference input (just before the space vector modulation for PWM drive). |
