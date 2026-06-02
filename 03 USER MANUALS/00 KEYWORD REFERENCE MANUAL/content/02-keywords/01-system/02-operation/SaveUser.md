---
keyword: SaveUser
summary: Saves current parameters to a dedicated user area in flash, separate from defaults.
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# SaveUser

Saves current parameters to a dedicated user area in flash, separate from defaults.

## Overview

`SaveUser` saves a dedicated set of user variables to a separate **user** area in flash, kept apart from the main parameter set. The saved values can later be restored with [LoadUser](LoadUser.md), giving an operator their own snapshot that is independent of the set written by [Save](Save.md). It is **not allowed while the motor is enabled or in motion**. Unlike [Save](Save.md), which writes the whole flash-saveable parameter set, `SaveUser` stores only this limited block of user variables.

## How it works

`SaveUser` is the user-area counterpart of [Save](Save.md): it captures the current values of a dedicated block of user variables as a snapshot and stores them in a separate region of flash, so doing so does not overwrite the main saved set. The two areas are wholly independent — `SaveUser` does not affect what [Load](Load.md) restores, and [Save](Save.md) does not affect what [LoadUser](LoadUser.md) restores. This lets an operator keep a personal snapshot alongside the standard one and switch between them on demand. If the erase or write step fails, `SaveUser` aborts and returns a flash error (27 for a failed erase, 28 for a failed write) rather than leaving a partial set.

> **Availability note.** `SaveUser` / `LoadUser` provide a second, user-owned snapshot in addition to the main [Save](Save.md) / [Load](Load.md) set. Whether the pair is present depends on the product and firmware build; if your controller does not implement it, use [Save](Save.md) / [Load](Load.md) for persistence.

## Examples

```text
ASaveUser            ; save the current parameters to the user area (motor must be off)
```

## See also

- [LoadUser](LoadUser.md) — restore the user parameter set
- [Save](Save.md) / [Load](Load.md) — main parameter set
