---
keyword: VelGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 102
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 0
    - 1000000000
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 速度环比例增益——乘以速度误差的系数。
---
# VelGain

速度环比例增益——乘以速度误差的系数。

## 概述

`VelGain` 是 PIV 级联中内环（速度环）的比例增益。每个控制周期，它将速度误差 [VelErr](../../10-motion/01-kinematics-status/VelErr.md) 相乘，构成速度 PI 输出的比例部分。该输出（比例项加上 [VelKi](VelKi.md) 积分项，经速度滤波器后），在位置模式下叠加加速度和速度前馈，构成环路侧电流参考（在 central-i v5 上报告为 [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)）。经电流补偿和注入后，最终形成驱动电流环的电机电流指令 [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)。

`VelGain` 是数组，因此可参与增益调度。未启用增益调度时，第一个元素 `VelGain[1]` 用于控制。参见 [ScheduleMode](../01-general-keywords/ScheduleMode.md)。

在龙门模式下，龙门专用速度增益将取代 `VelGain` 用于龙门轴。

## 工作原理

速度控制器作用于 [VelErr](../../10-motion/01-kinematics-status/VelErr.md)（速度参考 [VelRef](../../10-motion/01-kinematics-status/VelRef.md) 减去速度反馈）。比例项与积分项求和，并经内部缩放生成速度 PI 输出：

$$
\text{proportional} = \text{VelErr} \cdot \text{VelGain}
$$

$$
\text{VelPIOutput} = \big( \text{proportional} + \text{integral} \big) \cdot k_{\text{scale}}
$$

积分项是 `proportional × VelKi` 的累加（参见 [VelKi](VelKi.md)）。`VelPIOutput` 随后通过速度滤波器（[VelFiltOn](VelFiltOn.md) / [VelFiltDef](VelFiltDef.md)），在位置模式下叠加加速度和速度前馈，构成环路侧电流参考（在 central-i v5 上报告为 [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)）；经电流补偿和注入后，最终形成电机电流指令 [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)。

- **相乘对象：** 速度误差 [VelErr](../../10-motion/01-kinematics-status/VelErr.md)。
- **求和位置：** 其乘积与速度积分相加；该和（经内部缩放和速度滤波器，以及位置模式下的前馈后）构成环路侧电流参考，在 central-i v5 上报告为 [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)，经补偿/注入后最终为指令 [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)。
- **缩放/单位：** 作为乘数应用（缩放因子 1.0）；PI 综合结果由固定内部缩放换算为电流指令单位。

### 缩放、范围与默认值

| | v4（standalone 及 central-i）| v5（central-i）|
|---|---|---|
| 数据类型 | 32 位整数 | 32 位浮点 |
| 范围 | 0 到 1000000 | 0 到 1000000000 |
| 默认值 | 0 | 0 |

## 示例

```text
AVelGain[1]=1200    ; set the velocity-loop proportional gain (first scheduling element)
AVelGain[1]         ; read the velocity-loop proportional gain
```

### 计算示例：给定速度误差时的比例贡献

当 `VelGain = 1200`、速度误差 `VelErr = 50`（速度环单位）时，进入 PI 求和的比例项为：

`proportional = VelErr x VelGain = 50 x 1200 = 60000`

该乘积进入 PI 求和（连同积分项），然后经固定内部缩放换算为电流指令单位，再通过速度滤波器和前馈。

### 操作步骤：配置 PI 速度环并通过 StatReg 验证饱和

此步骤将内层速度环与外层位置环一起配置，然后通过状态字确认控制器是否将环路驱动至限值。

1. **设置比例增益**（未启用调度时使用第一个调度元素）：

   ```text
   AVelGain[1]=1200
   ```

2. **添加积分项**以消除稳态速度误差。输出饱和时积分自动抗积分饱和（参见 [VelKi](VelKi.md)）：

   ```text
   AVelKi[1]=80
   ```

3. **清除积分器历史**（轴静止状态下），使环路从已知状态启动：

   ```text
   AClearIntegral
   ```

4. **指令运动并观察 [StatReg](../../07-status-and-faults/StatReg.md)**。此处有三个饱和位需关注：

   ```text
   AStatReg                      ; read whole status word
   (AStatReg & 0x200000) >> 21   ; current saturation (bit 21) - current command hit PeakCL/ContCL
   (AStatReg & 0x400000) >> 22   ; voltage saturation (bit 22) - phase voltage hit MaxPWM
   (AStatReg & 0x800000) >> 23   ; velocity saturation (bit 23) - VelRef hit MaxVel
   ```

   若位 23 读为 `1`，表示位置环输出（或速度前馈）请求的速度超过 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) 的允许值，速度环正从钳位参考驱动。若位 21 读为 `1`，表示速度 PI 输出被钳位在电流限值，速度环积分器在 [VelKi](VelKi.md) 内部的抗积分饱和门中保持，直到饱和解除。位 22（电压饱和）对速度积分器的作用与位 21 相同：当指令相电压矢量在 MaxPWM 处被钳位时，电流环抗积分饱和同样门控速度环积分，因此持续的电压钳位与电流钳位一样使积分器保持。

5. **如需陷波器**以在速度 PI 输出形成电流指令前进行滤波，请在 [VelFiltDef](VelFiltDef.md) 中定义，在 [VelFiltOn](VelFiltOn.md) 中启用，然后运行 [CalcFilters](../01-general-keywords/CalcFilters.md) 使新系数生效。

## 版本变更

在 **v5（central-i）**中，`VelGain` 为浮点值，范围更宽（`0` 到 `1000000000`）；比例×误差 → PI → 电流指令的路径与之前相同。**v5 仅适用于 central-i。**

## 另请参见

- [VelErr](../../10-motion/01-kinematics-status/VelErr.md) — `VelGain` 所乘的速度误差
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — 速度环参考值
- [VelKi](VelKi.md) — 与 `VelGain` 项求和的速度积分增益
- [ClearIntegral](../01-general-keywords/ClearIntegral.md) — 将速度环积分器清零
- [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) — 环路侧电流参考（速度 PI 输出加前馈），在 central-i v5 上报告
- [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) — 补偿/注入后的最终电机电流指令
- [VelFiltOn](VelFiltOn.md) / [VelFiltDef](VelFiltDef.md) — PI 输出上的速度环滤波器
- [PosGain](../03-position-control/PosGain.md) — 外层（位置）环的比例增益
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 21（电流饱和）/ 位 22（电压饱和）/ 位 23（速度饱和）
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — 选择当前激活的数组元素
