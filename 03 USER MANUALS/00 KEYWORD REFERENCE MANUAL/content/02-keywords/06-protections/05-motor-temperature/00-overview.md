# Motor temperature

Motor-temperature protection guards the motor against overheating using a temperature sensor (RTD/PT100) wired to the temperature-sensor input.

- [MotorTempUsed](MotorTempUsed.md) is the master gate: with no sensor selected (`0`) the temperature reading and all protection are skipped; when enabled, the reading and protection become active.
- [MotorTemp](MotorTemp.md) is the measured temperature in °C.
- [MaxMotorTemp](MaxMotorTemp.md) is the over-temperature limit. Exceeding it disables the axis with fault code 1040 (motor temperature too high) on [ConFlt](../../07-status-and-faults/ConFlt.md); graduated warnings are reported in [StatReg](../../07-status-and-faults/StatReg.md) bits 15–16 before the limit is reached.
- [MotorTempOffset](MotorTempOffset.md) is an offset intended to compensate for sensor-cable resistance.
