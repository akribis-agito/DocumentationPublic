---
keyword: FIFOPushParP
summary: 将由位置值定义的抛物线段压入 FIFO 运动队列。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 287
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# FIFOPushParP

将由位置值定义的抛物线段压入 FIFO 运动队列。

## 概述

`FIFOPushParP` 将一个**按位置增量定义的抛物线**段（[FIFOType](FIFOType.md) 中的类型 3）追加到队列末尾。该值为段内需行进的位置增量。运动以恒定加速度进行，因此位置遵循抛物线规律：从当前规划器速度出发，在段结束时到达前一个位置参考加上增量的位置。它是 [FIFOPushParA](FIFOPushParA.md) 的基于位置的对应版本，后者通过加速度来定义段。

它是用于在运动前或运动过程中填充队列的 `FIFOPush*` 函数之一。条目将被添加到队列末尾。若队列已满（无空闲条目），则该压入操作会被拒绝并返回错误 105，且不会添加任何内容。

有关 FIFO 运动模式及所有相关关键字的完整说明，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

当控制器到达此段时，它计算在当前有效的 [FIFOCycleTime](FIFOCycleTime.md) 内从当前速度出发行进所请求增量所需的恒定加速度。然后，它在每个控制周期按该加速度增加速度，并相应地推进位置参考，使增量在最后一个采样时精确到达。变化中的速度和加速度在 [FIFOStatus](FIFOStatus.md)（索引 4 和 5）中报告。

若增量和周期时间解算出的加速度幅值低于 16 384 counts/s²（在标准 16 384 Hz 频率下为一个控制采样频率——每采样速度步长所能分辨的最小加速度），该段将使运动发生故障（电机关闭，故障 1031）。由于解算出的加速度要到段运行时才能确定，因此无法像 [FIFOPushParA](FIFOPushParA.md) 那样在压入阶段就检测到此问题。

### 计算示例

以连续形式最易于理解该形状：若 `FIFOCycleTime = 16384` 个采样（在 16384 Hz 下约 1 s），前一速度为 `0`，`FIFOPushParP = 20000`，则从静止出发在 1 s 内行进 20 000 单位所需的理想恒定加速度为 `a = 2 × 20000 / 1² = 40000` 单位/s²。速度从 0 线性增大，位置遵循对应的抛物线。

在固件中，每采样速度步长使用整数运算推导——位置增量以整数除以周期时间——因此解算出的加速度是量化的，不一定与上述理论值完全吻合。若解算出的幅值低于 16 384 counts/s²（在标准 16 384 Hz 频率下为一个控制采样频率——每采样速度步长所能分辨的最小加速度），该段将使运动发生故障（电机关闭，故障 1031）。上述 20 000 单位/16 384 个采样的示例实际上会解算出一个低于阈值的加速度并触发故障；此处仅用于说明抛物线形状，而非可运行的实际数值。若要使段通过阈值，请选择整数解算加速度明显高于 16 384 counts/s² 的增量和周期时间组合——例如，在 16 384 个采样（约 1 s）的周期内行进 200 000 000 单位的增量，解算结果约为 24 000 counts/s²——并将其加速度读取为近似量化值，而非精确的 `2 × delta / t²`。

## 示例

```text
AFIFOPushParP=20000  ; queue a parabolic segment that travels 20000 units
```

## 另请参阅

- [FIFOPushParA](FIFOPushParA.md) — 按加速度定义的抛物线段
- [FIFOPushCycle](FIFOPushCycle.md) — 设置段持续时间
- [FIFOType](FIFOType.md) — FIFO 模式完整说明
