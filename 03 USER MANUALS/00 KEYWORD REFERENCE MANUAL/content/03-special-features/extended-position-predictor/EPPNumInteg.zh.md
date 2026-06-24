# EPPNumInteg

**定义：**

EPPNumInteg 存储 EPP 超前/滞后（LL）滤波器某一分子抽头的整数部分。该 IIR 滤波器是 EPP 对位置误差 [PosErr] 施加的滤波器。每个抽头由两个关键字组合而成：整数部分 [EPPNumInteg] 与 1/65536 小数部分 [EPPNumFract]，组合方式为

$$\text{numerator}[k] = \texttt{EPPNumInteg}[k] + \frac{\texttt{EPPNumFract}[k]}{65536}$$

分母抽头以相同方式由 [EPPDenInteg] 和 [EPPDenFract] 构成。这些均为以 1..[EPPFiltLength] 为索引的数组（从 1 开始索引）；仅使用前 [EPPFiltLength] 个抽头。总体分子增益 [EPPNumFactor] 在运行时单独施加，不并入这些系数（这样可使存储的系数值保持较小）。EPPNumInteg 可读/写，并保存至闪存。

**另请参阅：**

[EPPNumFract](EPPNumFract.md)、[EPPNumFactor](EPPNumFactor.md)、[EPPDenInteg](EPPDenInteg.md)、[EPPFiltLength](EPPFiltLength.md)
