
from static.app.instructions.components import Product
from static.app.instructions.connect import connect
from static.app.instructions.general import enter_program_mode, test_blinds
from static.app.instructions.initialise import initialise_roller
from static.app.instructions.motor_direction import left_backroller, right_backroller, left_frontroller, \
    right_frontroller, blind_direction, switch_direction
from static.app.instructions.set_bottom_limit import re_set_bottom_limit, set_bottom_limit
from static.app.instructions.set_top_limit import set_top_limit
from static.app.instructions.skip_step import skiptop, skipbottom_end

rollerblind1 = Product("Roller blind", [connect,
                                        initialise_roller,
                                        left_backroller,
                                        right_backroller,
                                        left_frontroller,
                                        right_frontroller,
                                        enter_program_mode,
                                        set_bottom_limit,
                                        enter_program_mode,
                                        set_top_limit,
                                        test_blinds,
                                        skiptop,
                                        enter_program_mode,
                                        set_top_limit,
                                        skipbottom_end,
                                        enter_program_mode,
                                        re_set_bottom_limit
                                        ])

rollerblind_old = Product("Roller blind OLD", [connect,
                                               initialise_roller,
                                               enter_program_mode,
                                               blind_direction,
                                               switch_direction,
                                               set_bottom_limit,
                                               enter_program_mode,
                                               set_top_limit,
                                               test_blinds,
                                               skiptop,
                                               enter_program_mode,
                                               set_top_limit,
                                               skipbottom_end,
                                               enter_program_mode,
                                               re_set_bottom_limit
                                               ])