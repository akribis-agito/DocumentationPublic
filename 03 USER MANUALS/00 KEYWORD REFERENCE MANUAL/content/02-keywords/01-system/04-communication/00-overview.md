# Communication

**Overview:**

Agito supports communication over CAN Bus (Physical layer only), Ethernet (TCP/IP) and RS-232, USB. The following section briefly describes keywords related to communication.

![Communication interfaces: a host reaches the controller over CAN bus, a serial RS-232/USB connection (with an addressed multi-drop chain), or Ethernet TCP/IP, and can read or write keywords over any active interface](comm-interfaces.svg)

**Command and reply flow:** A command is processed and its reply is always returned on the same channel it arrived on — a command received on the serial mini-USB port is answered on that port, one received on the RJ45 serial port on that port, one received over CAN on CAN, and one received over Ethernet on Ethernet. Regardless of channel, the four access types are: inquire a scalar, inquire an array element, assign a scalar, and assign an array element.

**CAN frame format:** An incoming CAN command frame must carry 2, 4, 6, or 8 data bytes (the four access types above); any other data length is rejected with error 15. The reply frame is one of:

| Reply | Length | Contents |
|---|---|---|
| OK (assign / function) | 1 byte | `>` |
| Error | 3 bytes | 16-bit error code, then `>` |
| Inquiry value | 5 bytes | 32-bit value, then `>` |

Because the CAN value field is 32 bits, keyword values exchanged over CAN are limited to 32-bit integers. Keywords that hold a 64-bit value (for example a gear master or position reference) cannot be fully transferred over CAN; use the ASCII serial or Ethernet path, which formats the value as text and is not bound by the 32-bit frame field.

For more information, please refer to communication manual.
