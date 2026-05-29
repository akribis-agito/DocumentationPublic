---
summary: Digital filter applied to the incremental encoder A/B/Z input channels.
---
# EncFilt/AuxEncFilt

Digital filter applied to the incremental encoder A/B/Z input channels.

## Overview

`EncFilt` specifies the digital filter to apply on the encoder input channels A, B and Z. The filter is implemented in hardware and its definition varies according to product. It is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is 1 (digital incremental encoder); for the filter of SIN/COS encoders refer to [SinCosSetup](SinCosSetup-AuxSinCosSet.md). The filter rejects noise on the quadrature inputs by qualifying a logic level only after several consecutive identical samples, at the cost of lowering the maximum input frequency (and therefore the maximum supported axis speed). `AuxEncFilt` is the auxiliary-encoder counterpart and operates the same way.

## How it works

`EncFilt` is written into the encoder input-qualification filter in the decode hardware. On the **standalone controller** it sets the DSP input-qualification divider (firmware default 10, maximum 255). On **Central-i remote units** it is a 3-bit field packed into the remote encoder configuration word and sent to the remote unit (firmware default 2, maximum 7). Like [EncDir](EncDir-AuxEncDir.md) and [EncSubType](EncSubType-AuxEncSubType.md), it only takes effect for the incremental encoder path (`EncType=1`).

For the **standalone controller**, the filter is characterized as follows:

1. The A, B and Z inputs are sampled by the filter mechanism. An input level is qualified only after 6 consecutive samples with identical value. This means the "1" logic of the signal needs to be sampled at least 6 times, and the same for the "0" logic, for a total of (2*6) = 12 samples.

2. The filter frequency (sampling frequency) is determined by the `EncFilt` parameter.

   - If `EncFilt` is 0:

     $$\text{Filter frequency} = \text{DSP clock frequency} = 300\ [\text{MHz}]$$

   - If `EncFilt` is not 0:

     $$\text{Filter frequency} = \frac{300}{2 \cdot \text{EncFilt}}\ [\text{MHz}]$$

3. The maximum theoretical input frequency (when no noise is present) is as follows.

   - If `EncFilt` is 0:

     $$\text{Max input frequency} = \frac{300}{12}\ [\text{MHz}]$$

   - If `EncFilt` is not 0:

     $$\text{Max input frequency} = \frac{300}{2 \cdot 12 \cdot \text{EncFilt}}\ [\text{MHz}]$$

4. The maximum theoretical supported speed (when no noise is present) is as follows.

   - If `EncFilt` is 0:

     $$\text{Max theoretical supported speed} = \frac{4 \cdot 3 \cdot 10^{8}}{12}\ [\text{count/s}] = 1.0 \cdot 10^{8}\ [\text{count/s}]$$

   - If `EncFilt` is not 0:

     $$\text{Max theoretical supported speed} = \frac{4 \cdot 3 \cdot 10^{8}}{2 \cdot 12 \cdot \text{EncFilt}}\ \left[\frac{\text{count}}{\text{s}}\right] = \frac{5 \cdot 10^{7}}{\text{EncFilt}}\ [\text{count/s}]$$

5. From the filter point of view and disregarding hardware limitations, the highest filter frequency is 300 MHz, and the highest input frequency is 25 MHz when `EncFilt=0`, assuming no noise.

For **Central-i remote units**, the filter is characterized as follows:

1. The input is sampled by the filter mechanism. An input level is qualified only after 4 consecutive samples with identical value, for a total of (2*4) = 8 samples.

2. The filter frequency (sampling frequency) is determined by the `EncFilt` parameter.

   $$\text{Filter frequency} = \frac{100}{2^{\,\text{EncFilt} + 1}}\ [\text{MHz}]$$

3. The maximum theoretical input frequency (when no noise is present) is as follows.

   $$\text{Max input frequency} = \frac{100}{8 \cdot 2^{\,\text{EncFilt} + 1}}\ [\text{MHz}]$$

4. The maximum theoretical supported speed (when no noise is present) is as follows.

   $$\text{Max theoretical supported speed} = \frac{4 \cdot 10^{8}}{8 \cdot 2^{\,\text{EncFilt} + 1}}\ [\text{count/s}]$$

5. The table below summarises the respective frequencies and supported speed.

| EncFilt value | Filter frequency [MHz] | Max input frequency [MHz] | Max theoretical supported speed [*1E6 count/s] |
|----|----|----|----|
| 0 | 50 | 6.25 | 25 |
| 1 | 25 | 3.125 | 12.5 |
| 2 | 12.5 | 1.5625 | 6.25 |
| 3 | 6.25 | 0.78125 | 3.125 |
| 4 | 3.125 | 0.390625 | 1.5625 |
| 5 | 1.5625 | 0.1953125 | 0.78125 |
| 6 | 0.78125 | 0.09765625 | 0.390625 |
| 7 | 0.390625 | 0.048828125 | 0.1953125 |

6. From the filter point of view and disregarding hardware limitations, the highest filter frequency is 50 MHz, and the highest input frequency is 6.25 MHz when `EncFilt=0`, assuming no noise.

> **Note:**
> 1. The "Max input frequency" (or maximal axis speed) set by `EncFilt` is the theoretical upper limit, which assumes an ideal square-wave signal (infinite slew rate) and ideal electronics (no delays at the receiver chips). The actual max input frequency will be smaller, depending on signal quality.
> 2. Noise on the signal may prevent the filter from counting the required consecutive samples of a given logic level. It is therefore recommended not to set `EncFilt` too high.
> 3. It is recommended to set `EncFilt` such that the maximum theoretical supported speed is two times higher than the actual maximum speed expected in the system.
> 4. The initial value of `EncFilt` can be set according to the equations above, but the final value must be set in careful consideration of the encoder signal quality (e.g. noise).
> 5. Please consult Agito if faster input is required.

## Examples

```text
AEncFilt=0           ; no filtering (highest input frequency)
AEncFilt=3           ; apply filtering to reject noise
```

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `EncFilt` applies for `EncType=1`
- [EncSubType](EncSubType-AuxEncSubType.md) — digital incremental encoder subtype
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) — filter configuration for SIN/COS encoders
