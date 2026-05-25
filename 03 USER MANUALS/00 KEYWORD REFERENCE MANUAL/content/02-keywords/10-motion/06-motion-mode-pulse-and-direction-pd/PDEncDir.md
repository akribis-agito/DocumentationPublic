# PDEncDir

**Definition:**

PDEncDir configures the direction of PDPos accumulation.

| Value | Descriptions |
|---|---|
| 0 | **Normal direction** PDPos increments by the number of pulses received multiplied by scaling if the direction signal is logic high, and decrements by such value if the direction signal is logic low. |
| 1 | **Inverted direction** PDPos decrements by the number of pulses received multiplied by scaling if the direction signal is logic high, and increments by such value if the direction signal is logic low. |
