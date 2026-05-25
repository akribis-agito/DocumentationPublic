# AInMode

AInMode is used to assign functionality to the analog inputs.

The input is selected by the Index. For example, AAInMode\[2\] defines the functionality for Analog Input 2 of Axis A. The axis reference here is only relevant for Central-i product with multiple IO modules on different axes

The functionality is selected by the lower 16 bits of Value. The list of functionalities is as per the table below.

| Lower 16-bit value | Functionality                        |
|--------------------|--------------------------------------|
| 0                  | General input – no function          |
| 1                  | Velocity command                     |
| 2                  | Current command                      |
| 3                  | Force feedback                       |
| 4                  | Force command                        |
| 5                  | Joystick input                       |
| 6                  | Torque compensation                  |
| 7                  | Negative current limit (for CurrRef) |
| 8                  | Positive current limit (for CurrRef) |
| 9                  | Tachometer feedback                  |
| 10                 | Position feedback                    |

The axes for which the functionality applies to is selected by the upper 16 bits of Value. Each bit represents a particular axis; multiple bits can be selected to apply the functionality to multiple axes.

The bit-field list of axes which to use the functionality (bits 16 to bits 23) is as shown below.

| Value, Bit# | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|
| Axis        | A   | B   | C   | D   | E   | F   | G   | H   |

**Example:**

If the analog input 2 of axis C is to be used as force feedback of axis A, then the command would be

$$
CAInMode\lbrack 2\rbrack\  = \ 3\  + \ 2\hat{}16\  = \ 65539
$$
