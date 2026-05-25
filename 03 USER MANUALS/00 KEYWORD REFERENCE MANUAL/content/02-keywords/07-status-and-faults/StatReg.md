# StatReg

StatReg reports the general statuses of the axis, in terms of bit field. Some statuses are described using more than one bit. To get a specific status, use the following formula

$$
Status = (StatReg\ \&\ Bit\ mask) \gg Bit\ offset
$$

The table shows bit fields of StatReg and their meanings.

**Note:**

1. Check whether protections MaxVBus and MinVBus are set appropriately.
2. Check if warning is due to voltage exceeding limits during deceleration phase.
3. Check if warning is due to voltage dropping below limits during acceleration phase. If yes, check that power supply can provide sufficient current or lower the profile acceleration.
4. Check motor, driver and power supply sizing to fulfill current requirement
5. Check if MaxPWM is limiting driver’s output
6. Check current loop tuning gains
7. Redo phasing with high current and voltage and/or under lower tolerance setting to improve force constant.
8. Check the ambient temperature around the driver.
9. Install fans to circulate hot air out of the control box.
10. Relocate the drive to a position with more air flow.
11. Velocity saturation (MaxVel)
12. Current saturation (PeakCL or ContCL)
13. Voltage saturation (Va or Vb or Vc reaches MaxPWM)
14. Check first for voltage saturations, as it will affect the current, velocity and position loops.
15. PosFiltOn or PosFiltDef
16. VelFiltOn or VelFiltDef
17. FFFiltOn or FFFiltDef
18. ForceFiltOn or ForceFiltDef
19. UPMDistFilter
20. AnomDtctCnfg[2]
21. UPMRptLevel
22. PlantModel

**Note:**

Agito PCSuite uses the bits values of this status parameter to control the LEDs at its status panel. The warning statuses, which have 4 values (none, low, medium and high) are reflected as a multi-color LED at the PC Suite status panel (off, yellow, orange and red, respectively).
