from instructor.actions.confirm_product import confirm_twist
from instructor.translations import Translations as Tr
from instructor.actions.connect import connect_twist
from instructor.actions.general import keypad_move_buttons, \
    enter_program_mode, test_blinds, skipslat
from instructor.actions.initialise import initialise_twist
from instructor.actions.motor_direction import left_backroller, \
    right_backroller, \
    left_frontroller, right_frontroller, \
    blind_direction, switch_direction
from instructor.actions.set_bottom_limit import set_bottom_limit, \
    re_set_bottom_limit_twist
from instructor.actions.set_top_limit import set_top_limit_roller
from instructor.actions.skip_step import skiptop, skipbottom_next
from instructor.components import Row, Text, Step, Image, Confirm, \
    DelayedCommand, NordicCommands, Product, NavigationCommand, PvKeypadAlt, \
    Commands
from instructor.constants import ID_TEST_BLINDS, TWIST_JOG_1
from server.nordic import Nd

'''Instruction to quickly make a rb a twist. Not user friendly !'''
connect_make_twist = Step(
    Tr.CONNECT,
    [
        Row(Text(100,
                 "Connect your blind using normal procedure")),
        Row(PvKeypadAlt(
            25,
            okay=Commands(
                nordic_commands=NordicCommands(
                    Nd.NETWORKADD,
                    DelayedCommand(Nd.GROUP_ADD, 1),
                    DelayedCommand(Nd.RESET, 5),
                    DelayedCommand(Nd.TWIST, 5)),
                confirm_command=Confirm(
                    TWIST_JOG_1,
                    Tr.DID_THE_MOTOR_JOG,
                    yes=NavigationCommand(0)))))
    ]
)

# saveSlatOpen = PvKeypadAlt(30, ['okay'], 'okay',
#                            NordicCommands(Nd.SAVE_SLAT_OPEN))

"""
Setting the Twist slat open position
"""
set_twist_position = Step(
    Tr.SET_TWIST_SLAT_POSITION,
    [
        Row(Text(30, Tr.MOVE_BLIND_SLAT_OPEN),
            Text(30, Tr.SAVE_SLAT),
            Text(30, Tr.WATCH_THE_BLIND_JOG)),
        Row(keypad_move_buttons,
            PvKeypadAlt(
                30,
                okay=Commands(
                    nordic_commands=NordicCommands(Nd.SAVE_SLAT_OPEN),
                    confirm_command=Confirm(TWIST_JOG_1, Tr.DID_THE_MOTOR_JOG)
                )
            ),
            Image(30,
                  TWIST_JOG_1))
    ]
)

re_set_twist_slat_open = Step(
    Tr.SET_TWIST_SLAT_POSITION,
    [
        Row(Text(30, Tr.MOVE_BLIND_SLAT_OPEN),
            Text(30, Tr.SAVE_SLAT),
            Text(30, Tr.WATCH_THE_BLIND_JOG)),
        Row(keypad_move_buttons,
            PvKeypadAlt(
                30,
                okay=Commands(
                    nordic_commands=NordicCommands(Nd.SAVE_SLAT_OPEN),
                    confirm_command=Confirm(TWIST_JOG_1,
                                            Tr.DID_THE_MOTOR_JOG,
                                            yes=ID_TEST_BLINDS)
                )
            ),
            Image(30, TWIST_JOG_1))
    ]
)

twist = Product(
    Tr.PRODUCT_PV_TWIST,
    [
        confirm_twist,
        connect_twist,
        initialise_twist,
        left_backroller,
        right_backroller,
        left_frontroller,
        right_frontroller,
        enter_program_mode,
        set_bottom_limit,
        enter_program_mode,
        set_top_limit_roller,
        set_twist_position,
        test_blinds,
        skiptop,
        enter_program_mode,
        set_top_limit_roller,
        skipbottom_next,
        enter_program_mode,
        re_set_bottom_limit_twist,
        skipslat,
        re_set_twist_slat_open
    ])

twist_old = Product(
    {"content": "Twist OLD"},
    [
        confirm_twist,
        connect_twist,
        initialise_twist,
        enter_program_mode,
        blind_direction,
        switch_direction,
        set_bottom_limit,
        enter_program_mode,
        set_top_limit_roller,
        set_twist_position,
        test_blinds,
        skiptop,
        enter_program_mode,
        set_top_limit_roller,
        skipbottom_next,
        enter_program_mode,
        re_set_bottom_limit_twist,
        skipslat,
        re_set_twist_slat_open
    ])
