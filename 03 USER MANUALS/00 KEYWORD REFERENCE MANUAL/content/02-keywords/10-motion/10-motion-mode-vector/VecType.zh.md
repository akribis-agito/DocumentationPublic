---
keyword: VecType
summary: 选择矢量运动几何形状（0 = 线性，1 = 圆弧）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 630
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VecType

选择矢量运动几何形状（0 = 线性，1 = 圆弧）。

## 概述

`VecType` 定义所请求的矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）是线性（`VecType = 0`）还是圆弧（`VecType = 1`）。它选择协调路径的几何形状；当选择圆弧时，运动由 [VecArcCenter](VecArcCenter.md)、[VecArcDir](VecArcDir.md) 和 [VecNumCircles](VecNumCircles.md) 进一步描述。该参数保存至闪存，运动期间不可修改。仅接受 0（线性）和 1（圆弧）两个值。

## 工作原理

`VecType` 在运动启动时读取一次，并选择控制器在每个控制周期中将单一路径位置转换为各轴位置参考所使用的几何形状：

| 值 | 几何形状 | 成员轴 | 路径到各轴的映射方式 |
|----|----|----|----|
| 0 | 线性 | 2 个或更多 | 路径是从起始点到各轴终点的直线。总路径长度 [VecAbsTrgt](VecAbsTrgt.md) 为各轴单独距离的均方根。每个轴被驱动至路径的固定分数：其位置为起始点加上（路径分数 × 该轴的总距离），使所有轴同时起止。 |
| 1 | 圆弧 | 恰好 2 个 | 路径是两个成员轴平面内的圆弧。控制器从 [VecArcCenter](VecArcCenter.md) 和起始点推导半径，求出起始角和终止角，每个控制周期将路径位置转换为扫过角度（路径距离 ÷ 半径），再转换为圆上两轴位置。[VecArcDir](VecArcDir.md) 设置扫描方向，[VecNumCircles](VecNumCircles.md) 添加完整圈数。 |

对于两种几何形状，单一路径速度曲线（由 [VecSpeed](VecSpeed.md)、[VecAccel](VecAccel.md)、[VecDecel](VecDecel.md) 和 [VecJerk](VecJerk.md) 整形）推进路径位置；`VecType` 所选的几何形状决定该值如何在成员轴间分配。线性运动接受任意数量的成员轴（2 个及以上）；圆弧运动需要恰好两个轴，且从圆心推导的起始和终止半径必须在 3 个计数内吻合，否则运动将被拒绝。

## 示例

```text
AVecType=0           ; 线性矢量（默认）
AVecType=1           ; 圆弧矢量
```

### 演练：在轴 A 和 B 上运行线性后接圆弧路径

矢量运动按每次运动配置，并在编号最小的成员轴发出 `Begin` 后运行。以下示例在两轴组 `{A, B}` 上先运行直线，再运行圆弧。每次运动配置完毕、启动并允许结束后，再设置下一次运动；`VecType` 在运动期间不可修改。

```text
; ===== 运动 1：从当前点线性运动至 (15000, 5000) =====
; --- 1) 在编号最小的轴（A）上配置组 ---
AVecMemberAxes=3              ; 位 0 (A) + 位 1 (B) = 3
AVecType=0                    ; 0 = 线性

; --- 2) 使用 AbsTrgt 设置各轴终点 ---
AAbsTrgt=15000                ; 轴 A 终点
BAbsTrgt=5000                 ; 轴 B 终点

; --- 3) 在主轴（轴 A）上设置路径速度曲线 ---
AVecSpeed=8000
AVecAccel=20000
AVecDecel=20000

; --- 4) 使能矢量运动 ---
AMotionMode=16                ; 16 = 矢量
ABegin                        ; 控制器计算 VecAbsTrgt 并运行路径

; --- 5) 运动期间观察路径 ---
AVecPosRef                    ; 沿路径的当前运行位置（0 -> VecAbsTrgt）
AVecAbsTrgt                   ; 总路径距离（此处为 sqrt(dA^2 + dB^2)）
; ... 等待运动中状态清除 ...

; ===== 运动 2：顺时针圆弧，额外一整圈 =====
AVecType=1                    ; 1 = 圆弧（需要恰好两个成员轴）
AVecArcCenter=15000           ; 轴 A 上的圆心坐标（各轴标量）
BVecArcCenter=10000           ; 轴 B 上的圆心坐标（各轴标量）
AVecArcDir=1                  ; 扫描方向（参见 VecArcDir）
AVecNumCircles=1              ; 在扫过角度上额外增加一整圈
AAbsTrgt=20000                ; 圆弧终点，轴 A
BAbsTrgt=10000                ; 圆弧终点，轴 B
ABegin
```

若运动在 `Begin` 时被拒绝，请检查 `VecMemberAxes` 是否包含发出指令的轴，主轴是否为编号最小的成员轴，以及（对于圆弧）起始点和终止点是否在距 `VecArcCenter` 相同半径上。

## 另请参阅

- [VecArcCenter](VecArcCenter.md) — 圆弧圆心/半径（圆弧类型）
- [VecArcDir](VecArcDir.md) — 圆弧扫描方向（圆弧类型）
- [VecMemberAxes](VecMemberAxes.md) — 构成矢量的各轴
