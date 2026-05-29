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

### Capture and event generation share one channel (Central-i)

On Central-i, capture and event generation can both be active at the same time, but the master reads each captured position from the remote drive over a single shared communication channel that also carries event-output updates. The two features therefore take turns on that channel: when both are busy, servicing one can delay the other by one or more control cycles. This lowers the maximum sustained capture/event rate when capture and event generation run together, compared with running either one alone.

## Examples

```text
ALockEn=1            ; enable event-based feedback logging (resets LockCntr and the timer)
ALockEn=0            ; disable logging
```

### Walk-through: configure a Lock capture for registration

Set up a registration mark on digital input 1 (rising edge), arm the capture, then observe each mark's feedback position. The example uses a standalone product — for Central-i, see the source table in [LockSrc](LockSrc-AuxLockSrc.md).

```text
AMotorOn=0           ; on standalone products, LockEn takes the capture pin from event generation
ALockSrc=1           ; trigger source = digital input 1, rising edge
ALockEn=1            ; arm capture; LockCntr and the elapsed-cycle timer reset to 0
                     ; ... drive the axis past the marks ...
ALockCntr            ; count of marks captured so far
ALockVal             ; feedback position of the most recent mark
ALockValTable[1]     ; position of the first mark
ALockValTable[2]     ; position of the second mark
ALockTimeTable[1]    ; control cycles elapsed at the first mark
ALockEn=0            ; disarm when done (LockVal and LockCntr keep their last values)
```

For digital incremental and SIN/COS encoders the position is latched in hardware at the exact trigger edge, so `LockVal` is precise to the trigger instant — ideal for product registration. For absolute encoders the value is the most recently polled `Pos`, so keep axis speed low enough that the trigger does not pass between control cycles.

## Edge cases

- **Motor off.** Capture works whenever the encoder is being read; `LockEn=1` will latch events even when the axis is moved by hand.
- **In motion.** Permitted to write `LockEn` while moving; the capture arms on the next cycle and the running motion is not disturbed.
- **Already armed.** Writing `LockEn=1` while it is already `1` is a no-op — the counter and elapsed-cycle timer are reset *only* on the disabled→enabled transition.
- **Event-generation conflict (standalone only).** On non-Central-i products the capture pin is shared with event generation. Arming `LockEn=1` forces [EventOn](../../18-event-generation/EventOn.md)=0 (and vice-versa). The Central-i remote drives have independent hardware so the two features can coexist.
- **Tables full.** Once both [LockValTable](LockValTable-LockValTabB.md) and `LockValTabB` are full the history stops, but `LockCntr` and [LockVal](LockVal-AuxLockVal.md) keep updating on every further event. Disarm and re-arm to start over.
- **Auxiliary encoder.** `AuxLockEn` is provided for parity, but the current firmware wires the capture mechanism to the main encoder only.
- **Central-i disconnect.** On a disconnected port the remote drive is not feeding the lock-configuration register, and no captured positions return to the master.

## See also

- [LockSrc](LockSrc-AuxLockSrc.md) — selects the trigger source and edge
- [LockCntr](LockCntr-AuxLockCntr.md) — event counter, reset to 0 on enable
- [LockVal](LockVal-AuxLockVal.md) — last latched feedback position
- [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) — position and time-stamp history tables
