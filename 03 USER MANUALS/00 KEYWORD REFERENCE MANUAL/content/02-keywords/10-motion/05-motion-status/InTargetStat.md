# InTargetStat

**Definition:**

InTargetStat reports the motion and settling state of the axis. Its values’ definitions vary according to the OperationMode.

| InTargetStat | OperationMode = 2 (Velocity control) OperationMode = 3 (Position control) Keyword to monitor: PosErr Settling window: InTargetTol | OperationMode = 1 (Current control) OperationMode = 4 (Force control) Keyword to monitor: Vel[1] Settling window: InTargetVelTh |
|---|---|---|
| 0 | **Motor disabled** | **Motor disabled** |
| 1 | **Motor enabled** | **Motor enabled** |
| 2 | **In motion** | **Velocity out of range** *a**b**s*(*V**e**l*[1]) > *I**n**T**a**r**g**e**t**V**e**l**T**h* |
| 3 | **Settling** Axis is settling / axis has settled but is pending InTargetTime to elapse. | **Velocity within range** *a**b**s*(*V**e**l*[1]) ≤ *I**n**T**a**r**g**e**t**V**e**l**T**h*, but is pending InTargetTime to elapse. |
| 4 | **Target reached** Axis has settled within InTargetTol for at least InTargetTime. Once InTargetStat = 4, it will remain so until the next motion is commanded/ axis is disabled, even if position error exits the settling window, where *a**b**s*(*P**o**s**E**r**r*) > *I**n**T**a**r**g**e**t**T**o**l*. | **Target reached** *a**b**s*(*V**e**l*[1]) ≤ *I**n**T**a**r**g**e**t**V**e**l**T**h* for at least InTargetTime. |

**Example:**

<img alt="A screenshot of a graph AI-generated content may be incorrect." src="image29.png" style="width:5.40395in;height:5.06583in"/>

The example shows how InTargetStat changes with different motion phases, under position control operation mode (OperationMode=1).

| Time \[s\] | InTargetStat | Descriptions |
|----|----|----|
| 0 to 0.1 | 0 | Motor disabled. |
| 0.1 to 0.2 | 1 | Motor enabled. |
| 0.2 to 0.27 | 2 | In motion (where dPosRef!=0). |
| 0.27 to 0.42 | 3 | InTargetStat=3 after motion, until the absolute value of PosErr is less than InTargetTol for at least InTargetTime. |
| 0.42 to 1.17 | 4 | Target reached. InTargetStat=4 even when absolute value PosErr is more than InTartgetTol. |
| 1.17 to 1.24 | 2 | In motion (where dPosRef!=0). |
| 1.24 to 1.39 | 3 | Settling and waiting for InTargetTime to elapse. |
| 1.39 to 1.73 | 4 | Target reached. |
