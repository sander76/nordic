from instructor.actions.confirm_product import confirm_vvb
from instructor.actions.connect import connect_m25s_vvb
from instructor.actions.general import enter_program_mode_vvb, \
    enter_program_mode_vvb_id, test_blinds_open_close, \
    test_blinds_open_close_product_choice
from instructor.actions.motor_direction import vvb_left_stack, \
    vvb_right_stack, vvb_split_stack
from instructor.actions.same_product import same_vvb
from instructor.actions.set_bottom_limit import vvb_set_close_limit, \
    vvb_re_set_close_limit
from instructor.actions.set_top_limit import vvb_set_open_limit_moveup, \
    vvb_confirm_open_limit, vvb_set_open_limit
from instructor.actions.skip_step import skipopen, skipclose
from instructor.components import Product

from instructor.translations import Translations as Tr

m25s_vvb_obsolete = Product(
    Tr.PRODUCT_PV_M25S_VVB,
    [
        confirm_vvb,
        connect_m25s_vvb,
        vvb_left_stack,
        vvb_right_stack,
        vvb_split_stack,
        enter_program_mode_vvb_id,
        vvb_set_close_limit,
        enter_program_mode_vvb,
        vvb_set_open_limit_moveup,
        vvb_confirm_open_limit,
        vvb_set_open_limit,
        test_blinds_open_close,
        skipopen,
        enter_program_mode_vvb,
        vvb_set_open_limit,
        skipclose,
        enter_program_mode_vvb,
        vvb_re_set_close_limit
    ]
)

m25s_vvb = Product(
    Tr.PRODUCT_PV_M25S_VVB,
    [
        confirm_vvb,
        connect_m25s_vvb,
        vvb_left_stack,
        vvb_right_stack,
        vvb_split_stack,
        enter_program_mode_vvb_id,
        vvb_set_open_limit_moveup,
        vvb_confirm_open_limit,
        vvb_set_open_limit,
        enter_program_mode_vvb,
        vvb_set_close_limit,
        test_blinds_open_close,
        skipopen,
        enter_program_mode_vvb,
        vvb_set_open_limit,
        skipclose,
        enter_program_mode_vvb,
        vvb_re_set_close_limit
    ]
)

# m25s_vvb_with_product_nav = Product(
#     "M25S VVB",
#     [
#         connect_m25s_vvb,
#         vvb_left_stack,
#         vvb_right_stack,
#         vvb_split_stack,
#         enter_program_mode_vvb_id,
#         vvb_set_close_limit,
#         vvb_set_open_limit_moveup,
#         vvb_confirm_open_limit,
#         vvb_set_open_limit,
#         test_blinds_open_close_product_choice,
#         skipopen,
#         enter_program_mode_vvb,
#         vvb_set_open_limit,
#         skipclose,
#         enter_program_mode_vvb,
#         vvb_re_set_close_limit,
#         same_vvb
#     ]
# )

# m25s_vvb_left = Product(
#     "M25 VVB Left",
#     [connect_m25s_vvb,
#      initialise_vvb_left,
#      vvb_back_left,
#      vvb_above_left,
#      enter_program_mode_vvb,
#      vvb_set_close_limit,
#      vvb_set_open_limit_moveup,
#      vvb_confirm_open_limit,
#      vvb_set_open_limit,
#      test_blinds,
#      skipopen,
#      enter_program_mode_vvb,
#      vvb_set_open_limit,
#      skipbottom_end,
#      enter_program_mode_vvb,
#      vvb_re_set_close_limit
#      ])

# m25s_vvb_right = Product(
#     "M25 VVB Right",
#     [connect_m25s_vvb,
#      initialise_vvb_right,
#      vvb_back_right,
#      vvb_above_right,
#      enter_program_mode_vvb,
#      vvb_set_close_limit,
#      vvb_set_open_limit_moveup,
#      vvb_confirm_open_limit,
#      vvb_set_open_limit,
#      test_blinds,
#      skipopen,
#      enter_program_mode_vvb,
#      vvb_set_open_limit,
#      skipbottom_end,
#      enter_program_mode_vvb,
#      vvb_re_set_close_limit
#      ])

# m25s_vvb_center = Product(
#     "M25 VVB Center",
#     [connect_m25s_vvb,
#      ])
#
# m25s_vvb_upright_left = Product(
#     "M25 VVB upright Left",
#     [connect_m25s_vvb,
#      ])
#
# m25s_vvb_upright_right = Product(
#     "M25 VVB upright Right",
#     [connect_m25s_vvb,
#      ])
#
# m25s_vvb_upright_center = Product(
#     "M25 VVB upright Center",
#     [connect_m25s_vvb,
#      ])
