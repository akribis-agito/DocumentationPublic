# GoToPosMode

**Definition:**

GoToPosMode command instructs the controller to enter position operation mode in a graceful manner. Position value (Pos) upon receipt of command is recorded in ModeSwitchPos keyword.

Through BeginOnToPos flag, user may choose to immediately start a point-to-point motion to target position (set by RetractTarget or RelTrgt) at a defined speed (RetractSpeed) upon receipt of GoToPosMode command.

**Note:**

GoToPosMode cannot be used if axis is in velocity operation mode (OperationMode = 1).
