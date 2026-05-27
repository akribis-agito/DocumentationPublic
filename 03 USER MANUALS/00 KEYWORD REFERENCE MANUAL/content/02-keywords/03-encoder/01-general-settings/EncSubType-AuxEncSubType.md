---
summary: Selects the digital incremental encoder subtype (AqB, pulse-direction, C0/C1, up/down).
---
# EncSubType/AuxEncSubType

Selects the digital incremental encoder subtype.

## Overview

`EncSubType` selects how the controller decodes the incoming pulses of a digital incremental encoder. It is used only when the encoder type ([EncType](EncType-AuxEncType.md)) is 1 (digital incremental encoder). `AuxEncSubType` is the auxiliary-encoder counterpart and operates the same way.

Range 0–3, default 0 (A quad B).

## How it works

| Value | Digital incremental encoder type |
|-------|----------------------------------|
| 0     | A quad B encoder (AqB)           |
| 1     | Pulse-direction encoder          |
| 2     | C0/C1 bits                       |
| 3     | Up/down pulses                   |

When `EncSubType` is written, the controller programs the encoder-decoding hardware with the selected scheme. The subtype is packed together with the input filter ([EncFilt](EncFilt-AuxEncFilt.md)) and direction ([EncDir](EncDir-AuxEncDir.md)) into a single configuration word: the subtype occupies the low byte, and the filter and direction occupy the next bytes. On central-i this word is sent as a remote-encoder configuration message; on the standalone controller it is written to the encoder-setting register. Because the subtype, filter and direction share one word, changing any of them rewrites the whole configuration.

> [!note]
> `EncSubType` only governs **incremental** decoding (`EncType=1`). For absolute encoders the protocol/sub-protocol is selected by [EncType](EncType-AuxEncType.md) itself (EnDat 2.2, BiSS-C, Tamagawa); there is no separate subtype keyword for them.

### Auxiliary encoder (AuxEncSubType)

`AuxEncSubType` selects the decoding scheme for the auxiliary incremental encoder, using the same value table, and is packed into the auxiliary encoder configuration word alongside `AuxEncFilt` and `AuxEncDir`.

## Examples

```text
AEncSubType=0           ; A quad B (AqB) encoder
AEncSubType=1           ; pulse-direction encoder
AAuxEncSubType=3        ; auxiliary encoder uses up/down pulses
```

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `EncSubType` applies for `EncType=1`
- [EncFilt](EncFilt-AuxEncFilt.md) — digital input filter (packed with the subtype)
- [EncDir](EncDir-AuxEncDir.md) — encoder direction (packed with the subtype)
