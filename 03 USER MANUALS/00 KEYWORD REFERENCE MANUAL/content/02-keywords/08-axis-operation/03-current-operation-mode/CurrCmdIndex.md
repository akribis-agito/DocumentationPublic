# CurrCmdIndex

**Condition:**

This keyword is only applicable when CurrCmdSrc = 1 or 2.

**Definition:**

CurrCmdIndex is the index of existing CurrCmdVal and CurrCmdHTime values in use.

CurrCmdIndex will reset to 1 only

1.  upon receipt of GoToCurrMode command,

2.  upon automatic condition switching, or

3.  upon digital input for switching to current operation mode.

This means if OperationMode is directly assigned, user can configure it to any initial value so that the reference table starts from desired CurrCmdVal and CurrCmdHTime pair.

%%
Note DN: User can overwrite CurrCmdIndex at any time under current operation mode. This will cause sudden switch of CurrCmdVal in use, without reset of CurrCmdCntr timer.
%%
