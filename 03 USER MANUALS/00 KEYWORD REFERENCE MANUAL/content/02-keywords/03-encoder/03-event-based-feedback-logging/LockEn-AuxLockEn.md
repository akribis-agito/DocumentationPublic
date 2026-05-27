---
summary: Enables or disables event-based feedback logging.
---
# LockEn/AuxLockEn

Enables or disables event-based feedback logging.

## Overview

`LockEn` arms (`LockEn=1`) or disarms (`LockEn=0`) the event-based feedback-logging ("position lock" / "capture") feature. When armed, a hardware/firmware trigger selected by [LockSrc](LockSrc-AuxLockSrc.md) latches the encoder feedback position the instant the trigger event occurs. Each event records the latched position in [LockVal](LockVal-AuxLockVal.md) (and into [LockValTable](LockValTable-LockValTabB.md)), records the elapsed time in [LockTimeTable](LockTimeTable-LockTimeTabB.md), and increments the event counter [LockCntr](LockCntr-AuxLockCntr.md).

`AuxLockEn` is the auxiliary-encoder counterpart. In the current firmware the capture mechanism is wired to the main encoder; contact the vendor if auxiliary-encoder capture is required.

## How it works

| LockEn | State |
|---|---|
| 0 | Event-based feedback logging disabled |
| 1 | Event-based feedback logging enabled |

### Arming sequence (enable from disabled)

When `LockEn` transitions `0 → 1` the firmware:

1. Resets the event counter [LockCntr](LockCntr-AuxLockCntr.md) to `0`.
2. Resets the internal elapsed-cycle timer (the source of [LockTimeTable](LockTimeTable-LockTimeTabB.md)) to `0`. It then increments by one every control cycle while logging is enabled.
3. Configures the trigger hardware for the source and edge selected by [LockSrc](LockSrc-AuxLockSrc.md) and clears any pending trigger flag.

Writing `LockEn=1` while it is already `1` does **not** re-arm or reset the counter/timer — the reset only happens on the disabled → enabled transition.

### Capture pipeline

While enabled, each control cycle the firmware advances the timer and checks for a trigger:

- **Digital incremental / SIN-COS encoders** — the position is latched in hardware at the instant of the trigger edge (a true hardware capture), so the recorded value is exact to the trigger moment.
- **Absolute / other non-incremental encoders** — hardware capture is not available; the firmware records the most recent polled feedback position. The trigger must persist long enough to be seen at the control-cycle rate, and the value is the position at the polling instant (slightly delayed relative to the true trigger instant).

When a trigger is detected: latch position → store into `LockVal` → increment `LockCntr` → append position and time to the history tables.

### Mutual exclusivity with event generation (standalone only)

On non-Central-i products the capture trigger and the event-generation output share the same hardware pin, so the two features cannot be active at once. Arming `LockEn=1` automatically clears event generation (`EventOn=0`), and arming event generation automatically clears `LockEn`. This restriction does not apply to Central-i products.

## Examples

```text
ALockEn=1            ; enable event-based feedback logging (resets LockCntr and the timer)
ALockEn=0            ; disable logging
```

## See also

- [LockSrc](LockSrc-AuxLockSrc.md) — selects the trigger source and edge
- [LockCntr](LockCntr-AuxLockCntr.md) — event counter, reset to 0 on enable
- [LockVal](LockVal-AuxLockVal.md) — last latched feedback position
- [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) — position and time-stamp history tables
