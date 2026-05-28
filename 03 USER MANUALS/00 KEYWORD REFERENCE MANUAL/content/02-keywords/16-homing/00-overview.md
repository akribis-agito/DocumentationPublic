# Homing

The Agito controller has a built-in, programmable homing process that establishes a known reference position for the axis. The process is started by [HomingOn](HomingOn.md) and defined by [HomingDef](HomingDef.md); its status is reported by [HomingStat](HomingStat.md) and the current step by [HomingStep](HomingStep.md).

The homing process runs as an ordered sequence of steps. Up to 20 steps are supported. The number of steps, the instruction for each step, and that instruction's parameters are all defined by [HomingDef](HomingDef.md). A typical sequence approaches a switch, backs off, finds the encoder index, sets the position there, and ends.

![A typical homing sequence: approach the switch, back off, find the index, set the position and end; any step that times out, sees the wrong end-of-motion reason, or hits a fault aborts the run with a negative HomingStat](homing-overview.svg)

Most homing steps include built-in error detection. When an error is detected during the process, the run is aborted, [HomingOn](HomingOn.md) is cleared, and [HomingStat](HomingStat.md) is set to a negative code that identifies the failure.

The category contains:

- **Run and status** — [HomingOn](HomingOn.md) (start/stop), [HomingDef](HomingDef.md) (the step definitions), [HomingStat](HomingStat.md) (per-step status and error codes) and [HomingStep](HomingStep.md) (the step reached).
- **Switch inputs** — [HomeStat](HomeStat.md) (the home input level), with [StopOnHome](StopOnHome.md) and [StopOnIndex](StopOnIndex.md) arming a jog to stop on a home-input change or on the encoder index.
- **Commutation at home** — [HomeComtAngOn](HomeComtAngOn.md), [HomeComtAngWr](HomeComtAngWr.md) and [HomeComtAngRd](HomeComtAngRd.md), which capture and re-establish the commutation angle at the index so a known mechanical home can restore the electrical angle.

**Note:** on entering the homing process the axis kinematics (speed, acceleration, deceleration and emergency deceleration) are temporarily saved and restored when the run completes, because a homing run may change them.
