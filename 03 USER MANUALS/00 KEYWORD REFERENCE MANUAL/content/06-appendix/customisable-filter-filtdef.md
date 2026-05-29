# Customisable filter (FiltDef)

*Appendix*

Customisable filters are available for

1.  position control (PosFiltDef)

2.  velocity control (VelFiltDef)

3.  feedforward control (FFFiltDef)

4.  force control (ForceFiltDef)

All filter definition keywords’ structures are the same, where each customisable filter can be defined completely by up to 5 parameters. Subsequent filter will be described by the next 5 array parameters, and so on.

The table below shows the indices of the 5 parameters and their descriptions, with N defining the filter number.

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Index | FiltDef\[N\*5-4\] | FiltDef\[N\*5-3\] | FiltDef\[N\*5-2\] | FiltDef\[N\*5-1\] | FiltDef\[N\*5\] |
| Description | Type of filter | Parameter 1 | Parameter 2 | Parameter 3 | Parameter 4 |

All the keywords above are represented by a general term – FiltDef.

Depending on the type of filter, parameters 1 to 4 vary in definitions.

| Type of filter | Parameter 1 | Parameter 2 | Parameter 3 | Parameter 4 |
|---|---|---|---|---|
| 0 – None <br>1 | Not applicable | Not applicable | Not applicable | Not applicable |
| 1 – First order low-pass filter <br>$$\frac{\omega_{d}}{s + \omega_{d}}$$ | Cutoff frequency, *f**d* <br>Unit: [Hz/100] | Not applicable | Not applicable | Not applicable |
| 2 – Second order low-pass filter <br>$$\frac{{\omega_{d}}^{2}}{s^{2} + 2\zeta_{d}\omega_{d}s + {\omega_{d}}^{2}}$$ | Cutoff frequency, *f**d* <br>Unit: [Hz/100] | Damping ratio, *ζ**d* <br>Unit: [%] | Not applicable | Not applicable |
| 3 – Second order low-pass filter with one zero <br>$$\frac{{\omega_{d}}^{2}\left( s + \omega_{n} \right)}{\omega_{n}\left( s^{2} + 2\zeta_{d}\omega_{d}s + {\omega_{d}}^{2} \right)}$$ | Cutoff frequency, *f**d* <br>Unit: [Hz/100] | Damping ratio, *ζ**d* <br>Unit: [%] | Zero’s frequency, *f**n* <br>Unit: [Hz/100] | Not applicable |
| 4 – First order lead-lag filter <br>$$\frac{\omega_{d}\left( s + \omega_{n} \right)}{\omega_{n}\left( s + \omega_{d} \right)}$$ | Zero’s frequency, *f**n* <br>Unit: [Hz/100] | Pole’s frequency, *f**d* <br>Unit: [Hz/100] | Not applicable | Not applicable |
| 5 – Second order lead-lag filter <br>$$\frac{\omega_{d1}\omega_{d2}\left( s + \omega_{n1} \right)\left( s + \omega_{n2} \right)}{\omega_{n1}\omega_{n2}\left( s + \omega_{d1} \right)\left( s + \omega_{d2} \right)}$$ | First zero’s frequency, *f**n*1 <br>Unit: [Hz/100] | Second zero’s frequency, *f**n*2 <br>Unit: [Hz/100] | First pole’s frequency, *f**d*1 <br>Unit: [Hz/100] | Second pole’s frequency, *f**d*2 <br>Unit: [Hz/100] |
| 6 – First order lead-lag filter (type 2) <br>$$\frac{\omega_{d}\left( s + \omega_{n} \right)}{\omega_{n}\left( s + \omega_{d} \right)}$$ <br>where <br>$$\omega_{n} = \omega_{c}\left( \frac{1 - \sin\theta}{\cos\theta} \right)$$ <br>$$\omega_{d} = \omega_{c}\left( \frac{1 + \sin\theta}{\cos\theta} \right)$$ | Center frequency of lead-lag filter,*f**c* <br>Unit: [Hz/100] | Phase lead (positive) / lag (negative) at the center frequency <br>Unit: [degrees] | Not applicable | Not applicable |
| 7 – Second order lead-lag filter (type 2) <br>$$\frac{\omega_{d1}\omega_{d2}\left( s + \omega_{n1} \right)\left( s + \omega_{n2} \right)}{\omega_{n1}\omega_{n2}\left( s + \omega_{d1} \right)\left( s + \omega_{d2} \right)}$$ <br>where <br>$$\omega_{n1} = \omega_{c1}\left( \frac{1 - \sin\theta_{1}}{{\cos\theta}_{1}} \right)$$ <br>$$\omega_{d1} = \omega_{c1}\left( \frac{1 + \sin\theta_{1}}{{\cos\theta}_{1}} \right)$$ <br>$$\omega_{n2} = \omega_{c2}\left( \frac{1 - \sin\theta_{2}}{{\cos\theta}_{2}} \right)$$ <br>$$\omega_{d2} = \omega_{c2}\left( \frac{1 + \sin\theta_{2}}{{\cos\theta}_{2}} \right)$$ | First center frequency of lead-lag filter,*f**c*1 <br>Unit: [Hz/100] | Phase lead (positive) / lag (negative) at the first center frequency, *θ*1 <br>Unit: [degrees] | Second center frequency of lead-lag filter,*f**c*2 <br>Unit: [Hz/100] | Phase lead (positive) / lag (negative) at the second center frequency, *θ*2 <br>Unit: [degrees] |
| 8 – Notch filter <br>$$\frac{s^{2} + \omega_{w}s + \omega_{n}^{2}}{s^{2} + A\omega_{w}s + \omega_{n}^{2}}$$ | Notch’s frequency, *f**n* <br>Unit: [Hz/100] | Notch’s depth, 20log10(*A*) <br>Unit: [dB] | Notch’s width, *f**w* <br>Unit: [Hz/100] | Not applicable |
| 9 - Complex lead-lag filter (biquad filter) <br>$$\frac{{\omega_{d}}^{2}\left( s^{2} + 2\zeta_{n}\omega_{n}s + {\omega_{n}}^{2} \right)}{{\omega_{n}}^{2}\left( s^{2} + 2\zeta_{d}\omega_{d}s + {\omega_{d}}^{2} \right)}$$ | Numerator’s frequency, *f**n* <br>Unit: [Hz/100] | Numerator’s damping ratio, *ζ**n* <br>Unit: [%] | Denominator’s frequency, *f**d* <br>Unit: [Hz/100] | Denominator’s damping ratio, *ζ**d* <br>Unit: [%] |

**Note:**

Frequency is defined in unit of Hz/100. The formula uses angular frequency, where ω = 2 π f

**Example:**

If fourth velocity filter (N=4) is to be second-order low-pass filter at cutoff frequency of 850Hz and damping ratio of 0.71, then

- VelFiltDef\[16\] = 2 (second order low-pass filter)

- VelFiltDef\[17\] = 85000 (equals to 850Hz)

- VelFiltDef\[18\] = 71 (equals to 0.71)

- VelFiltDef\[19\] = any number (not applicable)

- VelFiltDef\[20\] = any number (not applicable)

## From transfer function to digital filter

Each transfer function above is specified in the continuous-time (Laplace, *s*) domain. The controller converts it to a digital second-order section using the **bilinear (Tustin) transform**, substituting
$$s \;\rightarrow\; 2 f_s\,\frac{z-1}{z+1}$$
where $f_s$ is the controller sample rate. The result is realised as a second-order (biquad) **Direct-Form** difference equation
$$y_k = b_0\,x_k + b_1\,x_{k-1} + b_2\,x_{k-2} - a_1\,y_{k-1} - a_2\,y_{k-2}$$
in which all five coefficients are normalised so the leading denominator coefficient is 1. Type 0 (None) sets $b_0=1$ and all other coefficients to 0, i.e. a pass-through. For the notch (type 8) and the first-order phase-defined lead-lag filter (type 6) the sample-rate term is additionally frequency pre-warped, so that the notch/center frequency lands exactly on the specified frequency after discretisation. The coefficients are computed only when [CalcFilters](../02-keywords/11-control-tuning/01-general-keywords/CalcFilters.md) is run after changing a FiltDef definition (or its FiltOn switch).
