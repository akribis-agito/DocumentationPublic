# EPPRequest

**定义：**

EPPRequest 选择 EPP（重复控制前馈）在下次运动中的行为。这是一个一次性请求：在运动开始时，其值被复制到 [EPPState] 中，然后 EPPRequest 被清零回 0。

| 值 | 含义 |
|-------|---------|
| 0 | 无请求：EPP 不在下次运动中运行。 |
| 1 | 首次运行：启动新的学习过程（存储的修正向量被清零，因此本次运行不贡献已学习的修正）。 |
| 2 | 重复运行：继续学习，应用并更新上次运行中存储的修正。 |

范围为 0..2，默认值为 0。EPPRequest 为读/写，可在运动中写入；不保存至闪存。

**另请参阅：**

[EPPState](EPPState.md)、[EPPFiltLength](EPPFiltLength.md)、[EPPModelRange](EPPModelRange.md)
