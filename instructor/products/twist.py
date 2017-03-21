import instructor.translations as tr
from instructor.actions.connect import connect_twist
from instructor.actions.general import keypad_move_buttons, enter_program_mode, \
    test_blinds, skipslat
from instructor.actions.initialise import initialise_twist
from instructor.actions.motor_direction import left_backroller, right_backroller, \
    left_frontroller, right_frontroller, \
    blind_direction, switch_direction
from instructor.actions.set_bottom_limit import set_bottom_limit, \
    re_set_bottom_limit_twist
from instructor.actions.set_top_limit import set_top_limit_roller
from instructor.actions.skip_step import skiptop, skipbottom_next
from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands, Product
from instructor.constants import ID_TEST_BLINDS, TWIST_JOG_1
from server.nordic import Nd

'''Instruction to quickly make a rb a twist. Not user friendly !'''
connect_make_twist = Step(
    tr.CONNECT,
    [
        Row(Text(100,
                 "Connect your blind using normal procedure")),
        Row(PvKeypad(25, ['okay'], 'okay',
                     Commands(Nd.NETWORKADD,
                              DelayedCommand(Nd.GROUP_ADD,
                                             1),
                              DelayedCommand(Nd.RESET, 5),
                              DelayedCommand(Nd.TWIST,
                                             5))))
    ],
    Confirm(TWIST_JOG_1,
            tr.DID_THE_MOTOR_JOG, yes=0))

saveSlatOpen = PvKeypad(30, ['okay'], 'okay', Commands(Nd.SAVE_SLAT_OPEN))

"""
Setting the Twist slat open position
"""
set_twist_position = Step(tr.SET_TWIST_SLAT_POSITION,
                          [
                              Row(Text(30, tr.MOVE_BLIND_SLAT_OPEN),
                                  Text(30, tr.SAVE_SLAT),
                                  Text(30, tr.WATCH_THE_BLIND_JOG)),
                              Row(keypad_move_buttons,
                                  saveSlatOpen,
                                  Image(30,
                                        TWIST_JOG_1))
                          ],
                          Confirm(TWIST_JOG_1,
                                  tr.DID_THE_MOTOR_JOG))

re_set_twist_slat_open = Step(
    tr.SET_TWIST_SLAT_POSITION,
    [
        Row(Text(30, tr.MOVE_BLIND_SLAT_OPEN),
            Text(30, tr.SAVE_SLAT),
            Text(30, tr.WATCH_THE_BLIND_JOG)),
        Row(keypad_move_buttons,
            saveSlatOpen,
            Image(30,
                  TWIST_JOG_1))
    ],
    Confirm(TWIST_JOG_1,
            tr.DID_THE_MOTOR_JOG, yes=ID_TEST_BLINDS))

twist = Product("Twist", [connect_twist,
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

twist_old = Product("Twist OLD", [connect_twist,
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
