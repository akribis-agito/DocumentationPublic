// Minimal stand-in for the v5 Firmware-Main CommonC/AG300_CTL01Params.c: the same row
// wrappers, value pools and positional table shape, over a handful of rows.
#include "ProductConfig.h"

#define PARAM			0
#define NO_USER_UNITS	0
#define FUNC_UNITS		0
#define USER_UNITS		1
#define RO				1
#define RW				0
#define OKINMOTN		1
#define NOMOTN			0
#define NOMTRON			1
#define OKMTRON			0
#define LONG32			0
#define FLOAT			1
#define LONG64			3
#define ISARRAY			1
#define NOARRAY			0
#define FLASH			1
#define NOFLASH			0
#define NON_AXIS		0
#define AXIS			1
#define FINAL			2

#if PRODUCT_TYPE == CI_MASTER
#define CW_TYPETAG_POS	LONG64
#define AXIS_CIM		AXIS
#define KW_PROPS_COL(p)	p,
#define KW_ROW_CIM_ONLY(idx, ...)	{ __VA_ARGS__ }
#define KW_ROW_CTL_ONLY(idx, ...)	KW_BOOT_STUB(idx)
#else
#define CW_TYPETAG_POS	LONG32
#define AXIS_CIM		NON_AXIS
#define KW_PROPS_COL(p)
#define KW_ROW_CIM_ONLY(idx, ...)	KW_BOOT_STUB(idx)
#define KW_ROW_CTL_ONLY(idx, ...)	{ __VA_ARGS__ }
#endif
#if CFG_FEAT_7SEG_DISPLAY == 1
#define KW_ROW_7SEG(idx, ...)	{ __VA_ARGS__ }
#else
#define KW_ROW_7SEG(idx, ...)	KW_BOOT_STUB(idx)
#endif

#define KW_BOOT_STUB(idx)	{ "ZZZZZZZZZZZZZ", { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, 0, KWV_ZZ_MIN, KWV_ZZ_MAX, KWV_ZZ_DFLT, KWS_1, { &glZZ }, KW_PROPS_COL(NULL) 0 }
#define KW_ROW(idx, ...)		{ __VA_ARGS__ }

#define POS_MAX			((long double) 2251799813685247LL)
#define CURR_MAX		(((long) MAX_CURRENT_COMMAND) * 1000)
#define GAIN_MAX		((1 << 12) - 1)

enum KW_VALUE_INDEX {
	KWV_ZZ_MIN,
	KWV_ZZ_MAX,
	KWV_ZZ_DFLT,
	KWV_POS_MIN,
	KWV_POS_MAX,
	KWV_CURR_MIN,
	KWV_CURR_MAX,
	KWV_GAIN_MAX,
	KWV_GAIN_DFLT,
	KWV_COUNT
};
const long double gldKwValues[KWV_COUNT] =
{
	(long double)(-2147483648),
	(long double)(2147483647),
	(long double)(0),
	(long double)(-POS_MAX),
	(long double)(POS_MAX),
	(long double)(-CURR_MAX),
	(long double)(CURR_MAX),
	(long double)(GAIN_MAX),
	(long double)(20.0f),
};
enum KW_SCALE_INDEX {
	KWS_1,
	KWS_TS,
	KWS_COUNT
};
const float gfKwScalings[KWS_COUNT] =
{
	(float)(1),
	(float)(1.024),
};

const struct STRUCT_KEYWORDS_TABLE KeywordsTableArray[8] =
{
	KW_ROW         (0, "ZZZZZZZZZZZZZ", { 0    , 0    , 0            , 0 , 0       , 0      , 0      , 0      , 0       , 0    , 0, 0              }, 0          , KWV_ZZ_MIN  , KWV_ZZ_MAX  , KWV_ZZ_DFLT  , KWS_1  , { &glZZ }      , KW_PROPS_COL(NULL) 0 ),
	KW_ROW         (1, "Pos"          , { PARAM, PARAM, USER_UNITS   , RO, NOMOTN  , NOMTRON, NOARRAY, NOFLASH, AXIS    , FINAL, 0, CW_TYPETAG_POS }, 0          , KWV_POS_MIN , KWV_POS_MAX , KWV_ZZ_DFLT  , KWS_TS , { &gwPos }     , KW_PROPS_COL(NULL) 0 ),
	KW_ROW         (2, "PosGain"      , { PARAM, PARAM, NO_USER_UNITS, RW, OKINMOTN, OKMTRON, ISARRAY, FLASH  , AXIS    , FINAL, 0, LONG32         }, 6-1        , KWV_ZZ_DFLT , KWV_GAIN_MAX, KWV_GAIN_DFLT, KWS_1  , { &glPosGain } , KW_PROPS_COL(NULL) 0 ),
	KW_ROW         (3, "CurrLim"      , { PARAM, PARAM, NO_USER_UNITS, RW, OKINMOTN, OKMTRON, NOARRAY, FLASH  , AXIS    , FINAL, 0, LONG32         }, 0          , KWV_CURR_MIN, KWV_CURR_MAX, KWV_ZZ_DFLT  , KWS_1  , { &glCurrLim } , KW_PROPS_COL(NULL) 0 ),
	KW_ROW         (4, "DInPort"      , { PARAM, PARAM, FUNC_UNITS   , RO, OKINMOTN, OKMTRON, NOARRAY, NOFLASH, AXIS_CIM, FINAL, 0, FLOAT          }, 0          , KWV_ZZ_MIN  , KWV_ZZ_MAX  , KWV_ZZ_DFLT  , KWS_1  , { &gfDInPort } , KW_PROPS_COL(NULL) 0 ),
	KW_ROW_CIM_ONLY(5, "PhaseVoltage" , { PARAM, PARAM, NO_USER_UNITS, RO, OKINMOTN, OKMTRON, NOARRAY, NOFLASH, AXIS    , FINAL, 0, FLOAT          }, 0          , KWV_ZZ_MIN  , KWV_ZZ_MAX  , KWV_ZZ_DFLT  , KWS_1  , { &gfPhaseV }  , KW_PROPS_COL(NULL) 0 ),
	KW_ROW_CTL_ONLY(6, "RptCount"     , { PARAM, PARAM, NO_USER_UNITS, RW, OKINMOTN, OKMTRON, NOARRAY, NOFLASH, NON_AXIS, FINAL, 0, LONG32         }, 0          , KWV_ZZ_MIN  , KWV_ZZ_MAX  , KWV_ZZ_DFLT  , KWS_1  , { &glRpt }     , KW_PROPS_COL(NULL) 0 ),
	KW_ROW_7SEG    (7, "Display7Seg"  , { PARAM, PARAM, NO_USER_UNITS, RW, OKINMOTN, OKMTRON, NOARRAY, NOFLASH, NON_AXIS, FINAL, 0, LONG32         }, 0          , KWV_ZZ_MIN  , KWV_ZZ_MAX  , KWV_ZZ_DFLT  , KWS_1  , { &glDisp7 }   , KW_PROPS_COL(NULL) 0 ),
};
