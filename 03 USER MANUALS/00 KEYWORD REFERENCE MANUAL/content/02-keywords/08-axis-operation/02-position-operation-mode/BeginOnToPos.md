# BeginOnToPos

**Definition:**

BeginOnToPos is a one-time flag, which if set, will instruct the controller to perform a point-to-point motion upon entering position operation mode. After the motion, BeginOnToPos is cleared.

The target position is defined by RetractTarget or RelTrgt, while velocity is defined by RetractSpeed. This flag only works for GoToPosMode command and internal switching algorithm. It will not work if OperationMode is changed manually.
