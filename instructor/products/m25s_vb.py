from instructor.actions.confirm_product import confirm_vb
from instructor.actions.connect import connect_m25s_vb
from instructor.actions.general import enter_program_mode_vb, test_blinds
from instructor.actions.initialise import initialise_vb35
from instructor.actions.motor_direction import (
    right_mount_vb,
    left_mount_vb,
    vb_16mm_type,
    vb_25mm_type,
    right_mount_vb35,
    left_mount_vb35,
)
from instructor.actions.set_bottom_limit import (
    set_bottom_limit_vb,
    re_set_bottom_limit_vb,
)
from instructor.actions.set_top_limit import (
    set_top_limit_vb,
    set_top_limit_vb_moveup,
    confirm_top_limit_vb,
)
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

from instructor.translations import Translations as Tr

m25s_vb_free = Product(
    Tr.PRODUCT_PV_M25S_VB,
    [
        confirm_vb,
        connect_m25s_vb,
        vb_16mm_type,
        vb_25mm_type,
        right_mount_vb,
        left_mount_vb,
        enter_program_mode_vb,
        set_bottom_limit_vb,
        enter_program_mode_vb,
        set_top_limit_vb_moveup,
        confirm_top_limit_vb,
        set_top_limit_vb,
        test_blinds,
        skiptop,
        enter_program_mode_vb,
        set_top_limit_vb,
        skipbottom_end,
        enter_program_mode_vb,
        re_set_bottom_limit_vb,
    ],
)

m25s_vb_35 = Product(
    Tr.PRODUCT_PV_M25S_VB,
    [
        confirm_vb,
        connect_m25s_vb,
        initialise_vb35,
        right_mount_vb35,
        left_mount_vb35,
        enter_program_mode_vb,
        set_bottom_limit_vb,
        enter_program_mode_vb,
        set_top_limit_vb_moveup,
        confirm_top_limit_vb,
        set_top_limit_vb,
        test_blinds,
        skiptop,
        enter_program_mode_vb,
        set_top_limit_vb,
        skipbottom_end,
        enter_program_mode_vb,
        re_set_bottom_limit_vb,
    ],
)
