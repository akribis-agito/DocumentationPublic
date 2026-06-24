---
keyword: Force
summary: 从模拟量输入获得的力反馈。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 582
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# Force

从模拟量输入获得的力反馈。

## 概述

`Force` 是从模拟量输入获得的力反馈。它取与力反馈功能相关联的模拟源（通过 [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) 配置的模拟端口）经过滤波后的值。它是力环朝着 [ForceRef](ForceRef.md) 驱动的被测量，二者之差以 [ForceErr](ForceErr.md) 报告。

## 工作原理

每个控制周期，控制器都会将经过滤波的模拟量力反馈通道复制到 `Force`。无论当前激活的 [OperationMode](../01-general-keywords/OperationMode.md) 为何，`Force` 都会持续更新，因此即使在力模式之外也可读取它用于监测。

这一相同的经调理滤波后的模拟读数也正是力环用作反馈的量：每个周期力环都会形成 `ForceErr = ForceRef - Force`，因此 `Force` 所显示的值正是从参考值中减去的量。该相同读数还会与 [ForceAInTh](ForceAInTh.md) 进行比较，用于自动进入力模式的模拟量（条件 B）。`Force` 是该内部读数的整数显示副本（用于报告时向零截断）；力环和阈值引擎作用于其底层值。

如果在尚未为任何模拟量输入分配力反馈功能时进入力运行模式，则力环无法运行：[ConFlt](../../07-status-and-faults/ConFlt.md) 会显示故障码 1046（无力反馈），并关闭电机。请在命令进入力模式之前用 [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) 分配反馈通道。

## 示例

```text
AForce              ; read the force feedback
```

### 边界情况

- **未配置模拟量力反馈** — `Force` 读取为 `0`。在此状态下进入力模式会失败，[ConFlt](../../07-status-and-faults/ConFlt.md) = `1046`（无力反馈），并禁用电机。
- **错误模式** — 无论 [OperationMode](../01-general-keywords/OperationMode.md) 为何，`Force` 都每个周期采样一次；即使在力模式之外，该值也是实时的经调理模拟读数。
- **电机失能** — 采样继续进行；在伺服关闭情况下可用于监测测试台。
- **只读** — 写入被拒绝。

## 参见

- [ForceRef](ForceRef.md) — 力环跟踪的滤波后力参考
- [ForceErr](ForceErr.md) — ForceRef 减去 Force
- [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) — 配置模拟量力反馈输入（力模式所必需）
