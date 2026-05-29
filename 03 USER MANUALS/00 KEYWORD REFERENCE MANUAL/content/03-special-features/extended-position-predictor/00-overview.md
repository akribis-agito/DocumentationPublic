# Extended position predictor (EPP)

EPP is a repetitive-control (iterative-learning) feedforward feature for motion that is repeated run after run. Instead of filtering position feedback, it learns a correction from one run and applies it on the next, so a repeated trajectory tracks better each time it is executed.

On each run, while motion is active, EPP:

1. takes the position error [PosErr] and passes it through a lead/lag (LL) IIR filter whose taps are set by [EPPNumInteg]/[EPPNumFract] (numerator), [EPPDenInteg]/[EPPDenFract] (denominator), [EPPFiltLength] (number of active taps), and [EPPNumFactor] (overall numerator gain);
2. adds the feedforward correction vector stored from the previous run (this stored vector is zeroed on the first run, so the first run contributes no learned correction);
3. passes the result through a second-order low-pass filter whose corner frequency and damping are set by [EPPModelRange];
4. stores the result back as the correction vector for the next run; and
5. adds the correction to the current reference [CurrRef].

EPP runs only in position-control mode and is not used with stepper motors. [EPPRequest] selects whether a run starts the learning (first run) or continues it (repetitive run), and [EPPState] reports what the feature is currently doing.
