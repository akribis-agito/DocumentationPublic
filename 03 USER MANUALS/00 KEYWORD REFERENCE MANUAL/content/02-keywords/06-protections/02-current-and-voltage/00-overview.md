# Current and voltage

Agito controller has several current and voltage protection mechanisms.

| No. | Protection mechanisms |
|---|---|
| 1 | **Limitation of the current command** — current command (`CurrRef`) is limited at the peak current limit ([PeakCL](PeakCL.md)) by default. You can override this saturation limit by using [CurrLimMode](CurrLimMode.md) with [CurrLimFwd](CurrLimFwd.md) / [CurrLimRev](CurrLimRev.md) or with analog-input limits. |
| 2 | **I²t protection** — protects the motor and amplifier from excessive continuous (RMS) current. The I²t trip curve's time constant is computed from the continuous current limit ([ContCL](ContCL.md)) and the peak current time ([PeakTime](PeakTime.md)); the engage/release outcome (current limitation vs. ConFlt code 1044 trip) is selected by `ControlMode` bit 3. |
| 3 | **Motor current protection** — the absolute value of motor current is monitored against [MaxMotorCurr](MaxMotorCurr.md). If `\|MotorCurr\|` exceeds the limit for 4 consecutive controller cycles (≈ 0.25 ms), the axis is disabled with [ConFlt](../../07-status-and-faults/ConFlt.md) code 1016. |
| 4 | **Phase current protection** — the absolute value of each motor phase current (`Ia`/`Ib`/`Ic`) is monitored against [MaxPhaseCurr](MaxPhaseCurr.md). If any phase current exceeds the limit for 4 consecutive cycles (≈ 0.25 ms), the axis is disabled with [ConFlt](../../07-status-and-faults/ConFlt.md) code 1013 / 1014 / 1015. This catches faults such as a stall where the total motor current is below limit but a single phase is above safe value. |
| 5 | **PWM duty cycle protection** — for PWM drives, the maximum PWM duty cycle is limited by [MaxPWM](MaxPWM.md). [MaxPWM](MaxPWM.md) is a saturation only; it does not raise a [ConFlt](../../07-status-and-faults/ConFlt.md). Voltage clamping is reflected in [StatReg](../../07-status-and-faults/StatReg.md) bit 22. |
| 6 | **Bus voltage protection** — bus voltage is monitored against [MinVBus](MinVBus.md) (immediate under-voltage trip, [ConFlt](../../07-status-and-faults/ConFlt.md) code 1009), [MaxVBus](MaxVBus.md) (over-voltage trip after [MaxVBusTime](MaxVBusTime.md), [ConFlt](../../07-status-and-faults/ConFlt.md) code 1008), and [MaxVBusAbs](MaxVBusAbs.md) (instantaneous absolute ceiling, [ConFlt](../../07-status-and-faults/ConFlt.md) code 1023). |
| 7 | **Drive power supply protection** — the drive input power terminals are monitored for disconnection. Configure the supply type with [PowerSupply](PowerSupply.md) so that only the pins your hardware actually uses are checked. A missing required AC phase raises [ConFlt](../../07-status-and-faults/ConFlt.md) code 1054. |

The bus-voltage protection (item 6) is layered into bands around the normal operating range:

![Bus-voltage protection bands: over MaxVBusAbs trips instantly, over MaxVBus for longer than MaxVBusTime trips, and at or below MinVBus trips instantly](vbus-bands.svg)

<u>I2t protection for Agito controller:</u>

Time-current curve is a safety curve depicting constant/step current applied against trip time (or time to damage). It is commonly represented by a plot of I-squared against trip time and assumes zero current before $t = 0$.

Generally, the trip curve used is

$$
I^{2} = \frac{{I_{c}}^{2}\ \ }{1 - e^{- \frac{t}{\tau}}\ }
$$

where

- $I_{c}$ and $I$ are continuous and applied current in unit of A (or Arms)

- $t$ and $\tau$ are trip time and time constant in unit of seconds

From this formula, if $I^{2} = {I_{c}}^{2}$, the trip time is infinite.

The following picture shows an Akribis motor trip curve.

**Trip curve of Akribis AUM2-S2-S motor**
Peak current: 8Arms, Continuous current: 1.6Arms, Peak time: 1s

```desmos-graph
left=0; right=5; bottom=0; top=70
height=300;
xAxisLabel=Time (s)
yAxisLabel=I² (Arms²)
---
y=2.56/(1-e^{-x/24.5})|x>0|blue
y=2.56|#aaaaaa|dashed
x=1|y>=0|y<=64|#aaaaaa|dashed
y=64|x>=0|x<=1|#aaaaaa|dashed
(1,64)|label:(1, 64)|black|noline
```

Agito will implement its own I2t protection based on this trip curve equation. User needs to define ContCL, PeakCL and PeakTime, which represent the continuous current, peak current and peak current time, respectively. The controller will calculate time constant according to the formula.

To protect the motor, it is recommended to use more conservative ContCL, PeakCL and PeakTime values than the actual motor’s values. ContCL, PeakCL and PeakTime should at most be equal to the motor datasheet values.

The controller tripping mechanism works by continuously obtaining $I^{2}$ (through MotorCurr parameter) and filtering this value with low-pass filter with time constant $\tau$. If the filtered result is higher than ${I_{c}}^{2}$, I2t trip event is triggered.

![I2t tripping mechanism: MotorCurr is squared and low-pass filtered, then compared against the squared continuous current limit to trigger the I2t trip event](I2t-tripping-mechanism.svg)

The low-pass filter, in continuous form, is

$$
G(s) = \ \frac{1\ }{\tau s + 1}
$$

The low-pass filter, in discrete form by forward Euler approximation, is

$$
G\left( z^{- 1} \right) = \ \frac{\frac{T_{s}}{\tau}\ z^{- 1}}{1 + \left( \frac{T_{s}}{\tau} - 1 \right)z^{- 1}}
$$

This low-pass filter obtains the equivalent continuous power dissipated at the motor.

**Note:**

1. For FW version 3.0.5 and later, user can select the protective action taken once the I2t trip event is triggered by changing bit 3 of ControlMode parameter.
2. I2t power limitation only works if current control loop is activated (please refer to ControlMode ) or if an external amplifier is used to drive an analog output.
3. If external amplifier is used, CurrRef is used for monitoring instead of MotorCurr.

**Example:**

![Simulated I2t example showing the desired current command, the filtered squared current against the I2t threshold, and the resulting current-command limiting](../../../assets/image24.png)

In this simulated example, the following parameters are used.

| Parameter | Value | Descriptions |
|----|----|----|
| ContCL | 2000 | ContCL is in mA. $I_{c} = 2A.$ |
| PeakCL | 4000 | PeakCL is in mA. $I_{p} = 4A.$ |
| PeakTime | 1000 | PeakTime is in ms. $t_{p} = 1s.$ |
| ControlMode, bit 3 | 0 | Current command is capped at $I_{c}$ instead of axis disabling when I2t event is enabled. |
| CurrLimMode | 0 | Default current command limit is set to $I_{p}$ if I2t protection is disabled. |

From $t = 0s$ to $t = 1.5s$, a step desired current command at $I_{p}$ is commanded. For this period, if there is no I2t current limitation, the filtered response, ${I_{filt}}^{2}\$is

$$
{I_{filt}}^{2} = {I_{p}}^{2}\left( 1 - e^{- \ \frac{t}{\tau}} \right)
$$

When $t = t_{p} = 1s$, ${I_{filt}}^{2}$ will be equivalent to ${I_{c}}^{2}$ and I2t trip event is triggered.

$$
{I_{filt}}^{2} = {I_{p}}^{2}(1 - e^{- \ \frac{t_{p}}{\tau}}) = {I_{c}}^{2}\ 
$$

Once the I2t trip event is triggered, current command limit is capped at $I_{c}$. Current saturation is seen from $t = 2.55s$ to $t = 2.63s$. This limit remains at $I_{c}$ until ${I_{filt}}^{2} < 0.9{I_{c}}^{2}$ as observed at $t = 2.7s$.

After the limit is released, current command limit is capped at $I_{p}$, as seen at $t = 4.22s$ and $t = 4.4s$.

I2t limitation also activates at $t = 4.45s$.
