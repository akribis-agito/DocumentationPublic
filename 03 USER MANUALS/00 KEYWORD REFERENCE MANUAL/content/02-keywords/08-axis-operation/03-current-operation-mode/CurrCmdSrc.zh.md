---
keyword: CurrCmdSrc
summary: 选择电流模式下电流参考的来源。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 330
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 3
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrCmdSrc

选择电流模式下电流参考的来源。

## 概述

在电流运行模式下，`CurrCmdSrc` 设定电流指令（`CurrRef`）的来源。每个控制周期，控制器根据所选来源生成电流参考；同一值还决定轴如何以及何时自动从电流模式退出回到位置模式（参见 [电流运行模式](00-overview.md)）。`CurrCmdSrc` 仅在轴实际处于电流模式（[OperationMode](../01-general-keywords/OperationMode.md) = 1）时才被查询。

## 工作原理

控制器根据该值生成电流参考，如下所示：

| 值 | 来源 | 生成机制 |
|----|----|----|
| 0 | 模拟量电流指令输入 | `CurrRef` 直接由配置为电流指令的滤波后模拟量输入设定（参见 [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)）。轴在电流模式中停留 [CurrCmdHTime](CurrCmdHTime.md)`[1]`（若为负值则无限期停留）。 |
| 1 | 用户自定义表 | `CurrRef` 逐步遍历 [CurrCmdVal](CurrCmdVal.md) 表，以 [CurrCmdSlope](CurrCmdSlope.md) 向每个条目斜坡变化并保持 [CurrCmdHTime](CurrCmdHTime.md)，通过 [CurrCmdIndex](CurrCmdIndex.md) 推进。 |
| 2 | 用户自定义表（插值） | 在当前固件中与值 1 的处理相同 — 插值处理保留用于未来版本。 |
| 3 | 主轴电流指令 | `CurrRef` 从主轴的 `CurrRef` 复制（主轴由 [CurrRefMaster](CurrRefMaster.md) 选择）。与模拟量来源完全一样由 [CurrCmdHTime](CurrCmdHTime.md)`[1]` 计时。**仅 central-i v5。** |

任何意外值都会强制 `CurrRef` 为 0。

无论选择哪个来源，生成的 `CurrRef` 随后都会经过共享的电流输出级：它被电流限制（[CurrLimMode](../../06-protections/02-current-and-voltage/CurrLimMode.md) / [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)，饱和时设置 [StatReg](../../07-status-and-faults/StatReg.md) bit 21）钳位，并在到达电流环之前由 [CurrDir](../../09-current-and-voltage/02-motor-variables/CurrDir.md) 反向。超过活动限制的值无论来源如何都会被限幅。

> **注意：** 值 1 和 2 当前行为相同。值 3（主轴从轴驱动器）仅存在于 central-i v5 固件中；standalone/v4 固件仅接受 `CurrCmdSrc` 为 0–2。

## 示例

```text
ACurrCmdSrc=1        ; use the user-defined CurrCmdVal table
ACurrCmdSrc=3        ; follow a master axis (slave drive, central-i v5)
```

### 边界情况

- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 1）— 不查询 `CurrCmdSrc`；写入立即生效，但新来源仅在轴进入电流模式后才适用。
- **超出范围** — 超出有效范围（v4 上为 `0`–`2`，v5 上为 `0`–`3`）的值会被参数表以超出范围错误**拒绝**，而不会被接受。（电流生成器在遇到意外来源值时强制 `CurrRef = 0` 的回退是内部保护机制，而非参数表已经拒绝的用户写入所走的路径。）
- **来源 0 但无模拟量映射** — 若没有模拟量输入通过 [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md) 映射到功能 2（电流指令），则 `CurrRef` 读为 `0`。
- **v4 上的来源 3** — 被 v4 参数表拒绝（最大值为 2）；尝试 `CurrCmdSrc = 3` 返回超出范围错误。
- **主轴丢失（来源 3）** — 若 [CurrRefMaster](CurrRefMaster.md) 指向已停止或无效的轴，则从轴的 `CurrRef` 镜像主轴所保持的任何值（通常为 `0`）。
- **保存** — 可保存至闪存；在启动时重新加载。
- **电机失能** — 任何时候都接受；该来源标志不需要电机。

## 版本间变化

central-i v5 新增来源值 3（主轴电流指令），将有效范围扩展到 0–3（standalone/v4：0–2）。来源 3 使轴成为复制主轴电流参考的从轴驱动器；参见 [CurrRefMaster](CurrRefMaster.md)。

## 另请参阅

- [CurrCmdVal](CurrCmdVal.md) — 用户自定义电流值（来源 1/2）
- [CurrRefMaster](CurrRefMaster.md) — 主轴索引（来源 3）
- [CurrCmdHTime](CurrCmdHTime.md) — 决定轴何时退出电流模式的计时
- [电流运行模式](00-overview.md) — 整体模式行为
