---
keyword: CIConnect
summary: Command that initiates a Central-i link on the selected axis port.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 504
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIConnect

Command that initiates a Central-i link on the selected axis port.

## Overview

`CIConnect` starts the Central-i connection sequence on the selected axis port. Central-i is the multi-axis network in which a master controller talks to one remote unit (amplifier or I/O unit) per port over a serial link. `CIConnect` brings that link up: the master resets the remote, reads back its device type and version, configures the link timing and the synchronous mailbox, and finally enters the synchronised, cyclic data-exchange state.

Configure the port first — the expected device role ([CIDeviceType](CIDeviceType.md)) and the link timing ([CILinkConfig](CILinkConfig.md)) — then issue `CIConnect`. It is a function keyword (it takes no value) and cannot be run while the motor is on or in motion. After a successful connection [CIIdentity](CIIdentity.md) is populated, the port's bit in [CIGlobalStat](CIGlobalStat.md) is set, and [CIStatus](CIStatus.md) reports the live link; on failure [CIStatus](CIStatus.md) shows the fault state and an error code.

## How it works

`CIConnect` does not block until the link is up. It validates the request, then arms a per-port state machine that the firmware advances (during boot it is driven to completion in a loop; once interrupts are running it advances one step per control cycle). The reported state is visible in `CIStatus[1]` — see [CIStatus](CIStatus.md) for the full state table.

![CIConnect sequence](ciconnect-sequence.svg)

The sequence is:

1. **Reset** — the master pulses the remote reset, enables the link, sets the default channel bit-rate and the offline mailbox sizes, and clears stale mailbox status. `CIStatus[1]` becomes `1` (in process) and the port's connected bit in [CIGlobalStat](CIGlobalStat.md) is cleared.
2. **Get device** — the master queries the remote's Central-i engine version, product type/sub-type, and application/FPGA version through offline (mailbox) messages, filling [CIIdentity](CIIdentity.md).
3. **Verify** — the engine version and device type are checked against [CIDeviceType](CIDeviceType.md). A mismatch, an unsupported engine version, or an `AmpType` that does not match the device class stops the sequence with an error (see the error-code table in [CIStatus](CIStatus.md)).
4. **Configure** — link timing from [CILinkConfig](CILinkConfig.md) is written to the port and the synchronous mailbox is set up for cyclic exchange.
5. **Sync** — the link enters synchronised operation: `CIStatus[1]` becomes `3` (connected) and per-cycle data is exchanged.

`CIConnect` rejects the request up front (returning an error, without changing state) when the port is already connected, when an amplifier device type is requested on a port that cannot drive a motor, or when the configured [CIDeviceType](CIDeviceType.md) class is incompatible with the axis's `AmpType`.

A simulation device type (see [CIDeviceType](CIDeviceType.md)) skips the physical sequence: the port is marked connected immediately and [CIIdentity](CIIdentity.md) is filled with default channel counts so tools show a plausible interface.

## Examples

```text
ACIConnect           ; bring up the Central-i link on the selected axis
ACIStatus[1]         ; then poll: 1 = in process, 3 = connected, 2 = fault
```

## See also

- [CIAutoConnect](CIAutoConnect.md) — run this sequence automatically at power-up
- [CIDisconnect](CIDisconnect.md) — tear down the link
- [CIDeviceType](CIDeviceType.md) / [CILinkConfig](CILinkConfig.md) — port configuration applied during connect
- [CIStatus](CIStatus.md) — per-axis state machine and error codes
- [CIGlobalStat](CIGlobalStat.md) — system-wide connection summary
- [CIIdentity](CIIdentity.md) — device identity populated on connect
