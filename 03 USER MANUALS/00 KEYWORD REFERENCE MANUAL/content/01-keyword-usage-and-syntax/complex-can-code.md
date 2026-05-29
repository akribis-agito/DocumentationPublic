# Complex CAN code

Complex CAN code is a unique, 32-bit integer identifier used to identify the axis-specific and index-specific Agito keywords.

The complex CAN code bits are divided into the following bit fields:

| Complex code bit fields | Descriptions                                    |
|-------------------------|-------------------------------------------------|
| Bits \#0 – 9 (LSB)      | CAN code of the keyword                         |
| Bits \#10 – 14          | Axis number (0 represents first axis/axis “A”)  |
| Bits \#16 – 31          | Index of the array (if the keyword is an array) |

For example, if keyword AInPort\[4\] is to be represented (CAN code = 35, axis number = 3 (axis D), array index = 4) , then complex CAN code = 35 + (3\<\<10) + (4\<\<16) = 35 + 3 \* 2<sup>10</sup> + 4 \* 2<sup>16</sup> = 265251.

The following table illustrates the complex CAN code of AInPort\[4\].

**Combined**: `0x00040C23` = `265251`

The following are variables that utilise complex CAN code.

| No. | Variables | Category |
|-----|-----------|----------|
| 1 | [AOutMode](../02-keywords/05-inputs-outputs/03-analog-outputs/AOutMode.md) | Inputs / Outputs |
| 2 | [GearMaster](../02-keywords/10-motion/07-motion-mode-gear-motion/GearMaster.md) | Motion / Gear |
| 3 | [ECAMMaster](../02-keywords/10-motion/08-motion-mode-electronic-cam-ecam/ECAMMaster.md) | Motion / ECAM |
| 4 | [RecParam](../02-keywords/19-data-recording/RecParam.md) | Data Recording |
| 5 | [RecParamA / RecParamB](../02-keywords/19-data-recording/RecParamA-RecParamB.md) | Data Recording |
| 6 | [RecTrigSrc](../02-keywords/19-data-recording/RecTrigSrc.md) | Data Recording |
| 7 | [LoggerParams](../02-keywords/19-data-recording/LoggerParams.md) | Data Recording |
| 8 | [VEncSrc](../02-keywords/03-encoder/06-virtual-encoder/VEncSrc.md) | Encoder |
| 9 | [ConFltSnapSrc](../02-keywords/07-status-and-faults/ConFltSnapSrc.md) | Status & Faults |
| 10 | [ProgEventPar](../02-keywords/17-user-program/02-program-execution/ProgEventPar.md) | User Program |
| 11 | [ProgSnapSrc](../02-keywords/17-user-program/02-program-execution/ProgSnapSrc.md) | User Program |
| 12 | [PushParam](../02-keywords/17-user-program/03-stack-operation/PushParam.md) | User Program |
| 13 | [PopParam](../02-keywords/17-user-program/03-stack-operation/PopParam.md) | User Program |
| 14 | [RemoteCANCCC](../02-keywords/01-system/04-communication/RemoteCANCCC.md) | System / Communication |
