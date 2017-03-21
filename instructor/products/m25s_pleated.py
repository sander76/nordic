from instructor.actions.connect import connect_m25s_pleated
from instructor.actions.general import enter_program_mode_pleated, test_blinds
from instructor.actions.initialise import initialise_pleated
from instructor.actions.motor_direction import right_mount_pleated, \
    left_mount_pleated
from instructor.actions.set_bottom_limit import pleated_set_bottom_limit, \
    pleated_re_set_bottom_limit
from instructor.actions.set_top_limit import pleated_set_top_limit_moveup, \
    pleated_confirm_top_limit, pleated_set_top_limit
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

m25s_pleated_free = Product("M25S Pleated",
                            [connect_m25s_pleated,
                             initialise_pleated,
                             right_mount_pleated,
                             left_mount_pleated,
                             enter_program_mode_pleated,
                             pleated_set_bottom_limit,
                             pleated_set_top_limit_moveup,
                             pleated_confirm_top_limit,
                             pleated_set_top_limit,
                             test_blinds,
                             skiptop,
                             enter_program_mode_pleated,
                             pleated_set_top_limit,
                             skipbottom_end,
                             enter_program_mode_pleated,
                             pleated_re_set_bottom_limit
                             ])
