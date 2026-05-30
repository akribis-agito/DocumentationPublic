# EPPState

**Definition:**

EPPState is a read-only status that reports what EPP (the repetitive-control feedforward) is currently doing.

| Value | Meaning |
|-------|---------|
| 0 | Idle: EPP is not running. |
| 1 | Active, first run: a new learning sequence is running. |
| 2 | Active, repetitive run: a continued learning run is applying and updating the stored correction. |

At the start of a motion, EPPState is set to 1 or 2 by copying the pending [EPPRequest] value. EPPState is forced back to 0 (idle) when the motor is off and when the motor is on but not in motion. EPPState is read-only and is not stored to flash.

**See also:**

[EPPRequest](EPPRequest.md), [EPPFiltLength](EPPFiltLength.md), [EPPModelRange](EPPModelRange.md)
