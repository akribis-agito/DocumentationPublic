---
summary: Static (holding) brake control — engagement mode and timing (BrakeUsed, BrakeMode, BrakeLockTime, BrakeRelTime).
---
# Static brake

Static braking controls an external holding brake — engaging it to hold the load and releasing it before motion. This page covers `BrakeUsed`, `BrakeMode`, `BrakeLockTime`, and `BrakeRelTime`.

## BrakeUsed

Enables or disables the static brake feature.

| Value | Description |
|-------|-------------|
| 0 | Disabled |
| 1 | Enabled |

## BrakeMode

Defines how the brake is controlled. (Engaged = not energized; released = energized.)

| Value | Description |
|-------|-------------|
| 0 | **Manual lock** — brake engaged (not energized). |
| 1 | **Manual release, with protection** — brake released, provided the motor is enabled. |
| 2 | **Manual release, without protection** — brake released (energized). |
| 3 | **Automatic by motor-on state** — released when the motor is enabled, engaged when disabled. |
| 4 | **Automatic by discrete input, with protection** — input high → engaged (if not in motion); input low → released (if motor enabled). |

## BrakeLockTime

> **Condition:** applicable when `BrakeMode = 3`.

Delay, in milliseconds, from receiving the motor-disable command until the motor is actually disabled — giving the brake time to engage first.

**Example:** if the brake takes 300 ms to engage after power is cut, set `BrakeLockTime = 350`. On a disable command, the controller cuts power to the brake, waits 350 ms for it to engage, then disables the motor.

## BrakeRelTime

> **Condition:** applicable when `BrakeMode = 3`.

Time to wait, in milliseconds, after energizing the brake before allowing motion.

**Example:** if the brake takes 150 ms to release, set `BrakeRelTime = 200`. On a motor-on command, the controller powers both motor and brake, waits 200 ms for the brake to release, then allows motion.

## See also

- [Dynamic brake](Dynamicbrake.md) — fast electrical braking
