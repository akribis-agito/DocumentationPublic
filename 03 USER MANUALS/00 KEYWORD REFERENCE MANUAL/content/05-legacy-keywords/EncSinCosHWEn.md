# EncSinCosHWEn

*Legacy keywords*

**Definition:**

EncSinCosHWEn selects which encoder source feeds the hardware lock/event capture mechanism for the axis. Range 0..7, default 0. Verified sources: 0 = main encoder (incremental), 1 = main encoder, 2 = virtual encoder, 3 = auxiliary encoder.

The selection only takes effect when the axis encoder is configured as a Sin/Cos type. For any other encoder type the controller internally forces the selection to 0, regardless of the value written.
