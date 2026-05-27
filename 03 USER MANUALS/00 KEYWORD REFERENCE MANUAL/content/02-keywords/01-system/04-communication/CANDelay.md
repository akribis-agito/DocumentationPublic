---
keyword: CANDelay
summary: Delay, in samples, applied to CAN messages.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 222
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1000
  default: 6
  scaling: 1.0
  implemented: final
overrides: {}
---
# CANDelay

Delay, in samples, applied to CAN messages.

## Overview

`CANDelay` sets a minimum spacing, measured in control-interrupt samples, between consecutive outgoing CAN messages. This affects only message *timing* — it does **not** change the baud rate ([CANBaud](CANBaud.md)). It is saved to flash. Use it when a slower CAN host cannot keep up with back-to-back replies from the controller and needs a guaranteed gap between messages.

## How it works

The controller keeps a countdown that ticks down by 1 on every control interrupt (the sampling clock runs at 16384 samples per second, so one sample is about 61 µs). Before transmitting a CAN message the firmware waits until the countdown reaches 0, then immediately reloads it with the `CANDelay` value. The wait happens **between** sends rather than being added to a send already in progress, so `CANDelay` enforces a minimum interval from one transmit request to the next:

$$
minimum\ spacing \approx CANDelay \times 61\ \mu s
$$

A value of 0 disables the spacing (messages are sent as fast as the bus allows). The maximum is 1000 samples (roughly 61 ms). See the communication manual for guidance on when a delay is needed.

## Examples

```text
ACANDelay=6          ; require at least ~0.37 ms between CAN messages
ACANDelay=0          ; no enforced spacing
```

## See also

- [CANAddr](CANAddr.md) — CAN base address
- [CANBaud](CANBaud.md) — CAN bus baud rate
