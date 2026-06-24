---
keyword: ScopeAbout
summary: 报告当前 Central-i 示波器会话的元数据。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 746
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 10
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
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ScopeAbout

报告当前 Central-i 示波器会话的元数据。

## 概述

`ScopeAbout` 是一个只读数组，用于报告当前示波器会话的元数据：包括会话信息以及已捕获信号列表的快照。它使上位机应用程序无需单独重新查询配置，即可解析 [ScopeUpload](ScopeUpload.md) 返回的数据。该快照在 [ScopeOn](ScopeOn.md) 启用示波器时获取，因此即使之后修改了 [ScopeParams](ScopeParams.md)，它仍反映捕获数据时实际使用的配置。该变量为非轴状态变量，不保存至闪存。

## 工作原理

该数组为 1 索引。其前导元素存储会话元数据（如会话开始时间），其余元素镜像 [ScopeParams](ScopeParams.md) 中已配置的信号列表，使上位机能够将上传中的每一捕获列与其对应的信号配对。每次示波器通过 [ScopeOn](ScopeOn.md) 从关闭切换至开启时，快照均会刷新。

由于采样间隔从 [ScopeGap](ScopeGap.md) 实时读取（可动态修改），它不包含在此快照中；请直接从 [ScopeGap](ScopeGap.md) 读取。该关键字是 [LoggerAbout](LoggerAbout.md) 在 Central-i 示波器中的对应项。

## 示例

```text
AScopeAbout[1]      ; 查询第一个会话元数据条目
AScopeAbout[4]      ; 查询会话快照中的某个捕获信号条目
```

## 另请参阅

- [ScopeOn](ScopeOn.md) — 启动/停止示波器
- [ScopeParams](ScopeParams.md) — 示波器捕获的信号
- [ScopeUpload](ScopeUpload.md) — 获取已捕获数据
- [LoggerAbout](LoggerAbout.md) — 连续记录器的等效元数据
