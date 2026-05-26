---
keyword: SaveUser
summary: Saves current parameters to a dedicated user area in flash, separate from defaults.
---
# SaveUser

Saves current parameters to a dedicated user area in flash, separate from defaults.

## Overview

`SaveUser` saves the current parameter values to a dedicated **user** parameter area in flash, kept separate from the main/factory parameter set. The saved values can later be restored with [LoadUser](LoadUser.md), giving an operator their own configuration snapshot that is independent of the defaults written by [Save](Save.md). As with any flash write, `SaveUser` is **not allowed while the motor is enabled**.

## Examples

```text
SaveUser            ; save the current parameters to the user area (motor must be off)
```

## See also

- [LoadUser](LoadUser.md) — restore the user parameter set
- [Save](Save.md) / [Load](Load.md) — main parameter set
