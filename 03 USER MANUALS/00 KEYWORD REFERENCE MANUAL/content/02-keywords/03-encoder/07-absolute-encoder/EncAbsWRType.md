# EncAbsWRType

**Definition:**

EncAbsWRType selects the type of register access (read or write) to perform when communicating with the absolute encoder via EncAbsSendCmd. Set this before issuing EncAbsSendCmd to define whether the transaction reads from or writes to the encoder register at EncAbsAddr. It is an axis-related parameter, not saved to flash, and cannot be changed while the motor is on or in motion.

**See also:**

[EncAbsAddr](EncAbsAddr.md), [EncAbsWData](EncAbsWData.md), [EncAbsRData](EncAbsRData.md), [EncAbsSendCmd](EncAbsSendCmd.md)
