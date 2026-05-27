---
keyword: ParamCS
summary: Read-only checksum over the controller's parameter set, for verifying configuration.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 428
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 4
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
overrides: {}
---
# ParamCS

Read-only checksum over the controller's parameter set, for verifying configuration.

## Overview

`ParamCS` is a read-only, 1-indexed array holding checksums computed over the controller's parameter set. A host can read it to verify that the parameters stored on the device match an expected configuration — for example to confirm a fleet of units is identically configured — without downloading and comparing the full parameter list. Comparing `ParamCS` before and after a [Save](../02-operation/Save.md) also confirms whether stored configuration changed.

## How it works

The checksum is recomputed when the parameter set is saved. The firmware walks every saved parameter value: each 32-bit value is split into its high and low 16-bit halves, and both halves are added (with 16-bit wraparound) into a running sum. Values that are stored with scaling are first converted back to their raw (unscaled) integer form, so the checksum reflects the stored representation rather than the displayed user-units value. Element `[0]` of array parameters is excluded (it is never uploaded), so array contents start contributing from element `[1]`.

Three sums are maintained in parallel, differing only in which network-identity parameters they include. They populate the three usable elements:

| Index | Covers |
|-------|--------|
| [1] | All parameters **except** the Ethernet IP address and Ethernet MAC address |
| [2] | All parameters **except** the Ethernet MAC address |
| [3] | All parameters, including IP and MAC |

(The array is declared with four slots; element `[0]` is unused so that communication indices start at 1.)

The reason for the three variants is that the network identity differs from unit to unit: comparing `ParamCS[1]` lets a host confirm that two units have identical *functional* configuration even though their IP and MAC addresses differ, while `ParamCS[3]` verifies an exact match including network identity.

## Examples

```text
AParamCS[1]         ; checksum ignoring IP and MAC (compare functional config across units)
AParamCS[2]         ; checksum ignoring only the MAC address
AParamCS[3]         ; checksum over the full parameter set
```

## See also

- [ParamAbout](ParamAbout.md) — metadata for a single parameter
- [Save](../02-operation/Save.md) — persist parameters to flash (recomputes the checksum)
- [Identity](Identity.md) — controller identification and feature flags
