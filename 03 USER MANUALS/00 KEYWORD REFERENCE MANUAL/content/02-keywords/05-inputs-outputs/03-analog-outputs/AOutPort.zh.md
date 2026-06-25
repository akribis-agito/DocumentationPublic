---
keyword: AOutPort
summary: 直接指令模式下命令的模拟量输出值（mV）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 219
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -11905
  - 11905
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
    data_type: float32
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# AOutPort

直接指令模式下命令的模拟量输出值（mV）。

## 概述

`AOutPort` 用于设置当某个模拟量输出处于**直接指令模式**时，在该输出上驱动的值（单位为毫伏）。数组索引即模拟量输出编号（从 1 开始：`AOutPort[1]` 为模拟量输出 1，`AOutPort[2]` 为模拟量输出 2）。可用的索引范围与物理输出数量一致（2 输出产品为 1 到 2，4 输出产品为 1 到 4）。`AOutPort[Index]` 仅在 `AOutMode[Index] == 0` 时生效；在监视模式下，输出转而跟随被仿真的参数。两种模式参见[模拟量输出概述](00-overview.md)。

±11905 mV 的范围直接来自 DAC：mV 到 DAC 的换算系数为 −2.752457 LSB/mV，因此满量程 −32768 LSB 对应 11905 mV。

## 工作原理

每个模拟量输出索引映射到一个物理 DAC 通道：索引 1 → DAC 通道 A，索引 2 → DAC 通道 B，索引 3 → C，索引 4 → D。

在直接指令模式下，每个周期按如下方式计算 DAC 码：

$$
\text{DAC code} = (\text{AOutPort} + \text{AOutOffset}) \cdot \text{(mV-to-DAC factor)}
$$

随后将其钳位至 DAC 范围，再写入通道。注意 [AOutOffset](AOutOffset.md) 在 LSB 转换**之前**以相同的毫伏单位相加。每个输出在直接模式与监视模式之间的选择，在写入 [AOutMode](AOutMode.md) 时确定：当 `AOutMode = 0` 时，或者当驱动器为模拟电流指令型／内置直线型时，强制采用直接模式（此时 DAC 驱动的是驱动器的电流指令）。

`AOutPort` 保存至闪存，为数组类型，可在运动中以及电机使能时更改。

模拟量输出由一个 16 位 DAC 产生。每个控制周期，控制器计算出新的 DAC 码并写入通道；通道每周期刷新一次（16 384 Hz，约 61 µs），新码大约在 1.5 µs 内载入。因此输出是一个以控制速率更新的阶梯式（采样保持）信号，而非连续插值的波形——命令的更改会在一个控制周期内出现在输出端。

## 示例

```text
AAOutMode[1]=0       ; direct command mode
AAOutPort[1]=5000    ; drive analog output 1 to 5000 mV
AAOutPort[1]          ; read back the commanded value
```

### 边界情况

- **索引 0** —— 无效；有效索引为 `AOutPort[1]`–`AOutPort[4]`。`AOutPort[0]` 不存在。
- **错误模式** —— 仅当 [AOutMode](AOutMode.md)`[i] = 0` 时，DAC 才读取 `AOutPort`。在 `AOutMode[i] ≠ 0` 时写入会存储该值，但输出仍跟随被监视参数；一旦将 `AOutMode[i]` 重新置为 `0`，存储的值即刻生效。
- **超出范围** —— 超出 ±11905 mV 的写入会被参数表拒绝；DAC 码也会在每个周期被钳位。该钳位为饱和而非回绕：当某个值（或 `AOutPort + AOutOffset` 之和）超过 ±11905 mV 时，输出会被钉在对应的轨电平上并保持，直到该值回到范围内——它不会翻转到相反的轨电平。由于 `AOutOffset` 也在此限值之内，过大的偏置可能使一个本在范围内的 `AOutPort` 触轨。
- **2 输出产品** —— 仅存在 `AOutPort[1]` 和 `AOutPort[2]`。数组大小按物理输出数量确定，因此 `AOutPort[3]` / `AOutPort[4]` 越界，对其写入会以索引超出数组大小错误被拒绝而不被存储。
- **驱动器覆盖** —— 当驱动器为模拟电流指令型或内置直线型时，DAC 由驱动器电流指令占用；`AOutPort` 写入会被存储但不会到达引脚。
- **电机使能／失能** —— 与 `MotorOn` 无关；无论伺服是否使能，DAC 都跟随 `AOutPort`。
- **保存** —— 可保存至闪存；最后命令的值会在启动时恢复。
- **平台** —— central-i v5 将该值存储为 `float32`；行为和单位不变。

## 另请参阅

- [AOutMode](AOutMode.md) —— 选择直接模式还是监视模式（此值仅在 `AOutMode = 0` 时被采用）
- [AOutOffset](AOutOffset.md) —— 输出校准偏置，在 DAC 转换之前相加
- [analog-output overview](00-overview.md) —— 完整信号路径
