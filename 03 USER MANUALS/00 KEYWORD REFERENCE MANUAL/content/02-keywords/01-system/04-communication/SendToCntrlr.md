---
keyword: SendToCntrlr
summary: Partially-implemented function that routes a parameter write to another controller.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 484
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 1001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    array_size: 10001
---
# SendToCntrlr

Partially-implemented function that routes a parameter write to another controller.

## Overview

`SendToCntrlr` relays a value from this controller's [GenData](../../20-arrays/GenData.md) array to another controller's `GenData` array over the serial (RJ45) port. It is flagged **partially implemented**, so behaviour may depend on the specific firmware build and the value transfer is one-directional with no parsed reply.

For writing an arbitrary parameter on a remote node, the [RemoteCAN](RemoteCANSend.md) group (over CAN) is the more general and direct mechanism.

## How it works

`SendToCntrlr` is a function that takes two arguments — a destination index and a source index — and emits an ASCII command on serial port B of the form:

```text
AGenData[<destination index>] = <value of local GenData[<source index>]>
```

In other words, it reads the value of the local [GenData](../../20-arrays/GenData.md) element named by the source index and sends a command that writes that value into the `GenData` element named by the destination index on the controller wired to the serial port. The transfer is fixed to the `GenData` array, but the destination and source indices are independent — they need not refer to the same element number on each side. Because it transmits a text command and does not parse a reply back into a parameter, it is best suited to pushing a working value to a downstream controller in a chained setup.

## Examples

```text
ASendToCntrlr[5]=5   ; send local GenData[5] to the remote controller's GenData[5] (destination 5, source 5)
```

## See also

- [RemoteCANSend](RemoteCANSend.md) — send a single CAN write/read to a remote node (more general)
- [GenData](../../20-arrays/GenData.md) — the general-purpose array this function transfers
- [RSBaud](RSBaud.md) — baud rate of the serial port used
- [CANAddr](CANAddr.md) — CAN addressing
