# Current compensation

This subgroup describes the keywords related to current offsets for the loop (before the decoupling matrix) and for the motor (after the decoupling matrix). For an axis that does not use the decoupling matrix (for example, not in gantry mode), loop and motor current compensation amount to the same thing.

The loop-side compensation (TorqComp) is summed into the current reference inside the position/velocity loop, while the motor-side offset and the commutation-angle table (UPMVelTable) are summed in later, in the current loop, before the current limit.

![Where current compensation adds in: loop-side TorqComp sums into the reference in the position/velocity loop, and the motor-side offset and angle table sum in later in the current loop, ahead of the current limit](compensation-injection.svg)

It contains:

- [CurrRefOffset](CurrRefOffset.md) — motor-side current reference offset.
- [TorqCompMode](TorqCompMode.md) — selects the source of the loop's current compensation.
- [TorqCompFix](TorqCompFix.md) — fixed loop current-compensation values.
- [UPMVelTable](UPMVelTable.md) — commutation-angle current compensation table (e.g. cogging compensation).
