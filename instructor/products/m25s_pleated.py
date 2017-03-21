from instructor.actions.connect import connect_m25s_pleated
from instructor.actions.general import enter_program_mode_pleated, test_blinds
from instructor.actions.initialise import initialise_pleated
from instructor.actions.motor_direction import right_mount_pleated, \
    left_mount_pleated
from instructor.actions.set_bottom_limit import set_bottom_limit_pleated, \
    re_set_bottom_limit_pleated
from instructor.actions.set_top_limit import set_top_limit_pleated_alternative, \
    confirm_top_limit_pleated, set_top_limit_pleated
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

m25s_pleated_free = Product("M25S Pleated",
                            [connect_m25s_pleated,
                             initialise_pleated,
                             right_mount_pleated,
                             left_mount_pleated,
                             enter_program_mode_pleated,
                             set_bottom_limit_pleated,
                             set_top_limit_pleated_alternative,
                             confirm_top_limit_pleated,
                             set_top_limit_pleated,
                             test_blinds,
                             skiptop,
                             enter_program_mode_pleated,
                             set_top_limit_pleated,
                             skipbottom_end,
                             enter_program_mode_pleated,
                             re_set_bottom_limit_pleated
                             ])
