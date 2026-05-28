# Error mapping

Error mapping corrects systematic position errors by adding a stored correction to the feedback. Agito supports 1D, 2D and 3D error mapping.

## Overview

Error mapping works by correcting the feedback ([Pos](../10-motion/01-kinematics-status/Pos.md)), not the command ([PosRef](../10-motion/01-kinematics-status/PosRef.md)). [PosBeforeMap](PosBeforeMap.md) is the position value from the encoder **before** error-mapping correction, while [Pos](../10-motion/01-kinematics-status/Pos.md) is the position value **after** correction. The difference between them is the correction contributed by the map.

![1D error-mapping correction summed onto the feedback position](error-mapping-sum.drawio.svg)

The category keywords fit together as follows:

- [MapType](MapType.md) selects the error-mapping dimension: 1D, 2D, or 3D.
- [MapEncoder](MapEncoder.md)`[]` selects which axis's encoder is used for the mapping.
- [MapStartPos](MapStartPos.md)`[]`, [MapPosGap](MapPosGap.md)`[]`, and [MapLength](MapLength.md)`[]` define the coordinates of the error-mapping points.
- [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md)`[]` stores the error values. `MapTableB[]`, `MapTableC[]`, `MapTableD[]`, and `MapTableE[]` extend the array size — i.e. `MapTableB[1]` comes after `MapTable[65536]`.
- [MapStartIndex](MapStartIndex.md) selects the `MapTable` index where the active map begins.
- [MapErrOffset](MapErrOffset.md), [MapErrOffRamp](MapErrOffRamp.md), and [MapErrOnStep](MapErrOnStep.md) govern how the correction is ramped in when mapping engages, avoiding an abrupt position jump.

The correction values are stored as one flat, 1-based list starting at [MapStartIndex](MapStartIndex.md). For multi-dimensional maps the **first** dimension varies fastest. For example, a 2D map of 3 first-dimension points by 2 second-dimension points occupies six consecutive table entries laid out like this:

| Second dimension | First-dim point 1 | First-dim point 2 | First-dim point 3 |
|------------------|:--:|:--:|:--:|
| Point 1 | `MapTable[1]` | `MapTable[2]` | `MapTable[3]` |
| Point 2 | `MapTable[4]` | `MapTable[5]` | `MapTable[6]` |
