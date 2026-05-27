---
keyword: SinCosAInPort
summary: Removed — formerly selected the analog port for sin/cos (resolver) encoder feedback.
---
# SinCosAInPort

Removed — formerly selected the analog port for sin/cos (resolver) encoder feedback.

> **Removed in firmware 1.3.0.1-36.** `SinCosAInPort` is no longer present in the parameter
> table of current firmware builds and cannot be used. This page is retained for reference
> to older firmware and documentation.

## Overview (historical)

`SinCosAInPort` formerly selected which analog input port was used to read the sine/cosine
encoder signals for resolver or sin/cos encoder feedback.

It was removed when support for the dedicated `SinCosSignals[1-6]` keyword was added (firmware
note 1.3.0.1-36); sin/cos feedback is no longer routed through the general analog-input ports.
It is absent from the parameter table on both current LTS and development firmware, and no
firmware code references it.

## See also

- [AInPort](AInPort.md) — analog-input readings
- [AInMode](AInMode.md) — analog-input function assignment
