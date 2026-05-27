---
summary: Array of complex CAN codes selecting the parameters to record.
---
# RecParam

Array of complex CAN codes selecting the parameters to record.

## Overview

`RecParam` is an array that holds the complex CAN codes of the parameters to record. It can hold up to 4 parameters. All assigned parameters, up until a zero is encountered, will be recorded. For per-scope selection on products with separate scope buffers, see [RecParamA/RecParamB](RecParamA-RecParamB.md).

## How it works

Recording proceeds through the array and stops at the first zero entry. To record a single parameter, enter the complex CAN code of that parameter in `RecParam[1]` and enter `0` in `RecParam[2]`; the values of `RecParam[3]` and `RecParam[4]` are then ignored.

## Examples

```text
RecParam[1]=1026    ; record this parameter
RecParam[2]=0       ; terminate the list (only RecParam[1] is recorded)
RecParam[1]?        ; query the first recorded parameter code
```

## See also

- [RecParamA/RecParamB](RecParamA-RecParamB.md) — per-scope parameter selection
- [RecData](RecData.md) — raw recorded values
- [RecUpload](RecUpload.md) — stream converted, user-unit data
