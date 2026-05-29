#define CONTROL_SIZE        6          // 5 sets of gains + 1
#define POSGAIN_MIN         0
#define POSGAIN_MAX         20000      // range opened for overflow protection
#define POSGAIN_DFLT        0
#define DERIVED_MAX         (POSGAIN_MAX * 2)
#define DONTCARE            "n/a"
#define POSKI_MIN           0
#define POSKI_MAX           1000
#define POSKI_DFLT          5
#define LONG64_MAX          2251799813685247
#define LONG64_MIN          -2251799813685248
#define POS64_MAX           (long double) LONG64_MAX
#define POS64_MIN           (long double) LONG64_MIN
#define PWM_FACT            1.526
#define FILTFREQ_MIN        1.0f
#define FILTFREQ_MAX        1000.0f
#define FILTFREQ_DFLT       200.0f
#define STD_MIN             0.01f
#define FLOAT_MAX           3.40282e+38
#define FLOAT_MIN           -3.40282e+38
#define VQ_MAX              FLOAT_MAX
#define VQ_MIN              FLOAT_MIN
#define INT_DIV             (POSGAIN_MAX / 2)
