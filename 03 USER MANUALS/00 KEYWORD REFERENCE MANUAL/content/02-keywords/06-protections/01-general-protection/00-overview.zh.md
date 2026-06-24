# 通用保护

报告并配置驱动器硬件保护条件（过流、编码器故障、看门狗、STO/安全输入、缺失电源相等等）的关键字。

- [HWProtectBits](HWProtectBits.md) 是一个只读位域，报告硬件保护信号的实时状态。
- [ProtectMask](ProtectMask.md) 选择允许其中哪些条件禁用轴。掩码位置为 1 表示禁用（屏蔽）该保护；某些关键保护不可屏蔽，无法被禁用。

当出现已启用的保护条件时，轴被禁用，并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 上触发对应的故障码。
