---
summary: Pushes a complete CNC segment (type and parameters) in one Ethernet message.
---
# CNCAPushSeg/CNCBPushSeg

Pushes a complete CNC segment (type and parameters) in one Ethernet message.

## Overview

`CNCAPushSeg` (and its `CNCBPushSeg` counterpart on the second CNC engine) lets the host push a complete segment (type and parameters) into the CNC FIFO using a single Ethernet message. This replaces a sequence of messages consisting of [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) followed by multiple [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) writes as required for the segment type. As a result, it significantly improves the throughput of pushing segments into the CNC FIFO.

> **Note:** This keyword is supported only over an Ethernet communication connection to the controller. It returns an error if used over any other communication connection (such as RS232, CAN, etc.).

## Examples

```text
ACNCAPushSeg=...     ; push a full segment (type + parameters) over Ethernet
```

## See also

- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — select the segment type
- [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) — push individual segment parameters
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
