---
summary: Enables or disables continuous-time recording for each recording channel.
---
# RecCTEnable

Enables or disables continuous-time recording for each recording channel.

## Overview

`RecCTEnable` is an array that enables or disables continuous (circular) recording mode for each scope. In continuous recording the scope keeps sampling into a circular buffer that always retains the most recent samples — up to the size set by [RecCTMaxSize](RecCTMaxSize.md) — instead of stopping after a fixed [RecLength](RecLength.md). It is a non-axis parameter saved to flash.

> **Note:** Continuous recording is not active in the current firmware. `RecCTEnable` and `RecCTMaxSize` are reserved and have no effect; use the standard triggered (one-shot) recording flow described in the [Data recording](00-overview.md) overview.

## Examples

```text
ARecCTEnable[1]=1    ; enable continuous-time recording on the first channel
ARecCTEnable[1]     ; query the continuous-time recording state
```

## See also

- [RecCTMaxSize](RecCTMaxSize.md) — buffer size for continuous-time recording
- [RecStart](RecStart.md) — start recording
- [RecStat](RecStat.md) — recording status
