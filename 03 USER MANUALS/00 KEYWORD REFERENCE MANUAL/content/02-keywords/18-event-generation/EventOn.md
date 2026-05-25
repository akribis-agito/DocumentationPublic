# EventOn

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

EventOn = 1 will load the first position according to the EventType to the position comparator
and turn on the events. EventOn = 1 should be entered when the motor is in a position that is
smaller than the first requested event to prevent unexpected behavior.
Event and Lock are mutually exclusive functionalities. EventOn = 1 will automatically cause
LockEN to become 0.
