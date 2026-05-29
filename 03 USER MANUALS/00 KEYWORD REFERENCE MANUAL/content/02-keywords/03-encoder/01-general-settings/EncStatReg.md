---
keyword: EncStatReg
summary: Read-only status register reporting absolute-encoder health bits (disconnect, error, warning, CRC).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 422
attributes:
  access: ro
  scope: axis
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
overrides: {}
---
# EncStatReg

Read-only status register reporting absolute-encoder health bits (disconnect, error, warning, CRC).

## Overview

`EncStatReg` is a read-only, per-axis bitfield that reports the health of a **serial absolute encoder**. Each control cycle the controller refreshes it from the encoder interface and keeps the low-order health bits. It is the encoder-specific companion to the general axis status register [StatReg](../../07-status-and-faults/StatReg.md): when one of these bits indicates a persistent fault, the axis is taken off and the matching code appears in [ConFlt](../../07-status-and-faults/ConFlt.md).

The register is meaningful only for an axis whose feedback is a serial absolute encoder (see [EncType](EncType-AuxEncType.md)). For incremental, Sin/Cos, or other feedback types the bits stay clear. It is not saved to flash and always reflects the live state.

## How it works

The controller reads the encoder-interface status each cycle and retains only the lowest five bits (mask `0x1F`); higher bits are not reflected. The meaningful health bits are:

| Bit | Mask | Meaning when set |
|---|---|---|
| 0 | `0x00000001` | Encoder did not respond / looks disconnected. |
| 1 | `0x00000002` | Encoder error bit asserted (read-head or scale problem reported by the encoder). |
| 2 | `0x00000004` | Reported but not acted upon by the controller (protocol-dependent meaning — see *Bit layout by encoder protocol* below). |
| 3 | `0x00000008` | Encoder warning asserted (a degraded but non-fatal condition reported by the encoder). |
| 4 | `0x00000010` | CRC of the encoder data frame failed (likely high noise on the link). |

Bit 2 (mask `0x00000004`) is retained and visible to a host, but the controller does not test it for fault handling — it never takes the axis off on bit 2 alone. Its meaning is protocol-dependent, so do not assume a clean encoder just because bit 2 is the only bit set.

The encoder warning (bit 3, mask `0x00000008`) is signalled separately from the error bit but is handled together with it for fault purposes. To confirm a clean encoder, test for the absence of all of these health bits rather than relying on any single bit.

How the bits are acted upon depends on [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md), the abnormal-condition timeout:

- **Disconnect (bit 0, without CRC):** if the motor is on, the axis is taken off immediately and [ConFlt](../../07-status-and-faults/ConFlt.md) reports fault `1070`. On a brushless motor the commutation status is also invalidated (it must re-phase), because the motor may have moved while the encoder was disconnected.
- **CRC error (bit 4):** while the condition persists the controller extrapolates the position and counts the cycles. If the condition lasts longer than [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) cycles and the motor is on, the axis is taken off and [ConFlt](../../07-status-and-faults/ConFlt.md) reports fault `1069`.
- **Error or warning (bit 1, or the warning condition):** handled the same way against the same timeout; on expiry [ConFlt](../../07-status-and-faults/ConFlt.md) reports fault `1068`.
- When no abnormal bit is present, the error counters reset.

Setting [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) to `-1` disables the error/warning/CRC monitoring (the bits may still be reported, but they do not trigger a fault). The disconnect handling is independent of `EncAbsErrTime`.

### Bit layout by encoder protocol

The controller reads the same five status bits regardless of encoder type and applies one fixed interpretation (bit 0 = disconnect, bit 1 = error, bit 3 = warning, bit 4 = CRC). What the encoder interface actually places on each bit, however, depends on the configured protocol:

| Bit (mask) | BiSS-C / SIN-COS | EnDat 2.2 | Tamagawa |
|---|---|---|---|
| 0 (`0x01`) | Disconnected / no response | Encoder error | No response / timeout (disconnect) |
| 1 (`0x02`) | Amplitude error | Frame CRC failed | Start/stop framing error |
| 2 (`0x04`) | Frequency error | Unsupported mode | Frame CRC failed |
| 3 (`0x08`) | System error | Additional encoder error flag | (unused) |
| 4 (`0x10`) | Frame CRC failed | Additional encoder error flag | (unused) |

The controller's fixed fault mapping (bit 4 = CRC -> fault `1069`; bit 1 or bit 3 = error/warning -> fault `1068`) lines up exactly with **BiSS-C / SIN-COS**. With **EnDat 2.2** the encoder's CRC failure appears on bit 1, so it is treated as an *error* (fault `1068`), not as a CRC fault (`1069`). With **Tamagawa** the CRC failure appears on bit 2, which is captured but not separately acted upon. For protocol-independent monitoring, test for the absence of *all* low bits rather than a specific bit position.

## Examples

```text
AEncStatReg          ; read the absolute-encoder status bits

; test a specific condition (host-side bit test)
; bit 4 (0x10) set  -> CRC errors are occurring
; bit 0 (0x01) set  -> encoder looks disconnected
```

## See also

- [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) — timeout that converts a persistent error/warning/CRC condition into a fault
- [EncType](EncType-AuxEncType.md) — feedback type; these bits apply to the serial absolute encoder
- [StatReg](../../07-status-and-faults/StatReg.md) — general axis status register
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault register; reports codes 1068 / 1069 / 1070 for these conditions
