---
keyword: BuffSplineMod
summary: 选择执行缓冲曲线时使用的样条插值模式。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 544
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
  - 1
  - 3
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BuffSplineMod

选择执行缓冲曲线时使用的样条插值模式。

## 概述

`BuffSplineMod` 选择计算缓冲曲线时通过 [BuffPos](BuffPos.md) 和 [BuffTime](BuffTime.md) 中路径点拟合的曲线类型。范围为 1 到 3，默认值为 3（三次曲线）。[BuffCalc](BuffCalc.md) 运行时，**主轴**的模式应用于所有成员轴。`BuffSplineMod` 保存至闪存，可随时修改，但修改只有在重新运行 [BuffCalc](BuffCalc.md) 后才会生效。

## 工作原理

每个值选择路径点之间不同的插值阶次。阶次越高，运动越平滑（导数连续阶次越高），但路径点之间超调的自由度越大；阶次越低，对路径点的跟踪越精确。

| 值 | 含义 |
|---|---|
| 1 | 线性插值。路径点之间为直线段。位置连续，但速度在每个路径点处发生突变（曲线在每个节点处有折角）。 |
| 2 | 抛物线样条。每段为二阶（二次）曲线。位置和速度在路径点处连续，实现平滑的速度过渡；加速度在节点处可能发生突变。 |
| 3 | 三次曲线样条（默认）。每段为三阶曲线。位置、速度和加速度在内部路径点处连续，产生三种模式中最平滑的运动。 |

抛物线和三次曲线模式的边界行为——在第一个和最后一个路径点处的约束——由 [BuffEdgeMode](BuffEdgeMode.md) 设定，可选用 [BuffSlopes](BuffSlopes.md) 中的边缘斜率。线性插值忽略边界设置，因为它没有自由端导数需要约束。

拟合完成后，[BuffCalc](BuffCalc.md) 将所选曲线扩展为每个伺服采样一个插值点并存储于内部，因此样条类型仅影响存储曲线的形状，不影响回放方式。

## 示例

```text
ABuffSplineMod=1     ; 路径点之间为直线段
ABuffSplineMod=2     ; 抛物线（速度连续）
ABuffSplineMod=3     ; 三次样条（默认，最平滑）
```

### 操作演示：定义路径点并执行一个三次样条周期

将四个路径点加载至 [BuffPos](BuffPos.md) 和 [BuffTime](BuffTime.md)（带零终止符），拟合三次样条，然后运行一个周期。假设轴 A 为单成员组的主轴，电机已使能且未处于运动中。

```text
; --- 1) 加载路径点位置（每个节点一个条目）---
ABuffPos[1]=0
ABuffPos[2]=5000
ABuffPos[3]=8000
ABuffPos[4]=10000

; --- 2) 加载对应的时间戳（严格递增，以零结尾）---
ABuffTime[1]=200              ; 路径点 1 的伺服采样索引
ABuffTime[2]=600              ; 路径点 2
ABuffTime[3]=900              ; 路径点 3
ABuffTime[4]=1200             ; 路径点 4（== 每周期采样数，BuffStatus[6]）
ABuffTime[5]=0                ; 终止符——必须设置

; --- 3) 选择曲线形状及周期重复次数 ---
ABuffSplineMod=3              ; 1 = 线性，2 = 抛物线，3 = 三次（默认）
ABuffEdgeMode=0               ; 起始/末端边界条件（参见 BuffEdgeMode）
ABuffCycles=1                 ; 执行一次周期

; --- 4) 在主轴上预计算轨迹 ---
ABuffCalc                     ; 若 BuffTime 未有效填充则拒绝执行

; --- 5) 使能样条缓冲运动 ---
AMotionMode=18                ; 18 = 样条缓冲
ABegin                        ; 控制器将存储的点流式传输至 PosRef

; --- 6) 观察回放状态 ---
ABuffStatus[4]                ; 当前播放的周期（1..BuffCycles）
ABuffStatus[5]                ; 周期内采样索引（1..BuffStatus[6]）
ABuffStatus[6]                ; 每周期采样数（= 最后一个 BuffTime 值）
```

对 `BuffPos`、`BuffTime`、`BuffSplineMod`、`BuffEdgeMode` 或 `BuffSlopes` 的修改会将轨迹标记为"过期"：在重新运行 `BuffCalc` 之前，下一次 `Begin` 将被拒绝。可通过 [StopBuff](../04-motion-command/StopBuff.md) 在下一个周期边界处结束运动。

## 参见

- [BuffEdgeMode](BuffEdgeMode.md) — 应用于抛物线/三次曲线拟合的起始/末端边界条件
- [BuffSlopes](BuffSlopes.md) — 边界条件需要时使用的边缘斜率
- [BuffPos](BuffPos.md) — 路径点位置
- [BuffTime](BuffTime.md) — 路径点时间戳
- [BuffCalc](BuffCalc.md) — 拟合所选曲线并扩展轨迹
