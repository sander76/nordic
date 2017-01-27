from instructor.components import Product
from instructor.connect import connect_m25s_vb
from instructor.general import enter_program_mode_vb, test_blinds
from instructor.initialise import initialise_vb
from instructor.motor_direction import right_mount_vb, left_mount_vb
from instructor.set_bottom_limit import set_bottom_limit_vb, \
    re_set_bottom_limit_vb
from instructor.set_top_limit import set_top_limit_vb, \
    set_top_limit_alternative_vb, confirm_top_limit_vb
from instructor.skip_step import skiptop, skipbottom_end

m25s_vb_free = Product("M25S VB Free", [connect_m25s_vb,
                                           initialise_vb,
                                           right_mount_vb,
                                           left_mount_vb,
                                           enter_program_mode_vb,
                                           set_bottom_limit_vb,
                                           enter_program_mode_vb,
                                           set_top_limit_vb,
                                           test_blinds,
                                           skiptop,
                                           enter_program_mode_vb,
                                           set_top_limit_vb,
                                           skipbottom_end,
                                           enter_program_mode_vb,
                                           re_set_bottom_limit_vb
                                           ])

m25s_vb_free_alt = Product("M25S VB Free ALT",
                          [connect_m25s_vb,
                           initialise_vb,
                           right_mount_vb,
                           left_mount_vb,
                           enter_program_mode_vb,
                           set_bottom_limit_vb,
                           # enter_program_mode,
                           set_top_limit_alternative_vb,
                           confirm_top_limit_vb,
                           set_top_limit_vb,
                           test_blinds,
                           skiptop,
                           enter_program_mode_vb,
                           set_top_limit_vb,
                           skipbottom_end,
                           enter_program_mode_vb,
                           re_set_bottom_limit_vb
                           ])

