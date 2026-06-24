---
keyword: SaveUser
summary: 将当前参数保存到闪存中专用的用户区域，与默认参数分开存放。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# SaveUser

将当前参数保存到闪存中专用的用户区域，与默认参数分开存放。

## 概述

`SaveUser` 将一组专用的用户变量保存到闪存中独立的**用户**区域，与主参数集分开存放。保存的值随后可用 [LoadUser](LoadUser.md) 恢复，从而为操作员提供一份独立于 [Save](Save.md) 所写入参数集的专属快照。在**电机使能或运动中时不允许**执行该操作。与写入整个可保存至闪存参数集的 [Save](Save.md) 不同，`SaveUser` 只存储这一有限的用户变量块。

## 工作原理

`SaveUser` 是 [Save](Save.md) 在用户区域中的对应操作：它将一组专用用户变量的当前值作为快照捕获，并存储到闪存中独立的区域，因此此操作不会覆盖主保存集。这两个区域完全独立——`SaveUser` 不影响 [Load](Load.md) 恢复的内容，[Save](Save.md) 也不影响 [LoadUser](LoadUser.md) 恢复的内容。这使操作员能够在标准快照之外保留一份个人快照，并按需在两者之间切换。如果擦除或写入步骤失败，`SaveUser` 将中止并返回闪存错误（擦除失败为 27，写入失败为 28），而不会留下不完整的参数集。

> **可用性说明。** `SaveUser` / `LoadUser` 在主 [Save](Save.md) / [Load](Load.md) 集之外，提供第二份由用户拥有的快照。该对功能是否存在取决于产品和固件版本；如果您的控制器未实现该功能，请使用 [Save](Save.md) / [Load](Load.md) 进行持久化。

## 示例

```text
ASaveUser            ; save the current parameters to the user area (motor must be off)
```

## 另见

- [LoadUser](LoadUser.md) — 恢复用户参数集
- [Save](Save.md) / [Load](Load.md) — 主参数集
