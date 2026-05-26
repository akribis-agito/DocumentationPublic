---
keyword: DOutSelect
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 314
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 17
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 15
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutSelect

**Definition:**

DOutSelect assigns specific hardware functions to digital outputs via a multiplexer.

Each index in DOutSelect corresponds to one output (1-based index).

| Index | Corresponds to |
|-------|----------------|
| 1     | Output 1       |
| 2     | Output 2       |
| 3     | Output 3       |
| …     | …              |

The following table shows the DOutSelect multiplexer options.

| DOutSelect\[Index\] | Standalone     | Central-I slaves                 |
|---------------------|----------------|----------------------------------|
| 0                   | Using DOutMode | Using DOutMode                   |
| 1                   | Reserved       | Reserved                         |
| 2                   | A event \#1    | Main event \#1                   |
| 3                   | A event \#2    | Main event \#2                   |
| 4                   | A event \#3    | Main event \#3                   |
| 5                   | B event \#1    | Aux. event \#1 (Not implemented) |
| 6                   | B event \#2    | Aux. event \#2 (Not implemented) |
| 7                   | B event \#3    | Aux. event \#3 (Not implemented) |
| 8                   | C event \#1    | Pulse (P/D control)              |
| 9                   | C event \#2    | Direction (P/D control)          |
| 10                  | C event \#3    | Reserved                         |
| 11                  | UserPWM 1      | Reserved                         |
| 12                  | UserPWM 2      | UserPWM 1                        |
| 13                  | Reserved       | UserPWM 2                        |
| 14                  | Reserved       | Reserved                         |
| 15                  | Reserved       | Central-I Remote Signal          |

**Example:**

If DOutSelect\[3\] = 0, digital output 3 uses the function defined in DOutMode\[3\].

If DOutSelect\[4\] = 2, digital output 4 is assigned **Main Event \#1** (on Central-I products)

%%
Note DN: See chapter xxx for more information on UserPWM e.t.c.
%%
