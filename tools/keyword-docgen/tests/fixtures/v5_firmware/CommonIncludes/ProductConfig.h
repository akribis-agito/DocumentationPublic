// Minimal stand-in for Firmware-Main CommonIncludes/ProductConfig.h: three products,
// two product types, two feature switches and the full-scale current.
#define CONTROLLER				1
#define CI_MASTER				2

#define PRODUCT_AGD301_ET_2D05	152
#define PRODUCT_AGD155_EC		300
#define PRODUCT_AGM800			400

#if PRODUCT == PRODUCT_AGD301_ET_2D05
	#define PRODUCT_TYPE			CONTROLLER
	#define CFG_FEAT_7SEG_DISPLAY	0
	#define MAX_CURRENT_COMMAND		16000
#elif PRODUCT == PRODUCT_AGD155_EC
	#define PRODUCT_TYPE			CONTROLLER
	#define CFG_FEAT_7SEG_DISPLAY	1
	#define CFG_FEAT_ECAT_CM		1
	#define MAX_CURRENT_COMMAND		8000
#elif PRODUCT == PRODUCT_AGM800
	#define PRODUCT_TYPE			CI_MASTER
	#define CFG_FEAT_7SEG_DISPLAY	0
	#define MAX_CURRENT_COMMAND		25500
#else
	#error "unknown PRODUCT"
#endif
