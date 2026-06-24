# EPPNumFract

**定义：**

EPPNumFract 设置扩展位置预测器传递函数某一分子抽头的小数部分，与 [EPPNumInteg] 共同构成分子多项式。每个抽头按 EPPNumInteg[k] + EPPNumFract[k]/65536 的方式组合，因此 EPPNumFract 承担 1/65536 的小数权重。与 EPPNumInteg 类似，它是以 1..[EPPFiltLength] 为索引的读/写数组（从 1 开始索引），并保存至闪存。

**另请参阅：**

[EPPNumInteg](EPPNumInteg.md)、[EPPNumFactor](EPPNumFactor.md)、[EPPDenFract](EPPDenFract.md)
