# Virtual encoder

A virtual encoder is a software-generated feedback source: instead of reading a physical encoder, the controller derives the axis position from another signal, scaled and delayed as configured. This is useful for simulation, for following a software-defined source, or for synchronising with an external process. The keywords in this section configure the virtual encoder:

- [VEncOn](VEncOn.md) — enables or disables the virtual encoder
- [VEncSrc](VEncSrc.md) — selects the source signal
- [VEncType](VEncType.md) — sets the output format
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — numerator / denominator of the scaling ratio
- [VEncDelay](VEncDelay.md) — fixed delay applied to the output
