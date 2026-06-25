# 步进失步（堵转）保护

步进失步（堵转）保护用于检测步进电机（由内置驱动器驱动）何时与其指令电角度失去同步。每个控制周期都会将由相电压导出的实时度量值与一个与速度相关的阈值进行比较；当该度量值降至阈值以下时，判定电机发生堵转。

该保护仅作用于由内置驱动器驱动的步进电机——对于伺服电机及外部驱动器配置，不会生成该度量值，这些关键字处于无效状态。

- [StallCfg](StallCfg.md) — 主开关及处理方式：`0` 禁用，`1` 仅告警（设置 [StallStat](StallStat.md) 及 [StatReg](../../../07-status-and-faults/StatReg.md) 堵转位），`2` 在此基础上还会以 [ConFlt](../../../07-status-and-faults/ConFlt.md) ConFlt 代码 1065 禁用该轴。
- [StallVal](StallVal.md) — 只读实时度量值（经低通滤波的 $(V_a-V_c)^2+(V_b-V_c)^2$）。
- [StallTh](StallTh.md) — 只读、由固件计算的阈值（与速度相关，经低通滤波）。
- [StallThPcnt](StallThPcnt.md) — 用户设置的灵敏度（10–90 %）。
- [StallCnst](StallCnst.md) — 速度相关拟合的斜率/截距。
- [StallStat](StallStat.md) — 只读堵转标志（镜像 [StatReg](../../../07-status-and-faults/StatReg.md) bit 31）。

![步进失步检测示意图：健康状态下 StallVal 保持在 StallTh 线之上较高位置；当转子失步时，StallVal 降至 StallTh 以下，并按 StallCfg 采取相应的堵转处理](stall-detect.svg)

当 `StallVal < StallTh` 时判定为堵转。在模式 1 和 2 下，会设置 [StallStat](StallStat.md) 并设置 [StatReg](../../../07-status-and-faults/StatReg.md) bit 31（`0x80000000`）；在模式 2 下还会额外禁用该轴。当度量值恢复至阈值以上时，堵转位会自动清除。

当电机失能时，度量值、阈值和堵转标志都会复位为 `0`；在依赖该检测之前，请针对若干速度下的健康 `StallVal` 整定 [StallCnst](StallCnst.md)。
