---
summary: Per-scope arrays of complex CAN codes selecting the parameters to capture.
---
# RecParamA/RecParamB

Per-scope arrays of complex CAN codes selecting the parameters to capture.

## Overview

`RecParamA` and `RecParamB` are arrays that store the [complex CAN codes](../../01-keyword-usage-and-syntax/complex-can-code.md) of the parameters to capture for the first and second scope, respectively. Each scope can capture up to 20 parameters. The capture order set here defines the order of the data returned by [RecUpload](RecUpload.md) and [RecUploadNext](RecUploadNext.md).

## How it works

When [RecStart](RecStart.md) runs, the controller scans the array from index 1 and resolves each entry until it reaches the first zero, which terminates the list. Every non-zero complex CAN code up to that point becomes a recorded channel. Duplicated complex CAN codes in the array result in duplicated capture.

Each entry is validated as recording starts. An entry is rejected (and the start fails) if the code is not a valid keyword, if it names a command rather than a parameter (commands cannot be recorded), if its axis is out of range, or if the array index it points to is missing or outside that keyword's bounds. The total sample count — number of channels multiplied by [RecLength](RecLength.md) — must also fit within the scope's buffer, otherwise the start is rejected.

The capture order set here is preserved end to end: it determines how samples are interleaved in the buffer and the column order returned by [RecUpload](RecUpload.md) and [RecUploadNext](RecUploadNext.md). For parameters held in user units, the controller also records each channel's scaling at start time so the upload can convert the raw samples back to user units.

## Examples

| RecParamA indices | 1 | 2 | 3 | 4 | 5 – 20 |
|---|---|---|---|---|---|
| Value (Complex CAN codes) | 1026 (BPos) | 66565 (BVel[1]) | 1050 (BCurrRef) | 0 | 0 |

When recording on the first scope is started with the array definition above, all of BPos, BVel\[1\] and BCurrRef are captured.

## See also

- [RecUpload](RecUpload.md) — stream captured data (in this order)
- [RecUploadNext](RecUploadNext.md) — packetized upload
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — raw per-scope buffers
- [RecStart](RecStart.md) — start recording once parameters are set
