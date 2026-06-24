---
keyword: InjectPoint
summary: 选择将注入波形施加到哪个指令信号。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 113
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
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# InjectPoint

选择将注入波形施加到哪个指令信号。

## 概述

`InjectPoint` 定义测试波形在控制环中的注入位置。注入用于系统辨识、阶跃响应整定及调试。所选位置决定使用哪个幅值参数：电流指令使用 [InjectCurrAmp](InjectCurrAmp.md) / [InjectCurrDC](InjectCurrDC.md)，速度指令使用 [InjectVelAmp](InjectVelAmp.md)，位置指令使用 [InjectPosAmp](InjectPosAmp.md)，力指令使用 [InjectForceA](InjectForceA.md)。波形本身由 [InjectType](InjectType.md) 选择。

## 工作原理

| 值 | 注入位置 | 方块图中的位置 |
|----|----|----|
| 0 | 电流指令 | 参见 [控制整定 – 电流控制](../11-control-tuning/06-current-control/00-overview.md) |
| 1 | 速度指令 | 参见 [控制整定 – 速度控制](../11-control-tuning/04-velocity-control/00-overview.md) |
| 2 | 位置指令 | 参见 [控制整定 – 位置控制](../11-control-tuning/03-position-control/00-overview.md) |
| 3 | 力指令 | 参见 [控制整定 – 力控制](../06-protections/04-force-control/00-overview.md) |

注入值在所选指令处的参考值形成点接入。在**直接** [InjectType](InjectType.md) 模式下，上游信号被丢弃，指令仅为注入值；在**叠加**模式下，注入值叠加在来自上游环路的指令之上。幅值缩放取决于所选位置：

| 值 | 幅值参数 | 幅值单位 |
|-------|-------------------|----------------|
| 0 | [InjectCurrAmp](InjectCurrAmp.md)（加 [InjectCurrDC](InjectCurrDC.md) 偏置） | mA |
| 1 | [InjectVelAmp](InjectVelAmp.md) | 用户速度单位（取决于双环设置） |
| 2 | [InjectPosAmp](InjectPosAmp.md) | 主用户位置单位 |
| 3 | [InjectForceA](InjectForceA.md) | 内部力单位 |

对于速度指令注入，注入项替代或叠加于速度环参考 [VelRef](../10-motion/01-kinematics-status/VelRef.md)。对于电流指令注入，当电机未完成定相时，[InjectCurrDC](InjectCurrDC.md) 偏置被抑制，以避免产生不受控的稳态电流。脉冲波形（[InjectType](InjectType.md) = 5）仅在电流指令（`InjectPoint = 0`）处有效。

## 示例

```text
AInjectPoint=0       ; 在电流指令处注入
AInjectPoint=2       ; 在位置指令处注入
AInjectPoint        ; 查询当前注入位置
```

## 另请参见

- [InjectType](InjectType.md) — 选择波形及注入模式
- [InjectCurrAmp](InjectCurrAmp.md) — 电流指令注入的幅值（InjectPoint = 0）
- [InjectVelAmp](InjectVelAmp.md) — 速度指令注入的幅值（InjectPoint = 1）
- [InjectPosAmp](InjectPosAmp.md) — 位置指令注入的幅值（InjectPoint = 2）
- [InjectForceA](InjectForceA.md) — 力指令注入的幅值（InjectPoint = 3）
- [InjectedValue](InjectedValue.md) — 当前注入值
- [VelRef](../10-motion/01-kinematics-status/VelRef.md) — 受速度指令注入影响的速度环参考
