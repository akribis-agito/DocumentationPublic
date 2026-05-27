---
summary: Selects the digital event source and trigger edge for feedback logging.
---
# LockSrc/AuxLockSrc

Selects the digital event source and trigger edge for feedback logging.

## Overview

`LockSrc` defines the source of the digital event that triggers event-based feedback logging, and its trigger edge. The sign of `LockSrc` selects the edge (positive for rising, negative for falling) and the absolute value selects the input source. It works together with [LockEn](LockEn-AuxLockEn.md) (to enable logging) and increments [LockCntr](LockCntr-AuxLockCntr.md) on each event. `AuxLockSrc` is the auxiliary-encoder counterpart.

`LockSrc` is stored in flash, so the trigger selection survives a power cycle; the source/edge are applied to the trigger hardware whenever `LockSrc` is written and whenever [LockEn](LockEn-AuxLockEn.md) is armed. The valid range is `-38` to `38`.

## How it works

The sign of `LockSrc` defines the trigger edge:

| Value | Trigger edge |
|-------|--------------|
| > 0   | Rising edge  |
| 0     | Main encoder index, rising edge (see below) |
| < 0   | Falling edge |

The absolute value of `LockSrc` determines the digital event source. The mapping varies by product.

### LockSrc = 0

`LockSrc=0` is a convenience setting that selects the **main encoder index of this axis** with normal (rising) polarity, without having to know the per-product index value. It is honoured on firmware/FPGA versions that advertise support for it; on older versions, use the explicit index value from the tables below instead (for example `32` on the standalone AGD101, or `16` on Central-i products).

For standalone products (non-Central-i):

| abs(Value) | AGD101 / AGD156 | AGD155 | AGD200 / AGC300 | AGD301 / AGC301 |
|:--:|:--:|:--:|:--:|:--:|
| 1 | Digital input 1 | Digital input 1 | Digital input 1 | Digital input 1 |
| 2 | Digital input 2 | Digital input 2 | Digital input 2 | Digital input 2 |
| 3 | Digital input 3 | Digital input 3 | Digital input 3 | Digital input 3 |
| 4 | Digital input 4 | Digital input 4 | Digital input 4 | Digital input 4 |
| 5 | Digital input 5 | Digital input 5 | Digital input 5 | Digital input 5 |
| 6 | Digital input 6 | Digital input 6 | Digital input 6 | Digital input 6 |
| 7 | Digital input 7 | Digital input 7 | Digital input 7 | Digital input 7 |
| 8 | Digital input 8 | Digital input 8 | Digital input 8 | Digital input 8 |
| 9 | Bidirectional differential digital I/O 1 (as digital input 9) | Digital input 9 | Digital input 9 | Digital input 9 |
| 10 | Bidirectional differential digital I/O 2 (as digital input 10) | Digital input 10 | Digital input 10 | Digital input 10 |
| 11 | Bidirectional differential digital I/O 3 (as digital input 11) | Digital input 11 | Digital input 11 | Digital input 11 |
| 12 | Bidirectional differential digital I/O 4 (as digital input 12) | Digital input 12 | Digital input 12 | Digital input 12 |
| 13 | - | Digital input 13 | - | Digital input 13 |
| 14 | - | Digital input 14 | - | Digital input 14 |
| 15 | - | Digital input 15 | Differential digital input 1 (as digital input 15) | Digital input 15 |
| 16 | - | Digital input 16 | Differential digital input 2 (as digital input 16) | Digital input 16 |
| 17 | - | Differential digital input 1 (as digital input 17) | Differential digital input 3 (as digital input 17) | Digital input 17 |
| 18 | - | Differential digital input 2 (as digital input 18) | Differential digital input 4 (as digital input 18) | Digital input 18 |
| 19 | - | Differential digital input 3 (as digital input 19) | Differential digital input 5 (as digital input 19) | Digital input 19 |
| 20 | - | Bidirectional differential digital I/O 1 (as digital input 20) | Differential digital input 6 (as digital input 20) | Digital input 20 |
| 21 | - | - | Differential digital input 7 (as digital input 21) | Digital input 21 |
| 22 | - | - | Differential digital input 8 (as digital input 22) | Digital input 22 |
| 23 | - | - | - | Digital input 23 |
| 24 | - | - | - | Digital input 24 |
| 25 | - | - | - | Digital input 25 |
| 26 | - | - | - | Digital input 26 |
| 27 | - | - | - | Digital input 27 |
| 28 | - | - | - | Bidirectional differential digital I/O 1 (as digital input 28) |
| 29 | - | - | - | Bidirectional differential digital I/O 2 (as digital input 29) |
| 30 | - | - | Axis C index | Axis C index |
| 31 | Auxiliary encoder index (from bidirectional differential digital I/O 4) | Auxiliary encoder index | Axis B index | Axis B index |
| 32 | Main encoder index | Main encoder index | Axis A index | Axis A index |
| 33 | - | - | - | Bidirectional differential digital I/O 3 (as digital input 30) |
| 34 | - | - | - | Bidirectional differential digital I/O 4 (as digital input 31) |
| 35 | - | - | - | Bidirectional differential digital I/O 5 (as digital input 32) |
| 36 | - | - | - | Bidirectional differential digital I/O 6 (as digital input 33) |
| 37 | - | - | - | Bidirectional differential digital I/O 7 (as digital input 34) |
| 38 | - | - | - | Bidirectional differential digital I/O 8 (as digital input 35) |

For Central-i products. The feedback logging feature is unavailable for the I/O units (AGIO01 and AGIO02) and the feedback unit (AGFB01).

| abs(Value) | AGA101 / AGA110 | AGA102 | AGA103 / AGL101 | AGA155 | AGL102 | AGL103 |
|---|---|---|---|---|---|---|
| 1 | Digital input 1 | Digital input 1 | Digital input 1 | Digital input 3 | Digital input 1 | Digital input 1 |
| 2 | Digital input 2 | Digital input 2 | Digital input 2 | Digital input 4 | Digital input 2 | Digital input 2 |
| 3 | Digital input 3 | Digital input 3 | Digital input 3 | - | Digital input 3 | Digital input 3 |
| 4 | Digital input 4 | Digital input 4 | Digital input 4 | - | Digital input 4 | Digital input 4 |
| 5 | Digital input 5 | Digital input 5 | Digital input 5 | - | Digital input 5 | Digital input 5 |
| 6 | Digital input 6 | Digital input 6 | Bidirectional differential digital I/O 1 (as digital input 6) | - | Digital input 6 | Bidirectional differential digital I/O 1 (as digital input 6) |
| 7 | Digital input 7 | Digital input 7 | Bidirectional differential digital I/O 1 (as digital input 7) | - | - | - |
| 8 | Digital input 8 | Bidirectional differential digital I/O 1 (as digital input 8) | - | - | - | - |
| 9 | Digital input 9 | - | - | - | - | - |
| 10 | Digital input 10 | - | - | Digital input 12 | - | - |
| 11 | Digital input 11 | - | - | Digital input 13 | - | - |
| 12 | Bidirectional differential digital I/O 1 (as digital input 12) | - | - | Digital input 14 | - | - |
| 13 | - | - | - | Digital input 15 | - | - |
| 14 | - | - | - | Bidirectional differential digital I/O 1 (as digital input 16) | - | - |
| 15 | Auxiliary encoder index | - | - | Auxiliary encoder index | - | Auxiliary encoder index |
| 16 | Main encoder index | Main encoder index | Main encoder index | Main encoder index | Main encoder index | Main encoder index |
| 17 | Event 1 | Event 1 | Event 1 | Event 1 | Event 1 | Event 1 |
| 18 | Event 2 | Event 2 | Event 2 | Event 2 | Event 2 | Event 2 |
| 19 | Event 3 | Event 3 | Event 3 | Event 3 | Event 3 | Event 3 |
| 20 | Central-i remote signal | Central-i remote signal | Central-i remote signal | Central-i remote signal | Central-i remote signal | Central-i remote signal |

### How the selection reaches the hardware

On **standalone** products the source/edge encode directly into the per-axis strobe-settings register that drives the encoder hardware capture (QEP strobe latch): the chosen input is multiplexed onto the strobe pin and the polarity bit sets rising vs. falling. The strobe pin is shared with event generation, so selecting a `LockSrc` and arming [LockEn](LockEn-AuxLockEn.md) takes ownership of that pin from event generation.

On **Central-i** products the source/edge are sent to the remote drive's FPGA lock-configuration registers (input-select bit-mask plus polarity). The remote FPGA performs the capture and the master reads back the latched position over the offline mailbox.

In both cases the absolute value is converted to a zero-based input index internally (value `1` → first input), so the tables above are the authoritative source-to-input mapping.

## Examples

```text
ALockSrc=32          ; main encoder index, rising edge (standalone AGD101)
ALockSrc=16          ; main encoder index, rising edge (Central-i)
ALockSrc=0           ; main encoder index, rising edge (where supported)
ALockSrc=-1          ; digital input 1, falling edge
ALockSrc              ; read back the configured source/edge
```

## See also

- [LockEn](LockEn-AuxLockEn.md) — enables event-based feedback logging
- [LockCntr](LockCntr-AuxLockCntr.md) — incremented on each `LockSrc` event
- [LockVal](LockVal-AuxLockVal.md) — feedback position logged on each event
