---
summary: 启用 CNC 队列 A（或 B）参考输出上的位置滤波器。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAPosFOn/CNCBPosFOn

启用 CNC 队列 A（或 B）参考输出上的位置滤波器。

## 概述

`CNCAPosFOn`（及其在第二 CNC 引擎上的对应项 `CNCBPosFOn`）用于启用 CNC 路径上的路径跟随位置滤波器。设置为 `1` 时，由 [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md) 定义的滤波器将在合成路径位置参考分配给各成员轴之前对其进行平滑处理；设置为 `0`（默认值）时，参考直接通过，不经滤波。对路径参考进行平滑处理可同时减少传递到所有成员轴机械部件的加加速度。它作用于整个 CNC 引擎（而非单个成员轴），保存至闪存，并可在任何时刻（包括运动中）进行修改。

该关键字仅接受 `0`（滤波器关闭）和 `1`（滤波器开启）。

## 工作原理

该滤波器作用于合成 CNC 路径参考，因此启用后可同时平滑所有成员轴，并保持协调几何关系的一致性。滤波器系数本身来自 [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md)；本关键字仅将该滤波器切换至路径中或从路径中切除。

当 CNC 路径开始时，控制器验证 `CNCAPosFOn` 与 [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md) 的组合：若滤波器已启用，定义必须描述一个有效的滤波器，否则运动将被拒绝。请先设置定义，再启用滤波器。在路径运行期间直接写入本关键字会更新存储值，但不会单独对实时滤波器进行重新整定；新设置将在下一次路径启动时应用。该滤波器仅在 CNC 路径运行期间起作用。如需在路径中途切换滤波器的开启或关闭状态，路径程序可将一个专用参数修改段排入队列，该段更新相同的启用标志和定义；当该段被执行时，控制器在后台重新计算工作系数，而不会中断队列。

## 示例

```text
ACNCAPosFOn=0        ; 位置滤波器禁用（默认值）
ACNCAPosFOn=1        ; 将 CNCAPosFDef 位置滤波器应用于 CNC 路径参考
```

## 另请参阅

- [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md) — 启用时所应用的滤波器定义
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 队列段数据
