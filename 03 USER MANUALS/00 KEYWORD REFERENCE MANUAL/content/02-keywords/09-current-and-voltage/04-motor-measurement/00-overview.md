# Motor measurement

This subgroup holds the motor electrical parameters measured by the PCSuite resistance and inductance tool — the motor resistance and inductance, and the setting that selects whether those measurements are reported as phase or line-to-line data — together with the current-feedback scale factors that convert an external/remote analog current-sense input into motor current feedback.

- [Rm](Rm.md) — measured motor resistance (mΩ).
- [Lm](Lm.md) — measured motor inductance (µH).
- [RLType](RLType.md) — phase vs line-to-line measurement type.
- [CurrFBFact](CurrFBFact.md) / [ExtCurrFBSca](ExtCurrFBSca.md) — scale factor converting an external/remote analog current-sense input into motor current feedback; CurrFBFact is the v4 integer form, ExtCurrFBSca the v5 floating-point form.
