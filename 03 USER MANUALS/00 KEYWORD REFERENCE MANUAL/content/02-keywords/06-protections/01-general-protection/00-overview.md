# General protection

Keywords that report and configure the drive's hardware protection conditions (over-current, encoder fault, watchdog, STO/safety inputs, missing power phases, and so on).

- [HWProtectBits](HWProtectBits.md) is a read-only bitfield reporting the live state of the hardware protection signals.
- [ProtectMask](ProtectMask.md) selects which of those conditions are allowed to disable the axis. A mask bit set to 1 disables (masks out) that protection; certain critical protections are non-maskable and cannot be disabled.

When an enabled protection condition appears, the axis is disabled and the matching fault code is raised on [ConFlt](../../07-status-and-faults/ConFlt.md).
