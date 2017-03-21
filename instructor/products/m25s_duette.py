from instructor.actions.connect import connect_m25s_duette
from instructor.actions.general import enter_program_mode, test_blinds, \
    enter_program_mode_duette
from instructor.actions.initialise import initialise_duette, \
    initialise_duette_tensioned
from instructor.actions.motor_direction import right_mount_duette, left_mount_duette
from instructor.actions.set_bottom_limit import set_bottom_limit_duette, \
    re_set_bottom_limit_duette
from instructor.actions.set_top_limit import set_top_limit_duette, \
    set_top_limit_duette_alternative, confirm_top_limit_duette
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

# Probably obsolete
m25s_duette_free = Product("M25S Duette Free", [connect_m25s_duette,
                                           initialise_duette,
                                           right_mount_duette,
                                           left_mount_duette,
                                           enter_program_mode_duette,
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
                           enter_program_mode_duette,
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
