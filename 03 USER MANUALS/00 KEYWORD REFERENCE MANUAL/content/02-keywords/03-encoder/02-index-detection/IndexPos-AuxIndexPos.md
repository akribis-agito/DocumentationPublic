---
summary: Records the latest position at which the encoder index was detected.
---
# IndexPos/AuxIndexPos

Records the latest position at which the encoder index was detected.

## Overview

`IndexPos` records the latest position where the index (reference mark) was encountered. It is only used when the encoder type ([EncType](../01-general-settings/EncType-AuxEncType.md)) is 1 (digital incremental encoder) or 4 (SIN/COS encoder), since only incremental encoders have an index mark. It is typically used in homing applications, together with the detection flag [IndexStat](IndexStat-AuxIndexStat.md). `AuxIndexPos` is the auxiliary-encoder counterpart.

## Examples

```text
AIndexPos           ; read the position of the last detected index
```

## See also

- [IndexStat](IndexStat-AuxIndexStat.md) — flag indicating whether the index has been detected
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; index detection applies for `EncType=1` or `4`
