# CNCAPushSeg/CNCBPushSeg

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

This keyword is supported only over Ethernet communication connection to the controller. It will
return an error if used over any other communication connection (such as RS232, CAN, etc.).
Using this keyword, the host/user can push a complete segment (type and parameters) using a
single Ethernet message.
This replaces a sequence of messages consisting me CNCAPushType followed by multiple
CNCAPushParam as required for the segment type.
As a result, it significantly improves the throughput of pushing segments into the CNC FIFO.
