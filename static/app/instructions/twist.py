
from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands, Spacer, NavigationCommand, Product

import static.app.instructions.translations as tr
from static.app.instructions.connect import connect
from static.app.instructions.general import keypad_move_buttons, enter_program_mode, test_blinds, skipslat
from static.app.instructions.initialise import initialise_twist
from static.app.instructions.motor_direction import left_backroller, right_backroller, left_frontroller, \
    right_frontroller, blind_direction, switch_direction
from static.app.instructions.set_bottom_limit import set_bottom_limit, re_set_bottom_limit_twist
from static.app.instructions.set_top_limit import set_top_limit
from static.app.instructions.skip_step import skiptop, skipbottom_next

'''Instruction to quickly make a rb a twist. Not user friendly !'''
connect_make_twist = Step(tr._connect,
                          [
                              Row(Text(100, "Connect your blind using normal procedure")),
                              Row(PvKeypad(25, ['okay'], 'okay', Commands('networkadd',
                                                                          DelayedCommand('group1add', 1),
                                                                          DelayedCommand('reset', 5),
                                                                          DelayedCommand('twist', 5))))
                          ],
                          Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog, yes=0))



saveSlatOpen = PvKeypad(30, ['okay'], 'okay', Commands('saveslatopen'))

"""
Setting the Twist slat open position
"""
set_twist_position = Step(tr._set_twist_slatposition,
                          [
                              Row(Text(30, tr._moveblind_slatopen),
                                  Text(30, tr._saveslat),
                                  Text(30, tr._watch_the_blind_jog)),
                              Row(keypad_move_buttons,
                                  saveSlatOpen,
                                  Image(30, "/app/images/m25t_motor_jog1x.png"))
                          ],
                          Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

re_set_twist_slat_open = Step(tr._set_twist_slatposition,
                              [
                                  Row(Text(30, tr._moveblind_slatopen),
                                      Text(30, tr._saveslat),
                                      Text(30, tr._watch_the_blind_jog)),
                                  Row(keypad_move_buttons,
                                      saveSlatOpen,
                                      Image(30, "/app/images/m25t_motor_jog1x.png"))
                              ],
                              Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog, yes="testblinds"))


twist = Product("Twist", [connect,
                          initialise_twist,
                          left_backroller,
                          right_backroller,
                          left_frontroller,
                          right_frontroller,
                          enter_program_mode,
                          set_bottom_limit,
                          enter_program_mode,
                          set_top_limit,
                          set_twist_position,
                          test_blinds,
                          skiptop,
                          enter_program_mode,
                          set_top_limit,
                          skipbottom_next,
                          enter_program_mode,
                          re_set_bottom_limit_twist,
                          skipslat,
                          re_set_twist_slat_open
                          ])

twist_old = Product("Twist OLD", [connect,
                                  initialise_twist,
                                  enter_program_mode,
                                  blind_direction,
                                  switch_direction,
                                  set_bottom_limit,
                                  enter_program_mode,
                                  set_top_limit,
                                  set_twist_position,
                                  test_blinds,
                                  skiptop,
                                  enter_program_mode,
                                  set_top_limit,
                                  skipbottom_next,
                                  enter_program_mode,
                                  re_set_bottom_limit_twist,
                                  skipslat,
                                  re_set_twist_slat_open
                                  ])