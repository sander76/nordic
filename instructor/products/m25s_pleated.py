from instructor.actions.confirm_product import (
    confirm_pleated_tensioned,
    confirm_pleated,
)
from instructor.actions.connect import connect_m25s_pleated
from instructor.actions.general import enter_program_mode_pleated, test_blinds
from instructor.actions.initialise import (
    initialise_pleated,
    initialise_pleated_tensioned,
)
from instructor.actions.motor_direction import (
    right_mount_pleated,
    left_mount_pleated,
    tensioned_duette_direction,
    tensioned_duette_switch_direction,
)
from instructor.actions.set_bottom_limit import (
    pleated_set_bottom_limit,
    pleated_re_set_bottom_limit,
)
from instructor.actions.set_open_limit import (
    pleated_set_top_limit_moveup,
    pleated_confirm_top_limit,
    pleated_set_top_limit,
)
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

from instructor.translations import Translations as Tr

m25s_pleated_free = Product(
    Tr.PRODUCT_PV_M25S_PLEATED,
    [
        confirm_pleated,
        connect_m25s_pleated,
        initialise_pleated,
        right_mount_pleated,
        left_mount_pleated,
        enter_program_mode_pleated,
        pleated_set_bottom_limit,
        enter_program_mode_pleated,
        pleated_set_top_limit_moveup,
        pleated_confirm_top_limit,
        pleated_set_top_limit,
        test_blinds,
        skiptop,
        enter_program_mode_pleated,
        pleated_set_top_limit,
        skipbottom_end,
        enter_program_mode_pleated,
        pleated_re_set_bottom_limit,
    ],
)

m25s_pleated_tensioned = Product(
    Tr.PRODUCT_PV_M25S_PLEATED_TENSIONED,
    [
        confirm_pleated_tensioned,
        connect_m25s_pleated,
        initialise_pleated_tensioned,
        enter_program_mode_pleated,
        tensioned_duette_direction,
        tensioned_duette_switch_direction,
        enter_program_mode_pleated,
        pleated_set_top_limit_moveup,
        pleated_confirm_top_limit,
        pleated_set_top_limit,
        enter_program_mode_pleated,
        pleated_set_bottom_limit,
        test_blinds,
        skiptop,
        enter_program_mode_pleated,
        pleated_set_top_limit,
        skipbottom_end,
        enter_program_mode_pleated,
        pleated_re_set_bottom_limit,
    ],
)
