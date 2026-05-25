# RevPLim

**Definition:**

RevPLim specifies reverse software travel limit, in unit of count.

Lower limit of reference position will be capped at RevPLim. As a result, motion stops at RevPLim if reference position is lower than this limit. Any negative/reverse motion with final target position above RevPLim is disallowed.
