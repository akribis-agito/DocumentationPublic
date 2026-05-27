---
summary: Selects the digital incremental encoder subtype (AqB, pulse-direction, C0/C1, up/down).
---
# EncSubType/AuxEncSubType

Selects the digital incremental encoder subtype.

## Overview

`EncSubType` defines the digital incremental encoder subtype. It is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is 1 (digital incremental encoder), where it tells the controller how to decode the incoming pulses. `AuxEncSubType` is the auxiliary-encoder counterpart and operates the same way.

## How it works

| Value | Digital incremental encoder type |
|-------|----------------------------------|
| 0     | A quad B encoder (AqB)           |
| 1     | Pulse-direction encoder          |
| 2     | C0/C1 bits                       |
| 3     | Up/down pulses                   |

## Examples

```text
EncSubType=0        ; A quad B (AqB) encoder
EncSubType=1        ; pulse-direction encoder
```

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `EncSubType` applies for `EncType=1`
- [EncFilt](EncFilt-AuxEncFilt.md) — digital filter for incremental encoder inputs
