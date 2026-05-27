---
keyword: CIIdentity
summary: Per-axis array of identifying information returned by the connected Central-i device.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 509
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 23
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 24
---
# CIIdentity

Per-axis array of identifying information returned by the connected Central-i device.

## Overview

`CIIdentity` is a read-only, axis-related array holding the identity and capability information that the connected Central-i device reports back to the master. The master fills it during the "get device" stage of [CIConnect](CIConnect.md) (and at [CIAutoConnect](CIAutoConnect.md)); before a successful connection its contents are not meaningful, and [CIDisconnect](CIDisconnect.md) clears it. It is not saved to flash. Index `[0]` is unused so the live fields start at index `[1]`.

## How it works

The elements describe the remote unit's class, firmware/FPGA versions, channel counts (how many digital and analog inputs/outputs it has), and the headline electrical ratings. Tools such as Agito PCSuite read these to present the correct interface for the connected device and to scale its I/O.

| Index | Field | Meaning |
|-------|-------|---------|
| [1] | Device class | Remote class as reported (amplifier / I/O / simulation) — see [CIDeviceType](CIDeviceType.md) |
| [2] | Device sub-type | Specific device variant within the class |
| [3] | Central-i engine version | Protocol-engine version in the remote |
| [4] | Application / FPGA version | Remote application/FPGA version word |
| [5] | Digital inputs | Number of digital input channels |
| [6] | Digital outputs | Number of digital output channels |
| [7] | Isolated digital outputs | Number of isolated digital output channels |
| [8] | Analog inputs | Number of analog input channels |
| [9] | Analog outputs | Number of analog output channels |
| [10] | Continuous-current rating | Max continuous current the device supports |
| [11] | Peak-current rating | Max peak current the device supports |
| [12] | Minimum bus voltage | Lower bus-voltage limit of the device |
| [13] | Maximum bus voltage | Upper bus-voltage limit of the device |
| [14] | Mid-PWM value | Device PWM mid-scale reference |
| [15] | App/FPGA version — major | Structured version: major |
| [16] | App/FPGA version — minor | Structured version: minor |
| [17] | App/FPGA version — patch | Structured version: patch |
| [18] | App/FPGA version — owner | Structured version: build owner field |
| [19] | App/FPGA version — sub-version | Structured version: sub-version |
| [20] | Communication version | Remote communication-layer version |
| [21] | Amplifier version | Amplifier firmware version |
| [22] | FPGA size | Remote FPGA size descriptor |

For a **simulated** device type, the master does not read a real remote; instead it writes default channel counts (elements [5]–[9]) so the host still sees a plausible interface.

The device's serial number, date code and detailed per-channel electrical calibration are read separately into the firmware's internal device table (not exposed through this array); `CIIdentity` carries the summary fields above.

## Examples

```text
ACIIdentity[1]      ; device class reported by the connected device
ACIIdentity[5]      ; number of digital inputs on the remote
ACIIdentity[8]      ; number of analog inputs on the remote
```

## Changes between versions

v5 (the Central-i-only, 64-bit firmware) extends the array to 24 elements, adding one further field:

| Index | Field | Meaning |
|-------|-------|---------|
| [23] | Amplifier variant | Amplifier hardware-variant descriptor |

Elements [1]–[22] are unchanged from v4.

## See also

- [CIConnect](CIConnect.md) — populates this array on connect
- [CIDisconnect](CIDisconnect.md) — clears this array
- [CIStatus](CIStatus.md) — live link state
- [CIDeviceType](CIDeviceType.md) — locally configured (expected) port class
