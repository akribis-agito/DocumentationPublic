---
keyword: DontDownload
summary: 只读安全互锁，置位时阻止固件下载。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 670
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# DontDownload

只读安全互锁，置位时阻止固件下载。

## 概述

`DontDownload` 是一个只读标志，反映当前运行的镜像是否会拒绝固件下载。值为 `0` 时允许下载；`1` 时阻止下载。它是非轴的且不保存至闪存，因此反映控制器的实时状态。

## 工作原理

该标志在启动期间被设置。在相关平台上，如果单元上电时其**"强制下载固件"配置 DIP 开关**被置位，运行中的应用程序会设置 `DontDownload = 1`，并在应用（非引导）镜像中擦除当前位于闪存中的固件镜像的头部。头部被擦除后，下一次重新上电将引导**黄金镜像**而非应用程序，随后即可执行正常的 [DownloadFW](../02-operation/DownloadFW.md)。

实际上，`DontDownload = 1` 表示该单元正处于恢复过程中：当前应用程序已使自身失效，以便在重新上电后能从黄金引导镜像执行干净的下载。在正常运行中该标志读取为 `0`。上位机应在尝试下载前读取它，如果它被置位，则先重新上电该单元。

## 示例

```text
ADontDownload       ; check whether firmware download is currently blocked
```

## 另请参见

- [DownloadFW](../02-operation/DownloadFW.md) / [DownloadFPGA](../02-operation/DownloadFPGA.md) — 此标志所门控的固件/FPGA 下载命令
- [UnitStat](UnitStat.md) — 单元硬件/固件健康状态
