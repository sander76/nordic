
from instructor.actions.connect import connect_m25s_vb
from instructor.actions.general import enter_program_mode_vb, test_blinds
from instructor.actions.initialise import initialise_vb_16, initialise_vb_25
from instructor.actions.motor_direction import right_mount_vb, left_mount_vb, \
    vb_16mm_type, vb_25mm_type
from instructor.actions.set_bottom_limit import set_bottom_limit_vb, \
    re_set_bottom_limit_vb
from instructor.actions.set_top_limit import set_top_limit_vb, \
    set_top_limit_alternative_vb, confirm_top_limit_vb
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

# Probably obsolete
# m25s_25mm_vb_free = Product(
#     "M25S 25mm VB Free obsolete",
#     [connect_m25s_vb,
#      initialise_vb_25,
#      right_mount_vb,
#      left_mount_vb,
#      enter_program_mode_vb,
#      set_bottom_limit_vb,
#      enter_program_mode_vb,
#      set_top_limit_vb,
#      test_blinds,
#      skiptop,
#      enter_program_mode_vb,
#      set_top_limit_vb,
#      skipbottom_end,
#      enter_program_mode_vb,
#      re_set_bottom_limit_vb
#      ])

m25s_vb_free = Product(
    "M25s VB",
    [
        connect_m25s_vb,
        vb_16mm_type,
        vb_25mm_type,
        right_mount_vb,
        left_mount_vb,
        enter_program_mode_vb,
        set_bottom_limit_vb,
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

# this is probably the most preferred way of programming this.
m25s_25mm_vb_free_alt = Product(
    "M25S VB 25mm Free",
    [connect_m25s_vb,
     initialise_vb_25,
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

m25s_16mm_vb_free_alt = Product(
    "M25S VB 16mm Free",
    [connect_m25s_vb,
     initialise_vb_16,
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
