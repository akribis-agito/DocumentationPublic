---
keyword: SaveUser
summary: Saves current parameters to a dedicated user area in flash, separate from defaults.
---
# SaveUser

Saves current parameters to a dedicated user area in flash, separate from defaults.

## Overview

`SaveUser` saves the current parameter values to a dedicated **user** parameter area in flash, kept separate from the main parameter set. The saved values can later be restored with [LoadUser](LoadUser.md), giving an operator their own configuration snapshot that is independent of the set written by [Save](Save.md). As with any flash write, `SaveUser` is **not allowed while the motor is enabled or in motion**.

## How it works

`SaveUser` is the user-area counterpart of [Save](Save.md): it captures the current flash-saveable parameters as a complete snapshot, but stores them in a separate region of flash so that doing so does not overwrite the main saved set. The two areas are wholly independent — `SaveUser` does not affect what [Load](Load.md) restores, and [Save](Save.md) does not affect what [LoadUser](LoadUser.md) restores. This lets an operator keep a personal configuration alongside the standard one and switch between them on demand.

> **Availability note.** `SaveUser` / `LoadUser` provide a second, user-owned snapshot in addition to the main [Save](Save.md) / [Load](Load.md) set. Whether the pair is present depends on the product and firmware build; if your controller does not implement it, use [Save](Save.md) / [Load](Load.md) for persistence.

## Examples

```text
ASaveUser            ; save the current parameters to the user area (motor must be off)
```

## See also

- [LoadUser](LoadUser.md) — restore the user parameter set
- [Save](Save.md) / [Load](Load.md) — main parameter set
