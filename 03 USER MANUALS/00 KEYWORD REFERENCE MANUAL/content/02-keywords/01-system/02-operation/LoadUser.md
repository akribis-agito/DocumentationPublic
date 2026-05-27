---
keyword: LoadUser
summary: Restores the user-saved parameter set from flash into the active parameters.
---
# LoadUser

Restores the user-saved parameter set from flash into the active parameters.

## Overview

`LoadUser` loads the user-defined parameter set — previously stored by [SaveUser](SaveUser.md) — from flash into the active parameter table, overwriting the current values. It is the counterpart of `SaveUser`. The user parameter area is separate from the main parameter set handled by [Load](Load.md) / [Save](Save.md), letting an operator keep and recall their own configuration independently of the main saved set. `LoadUser` cannot be executed while the motor is enabled or in motion.

## How it works

`LoadUser` is the user-area counterpart of [Load](Load.md): it restores the snapshot previously captured by [SaveUser](SaveUser.md), copying those values from the user region of flash back into the live parameter table and discarding any unsaved edits. It reads only the user area, so it has no effect on — and is unaffected by — the main set written by [Save](Save.md). Use it to return to your personal configuration after experimenting, or after a [Load](Load.md) has reverted the controller to the main set.

> **Availability note.** `SaveUser` / `LoadUser` provide a second, user-owned snapshot in addition to the main [Save](Save.md) / [Load](Load.md) set. Whether the pair is present depends on the product and firmware build; if your controller does not implement it, use [Save](Save.md) / [Load](Load.md) for persistence.

## Examples

```text
ALoadUser            ; restore the user-saved parameter set (motor must be stopped)
```

## See also

- [SaveUser](SaveUser.md) — save the user parameter set
- [Load](Load.md) / [Save](Save.md) — main parameter set
