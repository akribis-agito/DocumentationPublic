# Virtual encoder

A virtual encoder is a software-driven encoder-signal generator: when enabled, the controller emits a real quadrature or pulse/direction signal on the axis's encoder-emulation outputs that tracks a selectable internal source variable, scaled and delayed as configured. It does not replace the axis's own position feedback; it produces an output signal that a downstream device can read. This is useful for passing a software-defined source to another device, for simulation, or for synchronising with an external process. The keywords in this section configure the virtual encoder:

- [VEncOn](VEncOn.md) — enables or disables the virtual encoder
- [VEncSrc](VEncSrc.md) — selects the source signal
- [VEncType](VEncType.md) — sets the output format
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — numerator / denominator of the scaling ratio
- [VEncDelay](VEncDelay.md) — fixed delay applied to the output
