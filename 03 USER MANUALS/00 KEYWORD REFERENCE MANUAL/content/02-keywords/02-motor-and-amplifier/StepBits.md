# StepBits

**Condition:**

This keyword is only used when MotorType = 6 or 7.

**Definition:**

StepBits is used to define the number of steps per electrical cycle, where

$$
Steps\ per\ electrical\ cycle = 2^{StepBits}\ \lbrack step\ count\rbrack
$$

StepBits = 2 and StepBits = 3 correspond to full-stepping (4 steps per electrical cycle) and half-stepping (8 steps per electrical cycle) respectively.

Microstepping can be achieved by increasing StepBits above value of 2.
