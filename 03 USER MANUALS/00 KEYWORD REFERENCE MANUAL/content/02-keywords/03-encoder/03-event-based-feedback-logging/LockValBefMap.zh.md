---
summary: 读取最近一次位置锁存事件在误差映射前坐标系中的位置。
last_updated: '2026-11-23'
doc_revision: '2026.11'
keyword: LockValBefMap
can_code: 957
availability:
- controller
- ci-master
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
language: zh-CN
---
# LockValBefMap

`LockValBefMap`（CAN 957）是每个轴的只读位置参数。需要以 `PosBeforeMap` 或 `EventPos` 目标的坐标系读取最近一次锁存位置时，可读取此参数。它与 `LockVal` 来自同一次捕获，包含锁存坐标偏移。误差映射表、`MapErrOffset` 以及映射启停和偏移的渐变修正均不计入该值。[PosBeforeMap](../../04-error-mapping/PosBeforeMap.zh.md)

主编码器的硬件锁存使用触发时锁存的计数器值。软件捕获使用处理事件的控制周期中采样的位置。在 Central-i 主站上，`EncSinCosHWEn` 的辅助计数器选择值为 0 或 1 时使用远端锁存值加上映射前坐标偏移。来源 2 和 3 则分别使用虚拟编码器或辅助编码器的坐标，两个锁存参数都采用该坐标系。[LockSrc](LockSrc-AuxLockSrc.zh.md)

读取 `ALockValBefMap` 可取得 A 轴的映射前锁存位置。如需与 `ALockVal` 比较，应在读取这两个值前后各读取一次 `ALockCntr`。如果计数发生变化，请重新读取。应在同一次记录期间进行比较。重新使能记录会清零计数器，并保留上一次的锁存值，直至下一次捕获。在 AGM800 和 AGM800-EC 上，映射前位置为 64 位，`LockVal` 为 32 位。以编码器计数比较时，两者之差按 2³² 取模得到施加的修正量。[LockVal](LockVal-AuxLockVal.zh.md) · [LockCntr](LockCntr-AuxLockCntr.zh.md)

`EventTableSrc=0` 时，可直接将映射前的锁存位置用作事件目标。来源 1 要求输入已补偿的目标，并自行进行逆映射。采用二维或三维映射，或采用其他编码器作为映射索引时，需要额外的坐标才能还原捕获时的补偿后位置。[EventTableSrc](../../18-event-generation/EventTableSrc.zh.md)
