---
summary: 标记用户程序函数起始位置的标签关键字。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgFunc

标记用户程序函数起始位置的标签关键字。

## 概述

`ProgFunc` 在用户程序中用作标签，标记函数的入口点。当执行到对应索引的 [ProgFuncCall](ProgFuncCall.md) 时，执行将跳转到具有该索引的 `ProgFunc[]` 标签所在位置。函数末尾的 [Return](Return.md) 将跳回调用处并从下一行继续执行。可使用多个 `ProgFunc[]` 标签定义多个函数。

## 工作原理

`ProgFunc[]` 是标记程序位置的标签，而非一条可执行指令——它记录函数的起始位置，以便 [ProgFuncCall](ProgFuncCall.md) 可通过索引跳转至此。函数索引是两者之间的纽带：`AProgFuncCall,3` 始终跳转到 `AProgFunc[3]`。

函数可接收输入参数并返回输出值。调用前使用 [ProgPushArg](ProgPushArg.md) 将参数暂存于调用线程的调用栈上，在函数内部使用 [ProgArgThis](ProgArgThis.md) 读取参数，输出值由 [Return](Return.md) 放回数值栈。一个函数的输入参数、输出参数与局部变量之和有限制（Central-i v5 最多 26 个条目，v4 最多 20 个）；详见 [ProgArgThis](ProgArgThis.md)。

由于标签仅标记位置，若前置代码线性执行到达标签处，执行将*直接穿入*函数体。请在第一个 `ProgFunc[]` 标签之前放置 [ProgHalt](ProgHalt.md)（或无限循环），避免主程序运行进入函数——否则将在调用栈为空时遇到 [Return](Return.md) 并引发错误。

> **注意：** 若程序不是无限循环，请在程序末尾使用 [ProgHalt](ProgHalt.md)。否则执行将继续进入第一个函数，`Return` 关键字将引发错误。

## 示例

```text
...
AProgFuncCall,1     ; call function 1
...
AProgFunc[1]        ; label: start of function 1
; the contents of function 1
AReturn             ; return to the line after the call
```

## 参见

- [ProgFuncCall](ProgFuncCall.md) — 调用由 ProgFunc 标签定义的函数
- [Return](Return.md) — 从函数调用返回
- [ProgPushArg](ProgPushArg.md) — 调用前暂存参数
- [ProgArgThis](ProgArgThis.md) — 在函数内部读取参数
- [ProgHalt](ProgHalt.md) — 暂停线程（放置于函数定义之前）
