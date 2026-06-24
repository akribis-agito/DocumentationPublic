---
summary: 按示波器分组的复合 CAN 代码数组，用于选择要捕获的参数。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RecParamA/RecParamB

按示波器分组的复合 CAN 代码数组，用于选择要捕获的参数。

## 概述

`RecParamA` 和 `RecParamB` 分别存储第一个和第二个示波器要捕获的参数的[复合 CAN 代码](../../01-keyword-usage-and-syntax/complex-can-code.md)数组。每个示波器最多可捕获 20 个参数。此处设置的捕获顺序决定了 [RecUpload](RecUpload.md) 和 [RecUploadNext](RecUploadNext.md) 返回数据的顺序。

## 工作原理

[RecStart](RecStart.md) 运行时，控制器从索引 1 扫描至 20。在独立控制器和 Central-i v4 上，每个非零条目均成为一个记录通道，零条目被跳过，因此数组中间的零不会终止列表——其后的条目仍会被记录。在 Central-i v5 上，扫描在第一个零处停止，因此仅记录从索引 1 开始的连续非零条目。为在各版本间保持一致行为，请保持列表连续，并将所有末尾索引设为零。数组中重复的复合 CAN 代码将导致重复捕获。

记录启动时，每个条目均经过验证。若代码不是有效关键字、指向命令而非参数（命令无法记录）、轴超出范围，或所指向的数组索引缺失或超出该关键字的范围，则该条目被拒绝（启动失败）。通道数乘以 [RecLength](RecLength.md) 的总采样数也必须在示波器缓冲区内，否则启动被拒绝。

此处设置的捕获顺序全程保留：它决定了采样在缓冲区中的交织方式以及 [RecUpload](RecUpload.md) 和 [RecUploadNext](RecUploadNext.md) 返回的列顺序。对于以用户单位存储的参数，控制器还在启动时记录每个通道的比例因子，以便上传时将原始采样转换回用户单位。

## 示例

| RecParamA 索引 | 1 | 2 | 3 | 4 | 5 – 20 |
|---|---|---|---|---|---|
| 值（复合 CAN 代码） | 1026 (BPos) | 66565 (BVel[1]) | 1050 (BCurrRef) | 0 | 0 |

以上述数组定义启动第一个示波器的记录后，BPos、BVel\[1\] 和 BCurrRef 均被捕获。

## 另请参见

- [RecUpload](RecUpload.md) — 按此顺序流式传输捕获数据
- [RecUploadNext](RecUploadNext.md) — 分包上传
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — 按示波器分组的原始缓冲区
- [RecStart](RecStart.md) — 参数设置完成后启动记录
