---
keyword: EncStatReg
summary: 只读状态寄存器，报告绝对式编码器的健康位（断开、错误、告警、CRC）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 422
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-18'
doc_revision: '2026.10'
language: zh-CN
---
# EncStatReg

只读、按轴提供的编码器状态。在 PCSuite 中可用 `AEncStatReg` 读取 A 轴状态。位布局及可用信息取决于控制器、FPGA 镜像和反馈类型；它不是通用的反馈有效性寄存器。

## Central-i 主反馈

对于主 BiSS-C、EnDat 和 Tamagawa 反馈，CI_MASTER 固件根据收到的远端输入合成状态。包含[状态报告修复](https://github.com/akribis-agito/Firmware-Main/issues/1273)的固件会在初始化窗口结束后，每次执行主绝对式编码器处理程序时刷新以下现有映射位。包含 [Tamagawa 启动修复](https://github.com/akribis-agito/Firmware-Main/issues/1452)的固件还会在活动标准 AMP 主 Tamagawa 的稳定等待期间报告同样的映射位：

| 位 | 掩码 | 收到的输入 |
|---|---|---|
| 0 | `0x01` | 远端主编码器保护指示；物理含义取决于协议和硬件。 |
| 1 | `0x02` | 远端状态字中现有错误或告警输入之一；两种输入合并报告。 |
| 4 | `0x10` | 远端状态字中现有 CRC 输入。 |

各映射位独立反映当前输入，包括同时发生的条件。条件恢复后对应位会清除，包括 CRC；寄存器其他位保持不变。状态报告不依赖 [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md)。此修复仅改变报告，保留现有计数、电机关闭、换相及外推策略。

这些名称描述的是固件映射，并不表示所有协议提供相同的物理证据。在 CIG1 的 Tamagawa completed-main 路径中，共享字段报告 CRC、协议错误和不可用。不可用合并了多种原因，包括自最近一次 gather 以来没有新完成的数据；它并非电缆断开的判定。BiSS-C 和 EnDat 不使用同一 completed-main 发布路径，同一共享字段可能用于倒周期状态。主编码器保护信号的含义也取决于协议，例如 CIG1 的 EnDat 路径将 CRC 和编码器错误合并到该信号。因此不能将每次位 0 指示都理解为电缆物理断开，也不能将寄存器清零理解为反馈正常且新鲜。

## 独立控制器

本地主 BiSS-C、EnDat 和 Tamagawa 分支读取 FPGA 偏移 `0x005c` 的状态寄存器，并保留最低五位。必须考虑协议的位打包方式。在合并后的 FPGA 包中，BiSS-C 将断开、幅值、频率、系统及 CRC 分别放在位 0/1/2/3/4；EnDat 将编码器错误、不支持的模式、Error1、Error2 及 CRC 分别放在位 0/1/2/3/4。解释其他协议或变体前，应检查对应镜像的接口约定。

独立控制器的处理程序直接使用状态进行故障判断，并可能在旁路或无错误分支清除位 0/1。CI_MASTER 状态报告修复不改变此行为。不要假设独立控制器和 Central-i 具有相同的清除语义。SIN/COS 通过此寄存器进行独立的幅值状态处理，其位并非串行应答状态。此寄存器也不能证明辅助编码器具有同等监控，或证明支持 SSI/Nikon。

## 状态报告与故障响应

包含[已接受质量修复](https://github.com/akribis-agito/Firmware-Main/issues/1408)的固件保留上述当前输入诊断映射。对于 AGM800/EC 上活动的标准 AMP 主 BiSS-C、EnDat 和 Tamagawa 反馈，编码器错误策略改用通过 CRC1、与主位置一起被接受的质量。解码被拒绝或跳过后，诊断与保留的策略依据可能不同：被拒绝的异常帧可以设置诊断位，但不会污染已接受的正常质量；被拒绝的正常帧可以清除诊断位，但不会清除已接受的异常质量。这不会改变锁存/事件状态的归属，也不代表启动、物理新鲜度或完整编码器告警已通过资格确认。

`EncAbsErrTime=-1` 旁路现有 CRC/错误计数、外推和超时故障响应，但独立的主编码器保护处理仍有效。启用处理后，CRC 和通用错误条件使用各自的计数器，并可产生 [ConFlt](../../07-status-and-faults/ConFlt.md) 1069 和 1068；现有保护路径使用 1070。当前报告的条件与已记录的故障是不同的观察结果；历史故障应查看故障日志。

此状态不提供物理采样时间戳、通用的新鲜度保证、测量/保持/预测位置来源，或 Tamagawa 的详细 SF/ALMC 报警。寄存器清零本身不能确认位置样本有效。Tamagawa 启动修复使用独立的新接受回复及质量条件，并在稳定等待期间报告诊断，不提前执行现有故障计数和动作；其他反馈路径保留其初始化窗口。调查短暂异常时应按控制周期捕获数据，上位机轮询可能错过已经恢复的条件。

## 另请参阅

- [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) — 现有错误处理超时与旁路
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — 绝对位置初始化偏移
- [EncType](EncType-AuxEncType.md) — 反馈选择
- [StatReg](../../07-status-and-faults/StatReg.md) — 通用轴状态
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 报告的故障代码
