#define CONTROL_SIZE        6          // 5 sets of gains + 1
#define POSGAIN_MIN         0
#define POSGAIN_MAX         20000      // range opened for overflow protection
#define POSGAIN_DFLT        0
#define DERIVED_MAX         (POSGAIN_MAX * 2)
#define DONTCARE            "n/a"
