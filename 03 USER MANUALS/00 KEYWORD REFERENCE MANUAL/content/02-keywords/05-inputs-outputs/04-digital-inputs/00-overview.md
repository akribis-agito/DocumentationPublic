# Digital inputs

The state of the digital inputs can be read from DInPort. Functionalities may be assigned to the inputs via DInMode.

For digital inputs, the signal path is as shown.

![Digital-input signal path: debounce filter, optional inversion, then DInPort](digital-input-chain.drawio.svg)

First, the raw digital signals are passed through a debounce filter, the debounce time is configured via DInFilt. Next, the signals are passed through an optional inversion block, which is configured via DInLog. Finally, the information is stored in DInPort.

Digital inputs are represented by bits in a single signal variable. Each bit in the DInPort, DInLog, etc. corresponds to an input, using 0-based indexing.

| Bit \# | Corresponding Input |
|--------|---------------------|
| 0      | Input 1             |
| 1      | Input 2             |
| 2      | Input 3             |
| …      | …                   |

For products with higher than 32 digital inputs, keywords with suffix “High” will be used (DInPortHigh, DInLogHigh).

| Bit \# | Corresponding Input |
|--------|---------------------|
| 0      | Input 33            |
| 1      | Input 34            |
| 2      | Input 35            |
| …      | …                   |

For array-type keyword representing digital inputs in array indices, 1-based indexing is used. This applies for DInMode.

| Index \# | Corresponds to |
|----------|----------------|
| 1        | Input 1        |
| 2        | Input 2        |
| 3        | Input 3        |
| …        | …              |

For filtering purposes, the sampling rate of the raw digital signal is 80MHz. However, DInPort is only updated at 1kHz.
