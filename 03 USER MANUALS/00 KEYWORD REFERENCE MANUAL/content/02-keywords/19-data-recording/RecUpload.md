---
keyword: RecUpload
summary: Streams a scope's metadata and user-unit scaled recorded data to the host.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 244
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# RecUpload

Streams a scope's metadata and user-unit scaled recorded data to the host.

## Overview

`RecUpload` instructs the controller to stream all the metadata and the user-unit scaled recorded data for a scope. Unlike [RecDataA/RecDataB](RecDataA-RecDataB.md), which expose the raw, unconverted buffer, `RecUpload` applies unit conversions and returns the full data set. Each array index refers to a different scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

`RecUpload` can only be run after data recording is completed or stopped (see [RecStat](RecStat.md)).

## How it works

Over RS232 the data is returned as comma-delimited ASCII text. Over Ethernet each value is sent as a raw binary value followed by an ASCII comma; the value is 4 bytes wide in v4 (5-byte fields) and 8 bytes wide in v5 (9-byte fields). Over CAN each value is uploaded as a 5-byte message (4 bytes for the value, 1 byte for the ASCII comma) in both versions.

The first 80 values returned are the metadata. The subsequent values (81<sup>st</sup> value and above) are the recorded data, sequenced according to the [RecParamA/RecParamB](RecParamA-RecParamB.md) order, followed by the data sample order. For very large data sets, use [RecUploadNext](RecUploadNext.md) to retrieve the data in manageable packets.

`RecUpload` is only valid once the recording has finished. It returns an error if the scope is still recording (status 1, 2 or 3), if no recording has been made since power-up (status 0), or if the recording was stopped before the trigger fired (status 6, which has no valid triggered data). See [RecStat](RecStat.md) for the status values. On a triggered recording the captured area is a circular buffer, so the upload uses the stored start/trigger/end indices to read the samples out in true chronological order even when the data wraps within the buffer.

## Examples

![Example RecUpload console output: the metadata block followed by the recorded data values](../../assets/image77.png)

In the example, APosRef and AVel\[1\] are recorded. After the first 80 metadata values, the recorded data can be extracted as shown.

| Sample no. | APosRef | AVel[1] |
|---|---|---|
| 1 | 2 | 32768 |
| 2 | 4 | -65536 |
| 3 | 0 | 32768 |
| 4 | 2 | 0 |
| 5 | 2 | 65536 |
| and so on… | and so on… | and so on… |

## See also

- [RecUploadNext](RecUploadNext.md) — packetized upload for large data sets
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — raw, unconverted buffer
- [RecStat](RecStat.md) — recording status (must be completed/stopped)
- [RecParamA/RecParamB](RecParamA-RecParamB.md) — order of recorded parameters
