# Controller error codes

*Error codes*

While controller is operating, it may encounter fault that disables the axis. The error code is assigned to [ConFlt](../02-keywords/07-status-and-faults/ConFlt.md) and recorded at ErrLog.

The following is the list of controller error codes and their descriptions.

| Error code | Descriptions |
|---|---|
| 0 | No error |
| 1001 | Abort signal was detected |
| 1002 | Short from motor phase to ground |
| 1003 | The encoder is disconnected |
| 1004 | FPGA watchdog not received |
| 1005 | PWM dead time too short |
| 1006 | Hall input disconnected |
| 1007 | Motor is stuck |
| 1008 | Bus Voltage too high |
| 1009 | Bus Voltage too low |
| 1010 | Logic Voltage too high |
| 1011 | Logic Voltage too low |
| 1012 | Bus current too high |
| 1013 | Phase A current too high |
| 1014 | Phase B current too high |
| 1015 | Phase C current too high |
| 1016 | Motor current too high |
| 1017 | Driver power exceeds limit |
| 1018 | IPM temperature too high |
| 1019 | Velocity too high |
| 1020 | Position error exceeds limit |
| 1021 | Velocity error exceeds limit |
| 1022 | CPU temperature too high |
| 1023 | Bus Voltage too high - exceed absolute limitation |
| 1024 | STO1 activated |
| 1025 | Over current detected |
| 1026 | Auxiliary encoder disconnected |
| 1027 | IPM fault |
| 1028 | The selected encoder type is currently not supported |
| 1029 | The selected auxiliary encoder type is currently not supported |
| 1030 | The ECAM master variables changed more than 1 ECAM cycle in 1 sample |
| 1031 | The FIFO reached a motion segment which results with a too small acceleration:<br> below 1/Ts |
| 1032 | The main encoder modulus can't be used with input shaping feature |
| 1033 | Some fault was detected during power on BIT. Use BITFault to read its code |
| 1034 | STO2 activated or problem with Vcc of amplifier |
| 1035 | AC Power supply to the control was cut off |
| 1036 | Over current detected on motor B |
| 1037 | Over continuous current detected on built-in Linear Amplifier |
| 1038 | Over voltage detected by the built-in Linear Amplifier |
| 1039 | AAmpType and BAmpType have conflicting values. Can not be one Linear and<br> one PWM |
| 1040 | Motor temperature too high |
| 1041 | Unexpected error code, consult Agito |
| 1042 | Amplifier isolated 5v fault |
| 1043 | CI Communication was disconnected |
| 1044 | Motor current over I2T |
| 1045 | Force error exceeds limit |
| 1046 | Force control: analog force feedback not defined |
| 1047 | One of the 5v output pins for encoders or I/O activated the current limitation.<br> Check your HW connections! |
| 1048 | Other member axis got motor off |
| 1049 | Dual Loop high difference between velocities |
| 1050 | External fault input (e.g.: external drive) is activated |
| 1051 | Internal relay is still switched off. Try waiting more time after power on before<br> enabling the motor |
| 1052 | STO2 activated |
| 1053 | AmpType value not allowed for this product |
| 1054 | At least one required phase of the AC Power inputs was cut off. |
| 1055 | Position error exceeds limit in open-loop |
| 1056 | Velocity error exceeds limit in open-loop |
| 1057 | Force error exceeds limit in open-loop |
| 1058 | Undervoltage detected on 10.5 V supply (8 V threshold) |
| 1059 | Over current detected on motor C |
| 1060 | Product temperature (BoardTemp) too high |
| 1061 | Other gantry member axis got motor off |
| 1062 | External request to fault with controlled stop: stop ended and motor was disabled |
| 1063 | Other member axis got motor off |
| 1064 | Error in the encoder sine/cosine reading |
| 1065 | Stall detection activated, motor is turning off |
| 1066 | Virtual encoder has exceeded the max number of possible pulses per interrupt |
| 1067 | Anomaly/collision detected in the system (v5 only) |
| 1068 | Abs Encoder Error bit is asserted, either the assembly encoder readhead is not good, or the encoder scale needs to be inspected |
| 1069 | Abs Encoder CRC has failed beyond a time threshold set by EncAbsErrTime. The noise level might be too high |
| 1070 | Abs Encoder could not be detected and looks like is disconnected |
| 1071 | Unstable current loop detected (v5 only) |
| 1072 | High noise/jitter detected (v5 only) |
| 1080 | No phasing is detected (v5 only) |
| 1081 | CPU background loop watchdog timeout |
