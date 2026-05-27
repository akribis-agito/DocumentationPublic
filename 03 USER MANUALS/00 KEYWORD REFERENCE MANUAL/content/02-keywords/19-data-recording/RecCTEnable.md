---
summary: Enables or disables continuous-time recording for each recording channel.
---
# RecCTEnable

Enables or disables continuous-time recording for each recording channel.

## Overview

`RecCTEnable` is an array that enables or disables the continuous-time recording mode for each recording channel. When enabled, the channel captures data on every servo cycle, up to the size set by [RecCTMaxSize](RecCTMaxSize.md). It is a non-axis parameter saved to flash.

## Examples

```text
ARecCTEnable[1]=1    ; enable continuous-time recording on the first channel
ARecCTEnable[1]     ; query the continuous-time recording state
```

## See also

- [RecCTMaxSize](RecCTMaxSize.md) — buffer size for continuous-time recording
- [RecStart](RecStart.md) — start recording
- [RecStat](RecStat.md) — recording status
