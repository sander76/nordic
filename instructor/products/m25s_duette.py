from instructor.actions.connect import connect_m25s_duette
from instructor.actions.general import test_blinds, \
    enter_program_mode_duette
from instructor.actions.initialise import initialise_duette, \
    initialise_duette_tensioned, initialise_duette_tensioned_alt
from instructor.actions.motor_direction import right_mount_duette, \
    left_mount_duette, \
    tensioned_duette_direction, tensioned_duette_switch_direction
from instructor.actions.set_bottom_limit import duette_set_bottom_limit, \
    duette_re_set_bottom_limit
from instructor.actions.set_top_limit import duette_set_top_limit, \
    duette_set_top_limit_moveup, duette_confirm_top_limit
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

# preferred method.
m25s_duette_free = Product(
    "M25S Duette",
    [
        connect_m25s_duette,
        initialise_duette,
        right_mount_duette,
        left_mount_duette,
        enter_program_mode_duette,
        duette_set_bottom_limit,
        enter_program_mode_duette,
        duette_set_top_limit_moveup,
        duette_confirm_top_limit,
        duette_set_top_limit,
        test_blinds,
        skiptop,
        enter_program_mode_duette,
        duette_set_top_limit,
        skipbottom_end,
        enter_program_mode_duette,
        duette_re_set_bottom_limit
    ])

m25s_duette_tensioned = Product(
    "M25S Duette tensioned",
    [
        connect_m25s_duette,
        initialise_duette_tensioned,
        right_mount_duette,
        left_mount_duette,
        enter_program_mode_duette,
        duette_set_bottom_limit,
        enter_program_mode_duette,
        duette_set_top_limit_moveup,
        duette_confirm_top_limit,
        duette_set_top_limit,
        test_blinds,
        skiptop,
        enter_program_mode_duette,
        duette_set_top_limit,
        skipbottom_end,
        enter_program_mode_duette,
        duette_re_set_bottom_limit
    ])

m25s_duette_tensioned_alt = Product(
    "M25S Duette tensioned alt",
    [
        connect_m25s_duette,
        initialise_duette_tensioned_alt,
        enter_program_mode_duette,
        tensioned_duette_direction,
        tensioned_duette_switch_direction,
        enter_program_mode_duette,
        duette_set_bottom_limit,
        enter_program_mode_duette,
        duette_set_top_limit_moveup,
        duette_confirm_top_limit,
        duette_set_top_limit,
        test_blinds,
        skiptop,
        enter_program_mode_duette,
        duette_set_top_limit,
        skipbottom_end,
        enter_program_mode_duette,
        duette_re_set_bottom_limit
    ]
)
