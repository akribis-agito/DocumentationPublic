---
summary: First-order filter coefficient (1-64) smoothing PDPos into PosRef in direct P/D mode.
---
# PDFiltFact

First-order filter coefficient (1-64) smoothing PDPos into PosRef in direct P/D mode.

## Overview

Agito controllers support motion modes in which the desired motor position is defined by the pulse/direction input port. Refer to the [MotionMode](../02-motion-configuration/MotionMode.md) parameter, direct (3) and indirect (4) P/D motion modes.

The pulse/direction input port value can be read using the parameter [PDPos](PDPos.md). It is equal to the number of input pulses (direction taken into account) multiplied by the parameter [PDFact](PDFact.md).

In direct P/D motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 3), `PDPos` is used to set the position reference (`PosRef`, the desired position) directly. However, to avoid large steps in `PosRef` (especially when [PDFact](PDFact.md) is large), a first-order filter is applied to the change in `PDPos` before it is assigned to `PosRef`. `PDFiltFact` is the **integer coefficient** of that filter — it matters most when the pulse stream is coarse or fast.

`PDFiltFact` is an internal coefficient, **not set directly by the user**: it is computed automatically from the cut-off-frequency keyword [PDPosFilt](PDPosFilt.md). Set the filter through `PDPosFilt`; `PDFiltFact` is the value the controller derives from it.

## How it works

### The filter

Each control cycle in direct mode the reference offset is updated as a first-order low-pass of the P/D delta:

$$
\text{PosRef}_k = \frac{\Delta\text{PDPos}_k \cdot \text{PDFiltFact} + \text{PosRef}_{k-1} \cdot (64 - \text{PDFiltFact})}{64}
$$

`PDFiltFact` ranges from **1** (slowest filter, heaviest smoothing) to **64** (no filtering — `PosRef` follows the delta directly). The constant 64 is a fixed historical scaling.

> **Note:** The values above operate on `PDPos` and `PosRef` *relative to* the values latched at [Begin](../04-motion-command/Begin.md), so the filter starts from a clean zero offset at the start of motion.

### How it is derived from PDPosFilt

When [PDPosFilt](PDPosFilt.md) (a cut-off frequency in Hz × 100) is written, the controller converts it to the coefficient with a backward-Euler discretisation of `w / (s + w)`:

$$
\text{PDFiltFact} = 64 \cdot \frac{2\pi\,T_s\,\text{PDPosFilt}}{100 + 2\pi\,T_s\,\text{PDPosFilt}}
$$

where `Ts` is the sample time. The lower bound of `PDPosFilt` (4150) exists so the resulting `PDFiltFact` never rounds to 0.

## Examples

`PDFiltFact` is not written directly; configure the filter through [PDPosFilt](PDPosFilt.md):

```text
APDPosFilt=25000     ; 250 Hz cut-off -> controller computes the PDFiltFact coefficient
APDPosFilt=12800     ; 128 Hz cut-off (default)
```

## See also

- [PDPosFilt](PDPosFilt.md) — cut-off-frequency keyword that sets this coefficient
- [PDPos](PDPos.md) — the scaled P/D counter whose change is filtered
- [PDFact](PDFact.md) — scaling factor applied to input pulses
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects direct (3) / indirect (4) P/D motion
