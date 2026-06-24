# 语法

本文档中，关键字的赋值与查询采用 ASCII 编码。有关 ASCII 编码及语法的更多信息，请参阅 Agito Communication Manual。

在本文档中，每个关键字的语法均以占位符进行描述。占位符列表如下所示。

| 序号 | 占位符类型     | 占位符 | 语法示例                | 报文示例       |
| --- | ----------------------- | ----------- | ----------------------------- | --------------------- |
| 1   | 轴占位符        | ?           | ?CalcFilters                  | ACalcFilters          |
| 2   | 实参占位符    | Value       | ?EncDir = Value               | DEncDir = 1           |
| 3   | 数组索引占位符 | Index       | ?SinCosSetup\[Index\] = Value | ESinCosSetup\[3\] = 4 |
