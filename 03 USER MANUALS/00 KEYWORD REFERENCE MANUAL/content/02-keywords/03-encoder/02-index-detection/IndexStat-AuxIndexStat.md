---
summary: Flag indicating whether the encoder index pulse has been detected.
---
# IndexStat/AuxIndexStat

Flag indicating whether the encoder index pulse has been detected.

## Overview

`IndexStat` indicates whether an index pulse has been detected: `0` means the index has not been detected and `1` means it has. It is only used when the encoder type ([EncType](../01-general-settings/EncType-AuxEncType.md)) is 1 (digital incremental encoder) or 4 (SIN/COS encoder). When the index is detected, the controller records the feedback position to [IndexPos](IndexPos-AuxIndexPos.md) and raises this flag, which is commonly used in homing. `AuxIndexStat` is the auxiliary-encoder counterpart.

## How it works

| IndexStat | Meaning |
|---|---|
| 0 | Index not detected |
| 1 | Index detected |

## Examples

```text
IndexStat?          ; check whether the index has been detected
```

## See also

- [IndexPos](IndexPos-AuxIndexPos.md) — position recorded when the index is detected
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; index detection applies for `EncType=1` or `4`
