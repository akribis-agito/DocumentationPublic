---
keyword: Reset
summary: 执行软件重新上电；重启时重新加载闪存参数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 234
attributes:
  access: ro
  scope: non-axis
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Reset

执行软件重新上电；重启时重新加载闪存参数。

## 概述

`Reset` 执行控制器的软件重新上电。重启时，加载存储在闪存中的参数，覆盖易失性存储器中任何未保存的更改。可用它来应用仅在启动时生效的设置（例如在 [Save](Save.md) 之后），或将控制器返回到其保存状态。`Reset` 是一个**命令**（无值），不能在电机使能或运动中发出。

## 工作原理

`Reset` 是一次受控的、优雅的重启——它与切断电源不同，但会使固件完整地重新经历其上电流程：

1. **先确认。** 控制器在复位*之前*发送正常的命令确认，然后等待约一到两秒，以便在处理器重启前完整传输回复（包括任何正在传输的串口输出）。因此上位机会先收到确认，然后在控制器重启期间短暂失去连接。
2. **使硬件静默。** 关闭串行总线并复位 FPGA，使驱动器输出进入安全状态，而不是停留在它们原来的状态。I/O 引脚恢复到引导程序所期望的模式。
3. **重启。** 禁用中断，执行跳转到固件的启动入口点——与硬件复位后到达的相同点。

在随后的启动过程中，固件重新初始化，运行 [Load](Load.md) 以恢复保存的参数，并且——如果设置了 [AutoExec](AutoExec.md) 且存在用户程序——开始运行该程序。由于重新加载了闪存，任何未保存的修改都会被丢弃；如果希望当前设置在复位后保留，请先运行 [Save](Save.md)。

## 边界情况

- **电机使能 / 运动中。** 被拒绝——解释器返回错误。复位前请停止轴并禁用电机。
- **未保存的修改。** 在 `Reset` 时丢失——控制器以上一次 [Save](Save.md) 的内容重新启动。如果希望更改保留，请先保存。
- **Central-i 端口。** 主站的复位会拆除每条链路；端口只有在启动期间由 [CIAutoConnect](../05-central-i/CIAutoConnect.md) 驱动时（或在上位机重新发出 [CIConnect](../05-central-i/CIConnect.md) 之后）才会重新建立。
- **上位机链路。** 先发送复位确认，然后控制器等待约 1–2 秒才真正重启，以便回复能够发出；上位机应预期链路会断开并随后重新打开。

## 示例

```text
AReset               ; software power cycle (motor must be off)
```

## 参见

- [Save](Save.md) — 复位前持久化保存参数
- [Load](Load.md) — 从闪存重新加载而无需重新上电
- [AutoExec](AutoExec.md) — 复位后自动启动用户程序
