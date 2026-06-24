---
summary: CNC 队列 A（或 B）编码器缩放比例的分子。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAEncFactNu/CNCBEncFactNu

CNC 队列 A（或 B）编码器缩放比例的分子。

## 概述

`CNCAEncFactNu`（以及第二个 CNC 引擎上的 `CNCBEncFactNu`）是应用于 CNC 路径的每轴路径到编码器缩放比例的分子。轴的有效比例为 `CNCAEncFactNu / CNCAEncFactDn`，将 CNC 路径单位映射到轴编码器计数，从而使具有不同编码器分辨率的成员轴能够参与同一协调路径，同时保持几何精度。该参数为轴相关参数，保存至闪存，与分母 [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) 配对使用，运动中不可更改。这是 CNC 引擎实际应用的分子/分母形式；单值关键字 [CNCAEncRatio/CNCBEncRatio](CNCAEncRatio-CNCBEncRatio.md) 表达相同概念，但目前无效。

## 工作原理

设置该对参数，使 `CNCAEncFactNu / CNCAEncFactDn` 等于轴所需的分辨率比例。当分子与分母相等（默认值 `1` / `1`）时，比例为 1，不应用任何缩放。两个关键字均接受 `1`-`2000` 范围内的整数，因此可以表达宽范围的有理数比例——例如 `3` / `2` 表示 1.5:1 的分辨率差异。

该比例在路径运行时应用：引擎使用它将各轴的位置参考转换为队列路径单位，并反向将队列段坐标转换回每轴位置指令。由于运动中不可更改，请在启动运动前在每个成员轴上配置该参数对。

## 示例

```text
ACNCAEncFactNu=1        ; 轴 A 上的分子 = 1（默认值）
ACNCAEncFactNu=3        ; 与 CNCAEncFactDn = 2 组合，得到 3/2（1.5:1）缩放比例
ACNCAEncFactNu          ; 读取轴 A 上的当前分子
```

## 另请参阅

- [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) — 缩放比例的分母
- [CNCAEncRatio/CNCBEncRatio](CNCAEncRatio-CNCBEncRatio.md) — 单值形式（当前无效）
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 队列段数据
