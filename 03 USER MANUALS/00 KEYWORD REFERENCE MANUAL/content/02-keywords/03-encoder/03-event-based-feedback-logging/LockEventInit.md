---
keyword: LockEventInit
summary: Learns the capture offset in manual mode 1 or automatic mode 2.
availability:
  standalone: []
  central-i:
  - v5
can_code: 832
attributes:
  access: ro
  scope: axis
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
last_updated: '2026-10-17'
doc_revision: '2026.10'
---
# LockEventInit

Learns the offset between the hardware ancillary capture counter and the matching controller position. It is required in manual [LockEventMode](LockEventMode.md) 1 and can force a fresh measurement in automatic mode 2. Mode 0 uses initialization on arming; calling this command there is refused with error 334.

Turn `LockEn` and `EventOn` off, finish configuring the source, and keep it stationary during measurement. The matching coordinates are `Pos` for the main incremental/AqB source, `VEncValue` for the virtual source, and `AuxPos` for the auxiliary source. A successful applicable measurement sets [LockEventStat](LockEventStat.md) to 1.

For the main absolute-encoder source, no ancillary offset is needed: the command can return success without changing the status. Therefore interpret status according to the selected source. A remote read failure returns error 151 and leaves the offset invalid. Modes 1/2 refuse arming with error 335 when no measurement exists, or 404 when an earlier measurement is stale.

## Remote FPGA compatibility

On AGM800 and AGM800-EC, the remote FPGA must implement ancillary-position reads `0x72/0x73`. Historical remote FPGA v4.3.6 does not implement them and returns zero for unmapped reads. A successful zero reply or `LockEventStat=1` on that image does not certify a correct offset. Use a firmware/FPGA combination validated together before relying on capture coordinates.

## Example

```text
ALockEn=0
AEventOn=0
ALockEventMode=1
; configure the capture source and keep it stationary
ALockEventInit
ALockEventStat        ; require 1 for an applicable ancillary-counter source
ALockEn=1
```

Mode 1 requires another explicit measurement after a dependency change or reconnect invalidates the offset. Mode 2 attempts automatic recomputation while both features are off; this command remains available for an explicit refresh. See [LockEventMode](LockEventMode.md) and [LockEventStat](LockEventStat.md).
