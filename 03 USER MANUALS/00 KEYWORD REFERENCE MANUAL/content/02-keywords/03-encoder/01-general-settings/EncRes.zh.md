---
keyword: EncRes
summary: 编码器分辨率；每磁距（直线电机）或每转（旋转电机）的计数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 56
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EncRes

编码器分辨率；每磁距（直线电机）或每转（旋转电机）的计数。

## 概述

`EncRes` 定义编码器分辨率，根据电机类型（[MotorType](../../02-motor-and-amplifier/MotorType.md)）进行解释：

- 对于直线电机，`EncRes` 是每磁距（North-North）的编码器计数。
- 对于旋转电机，`EncRes` 是每转的编码器计数。
- 对于音圈电机，`EncRes` 无效，可设为任意值。

`EncRes` 与极对数（[PolePrs](../../02-motor-and-amplifier/PolePrs.md)）一起用于计算换相所用的每极对编码器计数。由于是轴相关且保存至闪存，因此当电机使能或运动中时无法更改。

> [!warning]
> `PolePrs` 和 `EncRes` 用于计算换相所用的每极对编码器计数。错误的值会导致换相过程失败或错误地通过，可能引发异常行为，例如高电机电流或飞车情况。这可能对控制器、电机或连接到电机的任何其他系统部件造成严重损坏。

## 工作原理

`EncRes` 是若干内部计算所使用的缩放常数，而非可被读回的量：

- **换相电气周期。** 固件将每电气周期的计数计算为 $\frac{\text{EncRes}}{\text{PolePrs}}$。这定义了测量位置如何映射到正弦换相的电气角度上，因此错误的 `EncRes` 会使换相角失准（参见上面的警告）。对于步进电机，每计数步数因子推导为 $\frac{\text{PolePrs} \cdot \text{electricalCycle}}{\text{EncRes}}$。

  *计算示例。* 一台 `EncRes = 10000` 且 [PolePrs](../../02-motor-and-amplifier/PolePrs.md) `= 4` 的旋转无刷电机，其每电气周期为 `10000 / 4 = 2500` 个计数。换相角每 2500 个机械计数前进一个完整的电气旋转一周（0 → 360° 电气）；电机每 4 个电气周期机械旋转一周。

> [!note]
> 对于数字 A-quad-B 增量式编码器（[EncType](EncType-AuxEncType.md)`=1`，子类型 0），`EncRes` 以**计数**表示，而非以编码器*线数*表示。控制器使用 x4（四边沿）正交解码：它在 A/B 对的每次跳变时产生一个计数，因此单个 A/B 周期（一个编码器线/周期）产生**四个计数**。因此一个 2500 线编码器给出每转 `2500 × 4 = 10000` 个计数，故设置 `EncRes = 10000`。请取编码器的线数（有时称为每转脉冲数，PPR）乘以四，以得到 `EncRes` 的值。
- **速度单位转换（BEMF 前馈与上报）。** `EncRes` 将内部 counts/s 转换为工程速度：
  - 直线电机：$\frac{\text{magneticPitch}\,[\text{m}]}{\text{EncRes}}$ —— counts/s 转 m/s（此处 `EncRes` 为每磁距的计数）。
  - 旋转电机 / 直流有刷电机：$\frac{60}{\text{EncRes}}$ —— counts/s 转 rpm（此处 `EncRes` 为每转的计数）。
  - 音圈电机：$\frac{1}{\text{EncRes}}$；`EncRes` 没有物理换相作用，可保留为任意值。

`EncRes` 是*原始*编码器分辨率；[Pos](../../10-motion/01-kinematics-status/Pos.md) 及其导出量的每轴单位显示缩放由 [UsrUnits](UsrUnits-AuxUsrUnits.md) 单独处理。

## 示例

```text
AEncRes=10000        ; 10000 counts per revolution (rotary) or per pitch (linear)
AEncRes             ; query the configured encoder resolution
```

## 参见

- [MotorType](../../02-motor-and-amplifier/MotorType.md) — 决定如何解释 `EncRes`
- [PolePrs](../../02-motor-and-amplifier/PolePrs.md) — 极对数，与 `EncRes` 结合用于换相
- [EncType](EncType-AuxEncType.md) — 编码器反馈类型
- [UsrUnits](UsrUnits-AuxUsrUnits.md) — 在原始计数之上应用的用户单位显示缩放
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 以编码器计数测量的反馈位置
