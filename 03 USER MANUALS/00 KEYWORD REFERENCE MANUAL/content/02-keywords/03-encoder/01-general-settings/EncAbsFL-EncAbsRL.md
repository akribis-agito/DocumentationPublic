# EncAbsFL/EncAbsRL

%%These keywords were a customization for Korea%%
%%For a rotary motor with an absolute encoder%%

**Condition:**

Only implemented on customized firmware version.

**Definition:**

EncAbsFL and EncAbsRL are used to offset the absolute encoder position upon power on. EncAbsFL defines the foward limit of the 

**Example:**

%%Assume a rotary motor with an absolute encoder. The stroke is limited by a hard stop that only allows motion between +-90 deg . If upon power on, the position is at -45 deg, then the aboslute position would read the position as 315 deg absolute values are read as an unsigned int. If a command is sent to move to 0 deg, it would move 315 deg in reverse (instead of 45 degs forward) and hit the hardstop. In this case, the desired behaviour is that the position is read as -45 deg instead of 315 deg upon power up.

Setting EncAbsFL to 90 deg and EncAbsRL to -90 deg will inform the controller that 315 is out of range and should be interpreted as -45 deg instead. This is applied after EncAbsOffset.%%
