# ChooseAxis

**Definition:**

ChooseAxis is a per-thread array parameter that selects which physical axis a user-program thread will operate on. Each thread index maps to an axis number, allowing multi-threaded programs to direct axis-specific commands independently. The array size equals the maximum number of concurrent threads.

**See also:**

[Load](Load.md), [Reset](Reset.md)
