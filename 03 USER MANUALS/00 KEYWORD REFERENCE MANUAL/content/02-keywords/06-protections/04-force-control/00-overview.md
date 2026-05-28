# Force control

Force-error protection guards force-control operation by monitoring the force error (commanded minus measured force) and disabling the axis if it grows too large — for example when the force feedback is lost or the load behaves unexpectedly.

- [MaxForceErr](MaxForceErr.md) sets the limit used in closed-loop force control. Exceeding it raises fault code 1045 (force error exceeds limit) on [ConFlt](../../07-status-and-faults/ConFlt.md).
- [MaxForceErrOL](MaxForceErrOL.md) sets the larger limit used while the force path is open-loop or signal-injected. Exceeding it raises fault code 1057 (open-loop force error too high).

The active limit is switched automatically between the two depending on whether the force loop is closed or open. If no analog force feedback is defined, the loop instead raises fault code 1046 (force feedback not defined).
