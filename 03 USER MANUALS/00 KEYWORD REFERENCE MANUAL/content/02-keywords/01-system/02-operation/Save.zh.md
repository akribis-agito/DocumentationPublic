---
keyword: Save
summary: 将所有可保存至闪存的参数从易失性存储器写入闪存。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 232
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
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# Save

将所有可保存至闪存的参数从易失性存储器写入闪存。

## 概述

`Save` 将参数持久化保存至非易失性（闪存）存储器。它首先擦除闪存中专用的参数区，然后遍历关键字表，将每个可保存至闪存的参数从易失性（RAM）存储器复制到其中——因此存储集始终反映控制器的当前配置。未保存的设置会在下一次重新上电或 [Load](Load.md) 时丢失。

`Save` 是一个**命令**（不取值）。它**不允许在电机使能或运动中执行**——解释器在这些状态下会以错误拒绝它，并且该操作在写入期间会阻塞主循环。给定参数是否被包含取决于其 `flash` 属性（在每个关键字的 Quick Facts 中显示）；只读和实时状态关键字不会被保存。

## 工作原理

`Save` 分三个阶段运行：

1. **擦除。** 首先擦除闪存中的参数块。如果擦除或任何后续编程步骤失败，`Save` 会中止并返回错误，而不是留下不完整的集合。
2. **写入记录。** 固件按 CAN 码扫描关键字表。对于每个设置了 `flash` 属性的参数，它写入一条自描述记录，以便即使将来的固件版本更改了参数的大小或轴布局，也能正确地重新读取数据。对于轴相关参数，该记录会按每个轴重复一次。每条记录为：

   | 字段 | 大小 | 内容 |
   |-------|------|----------|
   | CAN code | 1 word | 参数的 CAN 码，轴号打包在高位 |
   | Element count | 1 word | 数组成员的数量（标量为 1） |
   | Value(s) | 2 words each | 每个元素的 32 位值 |

   写入时，会在这些值上累加一个运行中的**参数校验和**（[ParamCS](../01-status/ParamCS.md) 字）。保留三种校验和变体，以便上位机在比较配置时可以忽略易变的标识字段（例如网络 IP/MAC 地址）。
3. **最终确定。** 在最后一个参数之后，`Save` 写入一个标记，记录最后存储的 CAN 码（供 [Load](Load.md) 用于得知保存集的结束位置）以及一个整区累加校验和，[Load](Load.md) 在每次恢复时都会重新校验它。如果在关键字表遍历完之前闪存已满，`Save` 会返回 "flash full" 错误。

由于该操作可能耗费明显的时间，固件在整个写入期间保持看门狗满足。在 central-i 上，命令会立即被确认——一个早期的空回复告知上位机操作已开始——并且由于漫长的闪存写入会阻塞通常喂养看门狗的循环，固件会预加载后台看门狗喂养约 120 秒。因此，上位机在将 `Save` 视为挂起之前，应允许最终 OK/错误回复最多等待大约那么长的时间。每个数组的索引 0 都被有意排除在校验和和上位机上传之外（数组是 1 索引的）。

## 示例

```text
ASave                ; persist current parameters to flash (motor must be off)
```

### 演练：保存当前配置并重启

将您的修改持久化保存至闪存，重启控制器，并确认返回的就是保存的集合。整个过程中电机必须关闭。

```text
AMotorOn=0           ; ensure the motor is off (Save is rejected otherwise)
AParamCS[1]          ; (optional) note the pre-save checksum for comparison
ASave                ; persist all flash-saveable parameters to flash
AParamCS[1]          ; checksum after save — reflects what was written
AReset               ; software power cycle; firmware auto-runs Load on restart
                     ; ... reconnect, then ...
AParamCS[1]          ; same value as the post-save checksum — confirms a clean restore
```

如果 `Reset` 前后的 `ParamCS[1]` 与保存后的 `Save` 值相匹配，则您保存的参数就是控制器上正在运行的参数。要在忽略各单元网络标识的情况下跨单元比较功能配置，请使用 `ParamCS[1]`；要验证包括 IP 和 MAC 在内的完全匹配，请使用 `ParamCS[3]`。

## 边界情况

- **电机使能 / 运动中。** 被拒绝——解释器返回错误且不写入任何内容。请先停止轴并禁用电机。
- **闪存错误。** 擦除失败返回错误 27，写入失败返回错误 28；任一情况下 `Save` 都会中止，而不是留下不完整的集合。
- **闪存板 / 构建不匹配。** 如果固件所针对构建的闪存芯片布局与其运行的板不匹配，`Save` 会在写入任何内容之前拒绝，并返回错误 251 或 252（单闪存与双闪存板不匹配，取决于构建）。这可防止以错误的闪存几何结构写入参数区。
- **闪存已满。** 如果参数集超出保留的闪存空间，`Save` 会在写入能容纳的部分后返回 "flash full" 错误（29）；在下一次 [Load](Load.md) 时只恢复实际写入的记录，缺失的参数恢复为其默认值。
- **Save 中途断电。** 由于 `Save` 会先擦除该区域，在最终校验和/标记写入之前断电会使该区域不完整；在下一次上电时 [Load](Load.md) 检测到校验和不匹配，固件会将所有参数初始化为其默认值（而不是加载不完整的集合）。
- **Central-i 断开。** 保存操作针对主站自身的参数，不受与任何远程单元链路状态的影响。

## 另请参阅

- [Load](Load.md) — 从闪存重新加载参数（并重新校验此处写入的校验和）
- [SaveUser](SaveUser.md) — 保存至单独的用户区而非主集
- [Reset](Reset.md) — 软件重新上电；重启时重新加载保存集
- [ParamCS](../01-status/ParamCS.md) — 此命令计算的参数校验和
