# AAmpFullScale

%%TO REVIEW FOR AMPTYPE = 8%%

**Condition:**

This keyword is only used when AmpType = 2, 5, 7 or 8.

**Definition:**

AAmpFullScale refers to the full-scale output value when external amplifier is used.

The definition differs according to AmpType, as shown below.

| AmpType | AAmpFullScale descriptions |
|---|---|
| 2 (Analog CurrRef command) | Full-scale current reference (CurrRef) output, in milliampere over 10V analog output. Unit: [mA/10V] |
| 5 (Analog VelRef command) | Full-scale velocity reference (VelRef) output, in count/s over 10V analog output. Unit: [count/s/10V] |
| 7 (Analog IaRef/IbRef command) | Full-scale phase current reference (IaRef/IbRef) output, in milliampere over 10V analog output. Unit: [mA/10V] |
| 8 (Digital SPI IaRef/IbRef command) | Full-scale current reference (IaRef/IbRef) output, in milliampere over value of 32768. Unit: [mA/32768] |

**Example:**

If AmpType = 2, AAmpFullScale = 5000 and CurrRef = 3000 \[mA\],

$$
AOutPort\lbrack x\rbrack = \ \frac{CurrRef}{AAmpFullScale} \bullet 10000 = \ \frac{3000}{5000} \bullet 10000 = 6000\ \lbrack mV\rbrack
$$
