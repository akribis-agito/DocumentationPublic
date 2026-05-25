# PopParam

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

PopParam is a user program low level language keyword. It will pop the last ("top") value in the
numeric stack of the current thread and assign it to the requested parameter. The parameter to
be assigned is indicated by using its complex CAN code.
Normally, the user does not need to be concerned with generating the code since the user
program IDE environment on the PC Suite will automatically generate it during compilation.
