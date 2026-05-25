# Math

Math is a user program low level language keyword. The syntax related to "Math" is usually

generated automatically by the PC suite during compilation.

Math will perform the mathematical operation requested on the top parameter or parameters

of the numeric stack. The number of parameters depends on the operation. For example:

addition requires two parameters while negate is an operation that is performed on one

parameter.

The index value determines which operation will be performed. The operands should be pushed

to the stack before Math is called.

The result is pushed to the numeric stack. If this function is called from communication the value

is also sent through communication.

Note that values in the stack and over communication are integers. Results in fractions will be

rounded.

Internally all the relevant mathematical operation are performed on long long type variables.

The definitions are compatible with C language.

Pop1 is the first value that is popped from the stack ("top" value)

Pop2 is the second value that is popped from the stack

The values of math:

Value Operation Type                                                 Number of parameters

1           Add: Result = Pop1 + Pop2                                2

2           Subtract : Result = Pop2-Pop1                            2

3           Multiply: Result = Pop1 * Pop2                           2

4           Divide: Result = Pop2 / Pop1                             2

5           Negate: Result = -Pop1                                   1

6           Invert: Result = 1/Pop1 *                                1

7           Modulo: Result = Pop2%Pop1                               2

8           Power: Result = Pop2^Pop1 (^ used as power 2

            operator)

9           Square root: Result = Square root(Pop1)                  1

10          Sine: Result = sin(Pop1)*                                1

11          Cosine: Result = cos(Pop1)*                              1

12          Tangent: Result = tan(Pop1)*                             1

13          Cotangent: Result = tan -1( Pop1)*                       1

14          Inverse sine: Result = arcsin(Pop1)*                     1

15          Inverse cosine: Result = arcos(Pop1)*                    1

16          Inverse tangent: Result = arctan(Pop1)*                  1

17          Bitwise not: Result = ~ Pop1                             1

18          Bitwise and: Result = Pop1 & Pop2                        2

19          Bitwise or: Result = Pop1 | Pop2                         2

20          Bitwise xor: Result = Pop1 ^ Pop2 (^ used as xor as in 2

            C)

21          Shift left: Result = Pop1 << Pop2                        2

22          Shift right: Result = Pop1 >> Pop2                       2

23          Absolute: Result = abs(Pop1)                             1

24          Logarithm: Result = logpop2 Pop1 *                       2

25          Base 10 logarithm: Result = log10Pop1 *                  1

                                                                                                      Page 392

            Tel: +972-9-8909797 Fax: +972-9-8909796 email: info@agito.co.il website: www.agito.co.il
