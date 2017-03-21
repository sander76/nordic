from instructor.actions.connect import connect_rb
from instructor.actions.general import enter_program_mode, test_blinds
from instructor.actions.initialise import initialise_rb
from instructor.actions.motor_direction import left_backroller, \
    right_backroller, \
    left_frontroller, right_frontroller, blind_direction, switch_direction
from instructor.actions.set_bottom_limit import re_set_bottom_limit, \
    set_bottom_limit
from instructor.actions.set_top_limit import set_top_limit_roller
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import Product

rollerblind1 = Product(
    "Roller blind",
    [connect_rb,
     initialise_rb,
     left_backroller,
     right_backroller,
     left_frontroller,
     right_frontroller,
     enter_program_mode,
     set_bottom_limit,
     enter_program_mode,
     set_top_limit_roller,
     test_blinds,
     skiptop,
     enter_program_mode,
     set_top_limit_roller,
     skipbottom_end,
     enter_program_mode,
     re_set_bottom_limit
     ])

rollerblind_old = Product(
    "Roller blind OLD",
    [connect_rb,
     initialise_rb,
     enter_program_mode,
     blind_direction,
     switch_direction,
     set_bottom_limit,
     enter_program_mode,
     set_top_limit_roller,
     test_blinds,
     skiptop,
     enter_program_mode,
     set_top_limit_roller,
     skipbottom_end,
     enter_program_mode,
     re_set_bottom_limit
     ])
