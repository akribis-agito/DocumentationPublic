# 可自定义滤波器（FiltDef）

*附录*

可自定义滤波器适用于以下控制环：

1.  位置控制（PosFiltDef）

2.  速度控制（VelFiltDef）

3.  前馈控制（FFFiltDef）

4.  力控制（ForceFiltDef）

所有滤波器定义关键字的结构相同，每个可自定义滤波器最多由 5 个参数完整定义。后续滤波器由接下来的 5 个数组参数描述，依此类推。

下表列出了 5 个参数的索引及其描述，其中 N 为滤波器编号。

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| 索引 | FiltDef\[N\*5-4\] | FiltDef\[N\*5-3\] | FiltDef\[N\*5-2\] | FiltDef\[N\*5-1\] | FiltDef\[N\*5\] |
| 描述 | 滤波器类型 | 参数 1 | 参数 2 | 参数 3 | 参数 4 |

以上所有关键字均以 FiltDef 作为通用术语表示。

根据滤波器类型的不同，参数 1 至 4 的含义有所不同。

| 滤波器类型 | 参数 1 | 参数 2 | 参数 3 | 参数 4 |
|---|---|---|---|---|
| 0 – 无 <br>1 | 不适用 | 不适用 | 不适用 | 不适用 |
| 1 – 一阶低通滤波器 <br>$$\frac{\omega_{d}}{s + \omega_{d}}$$ | 截止频率，*f**d* <br>单位：[Hz/100] | 不适用 | 不适用 | 不适用 |
| 2 – 二阶低通滤波器 <br>$$\frac{{\omega_{d}}^{2}}{s^{2} + 2\zeta_{d}\omega_{d}s + {\omega_{d}}^{2}}$$ | 截止频率，*f**d* <br>单位：[Hz/100] | 阻尼比，*ζ**d* <br>单位：[%] | 不适用 | 不适用 |
| 3 – 带一个零点的二阶低通滤波器 <br>$$\frac{{\omega_{d}}^{2}\left( s + \omega_{n} \right)}{\omega_{n}\left( s^{2} + 2\zeta_{d}\omega_{d}s + {\omega_{d}}^{2} \right)}$$ | 截止频率，*f**d* <br>单位：[Hz/100] | 阻尼比，*ζ**d* <br>单位：[%] | 零点频率，*f**n* <br>单位：[Hz/100] | 不适用 |
| 4 – 一阶超前/滞后滤波器 <br>$$\frac{\omega_{d}\left( s + \omega_{n} \right)}{\omega_{n}\left( s + \omega_{d} \right)}$$ | 零点频率，*f**n* <br>单位：[Hz/100] | 极点频率，*f**d* <br>单位：[Hz/100] | 不适用 | 不适用 |
| 5 – 二阶超前/滞后滤波器 <br>$$\frac{\omega_{d1}\omega_{d2}\left( s + \omega_{n1} \right)\left( s + \omega_{n2} \right)}{\omega_{n1}\omega_{n2}\left( s + \omega_{d1} \right)\left( s + \omega_{d2} \right)}$$ | 第一零点频率，*f**n*1 <br>单位：[Hz/100] | 第二零点频率，*f**n*2 <br>单位：[Hz/100] | 第一极点频率，*f**d*1 <br>单位：[Hz/100] | 第二极点频率，*f**d*2 <br>单位：[Hz/100] |
| 6 – 一阶超前/滞后滤波器（类型 2）<br>$$\frac{\omega_{d}\left( s + \omega_{n} \right)}{\omega_{n}\left( s + \omega_{d} \right)}$$ <br>其中 <br>$$\omega_{n} = \omega_{c}\left( \frac{1 - \sin\theta}{\cos\theta} \right)$$ <br>$$\omega_{d} = \omega_{c}\left( \frac{1 + \sin\theta}{\cos\theta} \right)$$ | 超前/滞后滤波器的中心频率，*f**c* <br>单位：[Hz/100] | 中心频率处的相位超前（正值）/ 滞后（负值） <br>单位：[degrees] | 不适用 | 不适用 |
| 7 – 二阶超前/滞后滤波器（类型 2）<br>$$\frac{\omega_{d1}\omega_{d2}\left( s + \omega_{n1} \right)\left( s + \omega_{n2} \right)}{\omega_{n1}\omega_{n2}\left( s + \omega_{d1} \right)\left( s + \omega_{d2} \right)}$$ <br>其中 <br>$$\omega_{n1} = \omega_{c1}\left( \frac{1 - \sin\theta_{1}}{{\cos\theta}_{1}} \right)$$ <br>$$\omega_{d1} = \omega_{c1}\left( \frac{1 + \sin\theta_{1}}{{\cos\theta}_{1}} \right)$$ <br>$$\omega_{n2} = \omega_{c2}\left( \frac{1 - \sin\theta_{2}}{{\cos\theta}_{2}} \right)$$ <br>$$\omega_{d2} = \omega_{c2}\left( \frac{1 + \sin\theta_{2}}{{\cos\theta}_{2}} \right)$$ | 超前/滞后滤波器的第一中心频率，*f**c*1 <br>单位：[Hz/100] | 第一中心频率处的相位超前（正值）/ 滞后（负值），*θ*1 <br>单位：[degrees] | 超前/滞后滤波器的第二中心频率，*f**c*2 <br>单位：[Hz/100] | 第二中心频率处的相位超前（正值）/ 滞后（负值），*θ*2 <br>单位：[degrees] |
| 8 – 陷波滤波器 <br>$$\frac{s^{2} + \omega_{w}s + \omega_{n}^{2}}{s^{2} + A\omega_{w}s + \omega_{n}^{2}}$$ | 陷波频率，*f**n* <br>单位：[Hz/100] | 陷波深度，20log10(*A*) <br>单位：[dB] | 陷波宽度，*f**w* <br>单位：[Hz/100] | 不适用 |
| 9 – 复杂超前/滞后滤波器（双二阶滤波器）<br>$$\frac{{\omega_{d}}^{2}\left( s^{2} + 2\zeta_{n}\omega_{n}s + {\omega_{n}}^{2} \right)}{{\omega_{n}}^{2}\left( s^{2} + 2\zeta_{d}\omega_{d}s + {\omega_{d}}^{2} \right)}$$ | 分子频率，*f**n* <br>单位：[Hz/100] | 分子阻尼比，*ζ**n* <br>单位：[%] | 分母频率，*f**d* <br>单位：[Hz/100] | 分母阻尼比，*ζ**d* <br>单位：[%] |

**注意：**

频率单位为 Hz/100。公式使用角频率，其中 ω = 2 π f

**示例：**

若第四个速度滤波器（N=4）需设为截止频率 850Hz、阻尼比 0.71 的二阶低通滤波器，则：

- VelFiltDef\[16\] = 2（二阶低通滤波器）

- VelFiltDef\[17\] = 85000（对应 850Hz）

- VelFiltDef\[18\] = 71（对应 0.71）

- VelFiltDef\[19\] = 任意数值（不适用）

- VelFiltDef\[20\] = 任意数值（不适用）

## 从传递函数到数字滤波器

上述每个传递函数均在连续时间（拉普拉斯，*s*）域中给出。控制器使用**双线性（Tustin）变换**将其转换为数字二阶节，变换关系为：
$$s \;\rightarrow\; 2 f_s\,\frac{z-1}{z+1}$$
其中 $f_s$ 为控制器采样率。结果以二阶（双二阶）**直接型**差分方程实现：
$$y_k = b_0\,x_k + b_1\,x_{k-1} + b_2\,x_{k-2} - a_1\,y_{k-1} - a_2\,y_{k-2}$$
其中所有五个系数均经过归一化处理，使分母的首项系数为 1。类型 0（无）将 $b_0$ 设为 1，其余系数设为 0，即直通。对于陷波滤波器（类型 8）和一阶相位定义的超前/滞后滤波器（类型 6），还会对采样率项进行频率预畸变，使陷波/中心频率在离散化后精确落在指定频率处。系数仅在更改 FiltDef 定义（或其 FiltOn 开关）后运行 [CalcFilters](../02-keywords/11-control-tuning/01-general-keywords/CalcFilters.md) 时才会重新计算。
