# PDUsrUnits

**Definition:**

PDUsrUnits scales the internal PD variables (PDPos and PDVel) from internal unit of counts to user unit, when the user queries for these statuses via communication channel.

For example,

$$
Queried\ PDPos\ \lbrack user\ units\rbrack = \frac{1}{\frac{PDUsrUnits}{65536}\left\lbrack \frac{counts}{user\ units} \right\rbrack\ } \bullet \ Controller\ PDPos\ \lbrack counts\rbrack\ 
$$
