---
summary: Per-scope arrays of complex CAN codes selecting the parameters to capture.
---
# RecParamA/RecParamB

Per-scope arrays of complex CAN codes selecting the parameters to capture.

## Overview

`RecParamA` and `RecParamB` are arrays that store the [complex CAN codes](../../01-keyword-usage-and-syntax/complex-can-code.md) of the parameters to capture for the first and second scope, respectively. Each scope can capture up to 20 parameters. The capture order set here defines the order of the data returned by [RecUpload](RecUpload.md) and [RecUploadNext](RecUploadNext.md).

## How it works

All array entries with a non-zero complex CAN code are recorded. Duplicated complex CAN codes in the array result in duplicated capture.

## Examples

| RecParamA indices | 1 | 2 | 3 | 4 | 5 – 20 |
|---|---|---|---|---|---|
| Value (Complex CAN codes) | 1026 (BPos) | 65565 (BVel[1]) | 0 | 1050 (BCurrRef) | 0 |

When recording on the first scope is started with the array definition above, all of BPos, BVel\[1\] and BCurrRef are captured.

## See also

- [RecUpload](RecUpload.md) — stream captured data (in this order)
- [RecUploadNext](RecUploadNext.md) — packetized upload
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — raw per-scope buffers
- [RecStart](RecStart.md) — start recording once parameters are set
