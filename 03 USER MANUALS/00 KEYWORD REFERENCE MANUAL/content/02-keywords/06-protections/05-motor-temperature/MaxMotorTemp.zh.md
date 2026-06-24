---
keyword: MaxMotorTemp
summary: 允许的最大电机温度（PT100 传感器）；超出即触发故障。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 399
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
  - 10
  - 150
  default: 80
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MaxMotorTemp

允许的最大电机温度（PT100 传感器）；超出即触发故障。

## 概述

`MaxMotorTemp` 是允许的最大电机温度，单位为 °C。如果测量得到的 [MotorTemp](MotorTemp.md) 超过该限值，控制器将禁用轴并触发故障以保护电机。该参数为轴相关参数，保存至闪存，可在任何时刻更改（范围 10…150 °C，默认 80 °C）。

> **条件：** 该限值仅在选择了温度传感器时生效，即 [MotorTempUsed](MotorTempUsed.md) ≠ 0。当 `MotorTempUsed = 0`（无传感器）时，故障检查与告警分段均被跳过。

## 工作原理

### 过温故障

控制环以约 16 kHz 运行，过温检查每约 1 ms 评估一次（告警分段在同一周期内一个独立的约 1 ms 子阶段中更新）。在电机使能且非仿真状态下，控制器每毫秒检查一次：

```text
if (MotorTempUsed != 0  &&  MotorTemp > MaxMotorTemp)
    → disable axis, raise the motor over-temperature fault, append to ErrLog
```

该动作为锁存故障：轴被禁用，[ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1040（电机温度过高），捕获一份快照，并将故障记入日志。该故障在轴重新使能时清除。

### 分级告警分段（StatReg）

在触发之前，控制器会在 [StatReg](../../07-status-and-faults/StatReg.md)（第 15–16 位）中按由 `MaxMotorTemp` 推导出的三个子阈值设置电机温度**告警**字段。每当写入 `MaxMotorTemp` 时，会重新计算分段边界：

| `MotorTemp` 分段 | StatReg 告警等级 | PCSuite LED |
|------------------|----------------------|-------------|
| < 0.88 × MaxMotorTemp | 0 —— 无 | 熄灭 |
| 0.88…0.92 × MaxMotorTemp | 1 —— 低 | 黄色 |
| 0.92…0.96 × MaxMotorTemp | 2 —— 中 | 橙色 |
| > 0.96 × MaxMotorTemp | 3 —— 高 | 红色 |
| > MaxMotorTemp | —— 故障（`ConFlt = 1040`） | —— |

因此告警会远在故障之前逐级上升，从而在状态面板上提供早期指示。

### 边界情形

- **电机失能：** 故障检查以电机使能为门控条件（如上文文档所述），因此电机失能时过温**不会**触发——传感器仍处于工作状态，但热浸只会在下次重新使能时才报故障。告警分段（StatReg 第 15–16 位）即使在电机失能时仍持续更新，因此你可以在状态面板上观察温度攀升；只是触发本身被抑制，直到下次重新使能。
- **未选择传感器：** 当 [MotorTempUsed](MotorTempUsed.md) = `0` 时，故障检查与告警分段完全被跳过，且告警字段被清除。
- **仿真模式：** 仿真状态下跳过触发（无真实传感器）。
- **范围溢出：** 超出 `10…150` 的写入将被**拒绝**（超范围错误），所存储的值保持不变——限值不会被钳位。每当一次有效的 `MaxMotorTemp` 写入被接受时，会重新计算告警分段边界。
- **清除故障：** ConFlt 码 1040 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 条目保留。
- **哪个轴触发：** 相应的 [ErrLog](../../07-status-and-faults/ErrLog.md) 条目会标记触发的轴——源标签的高 8 位携带从 1 开始的轴号（轴 A = 1），低位则携带故障码 1040——因此在多轴单元上你可以判断是哪个轴发生故障。
- **HWProtectBits / ProtectMask：** 电机过温触发不可通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽。

## 示例

```text
AMaxMotorTemp[1]=80    ; trip axis A if motor temperature exceeds 80 °C
AMaxMotorTemp          ; read the current limit
```

### 操作演练：验证告警分段在触发前逐级上升

确认传感器已启用，设置触发上限，然后在热浸（长占空比）过程中观察告警分段攀升：

```text
AMotorTempUsed[1]=1    ; enable the PT100/RTD sensor
AMaxMotorTemp[1]=80    ; over-temperature trip at 80 deg C
AMotorTemp             ; sample the live temperature
AStatReg               ; bits 15-16 carry the 4-level warning
```

在持续高占空比运动过程中：

| 读数 | StatReg 第 15-16 位的预期值 | PCSuite LED |
|---|---|---|
| `MotorTemp < 70` | 0（无） | 熄灭 |
| `70 <= MotorTemp < 74` | 1（低） | 黄色 |
| `74 <= MotorTemp < 77` | 2（中） | 橙色 |
| `77 <= MotorTemp <= 80` | 3（高） | 红色 |
| `MotorTemp > 80` | 触发：`AConFlt = 1040`，轴被禁用 | —— |

如果 `AMotorTemp` 即使在负载下也读出默认值 `25`，则 [MotorTempUsed](MotorTempUsed.md) 很可能仍为 `0`（传感器禁用）——此时告警与触发检查都会被跳过。

## 参见

- [MotorTemp](MotorTemp.md) —— 测量得到的电机温度
- [MotorTempUsed](MotorTempUsed.md) —— 传感器类型选择（对该限值起门控作用）
- [StatReg](../../07-status-and-faults/StatReg.md) —— 第 15–16 位携带 4 级告警
- [ConFlt](../../07-status-and-faults/ConFlt.md) —— 过温时触发的故障码 1040
