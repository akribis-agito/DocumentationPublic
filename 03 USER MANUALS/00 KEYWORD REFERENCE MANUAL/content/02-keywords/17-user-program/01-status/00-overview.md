# Status

This section is the **reader-journey landing page** for user-program status. The actual keyword pages live next to the run/halt/reset keywords under [Program execution](../02-program-execution/00-overview.md), but the three "did it succeed?" reads you usually want are linked here directly so you do not have to scroll the larger table.

| Use this when you want to know… | Read |
|---|---|
| …whether a specific thread is running, stopped, or has no program | [ProgStat](../02-program-execution/ProgStat.md)`[thread]` — values `-1` / `0` / `1` |
| …a one-shot overview of all threads (worst condition wins; refreshed about once per second) | [ProgStatAll](../02-program-execution/ProgStatAll.md) — values `-1` / `0` / `1` / `2` |
| …why a halted thread stopped (run-time error code, latched on the failing instruction) | [ProgError](../02-program-execution/ProgError.md)`[thread]` — `0` means no error |

For a typical poll-and-diagnose sequence: read [ProgStatAll](../02-program-execution/ProgStatAll.md); if it is `2`, walk [ProgStat](../02-program-execution/ProgStat.md) per thread to find the one stopped on an error, then read [ProgError](../02-program-execution/ProgError.md) for that thread and [ProgPointer](../02-program-execution/ProgPointer.md) for the failing offset; the same error is also tagged with the thread number in [ErrLog](../../07-status-and-faults/ErrLog.md). For step-by-step debugging see [ProgSnapSrc](../02-program-execution/ProgSnapSrc.md) / [ProgSnapVal](../02-program-execution/ProgSnapVal.md), which freeze a per-thread program-state snapshot at the moment of the error.
