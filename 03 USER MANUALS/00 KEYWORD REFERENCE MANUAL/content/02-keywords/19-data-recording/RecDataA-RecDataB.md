---
summary: Per-scope arrays holding recording metadata and raw (unconverted) captured data.
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# RecDataA/RecDataB

Per-scope arrays holding recording metadata and raw (unconverted) captured data.

## Overview

`RecDataA` and `RecDataB` store the recording metadata and raw captured data for the first and second scope respectively. Unlike [RecUpload](RecUpload.md), which applies unit conversion, these arrays expose the unconverted buffer directly, which is useful for custom analysis software.

> **Note:** For products with only a single scope, querying `RecDataB` is equivalent to querying `RecDataA`.

## How it works

The metadata for each scope is stored in the first 80 entries of the array. The raw captured data, without any unit conversion, is stored in the subsequent array entries, interleaved by channel in the [RecParamA/RecParamB](RecParamA-RecParamB.md) order (one sample per channel per sample tick). Each stored value occupies one buffer slot whose width is firmware-dependent: legacy firmware stores each value as 32 bits, while newer firmware stores each value as 64 bits regardless of the source type — 32-bit integers are widened to 64-bit, and floating-point values are held as their 64-bit bit pattern, so a raw float reads as an integer bit pattern rather than a number until it is reinterpreted. The user can read the metadata and raw captured data subject to an overall index cap of 32079; raw captured data with an index larger than the cap (i.e. captured data number 32000 and above) is not readable via `RecDataA`/`RecDataB`. To stream the entirety of the captured data, refer to [RecUpload](RecUpload.md).

Fields 23–25 are physical ring indices. To read a completed capture in time order, start at field 23 and read the number of cells in field 1, wrapping to index 81 after the last data slot. The final cell is at field 25, even if its index is smaller than field 23.

For firmware containing the recorder correction, field 24 points to the first channel of the sample that satisfies the combined trigger. At 0% pretrigger this equals field 23. At 100% the entire capture precedes the trigger, so field 24 marks the slot immediately after field 25, wrapping if necessary. With no trigger configured (type 0), field 24 marks the configured position within the ring and conveys no observed event. Earlier firmware can place the marker one sample after the observed crossing. [Firmware change #2675](https://github.com/akribis-agito/Firmware-Main/pull/2675)

| Index | Descriptions |
|---|---|
| 1 | Requested number of data cells across all channels. Stopping after the trigger updates this to the actual number of retained cells. |
| 2 | Number of requested data points per parameter (RecLength) |
| 3 | Total number of data points recorded |
| 4 | Trigger position (RecTrigPos) |
| 5 - 7 | Maximum trigger values (RecTrigValMax) |
| 8 | Scaling for all user units |
| 9 | Downsampling factor (RecGap) |
| 10 - 12 | Trigger sources (RecTrigSrc) |
| 13 - 15 | Trigger bit-wise masks (RecTrigMask) |
| 16 – 18 | Trigger types (RecTrigTyp) |
| 19 - 21 | Trigger values (RecTrigVal) |
| 22 | Current loop cycle rate |
| 23 | Ring index of the first retained cell |
| 24 | Ring index of the first channel at the trigger position |
| 25 | Ring index of the last retained cell (inclusive) when data are available for upload |
| 26 - 45 | Complex CAN codes of the recorded parameters |
| 46 | Trigger mode (RecTrigsMode) |
| 47 – 48 | Trigger logics (RecTrigsLogic) |
| 49 - 55 | Reserved |
| 56 - 75 | User unit of the recorded parameters |
| 76 – 80 | Reserved |

## See also

- [RecUpload](RecUpload.md) — stream the full, converted data set
- [RecParamA/RecParamB](RecParamA-RecParamB.md) — parameters captured per scope
- [RecStop](RecStop.md) — updates metadata length when recording is interrupted
- [RecStat](RecStat.md) — recording status
