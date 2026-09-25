---
keyword: ECATDrvReset
summary: Command that asks the EtherCAT communication module to reset the drive.
availability:
  standalone:
  - v5
  central-i: []
can_code: 888
attributes:
  access: ro
  scope: non-axis
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
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# ECATDrvReset

Command that asks the EtherCAT communication module to reset the drive.

## Overview

`ECATDrvReset` is a **command** (no value). Issuing it sends a reset request
across the internal link to the EtherCAT communication module, which performs the
reset; the controller replies as soon as the request has been handed over.

> **EtherCAT models only.** This keyword exists only on controllers with EtherCAT
> hardware. On every other model it is not implemented and returns the
> unknown-keyword error.

Unlike [Reset](Reset.md), which restarts the controller's own firmware,
`ECATDrvReset` acts on the EtherCAT side. Use it when the fieldbus interface
needs to be brought back to a known state without restarting the controller.

## How it works

1. The controller places a reset request in the shared message area used for
   communication with the EtherCAT module.
2. The module carries out the reset.
3. The controller replies **OK** once the request has been handed over.

The reply confirms that the request was *sent*, not that the drive has finished
resetting or has rejoined the fieldbus. Poll the EtherCAT state from your master
to confirm the outcome.

The command is accepted while the motor is on and while an axis is in motion. It
does not stop motion by itself — resetting the fieldbus interface during motion
will interrupt cyclic communication, so bring the axis to a stop first unless
you specifically intend to break the cyclic link.

## See also

- [Reset](Reset.md) — restarts the controller firmware
- [DownloadFW](DownloadFW.md) — firmware update, which restarts the unit
