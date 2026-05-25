# ScheduleGains

**Definition:**

ScheduleGains displays the active gains in use by the controller.

Each ScheduleGains array element corresponds to a type of gain, as shown.

| Index | Description                     |
|-------|---------------------------------|
| 1     | Position loop proportional gain |
| 2     | Acceleration feedforward gain   |
| 3     | Velocity loop proportional gain |
| 4     | Velocity loop integral gain     |
| 5     | Velocity feedforward gain       |
| 6     | Position loop integral gain     |

In case of no gain scheduling (ScheduleMode = 0), ScheduleGains values equal to first array elements of respective schedulable gain keywords. For example, ScheduleGains\[2\] = AccFFW\[1\].
