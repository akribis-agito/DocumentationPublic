# Anomaly detection

Anomaly (collision) detection watches a chosen signal during motion and trips the axis when the signal leaves an expected band. It is intended to catch mechanical anomalies — a collision, a jam, an unexpected load — by learning the normal shape of a repeated motion and flagging deviations from it.

The detector runs while motion is under way through a fixed pipeline:

![Monitored signal is low-pass filtered every control cycle, compared to the per-motion upper and lower limit tables at the start of each AnomDtctGap window, and on an out-of-band sample trips a controlled stop or ConFlt 1067; AnomDtctSt reports the state](anomaly-detection-pipeline.svg)

1. **Source** — [AnomDtctCnfg](AnomDtctCnfg.md) element 1 selects which signal is monitored (for example a current or force reading) by holding its complex CAN code.
2. **Filter** — the signal is passed through a second-order low-pass filter every control cycle; element 2 of [AnomDtctCnfg](AnomDtctCnfg.md) sets the filter pole frequency. The filtered value is reported in [AnomDtctSt](AnomDtctSt.md) element 2 every cycle.
3. **Compare** — the filtered value is compared against an expected band defined point-by-point along the motion by the [AnomDtctUL](AnomDtctUL.md) (upper) and [AnomDtctLL](AnomDtctLL.md) (lower) limit tables. The band check is evaluated at the start of each [AnomDtctGap](AnomDtctGap.md) window: with the default gap of 1 cycle this is effectively every cycle, but with a larger gap the band is sampled once per window (an excursion that occurs mid-window is not checked). [AnomDtctGap](AnomDtctGap.md) sets how many cycles each table point covers.
4. **React** — if a sampled filtered value goes above the upper limit or below the lower limit, the detector trips. Depending on configuration it either commands a controlled stop or disables the axis with fault code 1067 (anomaly/collision detected) on [ConFlt](../../07-status-and-faults/ConFlt.md).

[AnomDtctOn](AnomDtctOn.md) enables the detector and [AnomDtctSt](AnomDtctSt.md) reports its live state, the current filtered value, and the band currently in force.

This feature is available from v5 (central-i).

## Keywords

- [AnomDtctOn](AnomDtctOn.md) — enable or disable detection on the axis.
- [AnomDtctCnfg](AnomDtctCnfg.md) — configuration array: monitored source, filter pole, stop behavior, motion selection.
- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) — upper and lower limit tables that define the expected band along each monitored motion.
- [AnomDtctGap](AnomDtctGap.md) — how many control cycles each limit-table point spans, per motion.
- [AnomDtctSt](AnomDtctSt.md) — status array: detector state, filtered value, active band, active motion.
