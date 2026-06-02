---
keyword: ScopeOn
summary: Enables or disables the Central-i signal scope.
availability:
  standalone: []
  central-i:
  - v5
can_code: 742
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ScopeOn

Enables or disables the Central-i signal scope.

## Overview

`ScopeOn` starts or stops the Central-i signal scope — a streaming capture that samples the signals configured in [ScopeParams](ScopeParams.md) at the interval set by [ScopeGap](ScopeGap.md) and makes them available for incremental read-out with [ScopeUpload](ScopeUpload.md). When set to `1` the scope begins capturing; setting it to `0` stops it. It is a non-axis parameter and is not saved to flash, so the scope always starts disabled after power-up. It is available on Central-i (v5) only.

## How it works

Setting `ScopeOn` from `0` to `1` prepares a fresh session in one step:

1. The signal list in [ScopeParams](ScopeParams.md) is analyzed and the packet size (a time stamp plus one buffer slot per configured signal) is computed and published in [ScopeStatus](ScopeStatus.md) (index 1).
2. The circular capture buffer is reset (free space set to full, packet identifier and lost-packets counter cleared).
3. The configuration is snapshotted into [ScopeAbout](ScopeAbout.md) so an upload can be interpreted later.

From then on, the scope evaluates one sample every [ScopeGap](ScopeGap.md) tick in the background and appends it to the buffer. If the buffer fills before the data is read out, the scope **pauses** — [ScopeStatus](ScopeStatus.md) index 3 reads `2` (paused because full) and the lost-sample counter advances — and it resumes automatically once [ScopeUpload](ScopeUpload.md) frees space. Setting `ScopeOn` back to `0` stops sampling immediately; data already buffered remains available for upload.

The scope is one of three independent capture mechanisms: the trigger-aligned recording scope (`Rec*` keywords) captures a fixed-length window in one pass; the continuous logger ([LoggerOn](LoggerOn.md)) runs indefinitely with up to 40 parameters; and this Central-i scope streams up to six signals for live monitoring.

## Examples

```text
AScopeOn=1           ; start the Central-i scope
AScopeOn=0           ; stop the Central-i scope
AScopeOn            ; query whether the scope is running
```

## See also

- [ScopeParams](ScopeParams.md) — signals the scope captures
- [ScopeGap](ScopeGap.md) — scope sampling interval
- [ScopeStatus](ScopeStatus.md) — scope run state and buffer fill
- [ScopeUpload](ScopeUpload.md) — retrieve captured data
- [LoggerOn](LoggerOn.md) — the continuous data logger
