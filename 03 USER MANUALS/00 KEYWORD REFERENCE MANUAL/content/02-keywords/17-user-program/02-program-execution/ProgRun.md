# ProgRun

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

"ProgRun[Thread no.], Task no." will run the required task as the required thread number. For
**example:**
AProgRun[3],5
Runs task 5 as thread 3.
To run the "main" program that starts at the beginning of the file use "-1" as the task number.
