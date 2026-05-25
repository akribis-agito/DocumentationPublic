# CNCAPercents/CNCBPercents

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

Used by the user to scale the CNC speed (and acceleration/deceleration) along the CNC path. By
affecting the speed and acceleration/deceleration, the CNCAPercents actually affects the
duration of time that will be needed to perform the CNC motion.
A value of 100 (%) means that the motion will be according to the values defined in the CNC FIFO
segments. A value of 50 (%), for example, means that the CNC will be performed at twice the
time that was needed to perform the nominal CNC motion as defined in the CNC FIFO.
CNCAPercents can get values higher than 100 (%).
CNCAPercents can be modified at any time, including on-the-fly during the CNC motion.
User need to consider what value to give to CNCAPercents before starting a CNC motion.
