---
keyword: FIFOTorqueTrgt
summary: 读取或写入指定 EtherCAT 轴的 FIFO 转矩目标。
last_updated: '2026-11-23'
doc_revision: '2026.11'
can_code: 897
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
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FIFOTorqueTrgt

读取 `FIFOTorqueTrgt` 可查看该轴 EtherCAT FIFO 跟踪状态中的当前转矩目标。该值为 32 位有符号整数。EtherCAT 主站后续的周期更新可能会覆盖从终端输入的值。初始化 FIFO 时也会从接收到的周期数据重新载入转矩目标。[InitFifoParams](InitFifoParams.zh.md)

在包含固件 PR #2680 的版本上，`AFIFOTorqueTrgt` 和 `AFIFOTorqTrgt` 读取 A 轴的同一目标。对于从控制器 About 列表选择关键字的工具，请使用正式名称 `FIFOTorqueTrgt`。其 CAN 编号为 897。 [固件 PR #2680](https://github.com/akribis-agito/Firmware-Main/pull/2680)
