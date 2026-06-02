---
keyword: ScopeParams
summary: Lists the signals captured by the Central-i scope.
availability:
  standalone: []
  central-i:
  - v5
can_code: 744
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ScopeParams

Lists the signals captured by the Central-i scope.

## Overview

`ScopeParams` is an array that specifies which controller signals the Central-i scope records. Each element holds the [complex CAN code](../../01-keyword-usage-and-syntax/complex-can-code.md) of one signal to capture, so the scope started by [ScopeOn](ScopeOn.md) knows what to sample. Up to **six** signals can be selected. It is a non-axis parameter saved to flash, so the selection persists across power cycles.

## How it works

The array is 1-indexed: `ScopeParams[1]` is the first captured signal, up to `ScopeParams[6]`. An element of `0` is treated as empty and selects no signal. The complex CAN code encodes both the parameter and, for axis parameters, the axis it applies to, so the same parameter on different axes can be captured together.

The list is analyzed when the scope is started (see [ScopeOn](ScopeOn.md)), not when an element is written. An entry that does not resolve to a capturable signal — an unknown CAN code, an invalid axis or array index, or a command keyword — is silently skipped: it contributes nothing to the packet and raises no error.

Each captured sample written to the buffer consists of a time stamp followed by one value per configured signal; this determines the packet size reported by [ScopeStatus](ScopeStatus.md) (index 1). Selecting more signals makes each sample larger and therefore reduces the number of samples the fixed buffer can hold before it pauses. The configured list is snapshotted into [ScopeAbout](ScopeAbout.md) when the scope starts, so a host can interpret an upload even if the selection is later changed.

## Examples

```text
AScopeParams[1]=2      ; first captured signal (complex CAN code)
AScopeParams[2]=1026   ; second captured signal
AScopeParams[3]=0      ; clear the third slot (no signal)
AScopeParams[1]       ; query the first captured signal
```

## See also

- [ScopeOn](ScopeOn.md) — start/stop the scope
- [ScopeGap](ScopeGap.md) — scope sampling interval
- [ScopeAbout](ScopeAbout.md) — snapshot of the captured set
- [ScopeUpload](ScopeUpload.md) — retrieve captured data
