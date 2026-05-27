---
keyword: UserPWM
summary: Duty cycle of each user-controlled PWM output channel.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 626
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
  - 0
  - 4095
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# UserPWM

Duty cycle of each user-controlled PWM output channel.

## Overview

`UserPWM` sets the duty cycle of the user PWM output channels — one element per channel (two channels). The value is the on-time as a fraction of the PWM period over a **12-bit** range (0–4095): `0` = always off, `4095` ≈ always on, `2048` ≈ 50%. The period (and hence frequency) is set by [UserPWMDiv](UserPWMDiv.md). To drive a PWM signal on a physical output, route the channel to that output with [DOutSelect](DOutSelect.md) (the UserPWM 1 / UserPWM 2 selector codes). Saved to flash.

## How it works

The PWM waveform is generated in the FPGA, not by the control loop. When you write `UserPWM` (or `UserPWMDiv`), the firmware immediately writes the new duty value to the FPGA's PWM duty register for that channel — on a standalone controller directly, on central-i by sending it to the remote unit. From then on the FPGA produces the waveform continuously in hardware at the configured frequency, independent of the control-interrupt rate, so the duty resolution and edge timing are not limited by the loop sample time.

A `UserPWM` channel only appears on a pin once that pin's [DOutSelect](DOutSelect.md) is set to the matching UserPWM code; until then the channel runs internally but is not routed out. Because the signal is a hardware function, the [DOutPort](DOutPort.md) / [DOutMode](DOutMode.md) value for that output is irrelevant.

## Examples

```text
AUserPWM[1]=2048     ; ~50% duty cycle on PWM channel 1
AUserPWM[2]=1024     ; ~25% duty cycle on PWM channel 2
AUserPWM[1]          ; read channel 1 duty
```

## See also

- [UserPWMDiv](UserPWMDiv.md) — PWM period / frequency shared by both channels
- [DOutSelect](DOutSelect.md) — route a PWM channel to an output (UserPWM 1 / 2 codes)
