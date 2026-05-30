# Timing

**Overview:**

Agito controller reports the system timing in terms of cycle count. The timing can be used for user program function to trigger an event at correct time. Some timer keywords are also settable, allowing more flexibility in determining process time.

All timing in this section derives from the controller's control interrupt, which runs at a fixed rate of 16384 cycles per second (one cycle every ≈ 61 µs). The keywords expose this clock at three resolutions:

- Per control cycle: `CounterUp` and `CounterDown` advance once every control cycle (16384 per second), giving cycle-accurate up/down counting.
- Per second: `Time` is derived from the same clock and increments once every 16384 cycles, i.e. once per second.
- Sub-microsecond: on the central-i platform, `HWTimer` reads a fast hardware timer register for measuring short intervals at far finer than one-cycle resolution.

**Where the timekeeping happens in each cycle:** every control interrupt first does its time-critical work — reading feedback, running the control loops, and writing the PWM and digital outputs to the hardware — and only then, in a second, non-time-critical part of the same interrupt, updates the housekeeping timers. The `Time` seconds counter and the `CounterUp` / `CounterDown` counters are all advanced in that second part, after the cycle's outputs have already been committed to the hardware, so their bookkeeping never delays the control output. The position, velocity, and current loops themselves all execute on every control cycle at the full 16384 Hz; there is no slower outer loop and no decimation between the loops.
