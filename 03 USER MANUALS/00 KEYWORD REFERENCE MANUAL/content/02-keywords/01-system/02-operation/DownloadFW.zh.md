---
keyword: DownloadFW
summary: 使控制器进入固件下载模式的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 230
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
# DownloadFW

使控制器进入固件下载模式的命令。

## 概述

`DownloadFW` 将控制器切换至固件下载模式，之后即可传输新的固件镜像。它是一条**命令**（无值），并且不能在电机使能或运动中时发出。

> **仅可通过 Agito PCSuite 使用。** 为避免使控制器停留在意外状态，请仅通过 PCSuite 的固件下载选项卡发出 `DownloadFW`。如果您需要从自己的上位机软件驱动该下载过程，请联系 Agito。

[DontDownload](../01-status/DontDownload.md) 标志置位时，会作为安全互锁阻止固件下载。

## 工作原理

`DownloadFW` 将控制权从运行中的固件移交给板载引导程序，由其执行实际的镜像传输。传输方式因控制器类型而异：

- **Central-i 控制器仅通过以太网链路运行固件下载。** 通过 USB/串口（或 RJ45 串口）或 CAN 发出 `DownloadFW` 会被拒绝，并返回指令错误 235（“Download Firmware is only available via Ethernet connection”），控制器保持正常运行；PCSuite 通过以太网驱动整个镜像传输过程。
- **Standalone 控制器**则运行下述的逐链路密码握手，并且也可通过 USB/串口或 CAN 接受下载。

其流程（standalone）如下：

1. **密码握手。** 控制器请求密码，并等待上位机通过命令到达的同一链路（USB/串口或 CAN）发送预期的回复。PCSuite 会自动提供该密码。回复错误将返回密码错误，控制器保持正常运行；如果在约 10 秒内未收到回复，控制器将超时并保持正常运行，但在这种情况下它完全不发送回复，因此上位机只能看到自身的超时。
2. **使硬件静默。** 成功后，串行总线关闭，FPGA 复位以使驱动输出进入安全状态，并将 I/O 引脚恢复为引导程序所预期的模式。
3. **跳转至引导程序。** 固件记录哪个接口发起了下载，并跳转至引导程序，由其接收并写入新镜像。随后下载工具重启设备；在下一次启动时，控制器将运行新固件。

由于密码和超时握手因接口而异且必须精确匹配，因此该命令意在由 PCSuite 驱动，而非手动操作。

## 另请参阅

- [DownloadFPGA](DownloadFPGA.md) — 针对 FPGA 镜像的等效命令
- [DontDownload](../01-status/DontDownload.md) — 阻止固件下载的互锁
- [Reset](Reset.md) — 平滑软件重启（用于在下载后重新进入正常模式）
- [FWInfo](../01-status/FWInfo.md) — 当前固件版本
