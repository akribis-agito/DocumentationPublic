# MapTable/MapTableB/MapTableC/MapTableD/MapTableE

**Definition:**

MapTable (and its extended variants MapTableB through MapTableE) are axis-related arrays that store the position error correction values used by the error-mapping feature. Each element contains a correction offset in encoder counts applied to the feedback position when the axis is within the corresponding segment defined by MapStartPos, MapLength, and MapPosGap. MapTableB–MapTableE are larger arrays (MAP_TABLE_SIZE_HUGE elements) available for higher-resolution or multi-segment maps. All variants are saved to flash and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[MapType](MapType.md), [MapStartPos](MapStartPos.md), [MapLength](MapLength.md), [MapPosGap](MapPosGap.md), [MapEncoder](MapEncoder.md)
