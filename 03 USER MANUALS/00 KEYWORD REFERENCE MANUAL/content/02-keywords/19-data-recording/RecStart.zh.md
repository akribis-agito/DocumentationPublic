---
keyword: RecStart
summary: 命令，用于在所选示波器上启动记录。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 248
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# RecStart

命令，用于在所选示波器上启动记录。

## 概述

`RecStart` 命令所选示波器按已配置的设置和触发关键字开始记录。记录启动后，修改设置或触发关键字（[RecParamA/RecParamB](RecParamA-RecParamB.md)、[RecGap](RecGap.md)、[RecLength](RecLength.md) 及触发关键字）不会影响正在进行的记录。每个数组索引对应一个示波器。

| 索引 | 说明                         |
|-------|------------------------------|
| 1     | 第一个示波器                 |
| 2     | 第二个示波器（如适用）       |

启动后，使用 [RecStat](RecStat.md) 监控进度；如需要，可使用 [RecTrigForce](RecTrigForce.md) 强制触发，或使用 [RecStop](RecStop.md) 中止。

## 工作原理

`RecStart` 验证配置，然后将所有设置一次性快照至记录元数据，使后续对设置关键字的修改不影响当前运行。具体步骤如下：

- 若示波器已在记录中、[RecLength](RecLength.md) 或 [RecGap](RecGap.md) 不为正值、[RecTrigPos](RecTrigPos.md) 超出 0–100 范围，或触发类型无效或掩码为零，则拒绝启动。
- 遍历 [RecParamA/RecParamB](RecParamA-RecParamB.md) 以统计并解析通道，拒绝未知代码、命令及无效轴/索引引用；若通道数 × `RecLength` 超出缓冲区，则拒绝启动。
- 记录每个通道的数据类型和用户单位比例因子，将触发阈值转换为内部单位，并初始化用于检测边沿和变化的触发源前值/初值。
- 根据 `RecTrigPos` 计算触发前的采样点数和触发后所需点数，然后清除缓冲区索引和计数器。

随后通过将 [RecStat](RecStat.md) 设为 1（填充触发前数据）来使示波器进入就绪状态。若未配置触发（第一个触发类型为"无"），示波器直接跳至状态 3（已检测到触发）并立即记录完整请求长度。

## 示例

```text
ARecStart[1]         ; 在第一个示波器上启动记录
ARecStart[2]         ; 在第二个示波器上启动记录
```

## 另请参阅

- [RecStat](RecStat.md) — 记录状态
- [RecStop](RecStop.md) — 停止记录
- [RecTrigForce](RecTrigForce.md) — 强制触发
- [RecParamA/RecParamB](RecParamA-RecParamB.md) — 要捕获的参数
