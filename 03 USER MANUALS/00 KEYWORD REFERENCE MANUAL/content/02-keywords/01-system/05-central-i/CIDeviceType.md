---
keyword: CIDeviceType
summary: Selects the role/class of the Central-i port on an axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 503
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIDeviceType

Selects the role/class of the Central-i port on an axis.

## Overview

`CIDeviceType` declares the class of remote device the master expects to find on this axis's Central-i port — an amplifier, an I/O unit, or a *simulated* version of either. It is axis-related and saved to flash. It governs how the port is connected (real link versus simulation) and what the master verifies when [CIConnect](CIConnect.md) runs: if the device actually present does not match the declared class, the connection fails with a device-type error. Configure it, together with [CILinkConfig](CILinkConfig.md), before connecting.

## How it works

The value is a 32-bit word split into two 16-bit fields:

| Bits | Field | Meaning |
|------|-------|---------|
| 15–0 | Device class | The kind of remote (amplifier / I/O / simulation) — see the class table |
| 31–16 | Device sub-type | The specific device variant within that class |

### Device class (low 16 bits)

| Value | Class | Notes |
|-------|-------|-------|
| 0x1 | Amplifier | Real remote amplifier (drives a motor) |
| 0x2 | I/O unit | Real remote I/O unit |
| 0x3 | Simulated amplifier | No physical link; port is marked connected with default channel counts |
| 0x4 | Simulated I/O unit | As above, for an I/O unit |

(The v5 firmware adds one further real device class — see *Changes between versions*.)

The sub-type field identifies the specific product variant within the class (different amplifier models, adapter/linear-remote variants, or I/O-unit models). The exact sub-type codes are device-specific; the master uses them only to apply the correct channel sizes and limits, and to confirm the connected unit is the one declared.

### Behaviour on connect and on change

- During [CIConnect](CIConnect.md) the master reads the remote's reported class/sub-type and compares it with `CIDeviceType`. A real amplifier class also requires the axis's `AmpType` to be a compatible drive mode (built-in PWM for an amplifier, analog for an adapter); a mismatch stops the connection with an error (see [CIStatus](CIStatus.md) error codes).
- Setting an **amplifier** class on a port that cannot drive a motor is rejected by [CIConnect](CIConnect.md).
- A **simulation** class causes [CIConnect](CIConnect.md) and [CIAutoConnect](CIAutoConnect.md) to mark the port connected immediately and populate [CIIdentity](CIIdentity.md) with default counts, instead of running the physical link sequence.
- Writing a value that differs from the currently connected device forces an immediate disconnect (clearing [CIStatus](CIStatus.md) and [CIIdentity](CIIdentity.md)), so the port can reconnect with the new role.

## Examples

```text
ACIDeviceType        ; query the configured device class/sub-type for this axis
```

To set the port to a simulated amplifier (class 0x3, default sub-type 1):

```text
ACIDeviceType=0x00010003
```

## Changes between versions

v5 is the Central-i-only, 64-bit firmware. It adds one further real device class (value 0x5) beyond the amplifier/I/O/simulation classes above, plus additional amplifier-adapter sub-type variants. The class encoding and the amplifier/I/O/simulation values are otherwise unchanged.

## See also

- [CIConnect](CIConnect.md) — verifies the connected device against this value
- [CILinkConfig](CILinkConfig.md) — physical/protocol parameters
- [CIIdentity](CIIdentity.md) — the device's actual reported identity
- [CIStatus](CIStatus.md) — device-type error codes (9 and 7)
- [CISyncDef](CISyncDef.md) — synchronous data definition
