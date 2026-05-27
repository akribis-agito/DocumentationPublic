---
keyword: LoggerUpload
summary: Command that transfers the logged data buffer to the host.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 536
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
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LoggerUpload

Command that transfers the logged data buffer to the host.

## Overview

`LoggerUpload` is a command that streams accumulated logged samples from the controller to the host. It can be invoked while the logger started by [LoggerOn](LoggerOn.md) is active or after it has stopped. It is the continuous-logger counterpart of [RecUpload](RecUpload.md) for the recording scope. It is a non-axis command and is not saved to flash. Use [LoggerAbout](LoggerAbout.md) to interpret the uploaded contents.

## How it works

Each invocation streams only the samples (packets) that are complete and waiting in the buffer, then frees the space they occupied so logging can continue:

1. The number of complete packets currently in the buffer is determined from the free space and packet size reported by [LoggerStatus](LoggerStatus.md). If fewer than one full packet is available, nothing is sent.
2. A single call transmits at most about 100 buffer slots' worth of packets; if more are queued, repeated `LoggerUpload` calls are needed to drain them.
3. As packets are sent, their buffer space is released, which is reflected as increasing free space in [LoggerStatus](LoggerStatus.md) (index 2).

Because the logger runs continuously, a host typically calls `LoggerUpload` periodically to keep the buffer from filling. In stop mode ([LoggerFullMod](LoggerFullMod.md) = 0) this is also how a paused logger resumes, since uploading frees the space it was waiting for.

## Examples

```text
ALoggerUpload        ; stream the available logged packets to the host
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerStatus](LoggerStatus.md) — logger run state and buffer fill
- [LoggerAbout](LoggerAbout.md) — session metadata
- [RecUpload](RecUpload.md) — equivalent upload for the recording scope
