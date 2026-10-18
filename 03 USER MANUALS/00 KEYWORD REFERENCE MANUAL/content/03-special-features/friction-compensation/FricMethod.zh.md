---
keyword: FricMethod
summary: 选择摩擦前馈模型（0 = 关闭，1 至 5）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 926
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
  - 5
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricMethod

选择摩擦前馈模型（0 = 关闭，1 至 5）。

## 概述

`FricMethod` 选择摩擦前馈环节如何把速度换算为电流。适用于 AGM800 和 AGM800-EC（central-i v5）。这是同一个环节：无论选择哪种模型，其输出都经过同一个钳位（[FricLim](FricLim.md)）和同一条前馈通路（参见[摩擦前馈](00-overview.md)）。

| `FricMethod` | 模型 | 作用 |
|---|---|---|
| 0 | 关闭（默认） | 无摩擦前馈。 |
| 1 | 线性 | 在死区带内从 0 斜坡上升到库仑电平，之后保持该电平。无记忆。 |
| 2 | 滞环 | 速度离开死区带时在两个库仑电平之间切换。在死区带内保持上一次的电平。 |
| 3 | 间隙（Play） | 与 2 相同，但切换是穿过死区带的斜坡，而不是跳变。 |
| 4 | LuGre | 带内部状态的刷毛模型。使用库仑电平、静摩擦（起动）电平、Stribeck 速度和刷毛参数。 |
| 5 | Stribeck | 平滑的库仑电平加上随速度衰减的起动峰。无记忆。 |

## 工作原理

方法 5 对速度 $v$ 计算：

$$
I = \operatorname{sign}(v)\cdot\tanh\!\left(\frac{|v|}{V_{band}}\right)\cdot\left(F_c + (F_s - F_c)\,e^{-(v/V_s)^2}\right) + \text{FricViscous}\cdot v_{fb}
$$

其中按运动方向取：

- $F_c$ = 库仑电平：[FricIPos](FricIPos.md) 或 [FricINeg](FricINeg.md)（取幅值）
- $F_s$ = 起动电平：[FricIStatPos](FricIStatPos.md) 或 [FricIStatNeg](FricIStatNeg.md)（取幅值）
- $V_{band}$ = [FricVBandPos](FricVBandPos.md) 或 [FricVBandNeg](FricVBandNeg.md)：输出在零速附近建立的快慢
- $V_s$ = [FricVStribPos](FricVStribPos.md) 或 [FricVStribNeg](FricVStribNeg.md)：起动峰衰减到库仑电平所跨越的速度
- $v$ 来自 [FricVelSrc](FricVelSrc.md)；$v_{fb}$ 始终为速度反馈。

方法 5 取代了 5.3.0-rc4 中独立的 Stribeck 前馈（`StribOn` 及 `Strib*` 关键字）。象限切换补偿（[FricQSCOn](FricQSCOn.md)）仅叠加在方法 0 至 3 上；方法 4 和 5 已包含起动电平。

取值范围为 0 至 5。在 5.3.0-rc4 下保存的值不会被转换。从 rc4 升级后，请重新输入摩擦设置。

## 示例

```text
AFricMethod=5      ; Stribeck 模型
AFricMethod=0      ; 关闭摩擦前馈
```

## 另请参阅

- [摩擦前馈](00-overview.md) — 整个环节、整定顺序及 rc4 变更
- [FricLim](FricLim.md) — 环节输出的钳位
- [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md) — 读回摩擦电流（索引 6）
