---
summary: 定义 CNC 队列 A（或 B）位置滤波器配置的数组。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAPosFDef/CNCBPosFDef

定义 CNC 队列 A（或 B）位置滤波器配置的数组。

## 概述

`CNCAPosFDef`（及其在第二 CNC 引擎上的对应项 `CNCBPosFDef`）是为 CNC 路径定义路径跟随位置滤波器的数组。它描述了在路径参考分配给各成员轴之前对 CNC 合成路径参考进行平滑处理的滤波器，从而减少传递到机械部件的加加速度。仅当 [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md) 将其启用时，该滤波器才会生效。它作用于整个 CNC 引擎（而非单个成员轴），保存至闪存，并可在任何时刻（包括运动中）进行修改。

## 工作原理

该数组使用控制器的标准可自定义位置滤波器定义方式：元素 1 选择滤波器**类型**，元素 2–5 为该类型提供最多四个**参数**。类型为 `0`（默认值）表示无滤波器，路径参考直接通过。当选定某种滤波器类型且 [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md) = 1 时，控制器根据这些参数推导工作系数，并对合成路径参考施加二阶（biquad 风格）平滑滤波器。同样的定义约定在控制器的其他可自定义位置滤波器中同样适用。

定义在路径开始时进行检查（仅在滤波器启用时才会验证）：类型与参数的无效组合将导致运动被拒绝，因此在使用 [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md) 启用滤波器之前，请验证各数值。工作系数在此时由该数组推导得出。在路径运行期间直接写入数组会更新存储值，但不会自行重新计算实时滤波器；新定义将在下一次路径启动时生效。如需在路径运行期间重新整定滤波器，路径程序可将一个专用参数修改段排入队列，该段携带新的启用标志及五个定义元素；当该段被执行时，控制器在后台重新计算工作系数，从而可在路径的特定位置更改平滑效果，而不会中断队列。

## 示例

```text
ACNCAPosFDef[1]=0    ; 元素 1 = 滤波器类型（0 = 无滤波器，默认值）
ACNCAPosFDef[1]      ; 读取滤波器类型元素（数组从 1 开始索引）
ACNCAPosFDef[2]      ; 读取第一个滤波器参数
```

## 另请参阅

- [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md) — 启用/禁用此位置滤波器
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 队列段数据
