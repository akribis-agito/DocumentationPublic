---
keyword: BEMFFFWLevel
summary: Percentage level applied to the back-EMF voltage feedforward contribution.
availability:
  standalone: []
  central-i:
  - v5
can_code: 848
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 200.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BEMFFFWLevel

Percentage level applied to the back-EMF voltage feedforward contribution.

> Available from central-i v5.

## Overview

`BEMFFFWLevel` scales the back-EMF term of the voltage feedforward. The back-EMF voltage is computed from the motor constant [BEMFConst](BEMFConst.md) and the actual motor speed; `BEMFFFWLevel` is a percentage that sets how much of that computed voltage is applied. It lets you apply the full modelled back-EMF voltage (100%), a partial amount, or none, without changing the physical constant.

The back-EMF term is part of the quadrature-axis feedforward output [VqFFW](VqFFW.md) and is only applied when voltage feedforward is enabled by [VoltageFFWOn](VoltageFFWOn.md).

## How it works

`BEMFFFWLevel` is a percentage (in %). The back-EMF feedforward voltage is the modelled back-EMF (from [BEMFConst](BEMFConst.md) and the actual motor speed) multiplied by `BEMFFFWLevel`/100:

- `0` — no back-EMF feedforward (default);
- `100` — full modelled back-EMF voltage applied;
- values up to the maximum allow over- or under-compensation of the modelled term.

The valid range is 0 to 200 (%) and the default is 0. `BEMFFFWLevel` is a flash-backed parameter and may be set with the motor on or in motion; the change takes effect on the next control cycle. With either `BEMFFFWLevel` or [BEMFConst](BEMFConst.md) at 0, the back-EMF term is zero.

## Examples

```text
ABEMFFFWLevel=100    ; apply the full modelled back-EMF voltage
ABEMFFFWLevel        ; read back the configured level
ABEMFFFWLevel=0      ; disable the back-EMF feedforward term
```

## See also

- [BEMFConst](BEMFConst.md) — motor back-EMF constant this level scales
- [VqFFW](VqFFW.md) — q-axis feedforward output that carries the back-EMF term
- [VoltageFFWOn](VoltageFFWOn.md) — master enable for voltage feedforward
- [RmFFWLevel](RmFFWLevel.md) / [LmFFWLevel](LmFFWLevel.md) — level scalings of the resistive and inductive terms
