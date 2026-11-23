---
keyword: InitFifoParams
summary: 使用当前 EtherCAT 周期目标初始化指定轴的 FIFO 跟踪状态。
last_updated: '2026-11-23'
doc_revision: '2026.11'
can_code: 896
availability:
- controller
- ci-master
products:
- agd101-ec-17a
- agd101-ec-34a
- agd155-ec
- agd155-ec-var34
- agd155-ec-var34-3
- agd156-ec
- agm800-ec
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# InitFifoParams

调用 `InitFifoParams` 会把接收到的位置目标和转矩目标复制到指定轴的 FIFO 跟踪状态，并将该轴的位置、速度和电流跟踪偏移量清零。在线性插补模式下，固件会根据当前 EtherCAT 运行模式初始化插补器。[FIFOPosType](FIFOPosType.zh.md) · [FIFOPosTrgt](FIFOPosTrgt.zh.md) · [FIFOTorqueTrgt](FIFOTorqueTrgt.zh.md)

在包含固件 PR #2680 的版本上，`AInitFifoParams` 和 `AInitFifoParms` 都会在 A 轴执行同一命令。对于从控制器 About 列表选择关键字的工具，请使用正式名称 `InitFifoParams`。其 CAN 编号为 896。 [固件 PR #2680](https://github.com/akribis-agito/Firmware-Main/pull/2680)
