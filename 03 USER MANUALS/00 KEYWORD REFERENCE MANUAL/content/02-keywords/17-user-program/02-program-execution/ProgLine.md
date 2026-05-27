---
summary: Reports the current source line number of the executing user program task.
---
# ProgLine

Reports the current source line number of the executing user program task.

## Overview

`ProgLine` reports the current source line number of an executing user program thread — a human-readable position in the original program source, as opposed to the raw byte offset given by [ProgPointer](ProgPointer.md). It is a debugging aid used by the Agito PCSuite to highlight which line a thread is on.

## How it works

The controller itself tracks position only as a byte offset into the stored program; that value is what [ProgPointer](ProgPointer.md) reports. The mapping from that offset back to a line number in the original source is done using the debug information generated when the program is compiled. Because the controller does not store the original source, this translation is performed by the host tool (PCSuite) rather than by the controller, which is why `ProgPointer` is the underlying value to read when working without that tool.

> **Note:** `ProgLine` does not appear as a controller keyword in the firmware consulted for this reference — only [ProgPointer](ProgPointer.md) is available on the controller. Confirm availability against the current firmware and PCSuite before relying on `ProgLine` directly.

## See also

- [ProgPointer](ProgPointer.md) — current position as a byte offset (the controller-side value)
- [ProgStat](ProgStat.md) — running status of a thread
- [ProgBreaks](ProgBreaks.md) — breakpoints used alongside line/position readouts
