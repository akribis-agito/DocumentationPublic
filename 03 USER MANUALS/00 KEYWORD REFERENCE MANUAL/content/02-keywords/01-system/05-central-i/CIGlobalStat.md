# CIGlobalStat

**Definition:**

CIGlobalStat is a read-only non-axis register that encodes the connection state of all Central-i ports. Each port uses two bits: the low bit is set when the port is connected, and the high bit indicates the port is operating in simulation (offline) mode. Reading this single value gives a system-wide overview without querying each axis individually.

**See also:**

[CIStatus](CIStatus.md), [CIConnect](CIConnect.md), [CIDisconnect](CIDisconnect.md)
