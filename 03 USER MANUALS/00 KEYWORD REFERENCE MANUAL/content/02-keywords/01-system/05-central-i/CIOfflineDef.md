---
keyword: CIOfflineDef
summary: Per-axis array defining which parameters are included in the Central-i offline dataset.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 507
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CIOfflineDef

Per-axis array defining which parameters are included in the Central-i offline dataset.

## Overview

`CIOfflineDef` is a per-axis array that configures the Central-i **offline channel** for a port — the non-cyclic mailbox channel used for addressed reads/writes of remote-unit registers (the transactions carried by [CIOfflineData](CIOfflineData.md) / [CIOfflineSend](CIOfflineSend.md)). It is the offline counterpart of [CISyncDef](CISyncDef.md), which configures the live, per-cycle synchronous channel. The definition is saved to flash. Index `[0]` is unused; the configuration fields are `[1]` and `[2]`.

## How it works

| Index | Field | Meaning |
|-------|-------|---------|
| [1] | Frequency | Offline-channel frequency setting |
| [2] | Filter length | Offline-channel filter length |

These elements parameterise how the offline channel is run for the port. The per-transaction contents (what to read or write, and the reply) are not held here — they live in [CIOfflineData](CIOfflineData.md); `CIOfflineDef` carries only the channel-level definition. Set it before connecting so it is in place when the link comes up.

> Note: in the firmware examined, these two configuration fields are defined and stored but are not consumed by the active offline-message code path, which uses fixed mailbox sizing during [CIConnect](CIConnect.md). Treat the fields as the channel definition; the per-message behaviour is driven by [CIOfflineData](CIOfflineData.md).

## Examples

```text
ACIOfflineDef[1]    ; read the offline-channel frequency setting
ACIOfflineDef[2]    ; read the offline-channel filter length
```

## See also

- [CIOfflineData](CIOfflineData.md) — the per-transaction request/response buffer
- [CIOfflineSend](CIOfflineSend.md) — transmit an offline transaction
- [CISyncDef](CISyncDef.md) — synchronous (live-link) channel definition
