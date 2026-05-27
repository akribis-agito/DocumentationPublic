# Data recording

Data recording allows user to record time series of any set of parameters in which, the recorded data are stored within the controller, and they can be streamed to the PC afterwards.

Depending on the products, the number of scope and the maximum data points per scope vary. The following table shows the summary of the recording capability of each product.

| Properties | Limits |
|---|---|
| Number of recording systems (scope number) | 2 (For AGD301 and AGM800) 1 (For all other standalone products) |
| Maximum total data points, per scope | 30500 (For AGD301) 5 million (For AGM800) 16500 (For all other standalone products) |
| Maximum total number of parameters, per scope | 20 |
| Minimum sampling rate | 16.384kHz (typical) |

In case of multiple scopes, each scope runs independently from the other. Each scope will have its own specific keywords for the array-related variables. For single scope product, array-related keywords for the non-existent second scope will refer to those of the first scope.

| Scope no. | Array-related keywords |
|-----------|------------------------|
| 1         | RecDataA, RecParamA    |
| 2         | RecDataB, RecParamB    |

The common procedure in setting up a scope is as follows.

1.  Any ongoing recording process is stopped by using [RecStop](../../02-keywords/19-data-recording/RecStop.md) command.

2.  User selects the parameters to record by writing their complex CAN codes into the [RecParamA](../../02-keywords/19-data-recording/RecParamA-RecParamB.md) or [RecParamB](../../02-keywords/19-data-recording/RecParamA-RecParamB.md) array.

3.  The rate of recording is configured by selecting the down-sampling factor ([RecGap](../../02-keywords/19-data-recording/RecGap.md)).

4.  The period of recording is configured by writing the number of data point per parameter ([RecLength](../../02-keywords/19-data-recording/RecLength.md)).

5.  Trigger detection mode ([RecTrigsMode](../../02-keywords/19-data-recording/RecTrigsMode.md)) is configured.

    1.  Parallel (logical) trigger detection

> ![rec-start-flow-combined.drawio.svg](../../02-keywords/19-data-recording/rec-start-flow-combined.drawio.svg)
>
> The logics joining the trigger conditions are configurable by [RecTrigsLogic](../../02-keywords/19-data-recording/RecTrigsLogic.md).

2.  Serial trigger detection

> ![rec-start-flow-separate.drawio.svg](../../02-keywords/19-data-recording/rec-start-flow-separate.drawio.svg)

6.  For each trigger, the type of trigger (e.g. rising edge, greater than, etc.) is chosen through [RecTrigTyp](../../02-keywords/19-data-recording/RecTrigTyp.md). For single trigger application, RecTrigsMode, RecTrigsLogic and RecTrigTyp have to be configured to ignore the second and third trigger. Such configuration is supported by PCSuite.

7.  Depending on the type of trigger selected, additional settings for each trigger have to be set up ([RecTrigMask](../../02-keywords/19-data-recording/RecTrigMask.md), [RecTrigPos](../../02-keywords/19-data-recording/RecTrigPos.md), [RecTrigSrc](../../02-keywords/19-data-recording/RecTrigSrc.md), [RecTrigVal](../../02-keywords/19-data-recording/RecTrigVal.md), [RecTrigValMax](../../02-keywords/19-data-recording/RecTrigValMax.md)).

8.  Data recording is started by using [RecStart](../../02-keywords/19-data-recording/RecStart.md) command, and its progress is subject to the trigger condition(s). If needed, user can force-trigger via [RecTrigForce](../../02-keywords/19-data-recording/RecTrigForce.md) command.

9.  User queries [RecStat](../../02-keywords/19-data-recording/RecStat.md) for the recording status. It is also possible to stop the recording process using RecStop command at any time.

10. Once the recording is done (RecStat = 4), user can stream the data to PC via [RecUpload](../../02-keywords/19-data-recording/RecUpload.md) command.

11. If the metadata and raw recording data (without unit conversions) are needed, user can query [RecDataA](../../02-keywords/19-data-recording/RecDataA-RecDataB.md) or [RecDataB](../../02-keywords/19-data-recording/RecDataA-RecDataB.md). The array entry that can be query is subject to maximum index limitation.

**Note:**

1. for parameter of 32-bit int data type, the data is casted to 64-bit long data type and stored.
2. for parameter of 32-bit float data type, the data is casted to 64-bit double data type, type-punned to 64-bit long and finally stored.
3. for parameter of 64-bit long data type, the data is stored normally.
4. for parameter of 64-bit double data type, the data is type-punned to 64-bit long and stored.

**Continuous recording:** see [RecCTEnable](RecCTEnable.md) and [RecCTMaxSize](RecCTMaxSize.md).
