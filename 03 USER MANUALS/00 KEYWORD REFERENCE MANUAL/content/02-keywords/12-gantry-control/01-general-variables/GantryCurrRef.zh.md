---
keyword: GantryCurrRef
summary: 龙门偏摆校正的只读电流（力矩）参考值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 651
attributes:
  access: ro
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
overrides:
  central-i.v5:
    data_type: float32
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GantryCurrRef

龙门偏摆校正的只读电流（力矩）参考值。

## 概述

`GantryCurrRef` 是一个只读状态变量，报告龙门虚拟轴在重新合并为两个物理电机之前的电流（力矩）指令。在主轴上读取时，为**共模（线性）**电流指令；在偏摆轴上读取时，为响应 [GantryYawRef](GantryYawRef.md) 所产生的**差模（偏摆）**电流指令。因此，在龙门模式激活时（参见 [GantryOn](GantryOn.md)），该变量显示每个虚拟环路的工作强度。该参数为轴范围，不保存至闪存。在 central-i v5 上以浮点值形式报告。

## 工作原理

两个虚拟轴电流指令每个控制周期重新合并为两个电机电流。采用对称分配（无解耦映射表）时，电机 A 接收线性指令加偏摆指令，电机 B 接收线性指令减偏摆指令——因此纯线性运动使两个电机同向驱动，纯偏摆校正使两个电机反向驱动。当启用位置相关解耦映射表（[GantryMapType](GantryMapType.md) = 1）时，线性分配部分由映射比值（[GantryMapVal](GantryMapVal.md)）加权，而非固定 50/50 分配；偏摆部分仍然分别加到一个电机并从另一个电机减去。`GantryCurrRef` 报告的是重新合并之前各虚拟轴的指令。

## 示例

```text
AGantryCurrRef     ; 读取共模（线性）龙门电流指令
BGantryCurrRef     ; 读取差模（偏摆）龙门电流指令
```

### 边界情况

- **龙门关闭**（[GantryOn](GantryOn.md) = 0）——龙门环路未运行；`GantryCurrRef` 保持最后一次值（若龙门从未激活则为 `0`）。
- **电机关闭**——数值反映重新合并缓冲区，但实际电机电流为 `0`，因为电流环路未上电。
- **非龙门轴**——在非主轴或非偏摆轴上读取返回 `0`。
- **解耦映射表**（[GantryMapType](GantryMapType.md) = 1，仅 v5）——重新合并比值不再为 50/50；此处显示的虚拟轴指令不变，但下游的各电机分配使用 [GantryMapVal](GantryMapVal.md)。
- **只读**——写入操作将被拒绝。
- **平台**——v5 central-i 以 `float32` 报告；v4 以 `int32` 报告。

## 另请参阅

- [GantryYawRef](GantryYawRef.md) — 差模电流响应的偏摆校正参考值
- [GantryOn](GantryOn.md) — 激活控制器的龙门模式；说明共模与差模模式
- [GantryMapType](GantryMapType.md) / [GantryMapVal](GantryMapVal.md) — 可重新加权电流分配的解耦映射表
