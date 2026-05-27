---
keyword: MotorTempOffset
summary: Offset applied to the motor temperature reading (cable-resistance compensation).
---
# MotorTempOffset

Offset applied to the motor temperature reading (cable-resistance compensation).

## Overview

`MotorTempOffset` defines an offset applied to the [MotorTemp](MotorTemp.md) reading, used to compensate for the temperature-reading error introduced by the resistance of the sensor cable (the lead resistance adds to the RTD/PT100 resistance and so biases the apparent temperature).

> **Condition:** only applicable with a temperature sensor selected — i.e. [MotorTempUsed](MotorTempUsed.md) ≠ 0.

> **Implementation note:** the raw motor-temperature reading is produced by the fixed linear ADC-to-°C conversion described in [MotorTemp](MotorTemp.md) (`AG300_CTL01ControlInterrupt.c:12275`). A dedicated `MotorTempOffset` global is **not referenced** in the v4 (LTS) control code that was reviewed, so on this firmware the documented cable-compensation offset may not yet be applied in the reading path. Confirm with Agito whether your product/firmware applies it.

## See also

- [MotorTemp](MotorTemp.md) — measured temperature (and the conversion formula)
- [MaxMotorTemp](MaxMotorTemp.md) — over-temperature limit
- [MotorTempUsed](MotorTempUsed.md) — sensor-type selection
