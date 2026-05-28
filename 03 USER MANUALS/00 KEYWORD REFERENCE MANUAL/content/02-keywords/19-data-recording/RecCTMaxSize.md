---
summary: Sets the maximum sample count of the continuous-time recording buffer per channel.
---
# RecCTMaxSize

Sets the maximum sample count of the continuous-time recording buffer per channel.

## Overview

`RecCTMaxSize` is an array that sets the maximum number of samples retained by the continuous (circular) recording buffer for each scope. It bounds the buffer used when continuous recording is enabled by [RecCTEnable](RecCTEnable.md). It is a non-axis parameter saved to flash.

> **Note:** Continuous recording is not active in the current firmware. `RecCTMaxSize` and [RecCTEnable](RecCTEnable.md) are reserved and have no effect; use the standard triggered (one-shot) recording flow described in the [Data recording](00-overview.md) overview.

## Examples

```text
ARecCTMaxSize[1]=16500   ; allocate up to 16500 samples on the first scope
ARecCTMaxSize[1]        ; query the configured buffer size
```

## See also

- [RecCTEnable](RecCTEnable.md) — enable continuous-time recording
- [RecStart](RecStart.md) — start recording
- [RecLength](RecLength.md) — data points per parameter (triggered recording)
