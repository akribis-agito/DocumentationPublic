# Motor stuck protection

Motor stuck protection works by comparing the current and velocity over a period of time. A stuck condition occurs when the velocity is less than a defined threshold, while the current is greater a defined threshold, over a defined period of time. If stuck condition occurs, the axis is disabled and the error code reported on [ConFlt](../../../07-status-and-faults/ConFlt.md) (fault code 1007).

Criterion for stuck condition check:

- $abs(Vel\lbrack 3\rbrack)\  < \ StuckVel$, **and**

- $abs(MotorCurr)\  > \ StuckCurr$

for StuckTime.

This means that the axis is exerting force but not moving. The check is done over a period of time to ensure that the stuck condition persists, and to prevent false detection during acceleration or deceleration.

## Walk-through: configure and verify a stuck trip

A typical setup for catching mechanical jam on a horizontal stage:

```text
AStuckCurr[1]=4000      ; treat >= 4 A as "drive is pushing hard"
AStuckVel[1]=40000      ; treat <= 40000 user units/s as "not moving"
AStuckTime[1]=4096      ; require ~250 ms of unbroken stuck condition
```

Drive the axis into a hard endstop or simulate a jam:

```text
ABegin                  ; start the move
; ... obstruction encountered ...
AConFlt                 ; expect 1007 (motor stuck) after StuckTime elapses
AMotionReason           ; expect 8 (motor disabled)
```

If the trip never fires, the AND condition is not being held: either `StuckCurr` is too high (the drive never actually pushes that hard) or `StuckVel` is too low (the filtered velocity `Vel[3]` is still drifting just above the threshold). If the trip fires during normal accel/decel, increase `StuckTime` or lower `StuckCurr`. Stuck detection is **bypassed** for steppers and for Current/Force/auto-phasing/motor-learn modes; do not rely on it in those modes.

## See also

- [StuckCurr](StuckCurr.md) — current threshold half of the AND
- [StuckVel](StuckVel.md) — velocity threshold half of the AND
- [StuckTime](StuckTime.md) — required continuous duration
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — fault code 1007 on trip
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — reason 8 (motor disabled) recorded on trip
