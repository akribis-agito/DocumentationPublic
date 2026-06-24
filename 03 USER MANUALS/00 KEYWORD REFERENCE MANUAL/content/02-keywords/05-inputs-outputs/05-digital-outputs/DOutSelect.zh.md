---
keyword: DOutSelect
summary: 选择路由到每个数字量输出的硬件功能（或软件控制）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 314
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 17
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 15
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# DOutSelect

选择路由到每个数字量输出的硬件功能（或软件控制）。

## 概述

`DOutSelect` 通过多路复用器为数字量输出分配一项硬件功能。数组**索引**即输出编号（从 1 开始：`DOutSelect[1]` 为输出 1）。将其设置为 `0` 可通过 [DOutMode](DOutMode.md) 将该输出交回软件控制。硬件功能（事件、P/D 信号、UserPWM）在硬件层运行，用于高频信号；当选定某项硬件功能时，该输出的 `DOutMode` 与 `DOutPort` 无效。可用功能因产品而异：

| 值 | 独立式 | Central-i 从轴 |
|-------|------------|------------------|
| 0 | 软件（使用 DOutMode） | 软件（使用 DOutMode） |
| 1 | 编码器仿真 | 保留 |
| 2 | A event #1 | Main event #1 |
| 3 | A event #2 | Main event #2 |
| 4 | A event #3 | Main event #3 |
| 5 | B event #1 | Aux. event #1（未实现） |
| 6 | B event #2 | Aux. event #2（未实现） |
| 7 | B event #3 | Aux. event #3（未实现） |
| 8 | C event #1 | Pulse（P/D 控制） |
| 9 | C event #2 | Direction（P/D 控制） |
| 10 | C event #3 | 保留 |
| 11 | UserPWM 1 | 保留 |
| 12 | UserPWM 2 | UserPWM 1 |
| 13 | 保留 | UserPWM 2 |
| 14 | 保留 | 保留 |
| 15 | 保留 | Central-i 远程信号 |

## 工作原理

`DOutSelect` 在硬件中编程一个按输出划分的多路复用器，用以选择馈入每个物理输出引脚的信号。写入 `DOutSelect` 时，按输出划分的代码——**每个输出 4 位**——会被打包进硬件输出路由寄存器（在独立式控制器上），或发送至远程单元（在 central-i 上）。由于每个输出获得一个 4 位选择器，取值范围为 `0`–`15`。

- 代码 `0` 将输出连接到**软件层**——即 `DOutPort` 位（应用 [DOutLog](DOutLog.md) / [DOutType](DOutType.md)），可选地由 [DOutMode](DOutMode.md) 功能驱动。这是软件在每个控制周期以控制环速率更新的路径。
- 任何非零代码将输出连接到直接在硬件中生成的**硬件功能**（位置事件、编码器/脉冲方向信号、UserPWM）。这些功能以硬件时钟速率运行，远快于控制环，因此在选定某项硬件功能期间，该输出的软件 `DOutPort`/`DOutMode` 值无效。

该选择器仅为一个路由 MUX；它不改变信号的极性或级——[DOutLog](DOutLog.md) 与 [DOutType](DOutType.md) 仍适用于软件路径，[UserPWM](UserPWM.md) 占空比/分频器仍控制 PWM 输出。

## 示例

```text
ADOutSelect[3]=0     ; output 3 is software-controlled (uses DOutMode[3])
ADOutSelect[4]=2     ; output 4 = Main Event #1 (Central-i) / A event #1 (standalone)
```

### 边界情况

- **索引 0**——无效；有效索引为 `DOutSelect[1]`–`DOutSelect[16]`。`DOutSelect[0]` 不存在。
- **超出范围**——`0`–`15` 之外的值会被参数表拒绝。
- **非零 `DOutSelect`**——为该输出覆盖 [DOutMode](DOutMode.md) 和 [DOutPort](DOutPort.md)；硬件功能以 FPGA 时钟速率直接驱动引脚。
- **未实现的功能**——标记为"未实现"或"保留"的代码在所寻址的引脚上不产生有用输出。
- **仅软件路径**——[DOutPort](DOutPort.md) 位操作和 [DOutMode](DOutMode.md) 功能调度需要 `DOutSelect = 0`。
- **保存**——可保存至闪存；启动时重新加载到路由 MUX。
- **平台**——功能代码到信号源的映射在独立式与 central-i 之间不同；参见上表。

## 参见

- [DOutMode](DOutMode.md)——软件功能（当 DOutSelect = 0 时）
- [DOutPort](DOutPort.md)——手动输出状态
- [UserPWM](UserPWM.md)——用户 PWM 通道
