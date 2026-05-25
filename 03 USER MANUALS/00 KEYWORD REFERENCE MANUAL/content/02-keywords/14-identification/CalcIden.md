# CalcIden

**Condition:**

CalcIden is only applicable to sine sweep identification.

**Definition:**

CalcIden is the command that instructs the controller to calculate sinusoidal relation (at [InjectFreq](../../02-keywords/13-injection/InjectFreq.md)) between the internally recorded input and output data. The input and output data must have at least 30 data points and at most 250 data points each.

Once the calculation is complete, controller will return “OK” message and the results are stored in IdenResults.
