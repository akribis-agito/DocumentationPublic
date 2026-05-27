---
summary: Index of the master axis whose current reference a slave drive copies.
---
# CurrRefMaster

Index of the master axis whose current reference a slave drive copies.

## Overview

`CurrRefMaster` is the index of the master axis (0-based) used in slave-drive mode: the slave axis copies its current reference (`CurrRef`) from the `CurrRef` of the master axis. It is applicable only when [CurrCmdSrc](CurrCmdSrc.md) = 3.

## How it works

| Value | Axis |
|-------|------|
| 0     | A    |
| 1     | B    |
| …     | …    |

## Examples

```text
CurrCmdSrc=3        ; follow a master axis (slave drive)
CurrRefMaster=0     ; copy current reference from axis A
```

## See also

- [CurrCmdSrc](CurrCmdSrc.md) — selects master-axis current command (value 3)
- [Current operation mode](00-overview.md) — overview of current-mode keywords
