---
keyword: DOutPort
summary: Bit-packed manual state of the digital outputs (before DOutLog inversion).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 211
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
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
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
---
# DOutPort

Bit-packed manual state of the digital outputs (before DOutLog inversion).

## Overview

`DOutPort` holds the manual state of the digital outputs as a bitfield (0-based bit positions: bit 0 = output 1). Each bit: `1` = on, `0` = off. It is the value *before* any [DOutLog](DOutLog.md) inversion.

`DOutPort` is writable only when the output is under manual control — that is, [DOutSelect](DOutSelect.md)`[x] = 0` **and** [DOutMode](DOutMode.md)`[x] = 0`. It is not saved to flash, so manual states must be re-applied after power-up.

## How it works

`DOutPort` is the single word driven onto the physical output pins every cycle. At the end of each control cycle the *final* output word is computed and written straight to the hardware discrete-output stage:

$$
\text{Final output word} = \text{DOutPort} \oplus \text{DOutLog}
$$

So `DOutPort` is the raw on/off intent and [DOutLog](DOutLog.md) is the per-bit polarity applied on top of it. On controllers whose output stage has selectable sink/source pins (open-collector outputs), the final word is then split by [DOutType](DOutType.md): the sink driver gets the bits where `DOutType = 0` and the source driver gets the bits where `DOutType = 1`. Differential outputs occupy the high bits of the same word.

`DOutPort` is not just written by you. When an output is assigned a software function through [DOutMode](DOutMode.md), the controller *itself* sets or clears the corresponding `DOutPort` bit each cycle to mirror the chosen status — which is why a bit you write by hand is overwritten as soon as `DOutMode` for that output is non-zero. Manual control therefore requires `DOutMode[x] = 0` so that nothing else owns the bit.

The width of `DOutPort` (how many bits are real outputs) depends on the product — for example 8 bits (4 open-collector + 4 differential) on a small controller, up to 21 bits on a larger one. Bits beyond the product's output count have no effect.

## Examples

```text
ADOutPort=6          ; binary …0110 — turn outputs 2 and 3 on, all others off
ADOutPort            ; read the present manual output word
```

## Notes

1. Writing the whole word (`ADOutPort=value`) replaces every bit at once. To change one bit while leaving the others, a read–modify–write such as `DOutPort = DOutPort | mask` works but is **not safe against the controller**, which can write `DOutPort` (for `DOutMode` functions) between your read and your write. Prefer the [DOutPortSBit/CBit/TBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md) operations, which perform the bit change atomically.
2. Not saved to flash — re-apply manual states after power-up.
3. The final physical state is `DOutPort XOR DOutLog`, then routed by `DOutType` on products with selectable sink/source outputs.

### Edge cases

- **Output under function control** — bits where [DOutMode](DOutMode.md)`[x] ≠ 0` or [DOutSelect](DOutSelect.md)`[x] ≠ 0` are rewritten every cycle by the controller; manual writes to those bits are overwritten on the next cycle.
- **Bits beyond the product's output count** — accepted by the parameter table (the storage is 32-bit) but have no effect at the pin.
- **Race against the controller** — direct `DOutPort = DOutPort | mask` is unsafe; use [DOutPortSBit/CBit/TBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md) for atomic single-bit changes.
- **Motor on/off** — manual outputs are independent of `MotorOn`; the bit drives the pin whether the servo is on or not.
- **Mode independence** — independent of [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md).
- **Read after function update** — reading `DOutPort` returns the bits the controller is **actually driving**, which includes function outputs; do not assume the read value is what you last wrote.
- **Inverted polarity** — the pin level is `DOutPort XOR DOutLog`; reading `DOutPort` shows the pre-inversion value.
- **Bi-directional pins** — pins routed as outputs by [BiDirConfig](../01-general-keywords/BiDirConfig.md) reflect the value as in [DInPort](../04-digital-inputs/DInPort-DInPortHigh.md) when read back as inputs.
- **Save** — not flash-saveable; reset to defaults at every reboot.

## See also

- [DOutPortSBit-DOutPortCBit-DOutPortTBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md) — interrupt-safe set/clear/toggle of one bit
- [DOutLog](DOutLog.md) — per-bit polarity XORed onto DOutPort
- [DOutType](DOutType.md) — sink/source routing of the final word
- [DOutSelect](DOutSelect.md) / [DOutMode](DOutMode.md) — must both be 0 to write DOutPort manually
