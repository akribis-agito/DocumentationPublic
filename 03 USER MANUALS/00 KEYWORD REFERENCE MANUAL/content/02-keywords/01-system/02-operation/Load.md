# Load

**Definition:**

Load command is used to retrieve all the parameters from the non-volatile (flash) memory and is performed once internally upon power up. Running Load command will not cause power cycle.

Please refer to the attribute table to identify whether each parameter can be saved to/loaded from flash.

**Note:**

Load will overwrite all unsaved changes in volatile memory. As a use case, in case of bad and unsaved parameter settings, user can use Load to revert to good parameter settings saved in flash.
