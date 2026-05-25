# ForceCmdHTime

**Definition:**

If ForceCmdSrc is 0 (analog input), only ForceCmdHTime\[1\] is used to define the time to stay within force operation mode.

If ForceCmdSrc is 1 or 2, each ForceCmdHTime array element defines the holding time for the corresponding ForceCmdVal pair.

ForceCmdHTime value is defined as shown.

| Value | Descriptions |
|---|---|
| < 0 | Source value is held indefinitely. |
| 0 | Axis exits force operation mode and enters position operation mode. |
| > 0 | Source value is held for ForceCmdHTime, before exiting force operation mode (ForceCmdSrc = 0) or proceeding to the next pair (ForceCmdSrc = 1 or 2). For ForceCmdSrc is 1 or 2, if ForceCmdIndex reaches last index value and last ForceCmdHTime entry is more than 0, axis will hold onto the last ForceCmdVal value indefinitely. |
