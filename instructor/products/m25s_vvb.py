from instructor.actions.connect import connect_m25s_vvb
from instructor.actions.general import enter_program_mode_vvb, test_blinds
from instructor.actions.initialise import initialise_vvb_right, \
    initialise_vvb_left
from instructor.actions.motor_direction import vvb_back_right, vvb_above_right, \
    vvb_back_left, vvb_above_left
from instructor.actions.set_bottom_limit import vvb_set_close_limit, \
    vvb_re_set_close_limit
from instructor.actions.set_top_limit import vvb_set_open_limit_moveup, \
    vvb_confirm_open_limit, vvb_set_open_limit
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

m25s_vvb_left = Product(
    "M25 VVB Left",
    [connect_m25s_vvb,
     initialise_vvb_left,
     vvb_back_left,
     vvb_above_left,
     enter_program_mode_vvb,
     vvb_set_close_limit,
     vvb_set_open_limit_moveup,
     vvb_confirm_open_limit,
     vvb_set_open_limit,
     test_blinds,
     skiptop,
     enter_program_mode_vvb,
     vvb_set_open_limit,
     skipbottom_end,
     enter_program_mode_vvb,
     vvb_re_set_close_limit
     ])

m25s_vvb_right = Product(
    "M25 VVB Right",
    [connect_m25s_vvb,
     initialise_vvb_right,
     vvb_back_right,
     vvb_above_right,
     enter_program_mode_vvb,
     vvb_set_close_limit,
     vvb_set_open_limit_moveup,
     vvb_confirm_open_limit,
     vvb_set_open_limit,
     test_blinds,
     skiptop,
     enter_program_mode_vvb,
     vvb_set_open_limit,
     skipbottom_end,
     enter_program_mode_vvb,
     vvb_re_set_close_limit
     ])

m25s_vvb_center = Product(
    "M25 VVB Center",
    [connect_m25s_vvb,
     ])

m25s_vvb_upright_left = Product(
    "M25 VVB upright Left",
    [connect_m25s_vvb,
     ])

m25s_vvb_upright_right = Product(
    "M25 VVB upright Right",
    [connect_m25s_vvb,
     ])

m25s_vvb_upright_center = Product(
    "M25 VVB upright Center",
    [connect_m25s_vvb,
     ])
