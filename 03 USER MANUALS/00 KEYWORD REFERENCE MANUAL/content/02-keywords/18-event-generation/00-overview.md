# Event generation

The event-generation feature lets the controller produce digital pulses on a designated output when the feedback position reaches a compare position. It is used for position-synchronized output triggering (for example, firing a camera, marker, or external device at precise positions along a move).

Configure the generator with these keywords:

- Master switch and mode: [EventOn](EventOn.md), [EventSelect](EventSelect.md), [EventType](EventType.md), [EventAlwaysOn](EventAlwaysOn.md)
- Position ranges (single / by gap): [EventBegPos](EventBegPos.md), [EventEndPos](EventEndPos.md), [EventGap](EventGap.md)
- Pulse shape: [EventPulseWid](EventPulseWid.md), [EventPulseRes](EventPulseRes.md)
- Position tables: [EventTable](EventTable.md), [EventTableBeg](EventTableBeg.md), [EventTableEnd](EventTableEnd.md), [EventTableSel](EventTableSel.md), [EventTableSrc](EventTableSrc.md), [EventTableWid](EventTableWid.md), [EventTableCor](EventTableCor.md), [EventCorrect](EventCorrect.md)
- Rollover: [EventRollCntr](EventRollCntr.md), [EventRollOff](EventRollOff.md)
- Status: [EventCntr](EventCntr.md), [EventNextPos](EventNextPos.md), [EventLoopback](EventLoopback.md)
