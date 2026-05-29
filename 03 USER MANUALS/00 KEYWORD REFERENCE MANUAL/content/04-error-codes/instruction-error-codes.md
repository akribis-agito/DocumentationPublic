# Instruction error codes

*Error codes*

Controller will process instruction sent by through communication channel (AACommServer, used by PCSuite or other API). In case of invalid instruction, error code will be returned to the sender and be recorded at ErrLog.

The following is the list of instruction error codes and their descriptions.

| Error code | Descriptions |
|---|---|
| 0 | No fault has occurred |
| 1 | Message is too long |
| 2 | Illegal axis name in the first letter |
| 3 | Syntax error |
| 4 | Mnemonic too short |
| 5 | Closing bracket expected for array index |
| 6 | Array index value is invalid |
| 7 | Array index value is out of range |
| 8 | Assigned value not valid |
| 9 | Assigned value out of 32 bits range |
| 10 | Invalid character after ']' |
| 11 | Unexpected character: '=' or '[' expected |
| 12 | Mnemonic too long |
| 13 | Mnemonic not found in built in keywords table |
| 14 | Assigned value out of the range defined for this keyword |
| 15 | The number of received bytes is unexpected |
| 16 | Header must be 0 |
| 17 | Recorded data not valid after power up |
| 18 | Still recording, cannot upload or start recording |
| 19 | Cannot start recording of 0 or negative length |
| 20 | Index is larger than max allowed index for this keyword |
| 21 | The parameter assignment or function call are not valid during motion |
| 22 | The parameter assignment or function call are not valid with motor on |
| 23 | Trying to assign value to a read only parameter |
| 24 | This keyword requires array index |
| 25 | This keyword does not require an array index |
| 26 | During save to flash could not unlock |
| 27 | Could not erase flash |
| 28 | Error writing to flash |
| 29 | Flash full, not all parameters were saved |
| 30 | Flash checksum verification during load failed |
| 31 | Can't turn motor on if commutation was not found yet |
| 32 | Unexpected data encountered while loading from flash |
| 33 | Can't start recording because one or more of the requested parameters is a<br> function |
| 34 | Number of parameters in RecLength exceeds the recording array size |
| 35 | RecTrigMask = 0 will not enable recording to begin |
| 36 | RecStop was activated before a recording was started |
| 37 | RecTrigSrc is a function |
| 38 | RecStop stopped recording before trigger. Data incomplete |
| 39 | Can't start motion if motor is off |
| 40 | Motion mode not supported yet by this firmware version |
| 41 | Can't begin motion when already in motion |
| 42 | A line checksum error encountered during firmware download |
| 43 | An unexpected character was received during firmware download |
| 44 | Wrong number of characters in download file line |
| 45 | An address within the download file falls out of range |
| 46 | Wrong password entered. Download firmware process aborted |
| 47 | Timeout during firmware download process |
| 48 | Trying to begin motion with invalid motion mode value |
| 49 | Wrong index in recording parameter |
| 50 | This function keyword requires a parameter |
| 51 | This function keyword does not require a parameter |
| 52 | The numeric stack of the user program is full |
| 53 | Trying to pop from an empty stack. Please contact agito to debug! |
| 54 | Pointer to numeric stack is out of range |
| 55 | The user program thread indicated is out of range |
| 56 | Math function was called without enough data in stack |
| 57 | Math function called with divisor 0 |
| 58 | The result of the math function exceeds the allowed numeric range |
| 59 | Trying to access a location beyond the full area of the stack |
| 60 | Math operation requested does not exist |
| 61 | Negative power not implemented yet |
| 62 | Negative value entered to square root operation |
| 63 | MATH function not yet implemented |
| 64 | Recording trigger source can't be a function |
| 65 | Recording parameter from a non valid axis |
| 66 | Recording parameter with CAN code out of range |
| 67 | Recording gap out of range |
| 68 | Recording trigger source from an invalid axis |
| 69 | Recording trigger source with a CAN code out of range |
| 70 | Wrong index in recording trigger source |
| 71 | Recording trigger position out of range |
| 72 | Recording trigger type out of range |
| 73 | One of the ECAM table indexes into GenData[] is zero |
| 74 | The ECAM table indexes are not organized in growing values |
| 75 | The ECAM (master) gap has an illegal value of zero |
| 76 | The ECAM number of requested cycles has an illegal value of zero |
| 77 | ECAM, Gear master or virtual encoder source with a CAN code out of range |
| 78 | ECAM, Gear master or virtual encoder source from an invalid axis |
| 79 | Wrong index in ECAM, Gear master or virtual encoder source |
| 80 | ECAM, Gear master or virtual encoder source can't be a function |
| 81 | ECAM required range of master is outside of the limits of +/-2,000,000,000 |
| 82 | ECAM table includes at least two consecutive values that differs too much<br> from each other |
| 83 | Assigning a value to position is not allowed while Error Mapping is activated |
| 84 | Assigning a value to position is not allowed while Auto-Gain is activated |
| 85 | Assigning a value to position, while motor is on, is not allowed while Input<br> Shaping is activated |
| 86 | Can't enable motor if the initial delay is not completed |
| 87 | Can't enable motor if CalcFilters failed |
| 88 | Out of range filter definitions, at velocity filter number 1 |
| 89 | Out of range filter definitions, at velocity filter number 2 |
| 90 | Out of range filter definitions, at velocity filter number 3 |
| 91 | Out of range filter definitions, at velocity filter number 4 |
| 92 | Out of range filter definitions, at velocity filter number 5 |
| 93 | Out of range filter definitions, at velocity filter number 6 |
| 94 | Out of range filter definitions, at velocity filter number 7 |
| 95 | Out of range filter definitions, at position filter number 1 |
| 96 | Out of range filter definitions, at position filter number 2 |
| 97 | Out of range filter definitions, at position filter number 3 |
| 98 | Out of range filter definitions, at position filter number 4 |
| 99 | Out of range filter definitions, at position filter number 5 |
| 100 | Out of range filter definitions, at position filter number 6 |
| 101 | Out of range filter definitions, at position filter number 7 |
| 102 | Can't enable motor if filters were modified and CalcFilters was not executed |
| 103 | CalcIden can't perform calculations since recording length is out of min. or<br> max. ranges |
| 104 | CalcIden can't perform calculations since number of recorded parameters is<br> not two |
| 105 | Can't push since FIFO is full |
| 106 | Currently, in FIFO mode, acceleration can't be smaller than 1/Ts |
| 107 | Can't start FIFO motion if the FIFO is empty |
| 108 | Can't start FIFO motion if the first entry in the FIFO is not a definition of FIFO<br> cycle time |
| 109 | Can't start motion by user request while Homing is in process |
| 110 | There is no user program in the flash |
| 111 | This keyword can only be used in a user program |
| 112 | The user program call stack is full |
| 113 | The user program call stack is empty |
| 114 | Can't start motion by user request while Static Brake is locked |
| 115 | Trying to do indirect assignment into unknown array. Check IndirectArray<br> value |
| 116 | Trying to do indirect assignment with index out of range for the selected array.<br> Check IndirectIndex |
| 117 | Trying to push CNC FIFO type which is out of the allowed range |
| 118 | Trying to push CNC FIFO type but number of involved axes is out of range |
| 119 | Trying to push CNC FIFO type but at least one of the involved axes is out of<br> range |
| 120 | Trying to push CNC FIFO type but the involved axes are not organized properly |
| 121 | Trying to push CNC FIFO type but the involved axes include duplicated axis<br> in use |
| 122 | Trying to push CNC FIFO type but we didn't complete pushing parameters to<br> previous segment |
| 123 | Trying to push CNC FIFO type but we do not have enough space in CNC FIFO<br> at this time |
| 124 | Trying to push parameter into CNC FIFO but there is no open segment to get<br> this parameter |
| 125 | FIFO is empty, can't perform requested operation |
| 126 | Segment is in use (now in motion), so can't remove it |
| 127 | Trying to begin CNCA, but it is already in use |
| 128 | Trying to start CNC motion but the FIFO is empty |
| 129 | Pushed CNC segment has Speed parameter out of range |
| 130 | Pushed CNC segment has Radius mismatch (center to start point vs. center<br> to end point) |
| 131 | Pushed CNC segment has Direction parameter out of range |
| 132 | Pushed CNC segment has Pitch parameter out of range |
| 133 | Pushed CNC segment has Delay parameter out of range |
| 134 | Pushed CNC segment has Speed Percent parameter out of range |
| 135 | Pushed CNC segment has Acceleration parameter out of range |
| 136 | Pushed CNC segment has Deceleration parameter out of range |
| 137 | Pushed CNC segment has Jerk parameter out of range |
| 138 | Pushed CNC segment has Corner Radius (or Error) parameter out of range |
| 139 | This type of segment can't be the first motion segment of a CNC motion |
| 140 | This type of segment can be used only as the first segment of a CNC motion |
| 141 | The first segment is Set Positions, but it is not referring exactly to the list of<br> member axes |
| 142 | The first segment is Set Positions, but its values does not match the current<br> positions |
| 143 | ARC segment center definition gives different radiuses to start and end points |
| 144 | Helix segment center definition gives different radiuses to start and end<br> points |
| 145 | Helix segment definitions create inconsistent end point |
| 146 | An error occurred in RJ45 RS232 receive |
| 147 | An error occurred in mini USB RS232 receive |
| 148 | Reserved, contact Agito |
| 149 | Reserved, contact Agito |
| 150 | UPM Repetitive function not done, for the motion length plus extended UPMRptTime out of memory |
| 151 | Error in remote Central-i unit communication |
| 152 | The detected Central-i device type is not the same as the user entered |
| 153 | The Central-i transmit buffer is full |
| 154 | Central-i background offline message timed out |
| 155 | internal logic of extended protocol, no need to display ... |
| 156 | Can't start a motion while not in Position Operation Mode |
| 157 | Can't GoToPosMode from Velocity Operation Mode. Only from Current<br> Operation Mode |
| 158 | The requested connection is already active |
| 159 | This request is valid only for active (connected) Central-i ports |
| 160 | First type non zero and is currently not supported |
| 161 | Can't begin a motion if the final target position is outside of the software<br> position limits, RevPLim or FwdPLim |
| 162 | Can't begin a motion if we are inside RLS (or FLS) and the direction of the<br> motion is into the limit |
| 163 | Can't assign a position value that is outside the software position limits<br> (RevPLim to FwdPLim) |
| 164 | Can't start a motion at this motion mode if outside of the software position<br> limits. Use PTP, Jogging of Velocity Joystick modes |
| 165 | Can't find the requested task number |
| 166 | Can't find the requested function number |
| 167 | Operation not allowed when this thread is already running |
| 168 | Operation not allowed when any of the threads is running |
| 169 | Can't run user program: end of user program has been reached |
| 170 | Can't connect an amplifier to this port |
| 171 | Wrong user program checksum |
| 172 | Index for UserParam/GenData within CNC segment is out of range |
| 173 | Axis for DOutPort assignment within CNC segment is out of range |
| 174 | Value for DOutPort assignment within CNC segment is out of range |
| 175 | The device is not an amplifier. Keyword use not relevant |
| 176 | The amplifier current is different from DSP support |
| 177 | An unexpected character was received during user program download |
| 178 | A Keyword of property Func attribute type was inquired but is not supported<br> by AllStat |
| 179 | Communication type for executed keyword is not supported by the currently<br> connected connection type |
| 180 | Total received bytes by controller do not match the number of bytes that are<br> expected |
| 181 | The number of received parameters does not match the specified type |
| 182 | The user program call stack was found to be full while trying to call an event<br> function |
| 183 | Can't find the requested event function number |
| 184 | This keyword is not supported as part of Bulk Messaging |
| 185 | It is not allowed to push a keyword of type Function into the stack |
| 186 | The relay of the remote amplifier is still open |
| 187 | Can't GoToForceMode from Current Operation Mode. Only from Position or<br> Velocity Operation Modes |
| 188 | Pushed CNC segment has Number of Full Cycles parameter out of range<br> (must be 0 or positive) |
| 189 | Relative/Absolute as first segment of a CNC motion can't set Absolute mode |
| 190 | This CNC is in motion. Can't clear the CNC FIFO. |
| 191 | Can't go to Current or Force mode when in CNC motion |
| 192 | The VecMemberAxes parameter must include the axis to which Begin is sent<br> for vector motion |
| 193 | The motor of one of the vector member axes, as defined by VecMemberAxes,<br> is not enabled |
| 194 | One of the vector member axes, as defined by VecMemberAxes, is not in<br> vector motion mode |
| 195 | One of the vector member axes, as defined by VecMemberAxes, is already in<br> motion |
| 196 | Not enough vector member axes (VecMemberAxes must define at least two<br> member axes) |
| 197 | Vector ARC mode is valid only with exactly two member axes |
| 198 | Vector ARC center definition gives different radiuses to start and end points |
| 199 | Can't begin a motion if the final target position (for one of the member axes)<br> is outside of the software position limits, RevPLim or FwdPLim. Or, for ARC<br> type, if one of the members is now outside of position software limit |
| 200 | Can't begin a motion if we are inside RLS (or FLS) and the direction of the<br> motion (for one of the member axes) is into the limit. Or, for ARC type, if one<br> of the members is now inside a limit switch |
| 201 | Array selection for UserParam/GenData within CNC segment is out of range |
| 202 | Axis selection for UserParam/GenData within CNC segment is out of range |
| 203 | Trigger type of Wait Array CNC segment is out of range |
| 204 | The last motion segment has a non zero end speed and this segment can't<br> continue it (not the same involved axes or a motion-blocking segment) |
| 205 | Pushed CNC segment has Corner Type parameter out of range |
| 206 | Pushed CNC segment has Corner Axis Acceleration parameter out of range |
| 207 | Pushed CNC segment has Minimal Angle For Corner parameter out of range |
| 208 | Automatic Corner Motion segment is not allowed after the first Linear Motion<br> segment if Set Initial Positions segment is not used |
| 209 | Automatic Corner Motion segment must have all its dummy parameters with<br> value of zero |
| 210 | Automatic Corner Motion segment must appear following a Linear Motion<br> segment with 2 axes (non-motion segments are ignored) |
| 211 | Not enough arguments in the Call stack (consult Agito) |
| 212 | PeakTime, ContCL or PeakCL must not be zero |
| 213 | Encoder type is not supported by this product |
| 214 | To change CIDeviceType or AmpType first disconnect the active unit |
| 215 | The value entered in PStatParams is invalid |
| 216 | Device type is PWM amplifier and ampType is analog or adapter with PWM<br> ampType |
| 217 | Input Shaping frequency is out of range |
| 218 | Input Shaping parameters do not match. Please review the manual |
| 219 | Can't perform event correction if the error mapping is not activated |
| 220 | Can't perform event correction if first error mapping encoder is not the main<br> encoder of this axis |
| 221 | Can't perform event correction if the other axes are not enabled or are in<br> motion |
| 222 | Can't perform event correction if the other axes are not using their main<br> encoders |
| 223 | Indirect accessing of a controller parameter (pointer) for reading, does not<br> point to a legal parameter |
| 224 | The numeric stack does not have enough free space for the returned<br> arguments (consult Agito) |
| 225 | Event function with input and/or output arguments is not allowed (consult<br> Agito) |
| 226 | Pushed CNC segment has Corner Radius Method parameter out of range |
| 227 | Pushed CNC segment has Axis Acceleration Limit Type parameter out of range |
| 228 | Pushed CNC segment has Maximal Axis Acceleration parameter out of range |
| 229 | Pushed CNC segment has Axes Velocity Jump Mode parameter out of range |
| 230 | Pushed CNC segment has Axes Velocity Maximal Jump parameter out of<br> range |
| 231 | User1 debug mode, controller received an incoming 0x13 command with<br> keyword that is not supported within command 0x13 |
| 232 | This keyword is not supported in FW versions for User1 |
| 233 | This keyword is supported only for User1 special product |
| 234 | At least one of the plant model entries is illegal |
| 235 | Download Firmware is only available via Ethernet connection |
| 236 | No valid plant model (PlantModel[]) for UPM Repetitive calculation |
| 237 | This functionality is not yet supported by this FW version |
| 238 | The remote CAN Access failed due to time-out when waiting for send or receive to/from the remote unit |
| 239 | The remote CAN Access replied with an error (error code is stored at RemoteCANVal) |
| 240 | The remote CAN Access receive a reply it can't interpret |
| 241 | The overall (sum) of continuous current limitation (ContCL) of all axes is too high (greater than 28,000mA) |
| 242 | This function is not supported in this controller type |
| 243 | Download FPGA encountered an unknown FPGA type |
| 244 | A faulty FPGA has been detected. try to re-download the FPGA code, or consult Agito support |
| 245 | The FPGA in this unit does not match the FW (variant and full scale), consult Agito support |
| 246 | Out of range filter definitions, at CNC/Vector position filter |
| 247 | A parameter (one of: enable/disable, filter type, filter parameters) within CNC 'Modify CNC Position Filter' segment is out of range |
| 248 | This communication channel is blocked due to LCU mode |
| 249 | Trying to begin CNCB, but it is not supported in this product |
| 250 | The FPGA in this unit does not match this new FW (support for large arrays), consult Agito support for newer FPGA version |
| 251 | You are running a single flash FW on double flash board. Please download a correct version |
| 252 | You are running a double flash FW on single flash board. Please download a correct version |
| 253 | First entry of BuffTime[] should not be zero |
| 254 | Can't find a zero value in BuffTime[] to indicate end of valid values |
| 255 | BuffTime[] must include time values that are monotonously growing |
| 256 | The cycle time is longer than the available memory in internal buffers |
| 257 | The primary axis (used to send the BuffCalc) must be a member axis (defined by the index of BuffCalc[&lt;index&gt;]) |
| 258 | Begin command must be sent to the primary axis as was defined during BuffCalc |
| 259 | One or more of the spline buffer raw data parameters (BuffTime, BuffPos, BuffSplineMod...) were modified (or after power on or load from Flash) and BuffCalc was not executed to update internal buffers |
| 260 | One or more of the members axes, as was defined during BuffCalc is not ready for the motion (must be enabled and MotionMode=18 and not in motion) |
| 261 | One or more of the members axes, as was defined during BuffCalc is already moving member of another Spline Buffer motion |
| 262 | Arc center definition gives different radiuses to start and end points |
| 263 | Vector Arc direction parameter is out of range |
| 264 | Vector speed parameter out of range |
| 265 | Arc has Number of Full Cycles parameter out of range (must be 0 or positive) |
| 266 | The master vector axis must be the smallest member axis (A &lt; B &lt; C ...) |
| 267 | ModRev value is out of SW position range |
| 268 | The FPGA in this unit does not match this new FW (New dynamic braking implementation), consult Agito support for newer FPGA version |
| 269 | Speed can't be set higher than MaxVel |
| 270 | MaxVel can't be set lower than Speed |
| 271 | Can't start a motion if the desired maximal speed of the motion command (Speed) is higher than the MaxVel limitation |
| 272 | The EtherCAT is not synchronized or is not in the suitable motion mode (CSP) |
| 273 | Trying to push an item into the internal FIFO buffer of FIFO Position Tracking mode, but it is full |
| 274 | 3D ARC must have 3 non-collinear points to define the trajectory of the ARC |
| 275 | ConFlt Snapshot parameter with invalid CAN code |
| 276 | ConFlt Snapshot parameter with invalid axes |
| 277 | ConFlt Snapshot parameter with invalid index |
| 278 | ConFlt Snapshot parameter can't be function |
| 279 | ProgSnap Snapshot parameter with invalid CAN code |
| 280 | ProgSnap Snapshot parameter with invalid axes |
| 281 | ProgSnap Snapshot parameter with invalid index |
| 282 | ProgSnap Snapshot parameter can't be function |
| 283 | Selection between DInPort/AinPort within CNC segment is out of range |
| 284 | Axis selection for DInPort/AinPort within CNC segment is out of range |
| 285 | Trigger type of Wait Input CNC segment is out of range |
| 286 | Index for AInPort within CNC segment is out of range |
| 287 | The ASCII bulk message is too long |
| 288 | 3D Arc feature is supported for Central-i products only |
| 289 | Variable type mismatch (long / float) |
| 290 | Math operation input out of range (log of negative, etc.) |
| 291 | CNC segment is too short. Please reduce the End speed of previous segment or increase the target of the current segment |
| 292 | Can't start a motion after gantry on/off. Wait ~40msec after the transition |
| 293 | This communication channel is blocked due to Panel mode |
| 294 | There is no valid Draw Control project, or no draw control function for this scheme |
| 295 | Trying to use draw control but there is no draw control project or scheme for this axis. Consult Agito. |
| 296 | Trying to assign DrawMode that is different from the one set in the scheme. |
| 297 | Download or erase a Draw Control project is supported over Ethernet only. |
| 298 | Download or erase a Draw Control project while one of the schemes is not in DrawMode equal 0 or -1. |
| 299 | Wrong password entered. Download draw control process aborted |
| 300 | Timeout during draw control download process |
| 301 | This Draw Control functionality is allowed only for AGM800 |
| 302 | Draw Control download failed as AZDoNotUse[] items are not properly configured. Call Agito. |
| 303 | Gantry with dual loop is not allowed when DualLoopOn is not zero |
| 304 | Access to 64 bits keywords is not allowed over CAN Bus |
| 305 | The referenced keyword must be of type Long64 |
| 306 | This keyword is not allowed if the axis is in motion of type CNCA or CNCB or Vector |
| 307 | This keyword is allowed only when the axis is in Position Operation Mode |
| 310 | Dual-loop is not allowed when Gantry with dual-loop is on |
| 311 | Trying to set Speed, or Accel or Decel, outside the limits defined by Orbit FR for this system |
| 312 | Pushed CNC segment has Axis parameter out of range |
| 313 | Pushed CNC segment has Event Pulse Resolution parameter out of range |
| 314 | Pushed CNC segment has Event Pulse Width parameter out of range |
| 315 | Pushed CNC segment has Event Type parameter out of range |
| 316 | Pushed CNC segment has Event Select parameter out of range |
| 317 | Pushed CNC segment has Pos Event Source (see EncSinCosHWEn) parameter out of range |
| 318 | Pushed CNC segment has EventTableEnd parameter out of range |
| 319 | Pushed CNC segment has Is Pre Configured Table parameter out of range |
| 320 | Pushed CNC segment has EventTableBeg parameter out of range |
| 321 | Pushed CNC segment has Invalid EventTable |
| 322 | Pushed CNC segment has non-zero dummy parameter |
| 323 | The ECAMMasterIni parameter is out of the master range for one ECAM cycle |
| 324 | Can't start a motion if the desired maximal acceleration of the motion command (Accel) is higher than the MaxAcc limitation |
| 325 | Out of range filter definitions, at Force filter number 1 |
| 326 | Out of range filter definitions, at Force filter number 2 |
| 328 | Setting Product Serial Number is not allowed without Elevated Permissions |
| 329 | SetPosition is not allowed for the Yaw axis in gantry mode |
| 330 | AbsTrgt out of range in the current ModShort Mode |
| 331 | Out of range filter definitions, at feedforward filter |
| 334 | Using LockEventInit when LockEventMode is 0 (backward compatible mode) makes no sense. Please check your lock/event configuration logic |
| 335 | Can't enable Lock or Event if LockEventMode is 1, and LockEventInit was not executed |
| 336 | DrawRunBack requested with axis letter with no scheme or no valid scheme related to it |
| 337 | DrawRunBack requested for scheme that is not defined for Background execution, see DrawMode |
| 338 | Global User Units feature is mutually exclusive with embedded controller user units. Please disable one of the scaling factors |
| 339 | Cannot start recording without any parameter to record |
| 340 | UPMRptCalc is not allowed when UPM state is not Idle. Please check the UPMState before calling UPMRptCalc |
| 380 | Total stroke cannot be zero |
| 381 | Total stroke and cruise stroke must be in the same direction |
| 382 | Speed defined cannot be zero |
| 383 | Total stroke must be higher than pre-cruise stroke |
| 384 | Pre-cruise stroke is insufficient to achieve cruise velocity |
| 385 | Stopping stroke is insufficient to achieve zero velocity |
| 386 | Profile calculation has no solution |
| 387 | Waiting time for background calculation is longer than remaining motion/dwell time |
| 388 | Waiting time for background calculation too short as recalculation is not finished by the waiting time |
| 800 | The parameter assignment or function call are not valid with one of SparkOn[x] on |
