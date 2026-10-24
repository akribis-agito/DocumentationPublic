---
keyword: LockEventInit
summary: 在手动模式 1 或自动模式 2 下学习捕获偏移。
availability:
  standalone: []
  central-i:
  - v5
can_code: 832
attributes:
  access: ro
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
last_updated: '2026-10-17'
doc_revision: '2026.10'
language: zh-CN
---
# LockEventInit

学习硬件辅助捕获计数器与对应控制器位置之间的偏移。手动 [LockEventMode](LockEventMode.md) 1 必须执行该命令；自动模式 2 也可用它强制重新测量。模式 0 在使能时学习偏移，在该模式执行此命令会被错误 334 拒绝。

先关闭 `LockEn` 和 `EventOn`，完成捕获源配置，并在测量时保持捕获源静止。主增量式/AqB 源对应 `Pos`，虚拟源对应 `VEncValue`，辅助编码器源对应 `AuxPos`。适用源测量成功后，[LockEventStat](LockEventStat.md) 设为 1。

主绝对式编码器源不需要该辅助偏移：命令可能返回成功而状态保持不变。因此，应结合所选捕获源解释状态。远端读取失败时返回错误 151，偏移保持无效。在模式 1/2 下，未曾测量时，使能被错误 335 拒绝；已有测量过期时，被错误 404 拒绝。

## 远端 FPGA 兼容性

在 AGM800 和 AGM800-EC 上，远端 FPGA 必须实现辅助位置读取寄存器 `0x72/0x73`。历史版本 v4.3.6 未实现这些寄存器，读取未映射地址会返回零。因此，该版本上的成功零值回复或 `LockEventStat=1` 不能证明偏移正确。依赖捕获坐标前，请使用经过配套验证的固件和 FPGA 组合。

## 示例

```text
ALockEn=0
AEventOn=0
ALockEventMode=1
; 配置捕获源并保持静止
ALockEventInit
ALockEventStat        ; 对需要辅助计数器的源，要求状态为 1
ALockEn=1
```

模式 1 在相关配置变化或重连使偏移失效后，需要再次显式测量。模式 2 在锁存和事件均关闭时尝试自动重新计算，也仍可使用本命令显式刷新。另见 [LockEventMode](LockEventMode.md) 和 [LockEventStat](LockEventStat.md)。
