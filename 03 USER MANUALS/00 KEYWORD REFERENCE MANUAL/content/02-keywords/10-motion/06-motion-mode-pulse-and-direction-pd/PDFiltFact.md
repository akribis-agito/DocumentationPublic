# PDFiltFact

<!-- Imported from the 2021 PDF reference. Verify against current firmware
     behavior and update with the latest semantics. -->

Agito controllers support motion modes in which the desired motor position is defined by the Pulse/Direction input port. Refer to the documentation of the [MotionMode](../02-motion-configuration/MotionMode.md) parameter, `PD_DIRECT` and `PD_INDIRECT` motion modes.

The Pulse/Direction input port value can be read using the parameter [PDPos](PDPos.md). It is equal to the number of input pulses (direction taken into account) multiplied by the parameter [PDFact](PDFact.md).

In the `PD_DIRECT` motion mode, `PDPos` is used to set directly the position reference (`PosRef`: desired position). However, in order to avoid large steps in `PosRef` (especially when `PDFact` is large), a first-order filter is used to filter `PDPos` before it is assigned to `PosRef`. `PDFiltFact` defines the bandwidth of this first-order filter.

The relevant equation is:

$$
\text{PosRef}_k = \frac{\text{PDPos}_k \cdot \text{PDFiltFact} + \text{PosRef}_{k-1} \cdot (64 - \text{PDFiltFact})}{64}
$$

`PDFiltFact` takes values between 1 (slowest filter) and 64 (no filter at all).

**Note:**

1. Future versions of Agito controllers will not input the filter coefficient directly (which is not easy to calculate); instead the user will define the desired filter frequency and the controller will automatically calculate the resulting filter coefficient.
2. The above equation is only an illustration. Internally, the calculations are done relative to the initial `PosRef` and `PDPos` values during the `Begin` function (command to start motion in `PD_DIRECT` mode).
