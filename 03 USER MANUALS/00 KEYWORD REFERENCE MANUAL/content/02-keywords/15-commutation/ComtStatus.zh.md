---
keyword: ComtStatus
summary: 只读数组，报告轴的实际换相（定相）状态。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 143
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 4
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ComtStatus

只读数组，报告轴的实际换相（定相）状态。

## 概述

`ComtStatus` 是报告轴实际换相状态的只读数组。用于监控由 [ComtMode](ComtMode.md) 配置的换相过程并诊断故障：正值 100 表示换相成功完成，中间值表示进行中，负值为错误代码。由于该关键字为只读且不保存至闪存，可随时读取，包括电机使能或运动中。所得电角度由 [ComtAng](ComtAng.md) 报告。

当定相状态达到 `100`（完成）时，[StatReg](../07-status-and-faults/StatReg.md) 的换相完成位（位 0）置位。对于霍尔启动切换方法（`ComtMode[1]=3` 或 `4`），一旦建立可用的粗略霍尔角（状态 `300`/`400`）即置位，并在精细化到 `100` 的过程中保持置位，因此轴可立即运行。状态 `200`（不需要换相）也会置位该位。仅在尚无可用角度（状态 `0`/`1`）或换相失败（负状态）时，该位保持清零，此时正常运动被阻止。

## 工作原理

数组包含以下元素（从 1 开始索引）：

| 索引 | 说明 |
|---|---|
| `[1]` | 定相状态。默认 0。参见下方值表。 |
| `[2]` | "跳零"搜索方法（`ComtMode[1]=0`）期间连续成功跳动次数。默认 0；搜索在 3 次连续落在范围内的跳动后完成。 |
| `[3]` | 双向搜索状态（仅限 Central-i v5）。报告双向换相搜索的进度：`0` 未使用，`1` 已置位，`2` 第一方向完成，`3` 两个方向均完成。此索引在 v4/独立版上不存在。 |

`ComtStatus[1]`（定相状态）值：

| 值 | 换相状态 |
|---|---|
| 0 | 需要换相，尚未执行。 |
| 1 | 换相进行中。 |
| 100 | 成功完成。 |
| 200 | 不需要换相（例如直流、音圈或步进电机）。 |
| 300 | 粗略换相完成，等待索引脉冲进行精细换相调整。 |
| 400 | 粗略换相完成。等待霍尔序列变化进行精细换相调整。 |
| 500 | 学习过程已更改参数（建议保存至闪存）。 |
| 600 | 老化测试模式已激活。 |
| -1 | 意外电机关闭。换相期间发生电机关闭。 |
| -2 | 所选换相方法非法。 |
| -3 | "跳零"换相失败。请检查电机、编码器和换相参数（例如电压和精度）。 |
| -4 | 检测到编码器错误。需要换相。 |
| -5 | 参数已修改。需要换相。 |
| -6 | 需要驱动器重新上电。 |
| -7 | 检测到非法霍尔序列。 |
| -8 | 换相过程中发生 Central-I 故障。 |
| -9, -10, -11, -12 | 学习过程中检测到非法霍尔序列。 |
| -14 | 换相失败：搜索期间检测到方向错误（仅限 Central-i v5）。 |
| -15 | 换相失败：搜索期间达到机械硬限位（仅限 Central-i v5）。 |
| -16 | 换相失败：精细霍尔学习期间未找到霍尔跳变（仅限 Central-i v5）。 |

非法霍尔错误（`-7`、`-9`…`-12`）在 [HallsValue](HallsValue.md) 读取 `0` 或 `7`（合法范围 1–6 之外的两种组合）时，或观测到的霍尔序列与预期顺序不符时触发。

### 老化测试模式（状态 `600`）

老化测试运动激活时（参见 [BurnInMode](../../03-special-features/burn-in/BurnInMode.md)），定相状态读取 `600`。在此模式下，控制器为无刷电机驱动*虚拟*换相：电角度以固定电气频率（由 [BurnInFreq](../../03-special-features/burn-in/BurnInFreq.md) 设置）推进，无位置反馈。[StatReg](../07-status-and-faults/StatReg.md) 换相完成位（位 0）置位，轴可在测试期间运行。当老化测试模式关闭时，由于电机在角度被开环驱动期间可能已发生移动，定相状态变为 `-5`（参数已修改——需要换相），因此正常运动恢复前必须重新运行换相。

## 示例

```text
AComtStatus[1]      ; query the phasing status
AComtStatus[2]      ; consecutive successful jumps ("jump to zero" search method)
```

## 另请参阅

- [ComtMode](ComtMode.md) — 驱动此状态的换相设置
- [ComtAng](ComtAng.md) — 瞬时换相角
- [HallsValue](HallsValue.md) — 当前霍尔传感器原始状态（与非法霍尔序列错误相关）
- [StatReg](../07-status-and-faults/StatReg.md) — 位 0 报告换相完成
