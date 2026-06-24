# Simplified-Chinese (zh-CN) Translation Glossary — Motion-Control Firmware Documentation

Authoritative, deduplicated terminology for all per-doc translation agents. Conflicting candidate renderings have been resolved to a single preferred zh-CN term. Use these terms consistently across every document.

---

## DO NOT TRANSLATE — keep verbatim

Keep the following in their original English/code form. Do **not** translate, localize, or reword them:

- **Keyword mnemonics / names**: `MotorOn`, `PosRef`, `CurrRef`, `VelRef`, `ForceRef`, `PosErr`, `EncRes`, `PolePrs`, `ConFlt`, `ConFltSnapVal`, `StatReg`, `ErrLog`, `RecStat`, `RecGap`, `LoggerGap`, `OperationMode`, `ComtMode`, `ComtAng`, `FwdPLim`, `RevPLim`, `OpenLoopOn`, `ShapingOn`, `InTargetStat`, `MotionReason`, `ProgRun`, `ProgTask`, `ProgPriority`, `ProgError`, `ProgCallDepth`, `ProgExpDepth`, `ProgHaltThis`, `PStat`, `PStatPort`, `AInMode`, `AInOffset`, `DInMode`, `CurrAInTh`, `ForceAInTh`, `StuckVel`, `StuckCurr`, `MaxVel`, `MaxVBus`, `MinVBus`, `VBus`, `RetractTarget`, `RelTrgt`, `MapTable`, and all other firmware keyword identifiers.
- **Command syntax**: axis-prefixed forms such as `AKeyword[1]`, `AKeyword[1]=value`. Arrays are **1-indexed** — `keyword[1]` is the first element; `keyword[0]` does not exist. Never rewrite indices, never use a `?` query suffix.
- **Code blocks and inline code**: anything inside fenced code blocks or `inline backticks`.
- **Numeric values, ranges, units tokens**: e.g. `202`, `1..6`, `360`, `0x...`, `dB`, `Hz`, `PT100`, `RTD`, counts, etc.
- **Bit / register references and CAN codes**: bit numbers, bitmasks, register names, status-word bits, fault/error codes.
- **Acronyms / proper names kept verbatim** (may carry a parenthetical zh gloss on first use, but the token stays English): `Park`, `Clarke`, `PD`, `PIV`, `PI`, `PRBS`, `FOC`, `STO`, `IPM`, `IIR`, `FIR`, `LTI`, `ECAM`, `PTP`, `BEMF`, `Central-i`, `Flash` (when inside code/keyword context), `RMS`, `Bode`.

---

## Style

- **Language / register**: Simplified Chinese (zh-CN), technical-manual register — concise, neutral, consistent.
- **Punctuation**: Use full-width Chinese punctuation in prose. Keep **half-width** punctuation inside code, syntax, identifiers, ranges, and numeric tokens.
- **No enrichment**: Do not add explanation, rationale, or detail not present in the English source. This is critical for control-tuning content — translate only what is written.
- **Structure**: Preserve all Markdown / heading structure, lists, tables, and formatting exactly.
- **Control tuning**: Prefer **整定** over 调谐 for "tuning"; use neutral phrasing.
- **Consistency**: When a term has a parenthetical acronym (e.g. 磁场定向控制 (FOC)), keep the parenthetical on terms of art; do not repeat it every occurrence within the same doc unless the source does.

---

## Glossary

### Axes, motors & mechanics

| English | 中文 (zh-CN) | Note |
|---|---|---|
| axis | 轴 | per-axis scope / axis-scoped object |
| axis parameter / axis-related parameter | 轴相关参数 | scope: axis |
| motor | 电机 | |
| brushless motor / DC brushless motor (BLDC) | 无刷电机 / 直流无刷电机 | linear or rotary; ≥3 phases |
| DC brush motor | 直流有刷电机 | |
| linear motor | 直线电机 | |
| rotary motor | 旋转电机 | |
| voice coil (motor) | 音圈（电机） | voice-coil actuator |
| stepper motor | 步进电机 | open- or closed-loop |
| rotary axis | 旋转轴 | |
| pole pairs | 极对数 | magnet pole pairs (`PolePrs`) |
| force / torque | 力 / 力矩 | linear vs. rotary output |
| gravity-loaded / vertical axis | 重力负载 / 垂直轴 | can drop under gravity |
| hard stop | 机械硬限位 | physical end stop |
| backlash | 反向间隙 | transmission lash |
| cogging | 齿槽效应 | anti-cogging = 齿槽补偿 |
| gantry | 龙门 | dual-motor / dual-drive axis |
| dual-motor axis | 双电机轴 | |

### Amplifier, power & protection

| English | 中文 (zh-CN) | Note |
|---|---|---|
| amplifier | 驱动器 | servo amplifier/drive |
| built-in amplifier | 内置驱动器 | vs. external |
| external amplifier | 外部驱动器 | |
| power stage | 功率级 | drive output power stage |
| controller | 控制器 | master controller/drive unit |
| controller board | 控制器板 | |
| logic supply | 逻辑电源 | |
| DC bus voltage / bus voltage | 直流母线电压 / 母线电压 | `VBus` |
| over-voltage / under-voltage | 过压 / 欠压 | `MaxVBus` / `MinVBus` |
| over-current | 过流 | |
| regeneration | 再生（能量回馈） | regen circuit/chopper |
| brake chopper / chopper transistor | 制动斩波器 | |
| regeneration (braking resistor) | 再生制动（制动电阻） | |
| inrush (charge resistor / relay) | 浪涌（充电电阻/继电器） | inrush charge bypass |
| static brake / holding brake | 静态制动器（抱闸） | brake release = 松闸, brake lock = 抱闸 |
| dynamic brake | 动态制动 | |
| safe torque off (STO) | 安全转矩关断（STO） | |
| trip / disable the axis | 跳闸（触发保护）/ 禁用轴 | protective shutdown |
| intelligent power module (IPM) | 智能功率模块（IPM） | |
| cooling fan | 散热风扇 | |
| motor temperature | 电机温度 | |
| over-temperature | 过温 | |
| temperature sensor (RTD/PT100) | 温度传感器（RTD/PT100） | model names kept English |
| calibration curve / table | 校准曲线 / 校准表 | |
| warning band / level | 告警分段 / 告警等级 | |
| warning severity level | 告警严重级别 | none/low/medium/high |

### Commutation & motor phasing

| English | 中文 (zh-CN) | Note |
|---|---|---|
| commutation | 换相 | electronic commutation |
| commutation angle | 换相角 | `ComtAng`; electrical = 电气换相角 |
| auto-phasing / phasing | 自动定相 | phasing (commutation initialization) = 相位初始化 |
| phasing (commutation initialization) | 相位初始化（换相初始化） | |
| electrical angle | 电角度 | |
| electrical-angle offset | 电角度偏移 | |
| electrical cycle | 电气周期 | one commutation cycle |
| motor electrical revolution | 电气旋转一周 | 360 electrical degrees |
| Hall sensor | 霍尔传感器 | |
| Hall state | 霍尔状态 | raw 1..6 combination |
| current vector | 电流矢量 | |
| back-EMF (BEMF) | 反电动势 | keep `BEMF` in keywords |
| rotor flux | 转子磁链 | |
| search method | 搜索法 | applies command, observes response |
| jump to zero | 跳零 | search-based commutation method |
| minimal-jumps search | 最小跳动搜索 | |
| learn pass | 学习过程 | re-commutation learn pass |
| motor learning | 电机学习 | |
| motor resistance and inductance | 电机电阻与电感 | R/L measurement |
| line-to-line | 线间（线对线） | vs. phase data |
| phase data | 相数据 | vs. line-to-line |

### Control loops & FOC

| English | 中文 (zh-CN) | Note |
|---|---|---|
| control loop | 控制环 | real-time control cycle |
| control cycle / control sample | 控制周期 | per-cycle loop iteration |
| controller cycle | 控制器周期 | timing unit; not "cycle" alone |
| controller cycle time | 控制器周期时间 | Ts, sample period |
| sampling frequency | 采样频率 | |
| cascade (of loops) | 级联（控制环） | position→velocity→current |
| position loop | 位置环 | |
| velocity loop | 速度环 | |
| current loop | 电流环 | |
| force loop | 力环 | |
| closed loop | 闭环 | |
| open loop | 开环 | `OpenLoopOn` |
| dual-loop control | 双环控制 | load + motor feedback |
| non-collocated control | 非同位控制 | motor and load sensed separately |
| field-oriented control (FOC) | 磁场定向控制 (FOC) | vector control; dq-domain |
| current PI | 电流 PI 调节器 | keep `PI` |
| quadrature-axis (q axis) | 交轴 (q 轴) | torque-producing |
| direct-axis (d axis) | 直轴 (d 轴) | flux/field axis |
| q/d-axis (current) | q/d 轴（电流） | |
| Clarke transform | Clarke 变换 | keep `Clarke` |
| Park / inverse-Park transform | Park 变换 / 逆 Park 变换 | keep `Park` |
| loop integral / integrator | 积分项 / 积分器 | |
| saturation / saturated | 饱和 | current/voltage/velocity |
| clamp / clip / saturate (to limit) | 钳位 / 限幅 | clamped by limits |
| control effort | 控制量 | loop output |
| operation mode / control mode | 运行模式 / 控制模式 | `OperationMode` |
| position control mode | 位置控制模式 | |
| velocity control mode | 速度控制模式 | |
| current control mode | 电流控制模式 | |
| force control mode | 力控制模式 | |
| servo on / off | 伺服使能 / 伺服关闭 | `MotorOn` state |
| motor on / motor off | 电机使能 / 电机失能 | enable/disable motor output |
| enable / disable (motor) | 使能 / 禁用（电机） | |

### References, feedback & errors

| English | 中文 (zh-CN) | Note |
|---|---|---|
| reference | 参考值 | commanded reference |
| command / command source | 指令 / 指令源 | `CurrCmdSrc`, `ForceCmdSrc` |
| feedback | 反馈 | measured quantity |
| position reference | 位置参考 | `PosRef`; commanded position |
| velocity reference | 速度参考 | `VelRef` |
| current reference | 电流参考 | `CurrRef` |
| current command | 电流指令 | command to amplifier |
| velocity command / commanded velocity | 速度指令 / 指令速度 | |
| position feedback | 位置反馈 | |
| feedback position | 反馈位置 | the measured Pos |
| velocity feedback | 速度反馈 | |
| feedback current | 反馈电流 | |
| force feedback | 力反馈 | |
| load-side feedback | 负载端反馈 | e.g. load grating scale |
| load feedback | 负载反馈 | |
| motor feedback | 电机反馈 | |
| analog tachometer | 模拟测速机 | analog velocity feedback |
| phase current | 相电流 | per-phase current (Ia/Ib) |
| phase voltage | 相电压 | Va/Vb/Vc |
| following error | 跟随误差 | `PosErr` = `PosRef` − Pos |
| tracking error | 跟踪误差 | distinct from following error |
| position error | 位置误差 | reference minus feedback |
| following-error limit | 跟随误差限值 | |
| force error | 力误差 | |
| reference-derivative | 参考微分 | derivative for FF |
| reference trajectory | 参考轨迹 | |

### Tuning, feedforward & filters

| English | 中文 (zh-CN) | Note |
|---|---|---|
| control tuning | 控制整定 | prefer 整定 over 调谐 |
| auto-tuning / automatic gain tuning | 自整定 / 自动增益整定 | |
| feedback control | 反馈控制 | |
| feedforward (control) | 前馈（控制） | acts on reference ahead of feedback |
| feedforward gain | 前馈增益 | |
| acceleration feedforward | 加速度前馈 | |
| velocity feedforward | 速度前馈 | |
| voltage feedforward | 电压前馈 | |
| proportional gain | 比例增益 | |
| integral gain | 积分增益 | |
| PI gains | PI 增益 | keep `PI` |
| servo gains | 伺服增益 | |
| gain | 增益 | in dB where applicable |
| gain scheduling / gain-scheduled | 增益调度 | switching/interpolating gain sets |
| gain set | 增益组 | numbered scheduled gains |
| PIV control | PIV 控制 | keep `PIV` |
| feedforward control | 前馈控制 | |
| friction compensation | 摩擦补偿 | |
| torque compensation | 转矩补偿 | |
| spring compensation | 弹簧补偿 | |
| cost function | 代价函数 | optimization metric |
| root-mean-square error | 均方根误差 | |
| overshoot | 超调 | overshoot penalty = 超调惩罚 |
| repetitive control | 重复控制 | |
| iterative learning | 迭代学习 | |
| disturbance rejection | 扰动抑制 | |
| disturbance observer | 扰动观测器 | |
| plant | 被控对象 | control-theory plant |
| plant model | 被控对象模型 | identified mechanical TF |
| plant gain | 被控对象增益 | |
| closed-loop bandwidth | 闭环带宽 | |
| low-pass filter | 低通滤波器 | |
| first-order filter | 一阶滤波器 | |
| second-order | 二阶 | second-order filter |
| IIR filter | IIR 滤波器 | keep `IIR`; lead/lag = 超前/滞后 |
| finite-impulse-response (FIR) | 有限脉冲响应（FIR） | |
| cut-off / corner frequency | 截止频率 / 转折频率 | |
| damping | 阻尼 | |
| damping ratio | 阻尼比 | ζ |
| compensation filter | 补偿滤波器 | |
| complementary filter | 互补滤波器 | blends measured + predicted force |
| compensation table | 补偿表 | position-to-force prediction |
| velocity filter design | 速度滤波器设计 | |
| input shaping | 输入整形 | `ShapingOn` |
| input shaper | 输入整形器 | |
| resonance / resonance frequency | 谐振 / 谐振频率 | |
| residual vibration | 残余振动 | |
| settling oscillation | 整定振荡 | |
| jerk smoothing | 急动平滑 | jerk-smoothing history at enable |

### System identification

| English | 中文 (zh-CN) | Note |
|---|---|---|
| commissioning | 调试投运 | burn-in = 老化测试 |
| burn-in | 老化测试 | production stress test |
| identification | 辨识 | input-output characterization |
| system identification | 系统辨识 | |
| transfer function | 传递函数 | |
| frequency response | 频率响应 | |
| frequency-domain | 频域 | |
| time-domain tuning | 时域整定 | |
| step response | 阶跃响应 | |
| sine sweep | 正弦扫频 | identification excitation |
| chirp signal | 扫频信号（chirp） | linearly swept sine |
| frequency sweep | 频率扫描 | |
| PRBS signal / pseudorandom binary sequence | 伪随机二进制序列（PRBS） | keep `PRBS` |
| maximal-length sequence | 最大长度序列 | m-sequence |
| injection / excitation | 注入 / 激励 | injection frequency = 注入频率 |
| direct injection | 直接注入 | replaces signal at injection point |
| additive injection | 叠加注入 | adds to existing command |
| test signal | 测试信号 | |
| waveform | 波形 | |
| square wave | 方波 | |
| pulse | 脉冲 | |
| amplitude | 幅值 | |
| magnitude / amplitude ratio | 幅值 / 幅值比 | output over input |
| fundamental frequency | 基波频率 | first harmonic |
| harmonic | 谐波 | |
| phase difference | 相位差 | |
| DC offset | 直流偏置 | |
| Bode plot | 伯德图 | magnitude + phase |
| least-squares regression / fit | 最小二乘回归 / 拟合 | |
| pseudo-inverse | 伪逆 | |
| downsampling | 降采样 | |
| RMS | 均方根 | residual/noise metric |
| linear time-invariant (LTI) | 线性时不变（LTI） | |
| linear interpolation | 线性插值 | |

### Encoders & feedback devices

| English | 中文 (zh-CN) | Note |
|---|---|---|
| encoder | 编码器 | |
| main encoder | 主编码器 | load-side in dual-loop |
| auxiliary encoder | 辅助编码器 | motor-side; `Aux` prefix |
| incremental encoder | 增量式编码器 | |
| absolute encoder | 绝对式编码器 | |
| encoder count(s) | 编码器计数 | keep `count` token in code |
| encoder resolution | 编码器分辨率 | `EncRes` |
| resolution | 分辨率 | |
| counting direction | 计数方向 | |
| quadrature (A/B) | 正交（A/B） | AqB signal |
| encoder index / index pulse | 编码器索引 / 索引脉冲 | once-per-rev reference mark |
| index mark / reference mark | 参考标志 | encoder reference mark |
| index position | 索引位置 | |
| encoder emulation | 编码器仿真 | emit A/B/Z output |
| virtual encoder | 虚拟编码器 | software-generated |
| interpolation | 插值 | linear/bilinear/trilinear = 线性/双线性/三线性插值 |
| dual loop | 双环 | position/velocity dual feedback |
| corrected position | 校正位置 | after error-map correction |
| encoder error map / error mapping | 编码器误差映射 | |
| error mapping | 误差映射 | position-error compensation |
| correction | 修正值 | map correction added to feedback |
| lookup table | 查找表 | `MapTable` grid |
| grid point | 网格点 | correction points |
| modulo mode / modulo handling | 取模模式 / 取模处理 | endless rotary wrap |
| wrap / roll-over | 环绕 | roll-over = 翻转/越界回绕 |
| rollover | 循环回绕 | counter/position rollover |

### Motion profiling & moves

| English | 中文 (zh-CN) | Note |
|---|---|---|
| motion profile | 运动曲线 | generated trajectory |
| motion profiler | 运动规划器 | generates position reference |
| trajectory profiler / profile generator | 轨迹规划器 | second/third-order |
| velocity profiler | 速度规划器 | generates velocity command |
| point-to-point (PTP) motion | 点到点（PTP）运动 | |
| absolute / relative target | 绝对 / 相对目标 | `RetractTarget` vs `RelTrgt` |
| jerk | 加加速度（急动度） | jerk limit; profiler order |
| jerk mode | 加加速度模式 | |
| acceleration / deceleration | 加速度 / 减速度 | |
| cruise velocity | 巡航速度 | |
| deceleration ramp | 减速斜坡 | |
| emergency deceleration | 紧急减速 | |
| controlled stop | 受控停止 | per deceleration profile |
| ramp (engage/disengage) | 斜坡（接入/退出） | ramp-in/ramp-down |
| slew rate | 变化速率 | offset slews to target |
| kinematics | 运动学参数 | speed/accel/decel set |
| end-of-motion reason / motion reason | 运动结束原因 | `MotionReason` |
| in-target status | 到位状态 | `InTargetStat` |
| in target / settle in target | 到位 / 稳定到位 | target reached |
| jog | 点动 | jog/joystick move |
| user units | 用户单位 | position in user-defined units |
| set position | 设置位置 | |
| position capture / latch (Lock) | 位置捕获（Lock）/ 锁存 | capture feedback on event |
| abort | 中止 | e.g. homing run aborts |
| timeout | 超时 | |

### Homing & limits

| English | 中文 (zh-CN) | Note |
|---|---|---|
| homing / home | 回零（原点回归） | also 回原点 |
| homing process / homing run | 回零过程 / 回零运行 | |
| reference position | 参考位置 | |
| home input / home switch | 原点输入 / 原点开关 | Home discrete input |
| limit switch | 限位开关 | |
| forward / reverse limit (switch) | 正向 / 反向限位（开关） | FLS / RLS |
| software (position) limit / soft limit | 软件位置限位 | `FwdPLim` / `RevPLim` |
| travel direction | 运动方向 | |

### Motor / axis state

| English | 中文 (zh-CN) | Note |
|---|---|---|
| standstill | 静止 | at-standstill vs in-motion |
| in motion | 运动中 | axis moving |
| holding current | 保持电流 | stepper standstill current |
| current limit | 电流限制 | |
| peak current / peak current limit | 峰值电流 / 峰值电流限值 | |
| continuous current | 连续电流 | |
| current saturation | 电流饱和 | command clamped |
| open-loop / closed-loop | 开环 / 闭环 | control loop configuration |
| simulation mode | 仿真模式 | simulation motor |
| stall | 堵转 | stall detection |
| stepper stall | 步进失步（堵转） | loss of synchronization |
| motor stuck | 电机堵转 | `StuckVel`/`StuckCurr` |
| overspeed | 超速 | `MaxVel` trigger |
| threshold | 阈值 | activation/deactivation threshold |
| hysteresis | 迟滞 | switching hysteresis |
| deadband / dead-band | 死区 | no-change region |
| offset | 偏置 | bias |
| anomaly detection | 异常检测 | |
| stability detection / diagnostics | 稳定性检测 / 稳定性诊断 | detect oscillation/instability |
| unstable loop | 不稳定环路 | |
| oscillate / oscillation | 振荡 | |
| jitter | 抖动 | |
| sliding window | 滑动窗口 | running-statistics window |
| variance / spread | 方差 | spread = 离散度 acceptable |

### Gantry & multi-axis

| English | 中文 (zh-CN) | Note |
|---|---|---|
| master / slave (drive) axis | 主轴 / 从轴 | slave follows master `CurrRef` (v5) |
| master / slave | 主轴 / 从轴 | gear / ECAM |
| follower | 从动件（从轴） | cam follower / slave reference |
| common (linear) mode | 共模（线性）模式 | average of both ends = translation |
| differential (yaw) mode | 差模（偏摆）模式 | difference of ends = beam yaw |
| yaw | 偏摆 | beam yaw/twist angle |
| yaw correction | 偏摆校正 | |
| MIMO control | 多输入多输出（MIMO）控制 | |
| decoupling | 解耦 | |
| decoupling map | 解耦映射表 | position-indexed ratios |
| electronic cam (ECAM) | 电子凸轮（ECAM） | |
| cam profile / cam pattern | 凸轮曲线 | cam lobe profile |
| gear motion (electronic gearing) | 电子齿轮运动 | direct/indirect |

### I/O & signal conditioning

| English | 中文 (zh-CN) | Note |
|---|---|---|
| analog input (channel) | 模拟量输入（通道） | `AInMode` |
| analog output | 模拟量输出 | full-scale scaling |
| digital input | 数字量输入 | `DInMode` |
| digital output | 数字量输出 | |
| bi-directional I/O | 双向 I/O | configurable in or out |
| full scale | 满量程 | analog full-scale scaling |
| pulse-direction (PD) command / pulse/direction | 脉冲方向指令 / 脉冲/方向 | keep `PD`; step/direction P/D output |
| conditioning chain | 信号调理链 | filter/offset/deadband/gain chain |
| gain (signal) | 增益 | |
| low-pass filter (I/O) | 低通滤波器 | |
| debounce | 消抖 | digital input debounce |
| rising edge | 上升沿 | |
| falling edge | 下降沿 | |

### Faults, status & diagnostics

| English | 中文 (zh-CN) | Note |
|---|---|---|
| fault | 故障 | controller fault/error condition |
| controller fault | 控制器故障 | `ConFlt` disabling fault |
| fault code / error code | 故障码 / 错误码 | negative status values |
| fault register | 故障寄存器 | `ConFlt` |
| error code | 错误代码 | |
| status word / bitfield | 状态字 / 状态位域 | `StatReg` 32-bit field |
| status bit | 状态位 | individual flag |
| bit / bitmask | 位 / 位掩码 | |
| mask (bitwise mask) | 掩码（位掩码） | |
| interlock | 互锁 | safety interlock |
| watchdog (timeout) | 看门狗（超时） | CPU background-loop watchdog |
| diagnostic snapshot | 诊断快照 | `ConFltSnapVal` at fault |
| error log | 错误日志 | `ErrLog` ring buffer |
| runtime error | 运行时错误 | `ProgError` |

### Central-i link

| English | 中文 (zh-CN) | Note |
|---|---|---|
| Central-i link | Central-i 链路 | keep `Central-i` |
| remote unit | 远程单元 | remote amplifier/IO unit |
| cyclic data | 周期数据 | synchronous data exchange |
| link state | 链路状态 | up/down status |

### User program & scheduler

| English | 中文 (zh-CN) | Note |
|---|---|---|
| user program | 用户程序 | |
| thread | 线程 | execution thread |
| task | 任务 | code after a `ProgTask` label |
| cooperative scheduler / scheduling | 协作式调度器 / 调度 | |
| round-robin | 轮询 | round-robin scheduling |
| scheduling pass | 调度轮次 | |
| priority | 优先级 | `ProgPriority` |
| program pointer / instruction pointer | 程序指针 / 指令指针 | |
| call stack | 调用栈 | |
| numeric (expression) stack | 数值（表达式）栈 | |
| push / pop | 压入 / 弹出 | stack operations |
| operand | 操作数 | |
| function call | 函数调用 | |
| argument | 参数（实参） | distinguish from parameter via 实参 |
| breakpoint | 断点 | |
| single-step | 单步执行 | debugger step |
| snapshot | 快照 | program snapshot |
| event / event handler | 事件 / 事件处理程序 | user-program event system |
| trigger condition | 触发条件 | |
| pending / in service / waiting | 待处理 / 处理中 / 等待 | event states |
| re-arm | 重新置位 | one-shot arm = 一次性置位 |
| down counter / up counter | 减计数器 / 加计数器 | |
| heap | 堆 | shared memory heap |
| streaming (status streaming) | 流式传输（状态流式传输） | `PStat` periodic streaming |
| communication port / channel | 通信端口 / 通信通道 | |

### Position-compare / event generation

| English | 中文 (zh-CN) | Note |
|---|---|---|
| event generation | 事件生成 | position-synchronized output |
| position-compare engine | 位置比较引擎 | |
| compare position | 比较位置 | position where output fires |
| output pulse | 输出脉冲 | |
| pulse width | 脉冲宽度 | |
| pulse train | 脉冲序列 | |
| arm / arming | 使能（武装） | keep consistent within a doc |

### Data recording, scope & logger

| English | 中文 (zh-CN) | Note |
|---|---|---|
| data recording | 数据记录 | |
| triggered recorder / recorder | 触发式记录器 | the `Rec*` mechanism |
| scope (recording system) | 示波器（记录系统） | `Rec*` system, called scope 1/2 |
| signal scope | 信号示波器 | Central-i `Scope*` live monitoring |
| continuous logger / logger | 连续记录器 | the `Logger*` mechanism |
| sample / sampling | 采样 | |
| sampling rate | 采样率 | |
| down-sampling factor | 降采样因子 | set by `RecGap`/`LoggerGap` |
| recording trigger | 记录触发 | |
| trigger | 触发 | |
| trigger source | 触发源 | |
| trigger type / activation logic | 触发类型 | edge/comparison/range |
| pre-trigger / post-trigger | 触发前 / 触发后 | data before/after trigger |
| force-trigger | 强制触发 | |
| circular buffer | 循环缓冲区 | overwrite/circular mode |
| overwrite mode | 覆盖模式 | buffer-full behavior |
| buffer | 缓冲区 | |
| time stamp | 时间戳 | |
| packet | 数据包 | one logged sample group |
| lost-packets / lost-sample counter | 丢包计数器 | |
| upload / stream to host | 上传 / 流式传输至上位机 | streaming recorded data to PC |
| host / PC | 上位机 | |

### Parameters & memory

| English | 中文 (zh-CN) | Note |
|---|---|---|
| parameter | 参数 | |
| flash (memory) | 闪存（Flash） | keep `Flash` in code/keyword context |
| flash-saved / saved to flash | 保存至闪存 | flash attribute; persists across power cycles |
| flash-backed parameter | 闪存存储参数 | |
| non-volatile memory | 非易失性存储器 | |
| volatile memory | 易失性存储器 | RAM working copy |
| checksum | 校验和 | parameter checksum |
| read-only / writable | 只读 / 可写 | access attribute |
| in motion / motor on (writability) | 运动中 / 电机使能 | `ok_in_motion` / `ok_motor_on` |
| power-on / power-up | 上电 | |
| power cycle | 重新上电 | amplifier power cycle |

### Firmware & boot

| English | 中文 (zh-CN) | Note |
|---|---|---|
| firmware | 固件 | |
| FPGA image | FPGA 镜像 | firmware/FPGA image pair |
| firmware download | 固件下载 | download/programming mode |
| boot program | 引导程序 | on-board bootloader |
| golden image | 黄金镜像 | fallback firmware image |
| watchdog | 看门狗 | |
