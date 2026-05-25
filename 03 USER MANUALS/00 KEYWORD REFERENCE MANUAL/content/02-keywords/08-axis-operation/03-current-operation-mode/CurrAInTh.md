# CurrAInTh

**Condition:**

It is used only while axis is in velocity or position operation mode (OperationMode = 2 or 3).

**Definition:**

CurrAInTh is the threshold <span class="mark">analog force feedback</span> value used in the second condition check to enter current operation mode. Analog force feedback is defined using AInMode and is represented by AInPort.

| Value | Descriptions |
|----|----|
| \< 0 | Second condition is fulfilled if analog force feedback \< CurrAInTh. |
| 0 | Second condition is not fulfilled. |
| \> 0 | Second condition is fulfilled if analog force feedback \> CurrAInTh. |

**Note:**

Entry into current operation mode still subjects to the first condition check. If the first and second conditions are fulfilled, axis enters current operation mode and CurrAInTh is cleared to 0 to avoid undesired future switching. User needs to reconfigure its value for next switch. See Current operation mode for the overview.
