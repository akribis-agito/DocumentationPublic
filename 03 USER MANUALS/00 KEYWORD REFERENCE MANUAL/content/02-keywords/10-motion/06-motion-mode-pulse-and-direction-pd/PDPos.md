# PDPos

**Definition:**

PDPos is the pulse and direction counter that accumulates the number of pulses detected in each controller cycle, multiplied by the scaling factor (defined by PDFact and PDFactDen) and direction sign (defined by PDEncDir). The accumulation (integration) occurs at every controller cycle.

PDPos is represented in pulse-direction unit when queried (see [PDUsrUnits](../../../02-keywords/10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md)).
