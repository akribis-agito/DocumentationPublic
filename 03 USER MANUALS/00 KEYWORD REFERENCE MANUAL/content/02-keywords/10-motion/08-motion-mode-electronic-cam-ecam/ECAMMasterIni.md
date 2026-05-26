---
keyword: ECAMMasterIni
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# ECAMMasterIni

**Definition:**

ECAMMasterIni denotes the offset of starting master value relative to the ECAM range upon start of ECAM motion. It is an array of size 10, where each element corresponds to a cam pattern.

ECAMMasterIni must be at least zero or positive. The value of ECAMMasterIni must be such that when the ECAM motion is started, the first repetition cycle is not exceeded.

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

Please refer to the figures in [Motion mode – Electronic cam (ECAM)](../../../02-keywords/10-motion/08-motion-mode-electronic-cam-ecam/00-overview.md) for more information on the initial offset, which varies in definition according to ECAMGap and ECAMCycles.
