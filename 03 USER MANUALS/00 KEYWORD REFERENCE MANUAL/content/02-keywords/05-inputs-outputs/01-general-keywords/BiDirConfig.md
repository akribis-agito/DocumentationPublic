---
keyword: BiDirConfig
summary: Bitfield configuring each bi-directional I/O pin as an input or an output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 495
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - -2147483648
    - 2147483647
---
# BiDirConfig

Bitfield configuring each bi-directional I/O pin as an input or an output.

## Overview

`BiDirConfig` sets the direction of the controller's bi-directional I/O pins — which pins act as inputs and which as outputs. Each bit of the value corresponds to one bi-directional channel. It is saved to flash and can be changed at any time. Configure pin direction here before using the digital-input or digital-output keywords for those channels.

The number of bi-directional pins is **product-dependent**: some products expose a single differential bi-directional I/O, others up to eight. Bits beyond the pins a given product actually has have no effect.

## How it works

When `BiDirConfig` is written the value is passed straight to the hardware's bi-directional direction register:

- **Single-axis controller** — the low 16 bits are written directly to the hardware direction register.
- **Central-i** — the value is queued as an "assign" message and sent to the addressed remote I/O unit, where it configures that unit's pins. This is why the keyword is axis-scoped on Central-i: each I/O module is reached through its own axis index.

Each bit selects the direction of one pin; the hardware register interprets the bit pattern. A pin configured as an input is then read through the digital-input keywords (its bit appears in the bi-directional portion of [DInPort-DInPortHigh](../04-digital-inputs/DInPort-DInPortHigh.md)), and a pin configured as an output is driven through [DOutPort](../05-digital-outputs/DOutPort.md). Set `BiDirConfig` before relying on those keywords for a bi-directional channel.

> The value is written verbatim to the hardware register, so the per-bit polarity (whether a set bit means "input" or "output") is defined by the hardware. Confirm the convention for your product before driving outputs.

## Examples

```text
ABiDirConfig        ; read the current direction configuration
ABiDirConfig=0      ; default configuration (all pins in their default direction)
```

### Edge cases

- **Per-pin polarity** — set bit = "input" on some hardware, "output" on others; **always verify** with the product manual.
- **Bits beyond the available pins** — accepted by the parameter table but ignored at the hardware register.
- **Changing direction at runtime** — accepted; the pin is reconfigured immediately, but any wired-up logic on the other side may see a transient before settling.
- **Motor on/off** — independent of `MotorOn`.
- **Save** — flash-saveable; reloaded into the hardware direction register at boot.
- **Platform** — central-i sends the value as an assign message to the addressed remote unit; standalone writes directly to the FPGA register.

## See also

- [DInPort-DInPortHigh](../04-digital-inputs/DInPort-DInPortHigh.md) — digital-input port states (where bi-directional pins set as inputs appear)
- [DOutPort](../05-digital-outputs/DOutPort.md) — digital-output port states (drives bi-directional pins set as outputs)
