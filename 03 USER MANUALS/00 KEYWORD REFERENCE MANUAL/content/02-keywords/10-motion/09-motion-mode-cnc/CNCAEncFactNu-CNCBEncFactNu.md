# CNCAEncFactNu/CNCBEncFactNu

**Definition:**

CNCAEncFactNu (and its CNCB equivalent) is the numerator of the encoder scaling ratio applied to the CNC motion queue A (or B) position values. The effective scale is CNCAEncFactNu / CNCAEncFactDn, converting the CNC position units to internal encoder counts. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md), [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md)
