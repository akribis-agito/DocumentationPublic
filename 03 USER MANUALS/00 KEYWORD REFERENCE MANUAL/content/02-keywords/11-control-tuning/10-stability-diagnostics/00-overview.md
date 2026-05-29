# Stability-diagnostics

Stability diagnostics watch the closed loops at run time and shut the axis down if they start to oscillate or pick up excessive noise, before an unstable loop can damage the motor or load.

Two independent detectors are provided. The current-loop stability detector compares the spread (variance) of the measured motor current against the spread of the commanded current reference: when the motor current swings much more than the command and the tracking error stays large, the current loop is judged to be oscillating. The position/velocity (PIV) noise detector watches the spread of the current reference while the axis is being held at a commanded standstill, where the reference should be quiet; an elevated spread there indicates noise or jitter feeding through the position/velocity loops.

Both detectors compute a running statistic over a sliding window of samples and compare it to a threshold derived from the axis peak current limit. When the threshold is exceeded the detector turns the motor off and logs a controller fault, which is reported through [ConFlt](../../07-status-and-faults/ConFlt.md): fault code 1071 for an unstable current loop and fault code 1072 for high PIV noise/jitter. Each detector also publishes a read-only status array so the running statistic and the active thresholds can be inspected during tuning.

These keywords are available from v5 (central-i) only.

The following is the summary of stability-diagnostics keywords.

| No. | Keywords | Summary |
|----|----|----|
| 1 | [CurrStbleDtct](CurrStbleDtct.md) | Current-loop stability detector enable |
| 2 | [CurrStbleErr](CurrStbleErr.md) | Current-loop tracking-error threshold (% of peak current limit) |
| 3 | [CurrStbleSTD](CurrStbleSTD.md) | Current-loop spread threshold (% of peak current limit) |
| 4 | [CurrStbleStat](CurrStbleStat.md) | Current-loop stability detector status array |
| 5 | [PIVNoiseDtct](PIVNoiseDtct.md) | PIV noise detector enable |
| 6 | [PIVNoiseSTD](PIVNoiseSTD.md) | PIV noise spread threshold (% of peak current limit) |
| 7 | [PIVNoiseWSize](PIVNoiseWSize.md) | PIV noise sample window size |
| 8 | [PIVNoiseStat](PIVNoiseStat.md) | PIV noise detector status array |
