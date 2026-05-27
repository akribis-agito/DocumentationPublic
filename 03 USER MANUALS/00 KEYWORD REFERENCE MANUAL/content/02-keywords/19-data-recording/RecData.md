---
summary: Array holding the metadata and raw values of the latest recording.
---
# RecData

Array holding the metadata and raw values of the latest recording.

## Overview

`RecData` is an array that holds all the information pertaining to the latest recording. This data is best viewed as a graph using Agito's PC Suite. The information here is mainly useful for a user that wants to write their own software to analyze the data.

Use [RecUpload](RecUpload.md) to receive a comma-delimited list of the values in `RecData`. Note that `RecUpload` does not only upload the values as they are but also converts them, where needed, to values that are useful to the user. Some of the conversions use internal ratios, so the user cannot repeat them.

The values of `RecData` can be accessed individually by querying `RecData[n]`. This is not recommended, both because it is inconvenient and because `RecUpload` will convert the raw data to user data. For per-scope access on products with separate scope buffers, see [RecDataA/RecDataB](RecDataA-RecDataB.md).

## Examples

```text
ARecData[1]         ; query the first raw element of the latest recording
```

## See also

- [RecUpload](RecUpload.md) — stream converted, user-unit data
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — per-scope raw buffers
- [RecParam](RecParam.md) — parameters selected for recording
