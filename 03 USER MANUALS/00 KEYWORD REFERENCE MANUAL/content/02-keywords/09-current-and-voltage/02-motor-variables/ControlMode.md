# ControlMode

**Definition:**

ControlMode is used to select the current and voltage control options through bit assignment, as shown.

| ControlMode, Bit # | Source |
|---|---|
| 0 | **Space vector modulation limit (enhanced speed range)** **Default:** 0 (reset) If reset (0), maximum line-line voltage value of up to 0.75*V**B**u**s* is allowed. If set (1), maximum line-line voltage value of up to 0.866*V**B**u**s* is allowed. |
| 1 | **Vector control** **Default:** 0 (reset) If reset (0), current control is in dq0-domain (vector control). If set (1), current control is in abc-domain (phase control). |
| 2 | **Current control loop bypass** **Default:** 0 (reset) If reset (0), current control loop is used. If set (1), current control loop is bypassed. Phase voltage reference inputs (for SVM) are equal to phase current reference inputs. That is, Va and Vb equal IaRef and IbRef, respectively. |
| 3 | **Action taken for I2T protection** **Default:** 0 (reset) If reset (0), triggering I2T protection will cause clamping of current reference at ContCL, until the filtered *I*2 value is lower than (*C**o**n**t**C**L*)2. If set (1), triggering I2T protection will disable motor. Error code will be reported and recorded at ErrLog. If current control loop is bypassed (Bit 2, above), triggering I2T protection will always disable motor regardless of this bit’s value. |
