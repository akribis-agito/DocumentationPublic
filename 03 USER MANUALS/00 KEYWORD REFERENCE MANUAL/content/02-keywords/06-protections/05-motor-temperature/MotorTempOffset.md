---
keyword: MotorTempOffset
summary: Offset applied to the motor temperature reading (cable-resistance compensation).
---
# MotorTempOffset

Offset applied to the motor temperature reading (cable-resistance compensation).

## Overview

`MotorTempOffset` defines an offset applied to [MotorTemp](MotorTemp.md), used to correct temperature-reading errors caused by cable resistance.

> **Condition:** only applicable with a PT100 temperature sensor — i.e. [MotorTempUsed](MotorTempUsed.md) `== 1`.

## See also

- [MotorTemp](MotorTemp.md) — measured temperature
- [MaxMotorTemp](MaxMotorTemp.md) — over-temperature limit
- [MotorTempUsed](MotorTempUsed.md) — sensor-type selection
