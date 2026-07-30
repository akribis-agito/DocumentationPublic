---
keyword: AdVBusEn
summary: Enables DC-bus feedforward, which holds delivered voltage as the bus sags. Enabled by default.
availability:
  standalone: []
  central-i:
  - v5
can_code: 878
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
  range: [0, 1]
  default: 1
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# AdVBusEn

Enables DC-bus feedforward, which holds delivered voltage as the bus sags. Enabled by default.

## Overview

The drive converts a voltage command into a PWM duty cycle using a **fixed nominal** bus voltage. When the real bus sags — under hard acceleration, on a shared supply, or down a long DC run — the delivered voltage sags with it while the command does not. The motor quietly receives less than the current loop asked for.

With `AdVBusEn=1` the drive measures the bus and scales its voltage output by `nominal / measured`, so the delivered voltage matches the commanded one.

> **Important:** unlike most compensation features, this one is **enabled by default**. On an existing installation it becomes active after a firmware update.

## How it works

Each control cycle the measured [VBus](VBus.md) is pushed through a 16-tap moving average, and the current-loop voltage output is multiplied by `nominal / filtered` before the drive's voltage limit is applied. The applied ratio is readable as [VBusRatio](VBusRatio.md).

The nominal value and the whole filter window are latched from `VBus` at motor-on, gated on the bus reading at least [MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) so that a not-yet-charged bus cannot set a bad nominal. The ratio therefore begins at exactly 1.0 and there is no step at start-up.

> **Note:** the ratio is clamped to **[0.8, 1.2]**. The feature can correct a bus that has moved by up to 20 %, and no further. This bound is deliberate — it also means a fully collapsed bus cannot produce an unbounded voltage command.

> **Worked example:** with the nominal latched at 48.0 V at motor-on, a filtered bus of 44.0 V gives `ratio = 48.0 / 44.0 = 1.091`, and the drive scales its voltage output up by 9.1 % — exactly recovering what the sag would otherwise have cost. At a filtered 40.0 V the arithmetic gives 1.200, which is the clamp: the sag is 16.7 % and the compensation is still exact. At a filtered 30.0 V the arithmetic gives 1.600 but the ratio is **pinned at 1.200**, so only the first 20 % is recovered and the rest is not.
>
> Read [VBusRatio](VBusRatio.md) to see which of those three cases an axis is actually in.

> **Note:** how much a real move benefits depends on your supply and the move's peak power demand, not on this keyword. Measured figures are in the *Current-Loop Compensation* application note.

### When it helps, and when it does not

| Supply | Effect |
|---|---|
| Stiff, well sized | Negligible — nothing to correct |
| Moderately weak or shared | Most useful; the bus moves within the compensator's authority |
| Badly undersized | Little help — the sag exceeds the ±20 % clamp |

> **Important:** this feature buys **tolerance** to a weak or shared supply. It is not a substitute for sizing the supply for the move.

### Edge cases

- **Nominal is snapshotted, not configured:** it is the bus voltage at motor-on, which is the no-load operating point. Each motor-off/motor-on cycle latches a fresh nominal.
- **Collapsed bus:** because the divisor is the latched nominal rather than the live reading, a bus that falls to zero produces a ratio the clamp pins rather than a division by zero.
- **Filter lag:** the 16-tap average lags the bus, so a very fast, deep sag can be momentarily under- or over-compensated.
- **Per-axis scope:** on a Central-i master each remote amplifier has its own bus, so this keyword is per axis; on a standalone controller the bus is board-global.

## Examples

```text
AAdVBusEn=1           ; enabled (default)
AAdVBusEn=0           ; disable, e.g. to compare performance with and without
```

## See also

- [VBusRatio](VBusRatio.md) — the live ratio being applied
- [VBus](VBus.md) — the measured bus voltage
- [MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) — gates the initial latch
