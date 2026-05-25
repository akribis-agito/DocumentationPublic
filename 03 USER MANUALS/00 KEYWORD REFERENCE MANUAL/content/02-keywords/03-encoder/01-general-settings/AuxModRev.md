# AuxModRev

**Definition:**

AuxModRev is the modulo revolution divisor for the auxiliary encoder, analogous to [ModRev](ModRev.md) for the main encoder. When set to a non-zero value, the auxiliary encoder position (AuxPos) is wrapped to the range [0, AuxModRev − 1]. This parameter is axis-related, saved to flash, and is currently marked as not implemented in the firmware.

%%
Needs verification
AuxModRev is flagged NOT_IMPLEMENTED in the current firmware table; confirm availability before use.
%%
**See also:**

[ModRev](ModRev.md), [AuxPos](../../09-current-and-voltage/01-system-variables/AuxPos.md)
