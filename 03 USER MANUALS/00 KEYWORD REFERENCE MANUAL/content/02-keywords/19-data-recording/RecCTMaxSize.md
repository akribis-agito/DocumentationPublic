---
summary: Sets the maximum sample count of the continuous-time recording buffer per channel.
---
# RecCTMaxSize

Sets the maximum sample count of the continuous-time recording buffer per channel.

## Overview

`RecCTMaxSize` is an array that sets the maximum number of samples allocated to the continuous-time recording buffer for each recording channel. It bounds the buffer used when continuous-time recording is enabled by [RecCTEnable](RecCTEnable.md). It is a non-axis parameter saved to flash.

## Examples

```text
RecCTMaxSize[1]=16500   ; allocate up to 16500 samples on the first channel
RecCTMaxSize[1]?        ; query the configured buffer size
```

## See also

- [RecCTEnable](RecCTEnable.md) — enable continuous-time recording
- [RecStart](RecStart.md) — start recording
- [RecLength](RecLength.md) — data points per parameter (triggered recording)
