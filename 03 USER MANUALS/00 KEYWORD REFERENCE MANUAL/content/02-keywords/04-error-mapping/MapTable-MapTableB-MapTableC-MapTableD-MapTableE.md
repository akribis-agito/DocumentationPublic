---
summary: Arrays of position-error correction values used by error mapping.
---
# MapTable/MapTableB/MapTableC/MapTableD/MapTableE

Arrays of position-error correction values used by error mapping.

## Overview

`MapTable` and its extended variants `MapTableB` through `MapTableE` are axis-scoped arrays that store the position-error correction values used by the error-mapping feature. Each element holds a correction value that is added to the feedback position at the corresponding map point defined by [MapStartPos](MapStartPos.md), [MapPosGap](MapPosGap.md), and [MapLength](MapLength.md), for the map selected by [MapType](MapType.md) and referenced through [MapEncoder](MapEncoder.md). The result is the corrected [Pos](../10-motion/01-kinematics-status/Pos.md); the uncorrected value is reported by [PosBeforeMap](PosBeforeMap.md).

The `B`–`E` variants extend the addressable table beyond the base `MapTable`. The arrays are addressed as one continuous space: `MapTableB[1]` comes immediately after `MapTable[65536]`, so large maps simply continue into the next variant.

All variants are saved to flash and cannot be changed while the axis is in motion or the motor is on.

## How it works

The arrays form a single continuous index space. Indexing is 1-based within each variant, and the variants chain together:

| Array | Continues from |
|-------|----------------|
| `MapTable[1]` | start of the table |
| `MapTableB[1]` | after `MapTable[65536]` |
| `MapTableC[1]` | after `MapTableB` |
| `MapTableD[1]` | after `MapTableC` |
| `MapTableE[1]` | after `MapTableD` |

[MapStartIndex](MapStartIndex.md) selects which entry the active map begins at.

## Examples

```text
AMapTable[1]=12      ; correction value at the first map point (encoder counts)
AMapTable[1]        ; query the correction at the first map point
AMapTableB[1]       ; query the entry that follows MapTable[65536]
```

## See also

- [MapType](MapType.md) — enables mapping and selects 1D/2D/3D
- [MapStartPos](MapStartPos.md) — start position of each map dimension
- [MapLength](MapLength.md) — number of points per dimension
- [MapPosGap](MapPosGap.md) — spacing between points
- [MapEncoder](MapEncoder.md) — encoder source per dimension
- [MapStartIndex](MapStartIndex.md) — table index where the active map begins
- [PosBeforeMap](PosBeforeMap.md) — feedback position before these corrections are applied
