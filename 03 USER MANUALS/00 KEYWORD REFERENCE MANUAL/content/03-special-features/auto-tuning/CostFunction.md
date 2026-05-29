# CostFunction

**Definition:**

CostFunction evaluates the cost metric used by the automatic current-loop PI tuning. It computes a scalar score from the weighted root-mean-square error between the theoretical current response (TheorCurArray) and the recorded motor-current response, plus an overshoot penalty, which the tuning process minimizes when searching for the current-loop PI gains. It is an axis-related command and is not saved to flash.

**See also:**

[TheorCurArray](TheorCurArray.md)
