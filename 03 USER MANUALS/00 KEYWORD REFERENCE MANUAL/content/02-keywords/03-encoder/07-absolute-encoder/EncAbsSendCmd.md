---
keyword: EncAbsSendCmd
summary: Command that initiates a register read/write transaction to the absolute encoder.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 719
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    can_code: 902
    ok_in_motion: false
    ok_motor_on: false
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# EncAbsSendCmd

Command that initiates a register read/write transaction to the absolute encoder.

## Overview

`EncAbsSendCmd` is a command function that initiates a register read or write transaction to the absolute encoder using the address, data, and type previously loaded into [EncAbsAddr](EncAbsAddr.md), [EncAbsWData](EncAbsWData.md), and [EncAbsWRType](EncAbsWRType.md). After a read transaction completes, [EncAbsRData](EncAbsRData.md) holds the value read back. It is an axis-scope command function. The whole interface targets the on-encoder memory of a serial absolute encoder (the Tamagawa family, [EncType](../01-general-settings/EncType-AuxEncType.md) = 8) connected as the axis's main encoder; there is no auxiliary-encoder variant. The transaction runs on a standalone controller. On a central-i master it is refused on v5; on v4 it does not reach the encoder and changes unrelated settings in the remote drive (see [Changes between versions](#changes-between-versions)).

## How it works

The transaction is carried out synchronously while the command runs. The command branches on [EncAbsWRType](EncAbsWRType.md):

**Read ([EncAbsWRType](EncAbsWRType.md) = 0)**
1. Write [EncAbsAddr](EncAbsAddr.md) to the encoder-interface memory-address register.
2. Issue the encoder "read from memory" data command.
3. Wait a fixed number of control cycles for the encoder to respond.
4. Read the returned byte, bit-reverse it (the encoder transmits LSB-first), and store it in [EncAbsRData](EncAbsRData.md).

**Write ([EncAbsWRType](EncAbsWRType.md) = 1)**
1. Write [EncAbsAddr](EncAbsAddr.md) to the memory-address register.
2. Write [EncAbsWData](EncAbsWData.md) to the write-data register.
3. Issue the encoder "write to memory" data command.
4. Wait a fixed number of control cycles for the write to complete.

After either branch the firmware returns the encoder-interface command to its idle (normal position-readout) state, then replies OK to the host. On a v4 central-i master, if the addressed port is not active the command returns a "port not active" error. Registers and data are 8-bit (0–255).

> [!caution]
> **Do not use `EncAbsSendCmd` on a v4 central-i master.** The command is accepted, but the transaction does not reach the encoder: the central-i remote unit takes the Tamagawa command, address and write data only through its encoder configuration word, which `EncAbsSendCmd` does not use, so [EncAbsRData](EncAbsRData.md) does not hold encoder data. The command instead writes to unrelated settings in the remote drive. If it has been used on a v4 central-i master, check the remote drive's configuration and restore it before running the motor. **v5** refuses it on a central-i master (see below).

![Absolute-encoder register transaction sequence](encabs-transaction.svg)

Because the transaction blocks while it waits for the encoder, and the parameters cannot be changed with the motor on or in motion, this interface is intended for offline configuration/diagnostics rather than runtime use.

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| CAN code | 719 | 902 |
| On a central-i master | Do not use: accepted, but does not reach the encoder and changes unrelated settings in the remote drive | Refused with error 242 ("This function is not supported in this controller type") |
| Motor on | Allowed | Refused with error 22 ("The parameter assignment or function call are not valid with motor on") |
| In motion | Allowed | Refused with error 21 ("The parameter assignment or function call are not valid during motion") |
| Encoder type | Not checked: set [EncType](../01-general-settings/EncType-AuxEncType.md) = 8 first. With another encoder type the command writes to that encoder's interface settings. | Not applicable (refused on the central-i master) |

On **v5** the encoder EEPROM interface is not available: `EncAbsSendCmd` is refused on the central-i master, so [EncAbsWRType](EncAbsWRType.md), [EncAbsAddr](EncAbsAddr.md), [EncAbsWData](EncAbsWData.md) and [EncAbsRData](EncAbsRData.md) have no effect there. Position feedback from a Tamagawa encoder ([EncType](../01-general-settings/EncType-AuxEncType.md) = 8) over central-i is not affected. **v5 is central-i only.**

## Examples

```text
AEncAbsWRType=0      ; configure for a read
AEncAbsAddr=16       ; target register 16
AEncAbsSendCmd       ; execute the transaction; result in EncAbsRData
AEncAbsRData         ; read back the returned byte
```

## See also

- [EncAbsAddr](EncAbsAddr.md) — register address for the transaction
- [EncAbsWRType](EncAbsWRType.md) — selects read or write access
- [EncAbsWData](EncAbsWData.md) — data to write on a write transaction
- [EncAbsRData](EncAbsRData.md) — data read back on a read transaction
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; this interface applies to the serial absolute (Tamagawa) encoder
