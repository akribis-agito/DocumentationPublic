---
keyword: LockFifoKeep
summary: Selects whether disabling lock logging discards or drains pending FIFO captures.
availability:
  standalone: []
  central-i:
  - v5
can_code: 960
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1
  implemented: final
overrides: {}
last_updated: '2026-11-03'
doc_revision: '2026.11'
---
# LockFifoKeep

On AGM800 and AGM800-EC, selects what happens to pending FIFO captures when
[LockEn](LockEn-AuxLockEn.md) changes from 1 to 0. Set it before disabling logging;
the policy is sampled at that transition. It is per axis and is not saved to flash.

| Value | Behavior |
|---|---|
| 0 (default) | Discard the unread FIFO backlog and count the lost captures in [LockLost](LockLost.md). |
| 1 | Drain the pending FIFO captures into the capture tables before switching FIFO capture off. Captures successfully drained are not added to `LockLost`. |

Draining is bounded. Link loss, a remote reset, an encoder change, repeated read
failures or the drain limit can end it early; the remaining backlog is then
accounted for in `LockLost`. `LockEn = 0` does not mean that the drain has already
finished. This setting does not add a FIFO to a remote or encoder path that lacks
FIFO capture, and it does not change the single-latch path.

Read [LockCntr](LockCntr-AuxLockCntr.md) and `LockLost` after capture activity has
settled to distinguish delivered samples from lost ones. This policy applies to
the main `LockEn` FIFO path; it does not define an auxiliary FIFO drain policy.
