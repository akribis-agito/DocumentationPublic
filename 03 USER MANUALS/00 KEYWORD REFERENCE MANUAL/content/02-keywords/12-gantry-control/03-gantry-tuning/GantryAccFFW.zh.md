---
keyword: GantryAccFFW
summary: 龙门偏摆校正控制器的加速度前馈增益。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 655
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
  - 500000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    type: array
    array_size: 6
    data_type: float32
    range:
    - 0
    - 50000000
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryAccFFW

龙门偏摆校正控制器的加速度前馈增益。

## 概述

`GantryAccFFW` 是龙门控制环的加速度前馈增益。当龙门模式激活时（参见 [GantryOn](../01-general-variables/GantryOn.md)），它扮演普通 [AccFFW](../../11-control-tuning/05-feedforwards/00-overview.md) 在单轴环路中的角色，注入一个与指令加速度成比例的电流项，使反馈环不必单独承担加速负载的任务。它是一个轴相关参数，保存至闪存，可在任何时候修改，包括运动中和电机使能时。

## 工作原理

加速度前馈仅在位置运行模式下生效。控制器由整形/滤波后的位置参考的二阶差分（离散二阶导数）计算指令加速度，将其乘以 `GantryAccFFW`，并在形成差动电机电流指令时直接叠加到速度 PI 输出上：

$$
\text{CurrRef} = \text{VelPIOutput} + \frac{(\text{PosRef}_{n} - 2\,\text{PosRef}_{n-1} + \text{PosRef}_{n-2}) \cdot \text{GantryAccFFW}}{256}
$$

由于该项为前馈，仅依赖于参考轨迹而非位置误差，因此可在加速阶段提供所需电流，而无需等待 [GantryPosGain](GantryPosGain.md) / [GantryVelGain](GantryVelGain.md) 反馈环积累误差。每个龙门成员轴各自应用自己的值：主轴（共模/线性）将其 `GantryAccFFW` 注入线性环，偏摆轴将其值注入偏摆环。在 v4 上，龙门电流指令仅叠加加速度前馈项（偏摆轴启用时速度前馈项被丢弃）；在 v5 上，加速度前馈和速度前馈 [GantryVelFFW](GantryVelFFW.md) 均被应用。

该值无量纲（前馈缩放系数）。允许范围为 0 至 500000，默认值为 0，即除非配置否则加速度前馈关闭（在龙门增益为 6 元素增益调度数组的控制器上，上限范围扩展；详见关键字属性）。

## 示例

```text
AGantryAccFFW=1000  ; set acceleration feedforward gain
AGantryAccFFW      ; read the current gain
```

### 边界情况

- **龙门关闭** — 写入被接受；在 [GantryOn](../01-general-variables/GantryOn.md) = 1 之前增益无效。
- **模式错误** — 加速度前馈仅在 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 3（位置）时生效；电流/力/速度模式下忽略。
- **零增益** — 禁用该轴的加速度前馈。
- **逐轴生效** — 每个龙门成员轴各自应用其 `GantryAccFFW`：主轴（共模/线性）在线性环中使用其值，偏摆轴在偏摆环中使用其值。当该轴处于龙门模式时逐轴读取；非龙门轴的写入被接受但不使用。
- **超出范围** — 超出 `0`–`500000`（v4）/ `0`–`50000000`（v5 单元素）的值将被拒绝。
- **与 [GantryVelFFW](GantryVelFFW.md) 不匹配** — 较大的加速度前馈若未配合适当的速度前馈，可能在速度校正之前产生偏摆转矩；建议同时整定两者。
- **保存** — 可保存至闪存。
- **平台** — v5 以 6 元素增益调度 `float32` 数组存储；v4 以单个 `int32` 存储。

## 另请参阅

- [GantryPosGain](GantryPosGain.md) — 偏摆位置环比例增益
- [GantryVelGain](GantryVelGain.md) — 偏摆速度环比例增益
- [GantryVelFFW](GantryVelFFW.md) — 速度前馈增益
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — 偏摆校正参考值
