---
keyword: EncSinCosHWEn
summary: 选择为该轴硬件锁定/事件捕获机制提供信号的编码器源。
availability:
- controller
- ci-master
can_code: 496
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 7
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EncSinCosHWEn

*旧版关键字*

**定义：**

EncSinCosHWEn 选择为该轴硬件锁定/事件捕获机制提供信号的编码器源。范围 0..7，默认值 0。已验证的源：0 = 主编码器（增量式），1 = 主编码器，2 = 虚拟编码器，3 = 辅助编码器。

该选择仅在轴编码器配置为正弦/余弦类型时生效。对于其他任何编码器类型，控制器将内部强制将选择置为 0，无论所写入的值为何。

回零锁存步骤会暂时将硬件切换到主编码器。在此期间读取或保存 `EncSinCosHWEn` 得到的仍是用户配置值，尝试更改该选择将被拒绝。回零完成、超时或中止后，固件恢复配置的信号源，原有的锁存和事件保持禁用。模式 0 在下次启用时学习偏移量，模式 1 需要重新执行 `LockEventInit`，模式 2 在信号源写入成功且远端稳定后重新计算。
