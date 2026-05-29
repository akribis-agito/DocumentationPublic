---
summary: Parameter array configuring the SIN/COS encoder (gain, offsets, interpolation, index, error checks).
---
# SinCosSetup/AuxSinCosSet

Parameter array configuring the SIN/COS encoder interface.

## Overview

`SinCosSetup` is a parameter array that defines the SIN/COS encoder configuration. It is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is 4 (SIN/COS encoder). The array elements set signal conditioning (gain, sine/cosine offsets, amplitude ratio, phase), interpolation, index (Z) behaviour, error checks, direction, and test modes for calibration. `AuxSinCosSet` is the auxiliary-encoder counterpart.

> [!warning]
> Do not set any individual `SinCosSetup` value other than the values specified in the tables below. An improper value may result in unexpected feedback behaviour and may cause damage to the system.

> **Note:** The analog test mode (TMA) can be enabled via `SinCosSetup[20]` to check the SIN/COS signal. Both the time-domain and X/Y (Lissajous) views are suitable for signal offset and phase calibration.

## How it works

Each array index is described below.

### [1] Signal gain (default 2)

Sets the gain of the input differential SIN/COS signal. To get the most out of the ADC, set the gain so the input signal reaches a total of 4 V peak to peak.

| Value | Gain | Value | Gain |
|---|---|---|---|
| 0 | 2.667 | 8 | 20.000 |
| 1 | 3.333 | 9 | 26.667 |
| 2 | 4.000 | 10 | 28.571 |
| 3 | 5.333 | 11 | 33.333 |
| 4 | 6.667 | 12 | 40.000 |
| 5 | 8.000 | 13 | 53.333 |
| 6 | 10.000 | 14 | 66.667 |
| 7 | 14.287 | 15 | 80.000 |

### [2] Sine offset (default 0)

Calibrates the DC offset of the differential sine input.

| Value | Offset [mV] |
|---|---|
| 0 – 127 | -7.8125 * Value |
| 128 – 255 | 7.8125 * (Value - 128) |

For example, `SinCosSetup[2]=33` gives a sine offset of -7.8125 * 33 = -257.8125 mV.

> [!warning]
> A high center voltage may result in amplitude clamping of the sinusoidal signal.

### [3] Cosine offset (default 0)

Calibrates the DC offset of the differential cosine input.

| Value | Offset [mV] |
|---|---|
| 0 – 127 | -7.8125 * Value |
| 128 – 255 | 7.8125 * (Value - 128) |

For example, `SinCosSetup[3]=203` gives a cosine offset of -7.8125 * (203 - 128) = 585.9375 mV.

> [!warning]
> A high center voltage may result in amplitude clamping of the sinusoidal signal.

### [4] Amplitude ratio (default 0)

Calibrates the amplitude ratio between the sine and cosine signals.

| Value | Amplitude ratio |
|---|---|
| 0 – 15 | 1 + (0.1/15) * Value |
| 16 – 31 | 1 - (0.1/15) * (Value - 16) |

For example, `SinCosSetup[4]=19` gives an amplitude ratio of 1 - (0.1/15) * (19 - 16) = 0.98.

### [5] Phase calibration (default 0)

Calibrates the phase difference between the sine and cosine signals.

| Value | Phase difference [degrees] |
|---|---|
| 0 – 18 | 90 + (22.5/32) * Value |
| 32 – 50 | 90 - (22.5/32) * (Value - 32) |

For example, `SinCosSetup[5]=12` gives a phase difference of 90 + (22.5/32) * 12 = 98.4375 degrees.

### [6] Interpolation factor (default 0)

Defines the SIN/COS encoder interpolation factor.

| Value | Interpolation factor |
|---|---|
| 3 – 13 | $2^{\,16 - \text{Value}}$ |

For example, `SinCosSetup[6]=7` interpolates each SIN or COS cycle to $2^{\,16-7} = 512$ counts per cycle.

### [7] Hysteresis threshold (default 0)

Defines the digital angle hysteresis threshold for the SIN/COS signal. It separates the converter's switch points between CW and CCW operation, eliminating spurious A/B output switching during standstill if set high enough relative to the input noise.

| Value | Hysteresis threshold [deg] |
|---|---|
| 0 | 0 |
| 1 | 0.087890625 |
| 2 | 0.17578125 |
| 3 | 0.3515625 |
| 4 | 0.703125 |
| 5 | 1.40625 |
| 6 | 5.625 |
| 7 | 45 |

> [!warning]
> Setting the hysteresis threshold to 45 degrees is only recommended during calibration.

### [8] Maximum input frequency (default 16642)

Defines the maximum input frequency for the SIN/COS signals. In the formula below, let P be the frequency factor and Q be the interpolation factor.

| Value | Hex value | Frequency factor, P | Maximum input frequency [kHz] |
|---|---|---|---|
| 4 | 0x0004 | - | 1200 / Q |
| 16642 | 0x4102 | 0 | $\frac{2000 \cdot 2^{P}}{Q}$ |
| 16898 | 0x4202 | 1 | |
| 17154 | 0x4302 | 2 | |
| 18178 | 0x4702 | 3 | |
| 19202 | 0x4B02 | 4 | |
| 20226 | 0x4F02 | 5 | |
| 21250 | 0x5302 | 6 | |
| 22274 | 0x5702 | 7 | |
| 23298 | 0x5B02 | 8 | |
| 24322 | 0x5F02 | 9 | |
| 25346 | 0x6302 | 10 | |

Since the input frequency cannot be higher than 250 kHz, depending on the interpolation factor some input frequencies cannot be selected:

| SinCosSetup[6] | Interpolation factor | Maximum possible SinCosSetup[8] | Corresponding maximum input frequency [kHz] |
|---|---|---|---|
| 3 | 8192 | 25346 | 250 |
| 4 | 4096 | 24322 | |
| 5 | 2048 | 23298 | |
| 6 | 1024 | 22274 | |
| 7 | 512 | 21250 | |
| 8 | 256 | 20226 | |
| 9 | 128 | 19202 | |
| 10 | 64 | 18178 | |
| 11 | 32 | 17154 | |
| 12 | 16 | 16898 | |
| 13 | 8 | 16642 | |

For example, if `SinCosSetup[6]=4` (interpolation factor 4096), the maximum and minimum values of `SinCosSetup[8]` are 24322 and 4 respectively, corresponding to maximum input frequencies of 250 kHz and 0.293 kHz.

> **Note:** It is recommended to set `SinCosSetup[8]` to its maximum possible value to support the highest possible encoder speed.

### [9] Output A, B, Z configuration (default 0)

Configures what signals appear on the incremental A/B/Z signal lines. Typically used for calibration by means of digital signals as a function of PWM duty cycle, as opposed to the analog test mode (TMA).

| Value | Mode | Additional settings required |
|---|---|---|
| 0 | Normal | None |
| 1 | Control signals for external period counters | |
| 2 | Calibration mode (offset SIN / offset COS / phase) | SELRES = 0x0D, ZPOS = 0x00, HYS = 0x07, ROT = 0x00, CFGAB = 0x00, AERR = 0x00 |
| 3 | Calibration mode (offset SIN / offset COS / amplitude) | |

### [10] Invert direction (default 0)

Defines the direction of the SIN/COS encoder signals. This setting affects the direction of position reading.

| Value | Mode |
|---|---|
| 0 | Ascending (B leads A) (COS leads SIN) |
| 1 | Descending (A leads B) (SIN leads COS) |

### [11] Reset enable for period counter (default 0)

When activated, the period counter resets upon crossing an index (Z).

| Value | Mode |
|---|---|
| 0 | Deactivated |
| 1 | Activated |

### [12] Zero signal position (default 0)

Configures at what angle the index is asserted.

| Value | Angle [degrees] |
|---|---|
| 0 – 31 | Value * 11.25 |

### [13] Zero signal length (default 0)

Configures how long the index is asserted with respect to the SIN/COS signals.

| Value | Length |
|---|---|
| 0 | 90° with respect to the interpolated A/B signals |
| 1 | 180° with respect to the interpolated A/B signals |
| 2 – 3 | Synchronization; 180° with respect to the original SIN/COS signals |

### [14] Zero signal logic (default 0)

Configures the logic of when the index is asserted with respect to the interpolated A/B signals.

| Value | Logic |
|---|---|
| 0 | A = 1; B = 1 |
| 1 | A = 1; B = 0 |
| 2 | A = 0; B = 1 |
| 3 | A = 0; B = 0 |

### [15] Amplitude monitoring type (default 1)

Only valid when `SinCosSetup[17]=1`. Determines the amplitude checking mechanism.

| Value | Mechanism |
|---|---|
| 0 | Max(\|SIN\|, \|COS\|) |
| 1 | SIN² + COS² |

### [16] Amplitude threshold (default 0)

Only valid when `SinCosSetup[17]=1`. Determines the threshold for amplitude checking. If the amplitude is outside the threshold, an amplitude error is asserted when amplitude error checking is enabled. The threshold depends on the checking mechanism.

| Value | SinCosSetup[15]=0 | SinCosSetup[15]=1 |
|---|---|---|
| 0 | 1.4 Vpp | Invalid option |
| 1 | 2.0 Vpp | |
| 2 | 2.6 Vpp | |
| 3 | 3.1 Vpp | |
| 4 | Invalid option | 1.0 Vpp to 4.5 Vpp |
| 5 | | 1.5 Vpp to 4.5 Vpp |
| 6 | | 2.0 Vpp to 4.5 Vpp |
| 7 | | 2.5 Vpp to 4.5 Vpp |

### [17] Amplitude error check (default 1)

Enables/disables amplitude value checking. An amplitude error is triggered when the amplitude is outside the boundary set.

| Value | State |
|---|---|
| 0 | Disabled |
| 1 | Enabled |

### [18] Frequency check (default 0)

Only operational when the interpolation factor ≥ 16 (`SinCosSetup[6] ≤ 12`). Enables/disables checking of the SIN/COS input frequency. A frequency error is triggered when the input frequency exceeds the maximum input frequency for many consecutive cycles.

| Value | State |
|---|---|
| 0 | Disabled |
| 1 | Enabled |

### [19] Test mode (default 0)

Only operational when `SinCosSetup[9]=0`. Determines what signal appears on the Z incremental signal that goes to the DSP. The selectable range is 0–7; a value greater than 7 is rejected as out of range (the chip settings are not written and `SinCosSetup[21]` reports 1).

| Value | Signal on Z |
|---|---|
| 0 | Z |
| 1 | A xor B |
| 2 | ENCLK |
| 3 | NLOCK |

### [20] Analog test mode state (default 0)

Configures what signal appears on the incremental signal lines that go to the DSP. Used in signal calibration.

| Value | Signal on A | Signal on B | Signal on SDA | Signal on SCL |
|---|---|---|---|---|
| 0 | A | B | SDA | SCL |
| 1 | COS+ | COS- | SIN+ | SIN- |

### [21] SIN/COS status (default 0)

Denotes the status of the SIN/COS encoder settings in the encoder chip. This is the error message returned by the chip. A write/assignment to this array location is rejected.

| Value | Status |
|---|---|
| 0 | Chip settings are OK. |
| 1 | Chip settings not written: at least 1 `SinCosSetup` setting is out of range. |
| 2 | Failure to write chip settings. |
| 3 | Chip settings not written: a feature in `SinCosSetup` is not supported by the chip. |

## Examples

```text
ASinCosSetup[1]=2        ; signal gain
ASinCosSetup[6]=7        ; interpolation factor 2^(16-7) = 512 counts per cycle
ASinCosSetup[20]=1       ; enter analog test mode (TMA) for calibration
ASinCosSetup[21]        ; query chip settings status
```

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `SinCosSetup` applies for `EncType=4`
- [SinCosSignals](SinCosSignals-AuxSinCosSig.md) — read-only SIN/COS interpolation status
