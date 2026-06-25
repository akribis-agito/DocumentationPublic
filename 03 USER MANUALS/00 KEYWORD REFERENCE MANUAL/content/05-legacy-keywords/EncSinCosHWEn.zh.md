---
keyword: EncSinCosHWEn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
summary: 选择为该轴硬件锁定/事件捕获机制提供信号的编码器源。
---
# EncSinCosHWEn

*旧版关键字*

**定义：**

EncSinCosHWEn 选择为该轴硬件锁定/事件捕获机制提供信号的编码器源。范围 0..7，默认值 0。已验证的源：0 = 主编码器（增量式），1 = 主编码器，2 = 虚拟编码器，3 = 辅助编码器。

该选择仅在轴编码器配置为正弦/余弦类型时生效。对于其他任何编码器类型，控制器将内部强制将选择置为 0，无论所写入的值为何。
