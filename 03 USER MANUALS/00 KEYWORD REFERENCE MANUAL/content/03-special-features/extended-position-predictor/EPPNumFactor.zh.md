# EPPNumFactor

**定义：**

EPPNumFactor 是扩展位置预测器的总体分子增益。该增益不并入已存储的分子系数（[EPPNumInteg]/[EPPNumFract]，这些系数保持较小值以确保精度）；而是在运行时乘以超前/滞后滤波器的输出，对叠加到 [CurrRef] 的预测修正量进行缩放。EPPNumFactor 是单一读/写值（非数组），保存至闪存。其默认值为 0，因此在将 EPPNumFactor 设置为非零值之前，EPP 不施加任何已学习的修正。

**另请参阅：**

[EPPNumFract](EPPNumFract.md)、[EPPNumInteg](EPPNumInteg.md)、[EPPDenFract](EPPDenFract.md)
