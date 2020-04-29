from instructor.actions.confirm_product import confirm_rb
from instructor.actions.connect import connect_rb
from instructor.actions.general import (
    enter_program_mode,
    test_blinds,
    clearshade,
    test_blinds_disconnect,
)
from instructor.actions.initialise import initialise_rb
from instructor.actions.motor_direction import (
    left_backroller,
    right_backroller,
    left_frontroller,
    right_frontroller,
)
from instructor.actions.set_bottom_limit import (
    re_set_bottom_limit,
    set_bottom_limit,
)
from instructor.actions.set_open_limit import set_top_limit_roller
from instructor.actions.skip_step import skiptop, skipbottom_end
from instructor.components import (
    Product,
    Step,
    Row,
    PvKeypadAlt,
    default_open,
    default_close,
    default_tiltopen,
    default_tiltclose,
    default_stop,
    Commands,
    Confirm,
    NavigationCommand,
    NordicCommands,
)
from instructor.constants import RB_JOG_1, RB_JOG_2
from instructor.translations import Translations as Tr, load_translations
from server.nordic import Nd

# keypad_move_buttons_alt = PvKeypadAlt(
#     30,
#     open=default_open,
#     close=default_close,
#     tiltup=default_tiltopen,
#     tiltdown=default_tiltclose,
#     stop=default_stop,
#     cancel=Commands(
#         nordic_commands=NordicCommands(Nd.open),
#         confirm_command=Confirm(RB_JOG_1, "did it jog")
#     ),
#     okay=Commands(
#         navigation_command=NavigationCommand(1)
#     )
# )
#
# keypad_move_buttons_alt1 = PvKeypadAlt(
#     30,
#     open=default_open,
#     close=default_close,
#     tiltup=default_tiltopen,
#     tiltdown=default_tiltclose,
#     stop=default_stop,
#     cancel=Commands(
#         nordic_commands=NordicCommands(Nd.stop),
#         confirm_command=Confirm(RB_JOG_1, "did it jog")
#     ),
#     okay=Commands(
#         nordic_commands=NordicCommands(Nd.open),
#         confirm_command=Confirm(RB_JOG_2, "did it jog twice")
#     )
# )
#
# test_blinds1 = Product(
#     "tester",
#     [
#         Step(
#             Tr.TEST_BLINDS,
#             [
#                 Row(keypad_move_buttons_alt)
#             ]),
#         Step(
#             Tr.BLIND_DIRECTION,
#             [
#                 Row(keypad_move_buttons_alt1)
#             ])
#     ])
#
# test1 = Product("test", [
#     test_blinds1
# ])

# disconnect = Step(
#     Tr.TEST_BLINDS,
#     [
#         Row(Text(30, Tr.TEST_CHECK_BLINDS_OPEN_CLOSE),
#             Text(30, Tr.LIMITS_OK),
#             Text(30, Tr.LIMITS_NOT_OK)),
#         Row(keypad_move_buttons,
#             PvKeypadAlt(30,
#                         okay=Commands(
#                             nordic_commands=NordicCommands(
#                                 Nd.TO_HUB_ID,
#                                 DelayedCommand(Nd.NETWORK_RESET, 1),
#                                 DelayedCommand(Nd.SET_DONGLE_ID, 1)
#                             ),
#                             navigation_command=NavigationCommand(ID_START))),
#
#             PvKeypadAlt(30,
#                         cancel=Commands(
#                             navigation_command=NavigationCommand(1))))
#     ], nav_id=ID_TEST_BLINDS)

test_roller = Product(
    Tr.PRODUCT_PV_ROLLERBLIND,
    [
        confirm_rb,
        connect_rb,
        initialise_rb,
        left_backroller,
        right_backroller,
        left_frontroller,
        right_frontroller,
        enter_program_mode,
        set_bottom_limit,
        enter_program_mode,
        set_top_limit_roller,
        test_blinds_disconnect,
        skiptop,
        enter_program_mode,
        set_top_limit_roller,
        skipbottom_end,
        enter_program_mode,
        re_set_bottom_limit,
    ],
)
