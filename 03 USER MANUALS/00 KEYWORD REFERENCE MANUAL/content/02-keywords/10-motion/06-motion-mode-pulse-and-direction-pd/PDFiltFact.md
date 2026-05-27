---
summary: First-order filter coefficient (1-64) smoothing PDPos into PosRef in direct P/D mode.
---
# PDFiltFact

First-order filter coefficient (1-64) smoothing PDPos into PosRef in direct P/D mode.

## Overview

Agito controllers support motion modes in which the desired motor position is defined by the pulse/direction input port. Refer to the [MotionMode](../02-motion-configuration/MotionMode.md) parameter, `PD_DIRECT` and `PD_INDIRECT` motion modes.

The pulse/direction input port value can be read using the parameter [PDPos](PDPos.md). It is equal to the number of input pulses (direction taken into account) multiplied by the parameter [PDFact](PDFact.md).

In the `PD_DIRECT` motion mode, `PDPos` is used to set the position reference (`PosRef`, the desired position) directly. However, to avoid large steps in `PosRef` (especially when `PDFact` is large), a first-order filter is applied to `PDPos` before it is assigned to `PosRef`. `PDFiltFact` defines the bandwidth of this first-order filter, which is why it matters most when the pulse stream is coarse or fast.

## How it works

The relevant equation is:

$$
\text{PosRef}_k = \frac{\text{PDPos}_k \cdot \text{PDFiltFact} + \text{PosRef}_{k-1} \cdot (64 - \text{PDFiltFact})}{64}
$$

`PDFiltFact` takes values between 1 (slowest filter) and 64 (no filter at all).

> **Note:**
> 1. Future versions of Agito controllers will not input the filter coefficient directly (which is not easy to calculate); instead the user will define the desired filter frequency and the controller will automatically calculate the resulting filter coefficient.
> 2. The above equation is only an illustration. Internally, the calculations are done relative to the initial `PosRef` and `PDPos` values during the [Begin](../04-motion-command/Begin.md) function (command to start motion in `PD_DIRECT` mode).

## Examples

```text
APDFiltFact=64       ; no filtering (PosRef follows PDPos directly)
APDFiltFact=1        ; slowest first-order filter
```

## See also

- [PDPos](PDPos.md) — the scaled P/D counter being filtered
- [PDPosFilt](PDPosFilt.md) — cut-off-frequency form of the direct-mode P/D filter
- [PDFact](PDFact.md) — scaling factor applied to input pulses
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects `PD_DIRECT` / `PD_INDIRECT`
