---
keyword: PopParam
summary: 将数值栈顶值弹出并写入参数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 202
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PopParam

将数值栈顶值弹出并写入参数。

## 概述

`PopParam` 是一个低级用户程序关键字。它从当前线程的数值栈中弹出最后一个（"栈顶"）值，并将其赋给指定参数，该参数通过编码引用标识，包含关键字名称、轴和数组索引。它是 [PushParam](PushParam.md) 的逆操作——后者将参数值压入栈——通常用于将 [Math](../02-program-execution/Math.md) 运算结果存回参数。通常用户无需手动生成该引用——PC Suite 用户程序 IDE 在编译时会自动生成。该命令属于非轴域命令，不保存至闪存。

## 工作原理

`PopParam` 从当前线程的数值栈中移除栈顶值，并将其写入目标参数，使栈减少一个条目。由于写入参数是一次赋值操作，`PopParam` 会对其应用控制器对任意参数写入所执行的相同有效性检查（范围、访问权限以及该关键字的运动/电机状态规则），因此超出范围或被拒绝的写入将报告错误。

编译代码中常见两种模式：

- **直接存储。** 目标参数直接在指令中指定，栈顶值写入该参数。此操作消耗一个栈条目。从空栈弹出将报告栈空错误。
- **通过计算目标存储。** 程序可计算写入哪个参数——例如，目标的编码引用本身留在栈上，使赋值使用指针而非固定目标。这是编译器实现对运行时计算索引的数组元素赋值的方式。这种形式中，栈顶条目被作为目标引用消耗，其下方的值随后被存入该目标，因此计算目标的存储消耗两个栈条目而非一个；若栈中条目不足两个则报告无操作数错误。

当目标是数组元素且索引未指定时，`PopParam` 首先弹出一个值作为数组索引（同样需要至少两个条目，否则报告无操作数错误），然后将其下方的值存入该索引对应的元素。这与 [PushParam](PushParam.md) 处理间接（计算）数组索引的方式对称。

与 [PushParam](PushParam.md) 相同，当引用未指定特定轴时，轴取自线程的 [ChooseAxis](../02-program-execution/ChooseAxis.md) 条目。

## 示例

```text
; 将栈顶值存入参数（编码引用由编译器生成）
APopParam=<encoded reference to target parameter>
```

## 另请参阅

- [PushParam](PushParam.md) — 将参数值压入数值栈
- [PushConstant](PushConstant.md) — 将常量压入数值栈
- [Math](../02-program-execution/Math.md) — 对数值栈上的值执行运算
