# CNCAEncFactDn/CNCBEncFactDn

**Definition:**

CNCAEncFactDn (and its CNCB equivalent) is the denominator of the encoder scaling ratio applied to CNC motion queue A (or B) position values. Together with CNCAEncFactNu it defines the rational scale factor (CNCAEncFactNu / CNCAEncFactDn) that converts CNC position units to internal encoder counts. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md), [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md)
