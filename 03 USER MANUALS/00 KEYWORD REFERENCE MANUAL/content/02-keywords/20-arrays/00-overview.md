# Arrays

General arrays of various data types (GenData, GenDataD, GenDataF and GenDataLL) can be written and read by the user. Normally, they are not linked to any feature in the controller. Therefore, they can be used for

1.  User program (as program variables)

2.  Custom user functions within the firmware (as temporary variables)

3.  Debugging use

The user can set the value directly by a normal write operation, or indirectly by using the indirect-write function.

In contrast, user parameter arrays (UserParam, UserParamD, UserParamF, UserParamLL) are feature-related arrays, in which some of the array entries are used to store temporary variables. They are internally guaranteed to not be used by more than 1 feature at any time. For example, some UserParam entries are used in homing sequence and CNC motion variables. Therefore, it is not recommended to use user parameter arrays in the user program, custom functions or for debugging.
