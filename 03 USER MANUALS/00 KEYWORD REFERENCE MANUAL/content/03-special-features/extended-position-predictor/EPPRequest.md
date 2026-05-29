# EPPRequest

**Definition:**

EPPRequest selects how EPP (the repetitive-control feedforward) behaves on the next motion. It is a one-shot request: at the start of motion its value is copied into [EPPState] and then EPPRequest is cleared back to 0.

| Value | Meaning |
|-------|---------|
| 0 | No request: EPP does not run on the next motion. |
| 1 | First run: start a new learning sequence (the stored correction vector is zeroed, so this run contributes no learned correction). |
| 2 | Repetitive run: continue learning, applying and updating the correction stored from the previous run. |

Range is 0..2 and the default is 0. EPPRequest is read/write and may be written while in motion; it is not stored to flash.

**See also:**

[EPPState](EPPState.md), [EPPFiltLength](EPPFiltLength.md), [EPPModelRange](EPPModelRange.md)
