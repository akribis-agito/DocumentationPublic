# Static brake

##### BrakeUsed

**Definition:**

BrakeUsed enables/disables the static braking feature.

| Value | Descriptions |
|-------|--------------|
| 0     | Disabled     |
| 1     | Enabled      |

##### BrakeMode

**Definition:**

BrakeMode defines how the brake will be controlled.

| Value | Descriptions |
|---|---|
| 0 | **Manual Lock Command** Brake is engaged (not energized). |
| 1 | **Manual Release Command – with Protection** Upon setting BrakeMode = 1, brake is released (energized), provided motor enabled. |
| 2 | **Manual Release Command – without Protection** Brake is released (energized). |
| 3 | **Automatic – By MotorOn State** When motor is enabled, brake is released (energized). When motor is disabled, brake is engaged (not energized). |
| 4 | **Automatic – By Discrete Input – with Protection** When input logic is toggled high, brake is engaged (not energized), provided motor is not motion. When input logic is toggled low, brake is released (energized), provided motor is enabled. |

##### BrakeLockTime

**Condition:**

BrakeLockTime is only applicable when BrakeMode = 3 (in “Automatic – By MotorOn State”).

**Definition:**

BrakeLockTime defines the delay time, in milliseconds, from the receipt of motor disable command until the motor is actually disabled.

**Example:**

If the brake takes 300ms to physically engage upon cutting the power, then BrakeLockTime should be set to a value greater than that, e.g. 350ms. Upon sending the command to disable the motor, the controller will first cut the power to the brakes and wait for 350ms for the brakes to engage. Only then will it disable the motor.

##### BrakeRelTime

**Condition:**

BrakeLockTime is only applicable when BrakeMode = 3 (in “Automatic – By MotorOn State”).

**Definition:**

BrakeRelTime defines the time to wait, in milliseconds, before allowing the motor to move.

**Example:**

If the brake takes 150ms to release upon providing power, then BrakeRelTime should be set to a value greater than that, e.g. 200ms. Upon sending the command to motor on, the controller will provide power to both the motor and the brakes. It will wait for 200ms for the brakes to release, only then will it allow motion.
