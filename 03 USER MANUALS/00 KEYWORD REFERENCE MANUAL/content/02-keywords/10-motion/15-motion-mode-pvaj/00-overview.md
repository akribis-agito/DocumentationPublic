# Motion mode – PVAJ

PVAJ motion executes a **downloaded trajectory table** instead of a profile the controller computes for itself. The host uploads a list of position / velocity / acceleration / jerk rows into [PVAJList](PVAJList.md); the controller interpolates between consecutive rows with a quintic polynomial that matches position, velocity **and** acceleration at both ends of every interval, so all three stay continuous across every seam.

Two motion modes share that one executor and differ only in what a motion command reaches:

| [MotionMode](../02-motion-configuration/MotionMode.md) | Name | `Begin` / `Stop` / `Abort` acts on |
|---|---|---|
| `22` | PVAJ | the commanded axis alone |
| `23` | MultiAxisPVAJ | every axis currently in mode `23`, as one coordinated group |

## The sequence

Upload → [PVAJValidate](PVAJValidate.md) → [PVAJArm](PVAJArm.md) → `Begin`.

Arming takes a **snapshot** of the list, so a new list may be uploaded and validated while a motion is still executing. Completing a motion disarms the axis, so each run needs its own `PVAJArm = 1`.

Rows are consumed one every `Gap` control ticks, and are interpreted either as absolute positions or relative to wherever the axis stood at `Begin`, according to the `Mode` header entry.

## Keyword summary

| Keyword | Role |
|---|---|
| [PVAJList](PVAJList.md) | The trajectory table: header plus up to 8192 P/V/A/J rows |
| [PVAJValidate](PVAJValidate.md) | Checks the list before it may be armed |
| [PVAJArm](PVAJArm.md) | Snapshots the validated list and makes the axis eligible for `Begin` |
| [PVAJStatus](PVAJStatus.md) | State, current row and rows remaining |
| [PVAJPosTol](PVAJPosTol.md) | Position-continuity tolerance the validator applies |
| [PVAJVelTol](PVAJVelTol.md) | Velocity-continuity tolerance the validator applies |

## Group behaviour (mode 23)

One `Begin` starts every member, and it is **refused unless every member is ready** — a group that started partially would no longer follow the coordinated path. The refusal codes are `400` (the commanded axis is not itself armed), `402` (a member is not armed) and `401` (a member is motor-off or already in motion).

Members need not carry lists of the same length. A member that reaches the end of its own list holds its final position and keeps reporting In Motion until the last member finishes, so from outside the group starts and ends as a single motion.

When the group comes down, the members that never received the command report why through [MotionReason](../05-motion-status/MotionReason.md):

| MotionReason | Meaning |
|---|---|
| `42` | another member was stopped |
| `43` | another member was aborted |
| `44` | another member hit a limit switch |
| `45` | another member went motor-off |

## Product availability

PVAJ is **central-i v5 (AGM800) only**. The list is 32771 doubles per axis — about 3 MB, and the armed snapshot doubles that — which is unremarkable against the AGM800's DDR but exceeds the entire external-RAM pool of the C2000 products for even one axis.

On a product without the feature the six mnemonics are **absent rather than stubbed**, deliberately: a host detects PVAJ support by asking whether `PVAJList` exists, and that probe must fail on a controller that cannot serve it.
