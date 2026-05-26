---
keyword: LoadUser
summary: Restores the user-saved parameter set from flash into the active parameters.
---
# LoadUser

Restores the user-saved parameter set from flash into the active parameters.

## Overview

`LoadUser` loads the user-defined parameter set — previously stored by [SaveUser](SaveUser.md) — from flash into the active parameter table, overwriting the current values. It is the counterpart of `SaveUser`. The user parameter area is separate from the main parameter set handled by [Load](Load.md) / [Save](Save.md), letting an operator keep and recall their own configuration independently of the saved defaults. `LoadUser` cannot be executed while the motor is in motion.

## Examples

```text
LoadUser            ; restore the user-saved parameter set (motor must be stopped)
```

## See also

- [SaveUser](SaveUser.md) — save the user parameter set
- [Load](Load.md) / [Save](Save.md) — main parameter set
