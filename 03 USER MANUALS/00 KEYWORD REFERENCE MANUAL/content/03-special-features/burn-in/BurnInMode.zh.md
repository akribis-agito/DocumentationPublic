---
keyword: BurnInMode
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 424
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 使能老化测试运动功能，开环连续旋转换相角以对系统进行长时间压力测试。
---
# BurnInMode

**定义：**

BurnInMode 使能老化测试运动功能，该功能通过持续旋转开环换相角，对系统进行长时间压力测试。默认值为 0（禁用），且不能通过单次写入使能：使能需要按规定的解锁序列写入特定值，任何序列外的值均会将其重置回 0（禁用）。轴运动中或电机使能时均不可修改。这是一个轴相关参数，不保存至闪存。

使能后，控制器将换相标记为已建立，并以 [BurnInFreq](BurnInFreq.md) 设定的速率开环旋转换相角，与任何指令运动无关。禁用老化测试（写入或重置为 0）后，对无刷轴而言换相将被标记为无效，因此在恢复正常闭环运动之前必须重新建立换相。

老化测试运动仅对无刷电机类型（[MotorType](../../02-keywords/02-motor-and-amplifier/MotorType.md) 配置为无刷）驱动开环换相角。对于有刷/直流、音圈、步进及仿真电机类型，老化测试功能不驱动任何换相角。

**另请参阅：**

[BurnInFreq](BurnInFreq.md)
