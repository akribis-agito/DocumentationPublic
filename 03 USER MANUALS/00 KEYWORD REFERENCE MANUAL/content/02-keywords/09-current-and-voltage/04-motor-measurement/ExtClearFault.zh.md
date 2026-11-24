---
keyword: ExtClearFault
summary: 向所连接的 ADP05 外部驱动器发送一个控制周期的清除故障请求。
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 906
availability:
- controller
- ci-master
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# ExtClearFault

停止运动并关闭电机后，输入 `AExtClearFault`，向连接在 A 轴上的 ADP05（AGL105）驱动器请求清除故障。对于其他轴，请替换轴字母。

控制器将请求置入该轴的命令字后即应答。控制中断将清除故障位发送给远程单元，持续一个控制周期后将其清零。请在请求后检查驱动器的故障状态，以确认故障是否已清除。

本命令无需参数。Central-i ADP03、ADP04 和 ADP05 接口的电流反馈比例及偏置见 [ExtAmpConfig](ExtAmpConfig.zh.md)。
