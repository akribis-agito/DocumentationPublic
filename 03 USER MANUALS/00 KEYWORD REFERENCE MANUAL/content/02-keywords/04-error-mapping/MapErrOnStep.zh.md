---
keyword: MapErrOnStep
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 476
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
  - 16384
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: 映射接入时用于施加映射修正的步长。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MapErrOnStep

映射接入时用于施加映射修正的步长。

## 概述

`MapErrOnStep` 控制误差映射修正的**接入/退出斜坡**——即当 [MapType](MapType.md) 变为非零时整个修正（表值加上 [MapErrOffset](MapErrOffset.md) 分量）如何渐入，以及当其返回零时如何渐出。斜坡可防止在映射开启或关闭瞬间反馈中出现位置跳变。它与 [MapErrOffRamp](MapErrOffRamp.md) 不同，后者仅对偏置进行变化。有效范围为 `0` 至 `16384`。

它是一个轴相关参数，保存至闪存，可随时更改，包括在运动中更改。

## 工作原理

控制器维护一个斜坡**计数器**，从 `0`（修正关闭）运行至满量程 `16384`。所施加的修正按 `counter / 16384` 缩放，因此该计数器实际上是未修正反馈与完全修正反馈之间的 0…1 混合因子。`MapErrOnStep` 是该计数器**每个控制周期**的变化量：

- **接入**（[MapType](MapType.md) 设为 1/2/3）：计数器每周期增加 `MapErrOnStep`，直至饱和于满量程。
- **退出**（[MapType](MapType.md) 设为 0）：计数器每周期减少 `MapErrOnStep`；当其到达 0 时，内部映射类型恢复为关闭。
- **`MapErrOnStep = 0`（默认）：** 计数器在接入时直接跳至满量程、在退出时直接跳至 0——为即时的单周期切换（无斜坡）。

步长越大接入越快。步长为 `N` 时约在 `16384 / N` 个周期内接入，因此 `MapErrOnStep = 1` 在 `16384` 个周期内渐入（在基础采样率下约 1 s），而 `MapErrOnStep = 16384` 在单个周期内渐入（实际为即时）。中间值给出受控渐变——例如 `MapErrOnStep = 16` 需 `1024` 个周期才完全接入。

## 示例

```text
AMapErrOnStep=0      ; default: switch correction in/out immediately
AMapErrOnStep=16     ; gentle fade-in over ~1024 cycles (~62 ms at 16 kHz)
AMapErrOnStep        ; read the current step size
```

### 边界情况

- **超出范围** — 超出 `0`–`16384` 的值被拒绝。
- **零步长** — 接入/退出为即时（一个周期）；修正可能在反馈中产生位置跳变。
- **运动中** — 接受；斜坡在运动期间继续推进，因此只要步长足够小以吸收修正的不连续性，在运动中更改 `MapType` 是安全的。
- **`MapType = 0` 已设置** — 写入被接受，但在 `MapType` 设为非零之前，斜坡计数器保持在 `0`。
- **内部状态** — 斜坡计数器和内部映射类型与 [MapErrOffset](MapErrOffset.md) / [MapErrOffRamp](MapErrOffRamp.md) 共享；在 `MapErrOffset` 斜坡处于活动状态期间进行快速 `MapErrOnStep` 接入，会产生比预期更快的总变化。
- **快速开/关切换（斜坡中途重新接入）** — 内部映射类型仅在已完全关闭时才从零重新置位接入斜坡。如果你将 [MapType](MapType.md) 设为 0，然后在退出斜坡完成*之前*（计数器仍高于 0）又设回 1/2/3，该重新写入不会将计数器复位为 0；接入只是从计数器的当前部分值继续。因此修正的重新接入比完整斜坡更快且无位置跳变，因为反馈本来就未曾完全卸除该修正。
- **保存** — 可保存至闪存。

## 另请参阅

- [MapErrOffset](MapErrOffset.md) — 添加到修正上的恒定偏置
- [MapErrOffRamp](MapErrOffRamp.md) — 该偏置的变化速率
- [MapType](MapType.md) — 启用误差映射（其变化驱动此斜坡）
- [Pos](../10-motion/01-kinematics-status/Pos.md) — 渐入/渐出的修正反馈
