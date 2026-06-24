---
summary: 用于选择待记录参数的复合 CAN 码数组。
language: zh-CN
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# RecParam

用于选择待记录参数的复合 CAN 码数组。

## 概述

> **注意：** `RecParam` 在本参考手册所查阅的固件中不作为控制器关键字出现——控制器上仅提供按示波器区分的 [RecParamA/RecParamB](RecParamA-RecParamB.md) 变体。本页面保留用于说明旧版/单缓冲区名称；在直接使用 `RecParam` 之前，请对照当前固件确认其可用性。

`RecParam` 是一个数组，存储待记录参数（通道）的[复合 CAN 码](../../01-keyword-usage-and-syntax/complex-can-code.md)，最多可容纳 20 个参数。记录时从索引 1 开始按顺序遍历数组，并捕获非零条目。在较新固件中，扫描在遇到第一个零条目时停止，因此零值起终止作用；在较旧固件中，中间的零条目被跳过而非视为终止符，其后的非零条目仍会被记录。若要在任意固件版本上仅选择一个通道，可将其复合 CAN 码置于索引 1，其余条目保持为 0。如需在具有独立示波器缓冲区的产品上按示波器选择参数，请参见 [RecParamA/RecParamB](RecParamA-RecParamB.md)。

## 工作原理

执行 [RecStart](RecStart.md) 时，控制器从索引 1 开始扫描 `RecParam`，将每个非零复合 CAN 码解析为可记录通道。在较新固件中，扫描在遇到第一个零条目时停止；在较旧固件中，零条目被跳过，扫描继续遍历全部 20 个索引。无论哪种情况，将索引 1 设为目标值并将所有后续索引置为 0，均可仅记录该一个参数。通道数与 [RecLength](RecLength.md) 的乘积必须在示波器缓冲区容量内，否则启动将被拒绝。

每个已解析的通道在记录启动时进行验证。若 CAN 码不对应真实关键字、指向命令（命令不可被记录）、轴字母超出范围，或缺少数组索引或数组索引超出该关键字的范围，则该码将被拒绝。此处设置的顺序即为样本在缓冲区中的排列顺序，也是 [RecUpload](RecUpload.md) 返回数据的顺序。

## 示例

```text
ARecParam[1]=1026    ; 记录该参数
ARecParam[2]=0       ; 其余条目保持为 0（仅记录 RecParam[1]）
ARecParam[1]        ; 查询第一个已记录参数的 CAN 码
```

## 另请参阅

- [RecParamA/RecParamB](RecParamA-RecParamB.md) — 按示波器选择参数
- [RecData](RecData.md) — 原始记录值
- [RecUpload](RecUpload.md) — 流式传输经转换的用户单位数据
