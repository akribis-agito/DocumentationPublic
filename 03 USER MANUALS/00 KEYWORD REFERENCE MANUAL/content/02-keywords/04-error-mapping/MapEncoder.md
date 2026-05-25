# MapEncoder

**Definition:**

MapEncoder is a per-segment array that selects which encoder source is used as the position reference for that segment of the error-mapping table. Each element corresponds to a map segment defined by MapStartPos and MapLength. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[MapType](MapType.md), [MapStartPos](MapStartPos.md), [MapLength](MapLength.md), [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md)
