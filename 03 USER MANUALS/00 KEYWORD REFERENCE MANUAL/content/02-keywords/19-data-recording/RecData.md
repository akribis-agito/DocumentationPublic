---
summary: Array holding the metadata and raw values of the latest recording.
---
# RecData

Array holding the metadata and raw values of the latest recording.

## Overview

`RecData` is an array that holds all the information pertaining to the latest recording. This data is best viewed as a graph using Agito's PC Suite. The information here is mainly useful for a user that wants to write their own software to analyze the data.

Use [RecUpload](RecUpload.md) to receive a comma-delimited list of the values in `RecData`. Note that `RecUpload` does not only upload the values as they are but also converts them, where needed, to values that are useful to the user. Some of the conversions use internal ratios, so the user cannot repeat them.

The values of `RecData` can be accessed individually by querying `RecData[n]`. This is not recommended, both because it is inconvenient and because `RecUpload` will convert the raw data to user data. For per-scope access on products with separate scope buffers, see [RecDataA/RecDataB](RecDataA-RecDataB.md).

## How it works

The buffer is laid out as a fixed metadata header followed by the captured samples. The first 80 entries hold the recording's metadata (requested length, sampling factor, trigger settings, the captured parameter list, per-channel scaling, and the buffer indices that mark where the data begins and ends). The captured samples start after the header.

Samples are interleaved by channel in the order set by [RecParam](RecParam.md): one sample of each recorded parameter is stored per sample tick, then the next tick, and so on. Every sample is stored as a 64-bit value regardless of the source type — 32-bit integers are widened to 64-bit, and floating-point values are stored as their 64-bit bit pattern. `RecUpload` reverses this when it streams the converted data; reading `RecData` directly returns the stored 64-bit form.

While the trigger is being awaited the controller fills the sample area as a circular buffer, so on a completed triggered recording the first valid sample is not necessarily at the start of the data region — the header indices (see [RecDataA/RecDataB](RecDataA-RecDataB.md)) record where the recording actually begins, where the trigger fell, and where it ends.

## Examples

```text
ARecData[1]         ; query the first raw element of the latest recording
```

## See also

- [RecUpload](RecUpload.md) — stream converted, user-unit data
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — per-scope raw buffers
- [RecParam](RecParam.md) — parameters selected for recording
