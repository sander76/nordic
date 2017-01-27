from instructor.components import Product
from instructor.connect import connect_m25s_duette
from instructor.general import enter_program_mode, test_blinds
from instructor.initialise import initialise_duette, \
    initialise_duette_tensioned
from instructor.motor_direction import right_mount_duette, left_mount_duette
from instructor.set_bottom_limit import set_bottom_limit_duette, \
    re_set_bottom_limit_duette
from instructor.set_top_limit import set_top_limit_duette, \
    set_top_limit_duette_alternative, confirm_top_limit_duette
from instructor.skip_step import skiptop, skipbottom_end

m25s_duette_free = Product("M25S Duette Free", [connect_m25s_duette,
                                           initialise_duette,
                                           right_mount_duette,
                                           left_mount_duette,
                                           enter_program_mode,
                                           set_bottom_limit_duette,
                                           enter_program_mode,
                                           set_top_limit_duette,
                                           test_blinds,
                                           skiptop,
                                           enter_program_mode,
                                           set_top_limit_duette,
                                           skipbottom_end,
                                           enter_program_mode,
                                           re_set_bottom_limit_duette
                                           ])

m25s_duette_free_alt = Product("M25S Duette Free ALT",
                          [connect_m25s_duette,
                           initialise_duette,
                           right_mount_duette,
                           left_mount_duette,
                           enter_program_mode,
                           set_bottom_limit_duette,
                           # enter_program_mode,
                           set_top_limit_duette_alternative,
                           confirm_top_limit_duette,
                           set_top_limit_duette,
                           test_blinds,
                           skiptop,
                           enter_program_mode,
                           set_top_limit_duette,
                           skipbottom_end,
                           enter_program_mode,
                           re_set_bottom_limit_duette
                           ])

m25s_tensioned = Product("M25S Duette Tensioned", [connect_m25s_duette,
                                                   initialise_duette_tensioned,
                                                   ])
