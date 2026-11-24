---
keyword: ExtClearFault
summary: 向 Central-i ADP05 轴上的外部功率放大器发送清除故障脉冲。
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
last_updated: '2026-11-24'
doc_revision: '2026.11'
language: zh-CN
---
# ExtClearFault

向 Central-i ADP05 轴上的外部功率放大器发送清除故障脉冲。

先停止轴运动并关闭电机，再执行此命令。命令无参数。A 轴的命令如下。

```text
AExtClearFault
```

控制器确认收到请求后，在 ADP05 的 Central-i 控制周期中将故障清除位置位一个周期。请查看放大器的故障指示，以确认故障已清除。
