---
keyword: RegenOff
summary: 再生电阻被停用的直流母线电压阈值（mV），低于或等于该值时停用。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 96
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 12000
  - 95000
  default: 95000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RegenOff

再生电阻被停用的直流母线电压阈值（mV），低于或等于该值时停用。

## 概述

`RegenOff` 设置直流母线电压阈值（mV），当母线电压等于或低于该值时，再生（制动电阻）电路被切断。在母线电压上升越过 [RegenOn](RegenOn.md) 且制动斩波器晶体管导通后，电阻持续耗散能量，直到母线电压 [VBus](../01-system-variables/VBus.md) 回落至 `RegenOff`，此时斩波器被切断。因此 `RegenOff` 是开关迟滞的下边沿。

## 工作原理

`RegenOff` 是 [RegenOn](RegenOn.md) 的配对项；只要 [RegenUsed](RegenUsed.md) ≠ 0，二者就会在同一再生步骤中被评估（在 central-i 上为按轴，在独立控制器上为控制器范围）：

| 条件 | 动作 |
|-----------|--------|
| `VBus ≥ RegenOn`  | 斩波器开启，[StatReg](../../07-status-and-faults/StatReg.md) 位 1 置位 |
| `VBus ≤ RegenOff` | 斩波器关闭，`StatReg` 位 1 清除 |
| `RegenOff < VBus < RegenOn` | 无变化——斩波器保持当前状态 |

比较为 `VBus ≤ RegenOff`（含等号），因此电阻在母线电压达到该阈值的瞬间即被切断。`RegenOff` 与 `RegenOn` 之间的间隙就是防止斩波器抖动（频繁通断）的死区：应使其足够宽，以覆盖电阻通断所产生的母线电压纹波。请设置 **`RegenOff` < `RegenOn`**——二者相等会消除迟滞，而 `RegenOff` > `RegenOn` 不是有效配置。迟滞图请参见 [RegenOn](RegenOn.md)。

再生阈值不是在每个控制周期都被检测的。控制器以 16 步轮询方式处理其周期性检查（每个控制中断执行一步），`RegenOn`/`RegenOff` 比较在其中一步中运行——因此 `VBus` 每 16 个控制中断才与阈值比较一次。所以斩波器可能在 `VBus` 越过阈值后延迟至多 16 个控制中断周期才进行切换。请合理设置死区（`RegenOn` − `RegenOff`），使母线电压在该时间间隔内无法反向越过另一阈值，从而防止斩波器抖动。

在独立控制器上，`RegenOn` 与 `RegenOff` 的默认值、最小值和最大值与 [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md) 共用。在出厂默认情况下，两个阈值都等于 `MaxVBus` 的默认值，因此没有迟滞间隙，激活点与过压限值重合。在依赖再生电路之前，你必须自行降低 `RegenOff`（通常还有 `RegenOn`），以在 `MaxVBus` 以下创建一个可用的死区。

## 示例

```text
ARegenOff=75000      ; deactivate regen once the bus falls back to 75 V (mV)
ARegenOff            ; read the present deactivation threshold
```

## 另请参阅

- [RegenOn](RegenOn.md) — 激活阈值（迟滞的上边沿；含示意图）
- [RegenCurr](RegenCurr.md) — 斩波器开启时测得的再生电阻电流
- [RegenUsed](RegenUsed.md) — 使能再生电路；为 0 时忽略阈值
- [VBus](../01-system-variables/VBus.md) — 与此阈值比较的母线电压
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 1 报告再生处于激活状态
