# RecDataA/RecDataB

**Definition:**

RecDataA and RecDataB store the recording metadata and raw captured data, for the first and the second scope respectively.

**Note:**

For products with only single scope, querying RecDataB will equal to querying RecDataA.

The metadata for each scope are stored in the first 80 entries of the array. The raw captured data, without any unit conversion, are stored in the subsequent array entries. User can view the metadata and the raw captured data, subject to overall index cap of 32079. Raw captured data with index larger than the cap (i.e. captured data number 32000 and above) are not readable by user via RecDataA/RecDataB. To stream the entirety of captured data, please refer to [RecUpload](../../02-keywords/19-data-recording/RecUpload.md).

The first 80 RecDataA/RecDataB indices are described as shown.

| Index | Descriptions |
|---|---|
| 1 | (If recording is completed without RecStop) Expected total number of recorded data points (If recording is interrupted by RecStop) Index of the last recorded element before interruption |
| 2 | Number of requested data points per parameter (RecLength) |
| 3 | Total number of data points recorded |
| 4 | Trigger position (RecTrigPos) |
| 5 - 7 | Maximum trigger values (RecTrigValMax) |
| 8 | Scaling for all user units |
| 9 | Downsampling factor (RecGap) |
| 10 - 12 | Trigger sources (RecTrigSrc) |
| 13 - 15 | Trigger bit-wise masks (RecTrigMask) |
| 16 – 18 | Trigger types (RecTrigTyp) |
| 19 - 21 | Trigger values (RecTrigVal) |
| 22 | Current loop cycle rate |
| 23 | Index of the first recorded element |
| 24 | Index of the first recorded element when all triggers occur |
| 25 | Index of the expected last recorded element |
| 26 - 45 | Complex CAN codes of the recorded parameters |
| 46 | Trigger mode (RecTrigMode) |
| 47 – 48 | Trigger logics (RecTrigsLogic) |
| 49 - 55 | Reserved |
| 56 - 75 | User unit of the recorded parameters |
| 76 – 80 | Reserved |
