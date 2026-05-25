# MaxPWM

**Definition:**

For PWM amplifiers, MaxPWM is used to limit the maximum duty cycle of PWM drives, and effectively the maximum voltage output to the motor. The units for MaxPWM is 0.1%, where 1000 represents 100% duty cycle, and a 0 value represents maximum 0% duty cycle.

**Example:**

For example, an axis has default value of MaxPWM=900 and bus voltage is 48V. To limit to maximum 30% duty cycle, user should set MaxPWM=300 to limit maximum voltage output to 14.4V.
