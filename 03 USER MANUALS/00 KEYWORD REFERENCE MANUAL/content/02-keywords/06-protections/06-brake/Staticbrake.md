---
summary: Static (holding) brake control — engagement mode and timing (BrakeUsed, BrakeMode, BrakeLockTime, BrakeRelTime).
---
# Static brake

Static braking controls an external holding (electromechanical) brake — engaging it to hold the load when the axis is off and releasing it before motion. This page covers `BrakeUsed`, `BrakeMode`, `BrakeLockTime`, and `BrakeRelTime`.

## How it works

The brake is a fail-safe electromechanical device: **de-energized = engaged (holding)**, **energized = released**. The firmware controls it through one bit in the amplifier command word — `FPGA_AMPLIFIER_CMD_..._RELEASE_STATIC_BRAKE_BIT` (set = release, clear = lock) — and mirrors the request in [StatReg](../../07-status-and-faults/StatReg.md) **bit 29** (static-brake lock requested). The brake state machine runs each control cycle in slot `SAMPLE_12` (axis A) / `SAMPLE_13` (axes B, C) of the control interrupt (`AG300_CTL01ControlInterrupt.c:12709` onward), selecting behaviour from `BrakeMode`. If `BrakeUsed = 0` the firmware drives no voltage to the (absent) device, and in manual modes a 1→0 change of `BrakeUsed` leaves the brake in its last state.

## BrakeUsed

Enables or disables the static brake feature.

| Value | Description |
|-------|-------------|
| 0 | Disabled |
| 1 | Enabled |

## BrakeMode

Defines how the brake is controlled. (Engaged = de-energized; released = energized.) Firmware constants `STATIC_BRAKE_MODE_*` (`AG300_CTL01ParamsCommon.h:1122`–`:1126`); the **default is 2** (`BRAKEMODE_DFLT = STATIC_BRAKE_MODE_MANUAL_RELEASE_WITHOUT_PROTECTION`).

| Value | Mode | Behaviour (firmware) |
|-------|------|----------------------|
| 0 | **Manual lock** | Always clears the release bit → brake engaged. |
| 1 | **Manual release, with protection** | Releases the brake only while the motor is enabled; if the motor is off the brake re-engages (`:12727`). |
| 2 | **Manual release, without protection** *(default)* | Always sets the release bit → brake released, regardless of motor state (`:12748`). |
| 3 | **Automatic by motor-on state** | Released when the motor is enabled, engaged when disabled; the release/lock is timed by the `MotorOn` sequence using `BrakeRelTime` / `BrakeLockTime` (`:12761`, and `AG300_CTL01Funcs.c:17282`/`:17341`). |
| 4 | **Automatic by discrete input, with protection** | Driven from a discrete input inside the input-handling code: input high → engage (if not in motion); input low → release (if motor enabled). Handled in the discrete-input special functions, not in the `SAMPLE_12` switch (`:12789`, `:10698`, `:11186`). |

If `BrakeMode` is somehow out of range, the default action keeps the brake **locked** (safe state).

## BrakeLockTime

> **Condition:** active only when `BrakeMode = 3` (automatic by motor-on).

Delay, in milliseconds, from receiving the motor-disable command until the motor is actually disabled — giving the brake time to engage first. On a disable command the firmware first clears the release bit (engages the brake), arms a counter of `BrakeLockTime` (converted to control samples), waits for it to elapse, **then** disables the motor (`AG300_CTL01Funcs.c:17341`–`:17358`).

**Example:** if the brake takes 300 ms to engage after power is cut, set `BrakeLockTime = 350`. On a disable command the controller engages the brake, waits 350 ms, then disables the motor.

## BrakeRelTime

> **Condition:** active only when `BrakeMode = 3` (automatic by motor-on).

Time to wait, in milliseconds, after releasing (energizing) the brake before allowing motion. On a motor-on command the firmware enables the motor, sets the release bit, arms a counter of `BrakeRelTime` samples, and waits for it to elapse before returning — so motion is not commanded until the brake has had time to open (`AG300_CTL01Funcs.c:17282`–`:17307`).

**Example:** if the brake takes 150 ms to release, set `BrakeRelTime = 200`. On a motor-on command the controller energizes the brake, waits 200 ms, then allows motion.

> Both times are stored in control samples (keyword scaling `SAMPLES_TO_MS_FACT`) and the firmware notes they must not be set to 0 in `BrakeMode = 3`, or the timing logic would not behave as intended (`AG300_CTL01Controller.c:2451`).

## See also

- [Dynamic brake](Dynamicbrake.md) — fast electrical braking (shorting the phases)
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 29 reports the static-brake lock request
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — drives the `BrakeMode = 3` release/lock timing
