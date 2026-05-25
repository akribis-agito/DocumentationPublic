# EmulRat

**Definition:**

EmulRat sets the ratio between the feedback encoder counts and the quadrature pulses output on the encoder emulation interface. Setting this value to N causes the controller to emit one A/B quadrature step for every N feedback encoder counts, allowing the emulated output to match a downstream device's expected resolution. It is an axis-related parameter saved to flash.

**See also:**

[EmulFilter](EmulFilter.md), [EmulIndexType](EmulIndexType.md), [EncRes](../01-general-settings/EncRes.md)
