---
summary: Reports the current source line number of the executing user program task.
---
# ProgLine

Reports the current source line number of the executing user program task.

## Overview

`ProgLine` reports the current source line number of the executing user program task, derived from the debug information embedded in the compiled binary. It is a debugging aid that complements [ProgPointer](ProgPointer.md) (the raw instruction pointer) and [ProgStatAll](ProgStatAll.md) (task status), giving a human-readable position in the original source.

> **Note:** `ProgLine` was not found in the firmware parameter table consulted for this reference. Confirm availability and parameter attributes against the current firmware before relying on it.

## See also

- [ProgPointer](ProgPointer.md) — current instruction pointer of each task
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
