# 数字量输入

数字量输入的状态可从 DInPort 读取。可通过 DInMode 为输入分配功能。

对于数字量输入，信号路径如下所示。

![Digital-input signal path from the pin through debounce, polarity, and DInPort to the assigned function](digital-input-chain.drawio.svg)

首先，原始数字信号经过一个消抖滤波器，消抖时间通过 DInFilt 配置。接着，信号经过一个可选的取反模块，该模块通过 DInLog 配置。结果存入 DInPort。随后由 DInMode 分配的功能作用于该已存状态的上升沿和下降沿。

数字量输入由单个信号变量中的各个位表示。DInPort、DInLog 等中的每一位对应一个输入，采用 0 起始索引。

| 位 \# | 对应输入 |
|--------|---------------------|
| 0      | Input 1             |
| 1      | Input 2             |
| 2      | Input 3             |
| …      | …                   |

对于数字量输入数量超过 32 的产品，将使用带后缀 “High” 的关键字（DInPortHigh、DInLogHigh）。

| 位 \# | 对应输入 |
|--------|---------------------|
| 0      | Input 33            |
| 1      | Input 34            |
| 2      | Input 35            |
| …      | …                   |

对于在数组索引中表示数字量输入的数组类型关键字，采用 1 起始索引。这适用于 DInMode。

| 索引 \# | 对应 |
|----------|----------------|
| 1        | Input 1        |
| 2        | Input 2        |
| 3        | Input 3        |
| …        | …              |

出于滤波目的，原始数字信号的采样率为 80MHz。DInPort 本身在每个控制器控制周期刷新。
