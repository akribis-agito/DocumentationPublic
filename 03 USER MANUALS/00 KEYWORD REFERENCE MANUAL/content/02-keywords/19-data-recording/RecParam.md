# RecParam

RecParam array holds the complex CAN codes of the parameters to record. There can be up to 4
parameters. All the assigned parameters until a zero is encountered will be recorded. To record a
single parameter enter the complex CAN code of the parameter that should be recorded in
RecParam[1] and enter 0 in RecParam[2]. The values of RecParam[3] and [4] will be ignored.
