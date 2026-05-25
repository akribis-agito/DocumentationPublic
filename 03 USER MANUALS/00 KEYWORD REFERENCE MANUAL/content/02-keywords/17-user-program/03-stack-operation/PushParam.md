# PushParam

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

PushParam is a user program low level language keyword. It is used to push the value of a
parameter into the numeric stack of the current user program thread. The parameter to be
pushed is indicated by using its complex CAN code.
Normally, the user does not need to be concerned with generating the code since the user
program IDE environment on the PC Suite will automatically generate it during compilation.
