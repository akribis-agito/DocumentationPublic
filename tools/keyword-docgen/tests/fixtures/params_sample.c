#if (PRODUCT_TYPE == CONTROLLER) && (IS_BOOT_IMAGE == 0)
const struct STRUCT_KEYWORDS_TABLE KeywordsTableArray[NUM_OF_CAN_CODES] = \
{ \
    {0,   "ZZZZ",    0,     0,     0,             0,  0,        0,      0,       0,       0,       0,    0, 0,             ZZ_MIN,      ZZ_MAX,    ZZ_DFLT,    1, &glZZ,      NULL, NULL},\
    {100, "PosGain", PARAM, PARAM, NO_USER_UNITS, RW, OKINMOTN, OKMTRON,ISARRAY, FLASH,   AXIS,    FINAL,0, CONTROL_SIZE-1,POSGAIN_MIN, POSGAIN_MAX,POSGAIN_DFLT,1, &glPosGain, NULL, NULL},\
    {101, "PosKi",   PARAM, PARAM, NO_USER_UNITS, RW, NOMOTN,   OKMTRON,NOARRAY, NOFLASH, NON_AXIS,FINAL,0, 0,             POSKI_MIN,   POSKI_MAX, POSKI_DFLT, 1, &glPosKi,   NULL, NULL},\
};
#endif
#if (PRODUCT_TYPE == CI_MASTER) && (IS_BOOT_IMAGE == 0)
const struct STRUCT_KEYWORDS_TABLE KeywordsTableArray[NUM_OF_CAN_CODES] = \
{ \
    {100, "PosGain", PARAM, PARAM, NO_USER_UNITS, RW, OKINMOTN, OKMTRON,ISARRAY, FLASH,   AXIS,    FINAL,0, CONTROL_SIZE-1,POSGAIN_MIN, POSGAIN_MAX,POSGAIN_DFLT,1, &glPosGain, NULL, NULL},\
};
#endif
