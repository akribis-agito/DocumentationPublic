# 复合 CAN 码

复合 CAN 码是一个唯一的 32 位整数标识符，用于标识与轴相关、与索引相关的 Agito 关键字。

复合 CAN 码的各位被划分为以下位字段：

| 复合码位字段 | 说明                                    |
|-------------------------|-------------------------------------------------|
| Bits \#0 – 9 (LSB)      | 关键字的 CAN 码                         |
| Bits \#10 – 14          | 轴号（0 表示第一个轴/轴“A”）  |
| Bits \#16 – 31          | 数组索引（若关键字为数组） |

例如，若要表示关键字 AInPort\[4\]（CAN 码 = 35，轴号 = 3（轴 D），数组索引 = 4），则复合 CAN 码 = 35 + (3\<\<10) + (4\<\<16) = 35 + 3 \* 2<sup>10</sup> + 4 \* 2<sup>16</sup> = 265251。

下表展示了 AInPort\[4\] 的复合 CAN 码。

**Combined**: `0x00040C23` = `265251`

以下是使用复合 CAN 码的变量。

| 序号 | 变量 | 类别 |
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
