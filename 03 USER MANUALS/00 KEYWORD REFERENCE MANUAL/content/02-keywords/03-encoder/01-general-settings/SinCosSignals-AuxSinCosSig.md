---
summary: Read-only array reporting the status of the SIN/COS signal interpolation.
---
# SinCosSignals/AuxSinCosSig

Read-only array reporting the status of the SIN/COS signal interpolation.

## Overview

`SinCosSignals` is a read-only parameter array that displays the status of the SIN/COS signal interpolation. It is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is 4 (SIN/COS encoder). Depending on the product, each array element represents a different status, which is useful for inspecting raw signal levels and quadrant decoding during calibration. `AuxSinCosSig` is the auxiliary-encoder counterpart.

For all Agito products with SIN/COS support except AGFB01, `SinCosSignals` is operational only when the analog test mode is entered (`SinCosSetup[20] = 1`).

## How it works

For all Agito products with SIN/COS encoder support **except AGFB01**:

| Index | Description |
|---|---|
| 1 | Raw SIN+ signal reading, in millivolts (mV) |
| 2 | Raw SIN- signal reading, in millivolts (mV) |
| 3 | Difference between raw SIN+ and SIN- readings, in mV. Equals `SinCosSignals[1] - SinCosSignals[2]` |
| 4 | Raw COS+ signal reading, in millivolts (mV) |
| 5 | Raw COS- signal reading, in millivolts (mV) |
| 6 | Difference between raw COS+ and COS- readings, in mV. Equals `SinCosSignals[4] - SinCosSignals[5]` |

For **AGFB01**:

| Index | Description |
|---|---|
| 1 | **Quadrant alignment status** (default 0). The quadrant inferred from the comparator is checked against the quadrant inferred from the atan2 operation of the raw SIN/COS signals. `0` = Ok; `-1` = Fail (invalid quadrant difference). |
| 2 | **Raw quadrant counter from digital path** (default 0). SIN/COS signals are passed through comparators to form digital A/B signals; an internal counter counts the number of quadrants passed, respecting direction. For example, passing from quadrant 2 to 3 increments the counter, while passing from 2 to 1 decrements it. |
| 3 | **Raw sine signal reading** (default 0), in microvolts (µV), after the amplitude and phase offsets defined by `SinCosSetup`. |
| 4 | **Quadrant code from the comparators (digital path)** (default 0). Determined where SIN/COS signals are compared to 0 to form digital A/B signals. Reported as a quadrant code (not quadrant number); see the table below. |
| 5 | **Quadrant code from the SIN/COS values (analog path)** (default 0). Determined where the angle is computed by the atan2 formula. Reported as a quadrant code (not quadrant number); see the table below. |
| 6 | **Raw cosine signal reading** (default 0), in microvolts (µV), after the amplitude and phase offsets defined by `SinCosSetup`. |

Quadrant code for `SinCosSignals[4]` (digital / comparator path):

| Quadrant code | Quadrant | Comparator A (SIN) | Comparator B (COS) | Angle [degrees] |
|---|---|---|---|---|
| 3 | First | 1 (SIN > 0) | 1 (COS > 0) | [0, 90) |
| 2 | Second | 1 (SIN > 0) | 0 (COS ≤ 0) | [90, 180) |
| 1 | Third | 0 (SIN ≤ 0) | 0 (COS ≤ 0) | [180, 270) |
| 0 | Fourth | 0 (SIN ≤ 0) | 1 (COS > 0) | [270, 360) |

Quadrant code for `SinCosSignals[5]` (analog / atan2 path):

| Quadrant code | Quadrant | SIN sign | COS sign | Angle [degrees] |
|---|---|---|---|---|
| 3 | First | + | + | [0, 90) |
| 2 | Second | + | - | [90, 180) |
| 1 | Third | - | - | [180, 270) |
| 0 | Fourth | - | + | [270, 360) |

## Examples

```text
SinCosSignals[3]?       ; read the SIN+ minus SIN- difference (mV)
SinCosSignals[6]?       ; read the COS+ minus COS- difference (mV)
```

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `SinCosSignals` applies for `EncType=4`
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) — SIN/COS configuration array (enables test mode via index 20)
