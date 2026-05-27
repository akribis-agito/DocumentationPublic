---
summary: Command time for each current command, in milliseconds.
---
# CurrCmdTime

Command time for each current command, in milliseconds.

## Overview

`CurrCmdTime` is the command time for each current command, in milliseconds.

> **Obsolete / superseded:** This entry was imported from the 2021 PDF reference. The current keyword for per-entry timing in current operation mode is [CurrCmdHTime](CurrCmdHTime.md). A search of the current firmware (both the standalone/v4 and central-i v5 sources) finds no `CurrCmdTime` symbol anywhere — the holding-time table is implemented as `CurrCmdHTime`. Use [CurrCmdHTime](CurrCmdHTime.md) instead; this page is retained only to redirect users who encounter the old name.

## See also

- [CurrCmdHTime](CurrCmdHTime.md) — documented holding time per current-command entry
- [Current operation mode](00-overview.md) — overview of current-mode keywords
