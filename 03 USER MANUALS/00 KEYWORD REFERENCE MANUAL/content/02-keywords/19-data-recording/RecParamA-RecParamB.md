# RecParamA/RecParamB

**Definition:**

RecParamA and RecParamB are arrays that store the [complex CAN codes](../../01-keyword-usage-and-syntax/complex-can-code.md) of the parameters to capture for the first and the second scope, respectively. Each scope can capture up to 20 parameters.

<span class="mark">**DN:** To change it so that only entries before zero CCC are recorded.</span>

All array entries with non-zero complex CAN code will be recorded. Duplicated complex CAN codes in the array will result in duplicated capture.

<span class="mark">**DN:** Firmware issue in scaling array operation (RecUpload)</span>

**Example:**

| RecParamA indices | 1 | 2 | 3 | 4 | 5 – 20 |
|---|---|---|---|---|---|
| Value (Complex CAN codes) | 1026 (BPos) | 65565 (BVel[1]) | 0 | 1050 (BCurrRef) | 0 |

When the recording on the first scope is started with the array definition above, all BPos, BVel\[1\] and BCurrRef will be captured.
