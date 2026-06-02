---
keyword: ScopeUpload
summary: Command that transfers the Central-i scope buffer to the host.
availability:
  standalone: []
  central-i:
  - v5
can_code: 747
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
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
# ScopeUpload

Command that transfers the Central-i scope buffer to the host.

## Overview

`ScopeUpload` is a command that streams captured samples from the scope buffer to the host. It can be invoked while the scope started by [ScopeOn](ScopeOn.md) is running or after it has stopped. It is the Central-i-scope counterpart of [LoggerUpload](LoggerUpload.md) and [RecUpload](RecUpload.md). It is a non-axis command and is not saved to flash. Use [ScopeAbout](ScopeAbout.md) to interpret the uploaded contents.

## How it works

Each invocation streams the complete samples (packets) currently waiting in the buffer, then frees the space they occupied so capture can continue:

1. The number of complete packets available is determined from the free space and packet size reported by [ScopeStatus](ScopeStatus.md). If less than one full packet is available, nothing is sent.
2. A single call transmits a bounded amount of data; if more packets are queued than fit in one transfer, repeated `ScopeUpload` calls are needed to drain them.
3. As packets are sent, their buffer space is released, which is reflected as increasing free space in [ScopeStatus](ScopeStatus.md) (index 2).

Because the scope runs in the background, a host typically calls `ScopeUpload` periodically to keep the buffer from filling. Uploading is also how a scope that has paused because the buffer is full ([ScopeStatus](ScopeStatus.md) index 3 = `2`) resumes capturing, since the upload frees the space it was waiting for.

## Examples

```text
AScopeUpload         ; stream the available captured packets to the host
```

## See also

- [ScopeOn](ScopeOn.md) — start/stop the scope
- [ScopeStatus](ScopeStatus.md) — scope run state and buffer fill
- [ScopeAbout](ScopeAbout.md) — session metadata
- [LoggerUpload](LoggerUpload.md) — equivalent upload for the continuous logger
