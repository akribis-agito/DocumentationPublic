---
keyword: DInMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 225
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 33
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DInMode

**Definition:**

DInMode assigns specific software functions to digital inputs.

Each index in DInMode\[\] corresponds to an input (1-based index).

| Index | Corresponds to |
|-------|----------------|
| 1     | Input 1        |
| 2     | Input 2        |
| 3     | Input 3        |
| …     | …              |

The functionality is selected by the Value (lower 16 bits). The list of functionalities is as per the table below.

**Note:**

1. When the input is low, control set 1 is used.
2. When the input is high, control set 2 is used.

The axes, for which the function **applies to**, is selected by the bit 16 to 27 of Value. Each bit corresponds to an axis; multiple axes can be selected.

| Axis        | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Value, Bit# | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  | 27  |

**Example:**

If CDInMode\[2\] = 65,546 (binary 00000000 00000001 00000000 00001010):

1.  Index → 2 (Digital Input 2)

2.  Value (bit 16 to 27) → bit 16 (Axis B)

3.  Value (lower 16-bits) → 10 (FLS)

Digital Input 2 (of Axis C) is used as Axis B FLS input.

**Note:**

1. It is highly recommended to save to flash ( Save ) and reset the controller ( Reset ) after making changes to DInMode[] since some of the special functionalities require power cycle to work (or to stop working) properly.
2. It is not allowed to set more than 20 special functions to the discrete inputs. In case more than 20 functions are set, only the first 20 will be operational. For example, if a special function is assigned to a given input and is applied on two axes, it is counted as 2 special functions.
3. The functionality is checked in ascending order of the array elements. Any subsequent digital inputs with duplicated functionality definition (except for the general-purpose input functionality) will be ignored/ineffective. For example, if DInMode[1] = 9 and DInMode[3] = 9, digital input 3 (corresponds to DInMode[3]) will be ignored and will not act a reverse limit switch input. No error message is thrown, but a warning will be shown on PCSuite.
