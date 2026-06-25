---
keyword: MapErrOffset
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 411
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: 在映射修正之上叠加应用的当前位置误差偏置。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MapErrOffset

在映射修正之上叠加应用的当前位置误差偏置。

## 概述

`MapErrOffset` 是一个加到插值后映射修正上的**目标**位置误差偏置（以编码器 counts 为单位）。它允许你在 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 所产生结果的基础上，再用一个常量来偏置校正位置——例如在不重新测量映射的情况下微调残余偏置。映射本身由 [MapType](MapType.md) 启用。

它是一个轴相关参数，不保存至闪存，且不能在轴处于运动中或电机使能时更改。

## 工作原理

你写入的值是**目标值**；固件不会以阶跃方式应用它。在内部，固件维护一个单独的*实际*偏置，该偏置每个控制周期以固定量向 `MapErrOffset` 逼近：

$$
\text{actual} \mathrel{+}= \text{MapErrOffRamp} \cdot \text{SampleTime} \quad \text{(toward the target, clamped on arrival)}
$$

因此 [MapErrOffRamp](MapErrOffRamp.md) 设置变化速率（counts 每秒），而 `MapErrOffset` 设置目标值。每个周期将*实际*偏置加到插值后的修正上，然后该和值在加到反馈以形成 [Pos](../10-motion/01-kinematics-status/Pos.md) 之前，会先按接入斜坡进行缩放（参见 [MapErrOnStep](MapErrOnStep.md)）。以这种方式按斜坡变化意味着更改 `MapErrOffset` 会使校正位置产生平滑移动，而非突跳。实际偏置仅在内部映射类型完全恢复为关闭（退出斜坡完成）后或在仿真中才被强制为 0——而*不是*在退出斜坡过程中。

## 示例

```text
AMapErrOffset        ; read the offset target
AMapErrOffset=0      ; clear the offset (slews back to 0 at MapErrOffRamp)
AMapErrOffset=500    ; bias the corrected position by 500 counts
```

### 边界情况

- **写入时电机使能 / 运动中**——电机使能或轴处于运动中时，写入被拒绝；请改用 [MapErrOffRamp](MapErrOffRamp.md) 来控制变化速率。
- **映射关闭**（[MapType](MapType.md) = 0）——**实际**内部偏置仅在退出斜坡完全完成（内部类型已恢复为关闭）之后才被强制为 `0`。在退出斜坡退出*过程中*，实际偏置照常继续向其目标值逼近；使其从反馈中淡出的是接入斜坡计数器（整个修正按 `counter / 16384` 缩放；参见 [MapErrOnStep](MapErrOnStep.md)），而非强制将偏置归零。一旦关闭，对 `MapErrOffset` 的写入会被存储，但在映射重新接入之前不影响反馈。
- **仿真电机**——仿真中完全跳过映射，因此实际偏置无论如何都保持为 `0`。
- **变化速率始终有进展**——[MapErrOffRamp](MapErrOffRamp.md) 的最小值为 `1`，因此它永远不会为 `0`；实际偏置始终向目标值逼近（唯一的问题只是速度多快）。
- **保存**——不可保存至闪存；每次启动时复位为 `0`。

## 另请参阅

- [MapErrOffRamp](MapErrOffRamp.md) — 已应用偏置向该目标值收敛的变化速率
- [MapErrOnStep](MapErrOnStep.md) — 整个修正的接入/退出斜坡
- [MapType](MapType.md) — 启用本偏置所修改的误差映射
- [Pos](../10-motion/01-kinematics-status/Pos.md) — 本偏置所平移的校正反馈
