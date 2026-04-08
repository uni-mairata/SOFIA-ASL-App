/**
 * @file Teddy_BEAR_gen.h
 */

#ifndef TEDDY_BEAR_GEN_H
#define TEDDY_BEAR_GEN_H

#ifndef UI_SUBJECT_STRING_LENGTH
#define UI_SUBJECT_STRING_LENGTH 256
#endif

#ifdef __cplusplus
extern "C" {
#endif

/*********************
 *      INCLUDES
 *********************/

#ifdef LV_LVGL_H_INCLUDE_SIMPLE
    #include "lvgl.h"
    #include "src/core/lv_obj_class_private.h"
#else
    #include "lvgl/lvgl.h"
    #include "lvgl/src/core/lv_obj_class_private.h"
#endif



/*********************
 *      DEFINES
 *********************/

#define DARK_BLUE lv_color_hex(0x264653)

#define YELLOW lv_color_hex(0xe9c46a)

#define TEAL lv_color_hex(0x2a9d8f)

#define VIBRANT_YELLOW lv_color_hex(0xf9c74f)

#define ORANGE lv_color_hex(0xf4a261)

#define UNIT_SMALL 6

#define UNIT_MEDIUM 12

#define UNIT_LARGE 24

/**********************
 *      TYPEDEFS
 **********************/

/**********************
 * GLOBAL VARIABLES
 **********************/

/*-------------------
 * Permanent screens
 *------------------*/

/*----------------
 * Global styles
 *----------------*/

/*----------------
 * Fonts
 *----------------*/

/*----------------
 * Images
 *----------------*/

/*----------------
 * Subjects
 *----------------*/

extern lv_subject_t selected_letter;

/**********************
 * GLOBAL PROTOTYPES
 **********************/

/*----------------
 * Event Callbacks
 *----------------*/

/**
 * Initialize the component library
 */

void Teddy_BEAR_init_gen(const char * asset_path);

/**********************
 *      MACROS
 **********************/

/**********************
 *   POST INCLUDES
 **********************/

/*Include all the widgets, components and screens of this library*/
#include "screens/screen_feedback_gen.h"
#include "screens/screen_main_gen.h"

#ifdef __cplusplus
} /*extern "C"*/
#endif

#endif /*TEDDY_BEAR_GEN_H*/