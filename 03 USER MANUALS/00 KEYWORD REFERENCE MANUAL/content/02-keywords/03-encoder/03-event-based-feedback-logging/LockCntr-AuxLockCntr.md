# LockCntr/AuxLockCntr

**Definition:**

LockCntr tracks the number of digital events encountered, as defined by LockSrc. It is also used as an index for populating LockValTable and LockTimeTable. LockCntr increments (by 1) every time the digital event is encountered.

LockCntr is reset to 0 upon enabling the logging feature from disabled state. User can write any value to LockCntr so that LockValTable and LockTimeTable are populated at the desired index.
