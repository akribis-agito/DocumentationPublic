# EventEndPos

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

EventEndPos is the highest position for which events will be generated when using EventType = 2
(by gap). EventEndPos does not have to be a location where an event is generated.
**Example:**
EventType = 2 // Event generation by gap
EventBegPos = 1000
EventGap = 2000
EventEndPos = 8000
EventOn = 1 // This assignment must be made in a position that is smaller than EventBegPos
to prevent unexpected behavior.
This sequence will cause the event out to be "ON" for the duration defined by PulseWidth when
passing in the following positions: 1000, 3000, 5000, 7000.
After passing position 8000 no more events are generated, and EventOn should be toggled to
restart generating events.
