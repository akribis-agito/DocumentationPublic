---
keyword: EthernetPort
summary: 用于以太网通信的 TCP 端口。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 601
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 65535
  default: 50000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 65524
last_updated: '2026-10-13'
doc_revision: '2026.06'
language: zh-CN
---
# EthernetPort

用于以太网通信的 TCP 端口。

## 概述

`EthernetPort` 配置主 TCP 命令端口，默认值为 **50000**。它会保存至闪存并在启动时读取，因此更改需要执行 [Save](../02-operation/Save.md) 和 [Reset](../02-operation/Reset.md)。

该值的使用方式取决于平台：

- **Standalone 控制器及其他产品**保持原有的 **0–65535** 关键字范围和侦听行为。Standalone 的“all-to-default”恢复 DIP 设置会强制使用主端口 50000，而不论存储的值如何。
- **包含 [Firmware-Main #1213](https://github.com/akribis-agito/Firmware-Main/pull/1213) 的 AGM800 和 AGM800-EC 开发固件**允许关键字范围 **0–65524**。启动时，**1024–65524** 范围内的已保存值选择主命令端口；push/printf 侦听主端口 +10，固件中包含可选 PStat 侦听器时，PStat 使用主端口 +11。低于 1024 的值、旧固件保存的高于 65524 的值，或“all-to-default”DIP 设置会选择有效默认端口：主端口 50000、push 50010，以及可选 PStat 50011。启动时的下限与关键字允许写入的范围不同。
- **较早的 Central-i 固件**使用固定主端口 50000。上述开发固件行为不适用于已冻结的 5.3.0 发布版本或其 rc3 候选版本。

## 保留端口与已保存值的恢复

在包含端口策略前置工作 [Firmware-Main #1241](https://github.com/akribis-agito/Firmware-Main/issues/1241) 的 AGM800/AGM800-EC 开发固件中，新写入 **49990** 会被拒绝，因为其 push 端口会占用保留命令端口 50000。仅当固件包含可选 PStat 侦听器时，**49989** 才会被拒绝，因为该侦听器会占用 50000。被拒绝的写入不会改变原有关键字值。其他产品保持原有策略。

若旧的已保存值存在上述冲突，启动时将使用有效主端口 **50000** 及其派生默认端口，并报告端口冲突诊断；已保存的关键字值和闪存均保持不变。要替换该设置，请写入有效值，然后明确执行 Save 和 Reset。

**Identity[52] 报告实际使用的主命令端口。** 因此，即使读取 `EthernetPort` 仍返回旧的已保存值，在使用有效默认端口启动后，Identity[52] 也会报告 50000。对于有效的已保存端口 51234，它会报告 51234，push 使用 51244。

该端口策略前置工作仅创建启动时选择的主侦听器；主端口不为 50000 时，它不会在保留端口 50000 上增加第二个命令侦听器。

在正常使用中，此关键字保持其默认值 50000。

## 示例

```text
AEthernetPort       ; read the configured port
AEthernetPort=50000 ; set the TCP port (default), then Save and Reset
```

## 另请参阅

- [EthernetIP](EthernetIP.md) — IP 地址
- [EthernetMAC](EthernetMAC.md) — MAC 地址
