---
keyword: LockFifoKeep
summary: 选择关闭锁存记录时丢弃还是读完 FIFO 中尚未处理的捕获。
availability:
  standalone: []
  central-i:
  - v5
can_code: 960
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
  - 0
  - 1
  default: 0
  scaling: 1
  implemented: final
overrides: {}
language: zh-CN
---
# LockFifoKeep

在 AGM800 和 AGM800-EC 上，选择 [LockEn](LockEn-AuxLockEn.zh.md) 从 1 变为 0 时如何处理
FIFO 中尚未读取的捕获。请在关闭记录前设置本参数；固件在该跳变时读取此策略。
本参数按轴设置，不保存到闪存。

| 值 | 行为 |
|---|---|
| 0（默认） | 丢弃未读的 FIFO 积压，并将丢失的捕获计入 [LockLost](LockLost.zh.md)。 |
| 1 | 先将 FIFO 中积压的捕获读入捕获表，再关闭 FIFO 捕获。成功读出的捕获不计入 `LockLost`。 |

读完积压的过程有界。链路丢失、远端复位、编码器变更、反复读取失败或达到读取时限都可能使其提前结束，
此时剩余积压计入 `LockLost`。`LockEn = 0` 不表示积压已经读完。
本参数不会为不支持 FIFO 捕获的远端或编码器路径增加 FIFO，也不改变单锁存器路径。

捕获活动稳定后，读取 [LockCntr](LockCntr-AuxLockCntr.zh.md) 和 `LockLost`，区分已交付和丢失的样本。
该策略适用于主 `LockEn` 的 FIFO 路径，不定义辅助 FIFO 的排空策略。
