---
summary: Array of complex CAN codes selecting the parameters to record.
---
# RecParam

Array of complex CAN codes selecting the parameters to record.

## Overview

> **Note:** `RecParam` does not appear as a controller keyword in the firmware consulted for this reference — only the per-scope [RecParamA/RecParamB](RecParamA-RecParamB.md) variants are available on the controller. This page is retained for the legacy/single-buffer name; confirm availability against the current firmware before relying on `RecParam` directly.

`RecParam` is an array that holds the [complex CAN codes](../../01-keyword-usage-and-syntax/complex-can-code.md) of the parameters (channels) to record. It can hold up to 20 parameters. Recording walks the array in order and captures every entry up to (but not including) the first zero, so a zero entry terminates the list. For per-scope selection on products with separate scope buffers, see [RecParamA/RecParamB](RecParamA-RecParamB.md).

## How it works

At [RecStart](RecStart.md) the controller scans `RecParam` from index 1 and resolves each non-zero complex CAN code into a recordable channel. The scan stops at the first zero, so to record a single parameter you enter its complex CAN code in `RecParam[1]` and `0` in `RecParam[2]`; later entries are then ignored. The number of channels found multiplied by [RecLength](RecLength.md) must fit the scope buffer, otherwise the start is rejected.

Each resolved channel is validated when recording starts. A code is rejected if it is not a real keyword, if it names a command (functions cannot be recorded), if its axis letter is out of range, or if an array index is missing or out of bounds for that keyword. The order set here is the order in which samples are laid out in the buffer and returned by [RecUpload](RecUpload.md).

## Examples

```text
ARecParam[1]=1026    ; record this parameter
ARecParam[2]=0       ; terminate the list (only RecParam[1] is recorded)
ARecParam[1]        ; query the first recorded parameter code
```

## See also

- [RecParamA/RecParamB](RecParamA-RecParamB.md) — per-scope parameter selection
- [RecData](RecData.md) — raw recorded values
- [RecUpload](RecUpload.md) — stream converted, user-unit data
