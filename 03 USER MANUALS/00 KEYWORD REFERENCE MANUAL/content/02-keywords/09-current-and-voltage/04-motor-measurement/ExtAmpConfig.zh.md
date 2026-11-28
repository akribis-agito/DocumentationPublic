---
keyword: ExtAmpConfig
summary: 设置外部驱动器的电流反馈比例及各相的电流偏置。
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 866
availability:
- controller
- ci-master
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -4000.0
  - 4000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# ExtAmpConfig

对于配有 ADP03、ADP04 或 ADP05 外部驱动器接口的 Central-i 主站，请在该远程单元所连接的轴上使用 `ExtAmpConfig`。以下五个浮点参数随轴参数保存。

| 索引 | 设置 | 单位 | 默认值 |
| --- | --- | --- | --- |
| 1 | 两路相电流反馈共用的比例因子 | 比例因子 | 远程单元初始化时为 −1.049041748046875 |
| 2 | A 相（Ia）电流指令偏置 | mA | 0 |
| 3 | B 相（Ib）电流指令偏置 | mA | 0 |
| 4 | A 相（Ia）电流反馈偏置 | mA | 0 |
| 5 | B 相（Ib）电流反馈偏置 | mA | 0 |

参数表将五个元素均初始化为零。上述远程单元初始化时，如果元素 1 为零，则写入表中所列比例因子；已保存的非零比例因子会保留。负比例因子反转反馈极性。

对于数字 SPI 驱动器，指令通道先加上相应的指令偏置，再乘以 `32768 / AAmpFullScale`。例如，比例为 8 计数/mA、Ia 指令为 1,000 mA 且 `ExtAmpConfig[2]=250` 时，DAC 输出码为 42,768。反馈通道先对去除中点值的采样值进行缩放，再减去对应的反馈偏置。

读取 `AExtAmpConfig[1]` 可查看 A 轴的比例因子，读取 `AExtCurrCmdVal[1]` 可查看发往驱动器的 A 相 DAC 码。[ExtCurrCmdVal](ExtCurrCmdVal.zh.md) · [AAmpFullScale](../../02-motor-and-amplifier/AAmpFullScale.zh.md)
