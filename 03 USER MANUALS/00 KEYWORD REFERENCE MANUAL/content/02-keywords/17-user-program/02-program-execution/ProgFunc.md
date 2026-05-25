# ProgFunc

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

ProgFunc keyword is used as a label in user programs. In high level the following text can be
used, for example:

         ...
         AProgFuncCall,1
         ...
         AProgFunc[1]
         // The contents of function 1
         AReturn
When the line AProgFuncCall,1 is reached, the program execution jumps to the location of the
label keyword ProgFunc[1]. Return will cause a jump back to the user program that will continue
execution on the next line.
Use multiple ProgFunc[] labels for multiple functions.
**Note:**
Use ProgHalt at the end of the program if your program is not an endless loop. Otherwise
execution will continue into the first function and the "return" keyword will cause an error.
