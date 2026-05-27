---
keyword: ECAMMasterIni
summary: Offset of the starting master value relative to the ECAM range at start of motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 306
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# ECAMMasterIni

Offset of the starting master value relative to the ECAM range at start of motion.

## Overview

`ECAMMasterIni` denotes the offset of the starting master value relative to the ECAM range upon start of ECAM motion. It is an array of 10 cam patterns, one element per pattern. It positions where, within the cam range, the master begins when ECAM motion starts; its exact role depends on the sign of [ECAMGap](ECAMGap.md) and the value of [ECAMCycles](ECAMCycles.md).

`ECAMMasterIni` must be zero or positive, and small enough that the first repetition cycle is not exceeded when motion starts.

## How it works

The maximum allowed value depends on `ECAMCycles`:

| ECAMCycles | Maximum value of ECAMMasterIni                   |
|------------|--------------------------------------------------|
| 1          |                                                  
              ``` math                                          
              abs(ECAMGap)\ *\ (ECAMEnd\  - \ ECAMStart)        
              ```                                               |
| \> 1       |                                                  
              ``` math                                          
              abs(ECAMGap)\ *\ (ECAMEndCyc\  - \ ECAMStart)     
              ```                                               |
| \< 0       |                                                  
              ``` math                                          
              abs(ECAMGap)\ *\ (ECAMEndCyc\  - \ ECAMStartCyc)  
              ```                                               |

## Examples

```text
AECAMMasterIni[1]=0  ; start at the beginning of the ECAM range for cam pattern 1
AECAMMasterIni[1]   ; read current value
```

Refer to the figures in [Motion mode – Electronic cam (ECAM)](00-overview.md) for more information on the initial offset, which varies according to ECAMGap and ECAMCycles.

## See also

- [ECAMGap](ECAMGap.md) — spacing/direction of master values
- [ECAMCycles](ECAMCycles.md) — number of pattern occurrences
- [ECAMMaster](ECAMMaster.md) — selects the master variable
