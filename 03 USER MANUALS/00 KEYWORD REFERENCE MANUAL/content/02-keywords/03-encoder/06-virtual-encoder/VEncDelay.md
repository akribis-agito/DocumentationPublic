---
keyword: VEncDelay
summary: Fixed delay between the source signal and the virtual encoder output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 616
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 25
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncDelay

Pulse/direction setup delay (in microseconds) between a direction change and the first pulse.

## Overview

`VEncDelay` sets the setup time, **in microseconds**, that the virtual encoder waits after changing the direction line before emitting the first pulse, when the output is in pulse/direction format ([VEncType](VEncType.md) = 0). This guarantees the receiving device sees a stable direction level before the leading pulse edge. The value range is 0 to 25 (µs), with a default of 0. It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

It is **not** a feedback-path delay and does not delay the tracked value itself — it only shifts the first pulse following a direction reversal within a control cycle.

## How it works

`SpVEnc` (`SpecialFuncs.c:5180`) converts `VEncDelay` from microseconds into FPGA clocks (`VEncDelay × FPGA_CLOCK_IN_US`) and stores it as the "clocks-to-first-pulse" value. Each control cycle, when the emitted direction sign changes, the firmware loads `2 × VEncDelay` worth of clocks before the first pulse of the new direction (`AG300_CTL01ControlInterrupt.c`, around line 6391); when the direction is unchanged, no extra delay is inserted.

For A-quad-B output (`VEncType = 1`) the delay is forced to **0** — quadrature channels are never switched simultaneously, so no direction-setup time is required.

## Examples

```text
AVEncDelay=0         ; no setup delay (default)
AVEncDelay=5         ; 5 us between a direction change and the first pulse
```

## See also

- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncType](VEncType.md) — output format; the delay applies only to pulse/direction (`VEncType=0`)
- [VEncSrc](VEncSrc.md) — source variable being tracked
