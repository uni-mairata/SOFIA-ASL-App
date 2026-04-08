/**
 * @file screen_feedback_gen.c
 * @brief Template source file for LVGL objects
 */

/*********************
 *      INCLUDES
 *********************/

#include "screen_feedback_gen.h"
#include "../Teddy_BEAR.h"

/*********************
 *      DEFINES
 *********************/

/**********************
 *      TYPEDEFS
 **********************/

/***********************
 *  STATIC VARIABLES
 **********************/

/***********************
 *  STATIC PROTOTYPES
 **********************/

/**********************
 *   GLOBAL FUNCTIONS
 **********************/

lv_obj_t * screen_feedback_create(void)
{
    LV_TRACE_OBJ_CREATE("begin");


    static bool style_inited = false;

    if (!style_inited) {

        style_inited = true;
    }

    lv_obj_t * lv_obj_0 = lv_obj_create(NULL);
    lv_obj_set_name_static(lv_obj_0, "screen_feedback_#");
    lv_obj_set_style_bg_color(lv_obj_0, lv_color_hex(0x264653), 0);
    lv_obj_set_style_text_color(lv_obj_0, lv_color_hex3(0xfff), 0);

    lv_obj_t * lv_label_0 = lv_label_create(lv_obj_0);
    lv_label_set_text(lv_label_0, "ASL sign you chose: ");
    lv_obj_set_align(lv_label_0, LV_ALIGN_TOP_LEFT);
    lv_obj_set_x(lv_label_0, 10);
    lv_obj_set_y(lv_label_0, 10);
    
    lv_obj_t * lv_label_1 = lv_label_create(lv_obj_0);
    lv_label_bind_text(lv_label_1, &selected_letter, NULL);
    lv_obj_set_align(lv_label_1, LV_ALIGN_TOP_LEFT);
    lv_obj_set_x(lv_label_1, 160);
    lv_obj_set_y(lv_label_1, 10);
    lv_obj_set_width(lv_label_1, 53);
    lv_obj_set_height(lv_label_1, 37);
    
    lv_obj_t * lv_label_2 = lv_label_create(lv_obj_0);
    lv_label_set_text(lv_label_2, "Detected ASL sign:");
    lv_obj_set_y(lv_label_2, -40);
    lv_obj_set_x(lv_label_2, 10);
    lv_obj_set_align(lv_label_2, LV_ALIGN_LEFT_MID);
    lv_obj_set_style_text_align(lv_label_2, LV_TEXT_ALIGN_CENTER, 0);
    
    lv_obj_t * lv_button_0 = lv_button_create(lv_obj_0);
    lv_obj_set_align(lv_button_0, LV_ALIGN_BOTTOM_RIGHT);
    lv_obj_set_y(lv_button_0, -10);
    lv_obj_set_x(lv_button_0, -10);
    lv_obj_set_style_bg_color(lv_button_0, lv_color_hex(0x2a9d8f), 0);
    lv_obj_t * lv_label_3 = lv_label_create(lv_button_0);
    lv_label_set_text(lv_label_3, "Back");
    
    lv_obj_add_screen_load_event(lv_button_0, LV_EVENT_CLICKED, screen_main, LV_SCREEN_LOAD_ANIM_MOVE_BOTTOM, 500, 0);

    LV_TRACE_OBJ_CREATE("finished");

    return lv_obj_0;
}

/**********************
 *   STATIC FUNCTIONS
 **********************/

