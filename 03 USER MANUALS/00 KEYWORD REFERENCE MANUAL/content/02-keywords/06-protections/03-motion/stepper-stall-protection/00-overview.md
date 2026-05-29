# Stepper stall protection

Stepper stall protection detects when a stepper motor (driven by the internal amplifier) loses synchronisation with its commanded electrical angle. A live metric derived from the phase voltages is compared against a speed-dependent threshold every control sample; when the metric collapses below the threshold the motor is declared stalled.

The protection only operates on stepper motors driven by the internal amplifier — for servo motors and external-amplifier configurations the metric is not generated and these keywords are inert.

- [StallCfg](StallCfg.md) — master switch and outcome: `0` disabled, `1` alert-only (sets [StallStat](StallStat.md) and the [StatReg](../../../07-status-and-faults/StatReg.md) stall bit), `2` also disables the axis with [ConFlt](../../../07-status-and-faults/ConFlt.md) ConFlt code 1065.
- [StallVal](StallVal.md) — read-only live metric (low-pass filtered $(V_a-V_c)^2+(V_b-V_c)^2$).
- [StallTh](StallTh.md) — read-only firmware-computed threshold (speed-dependent, low-pass filtered).
- [StallThPcnt](StallThPcnt.md) — user-set sensitivity (10–90 %).
- [StallCnst](StallCnst.md) — slope/intercept of the speed-dependent fit.
- [StallStat](StallStat.md) — read-only stall flag (mirrors [StatReg](../../../07-status-and-faults/StatReg.md) bit 31).

![Stepper stall detection sketch: a healthy StallVal stays well above the StallTh line; when the rotor loses step, StallVal collapses below StallTh and the stall outcome is taken from StallCfg](stall-detect.svg)

A stall is declared when `StallVal < StallTh`. In modes 1 and 2 [StallStat](StallStat.md) is set and [StatReg](../../../07-status-and-faults/StatReg.md) bit 31 (`0x80000000`) is set; in mode 2 the axis is additionally disabled. When the metric recovers above the threshold the stall bit clears automatically.

The metric, threshold, and stall flag are all reset to `0` when the motor goes off; tune [StallCnst](StallCnst.md) against the healthy `StallVal` at several speeds before relying on detection.
