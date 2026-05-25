# ProgTask

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

ProgTask keyword is used as a label in user programs. The task is called by using
AProgRun[thread],task no. In high level the following text can be used

This program runs the task after label AProgTask[task no] until ProgHalt using the assigned
thread number.
**Note:**
If halt is not used the code will continue linearly to the next line in the file.
