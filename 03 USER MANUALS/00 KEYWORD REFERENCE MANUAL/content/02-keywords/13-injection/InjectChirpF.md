# InjectChirpF

**Condition:**

InjectChirpF is only applicable for chirp injection (InjectType = 8 or 9).

**Definition:**

InjectChirpF is an array that defines the initial and final frequencies of the chirp signal, in terms of Hz/100.

| Index | Definition        |
|-------|-------------------|
| 1     | Initial frequency |
| 2     | Final frequency   |

For example, if initial chirp frequency is 5Hz, InjectChirpF\[1\] should be 500. Please refer to InjectType for more information on the chirp waveform.
