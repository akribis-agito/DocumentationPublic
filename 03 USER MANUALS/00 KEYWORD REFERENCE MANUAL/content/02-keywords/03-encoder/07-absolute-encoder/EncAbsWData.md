# EncAbsWData

**Definition:**

EncAbsWData holds the data value to be written to the absolute encoder register when a write transaction is issued via EncAbsSendCmd. Load this parameter with the desired value before calling EncAbsSendCmd with EncAbsWRType set to write. It is an axis-related parameter, not saved to flash, and cannot be changed while the motor is on or in motion.

**See also:**

[EncAbsAddr](EncAbsAddr.md), [EncAbsWRType](EncAbsWRType.md), [EncAbsRData](EncAbsRData.md), [EncAbsSendCmd](EncAbsSendCmd.md)
