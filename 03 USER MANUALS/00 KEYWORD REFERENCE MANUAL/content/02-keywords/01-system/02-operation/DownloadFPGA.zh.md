---
keyword: DownloadFPGA
summary: 使控制器进入 FPGA 下载模式的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 231
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# DownloadFPGA

使控制器进入 FPGA 下载模式的命令。

## 概述

`DownloadFPGA` 将控制器切换至 FPGA 下载模式，之后即可传输新的 FPGA 镜像。它是一条**命令**（无值），并且不能在电机使能或运动中时发出。

> **仅可通过 Agito PCSuite 使用。** 为避免使控制器停留在意外状态，请仅通过 PCSuite 的 FPGA 下载选项卡发出 `DownloadFPGA`。如果您需要从自己的上位机软件驱动该下载过程，请联系 Agito。

固件/FPGA 版本不匹配会由 [UnitStat](../01-status/UnitStat.md) 报告。

## 工作原理

`DownloadFPGA` 因控制器类型而表现不同：

- **Central-i 控制器不接受单独的 FPGA 下载。** 在正常运行镜像中，`DownloadFPGA` 返回指令错误 242（“This function is not supported in this controller type”），控制器保持正常运行。在 Central-i 上，FPGA 配置包含在单一的组合固件镜像内，并作为 [DownloadFW](DownloadFW.md) 的一部分进行更新；不存在独立的 FPGA 传输步骤。
- **Standalone 控制器**执行专门的 FPGA 传输，其流程与 [DownloadFW](DownloadFW.md) 相同，只是目标是 FPGA 配置镜像而非处理器固件：

  1. **密码握手。** 控制器请求密码，并等待上位机通过命令到达的链路（USB/串口或 CAN）回复。PCSuite 会自动提供该密码；回复错误，或在约 10 秒内无回复，将使单元保持正常运行。
  2. **检查 FPGA 类型。** 握手成功后，控制器会验证所装配的 FPGA 是否为其可识别的类型。如果不是，下载将以指令错误 243（“Download FPGA encountered an unknown FPGA type”）中止，控制器保持正常运行。
  3. **使硬件静默。** 成功后，串行总线关闭，FPGA 复位以使驱动输出处于安全状态，并将 I/O 引脚设置为引导程序所预期的模式。
  4. **跳转至引导程序。** 固件记录发起接口并将控制权移交给引导程序，由其接收并写入新的 FPGA 镜像，然后重启单元。

固件和 FPGA 镜像是一起进行版本管理的；更新其中一个后，您可能需要更新另一个以使二者匹配。控制器会在 [UnitStat](../01-status/UnitStat.md) 中标记不匹配，并在存在相关不匹配时拒绝使能电机。

## 另请参阅

- [DownloadFW](DownloadFW.md) — 针对固件镜像的等效命令
- [DontDownload](../01-status/DontDownload.md) — 阻止下载的互锁
- [Reset](Reset.md) — 下载后使用的平滑软件重启
- [UnitStat](../01-status/UnitStat.md) — 标记 FW/FPGA 镜像不匹配
