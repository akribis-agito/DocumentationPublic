---
keyword: DTCompLvl
summary: 零电流附近对死区补偿进行插值（而非切换）的电流区间，单位 mA。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 868
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: [0, 1000]
  default: 1
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# DTCompLvl

零电流附近对死区补偿进行插值（而非切换）的电流区间。

## 概述

死区补偿所叠加电压的**符号**跟随指令相电流。在过零点附近该符号难以确定，若直接切换会使补偿因噪声而反复翻转。`DTCompLvl` 以 mA 为单位设定零电流附近该区间的半宽，在此区间内符号采用线性斜坡而非直接切换。

## 工作原理

对各相，设指令电流为 `i`：

- `i > DTCompLvl` → 全额正向补偿
- `i < −DTCompLvl` → 全额负向补偿
- 其他情况 → 补偿按 `i / DTCompLvl` 缩放

> **注意：** `DTCompLvl` 必须大于零。插值斜率为 `1/DTCompLvl`，取值为零将导致除零；驱动器通过禁用该斜率来防护，其结果是补偿变为直接切换。

### 取值选择

将其设为略高于电流测量噪声底的水平。取值过小，补偿会在过零附近抖振；取值过大，则一段有实际意义的低电流工作区间只能获得部分补偿——而这恰恰是死区影响最严重的区间。

### 边界情况

- **禁用时无效：** 当 [DTCompGain](DTCompGain.md) 为 0 时，本关键字完全不起作用。
- **范围：** 超出 `0…1000` mA 的写入将被钳位。

## 示例

```text
ADTCompLvl=50        ; 在零电流 +/-50 mA 内插值
```

## 另请参阅

- [DTCompGain](DTCompGain.md) — 补偿增益本身
