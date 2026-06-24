---
keyword: LoadUser
summary: 将用户保存的参数集从闪存恢复到活动参数中。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# LoadUser

将用户保存的参数集从闪存恢复到活动参数中。

## 概述

`LoadUser` 将之前由 [SaveUser](SaveUser.md) 存储的用户自定义参数集从闪存载入活动参数表，覆盖当前值。它是 `SaveUser` 的对应操作。用户参数区与由 [Load](Load.md) / [Save](Save.md) 处理的主参数集相互独立，使操作员能够独立于主保存集来保留并调用自己的配置。`LoadUser` 不能在电机使能或运动中执行。

## 工作原理

`LoadUser` 是 [Load](Load.md) 的用户区对应操作：它恢复之前由 [SaveUser](SaveUser.md) 捕获的快照，将这些值从闪存的用户区复制回实时参数表，并丢弃任何未保存的修改。它仅读取用户区，因此对由 [Save](Save.md) 写入的主集没有影响，也不受其影响。可在试验之后用它返回到您的个人配置，或在 [Load](Load.md) 已将控制器恢复为主集之后使用它。

> **可用性说明。** `SaveUser` / `LoadUser` 在主 [Save](Save.md) / [Load](Load.md) 集之外提供第二个由用户拥有的快照。该对是否存在取决于产品和固件构建；如果您的控制器未实现该功能，请使用 [Save](Save.md) / [Load](Load.md) 进行持久化保存。

## 示例

```text
ALoadUser            ; restore the user-saved parameter set (motor must be stopped)
```

## 另请参阅

- [SaveUser](SaveUser.md) — 保存用户参数集
- [Load](Load.md) / [Save](Save.md) — 主参数集
