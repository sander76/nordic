from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands, Spacer, NavigationCommand

import static.app.instructions.translations as tr

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

initialise_twist = Step(tr._initialise,
                        [Row(Text(30, tr._press_okay_button.add_number(1)),
                             Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
                         Row(PvKeypad(30, ['okay'], 'okay', Commands('reset', DelayedCommand('twist', 4))),
                             Image(30, "/app/images/m25t_motor_jog2x.png"))
                         ],
                        Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

saveSlatOpen = PvKeypad(30, ['okay'], 'okay', Commands('saveslatopen'))

set_twist_position = Step(tr._set_twist_slatposition,
                          [
                              Row(Text(30, tr._moveblind_slatopen),
                                  Text(30, tr._saveslat),
                                  Text(30, tr._watch_the_blind_jog)),
                              Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                  saveSlatOpen,
                                  Image(30, "/app/images/m25t_motor_jog1x.png"))
                          ],
                          Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

re_set_twist_slat_open = Step(tr._set_twist_slatposition,
                              [
                                  Row(Text(30, tr._moveblind_slatopen),
                                      Text(30, tr._saveslat),
                                      Text(30, tr._watch_the_blind_jog)),
                                  Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                      saveSlatOpen,
                                      Image(30, "/app/images/m25t_motor_jog1x.png"))
                              ],
                              Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog, yes="testblinds"))

skipbottom_twist = Step(tr._skipbottomtitle,
                        [
                            Row(Text(30, tr._make_choice),
                                Text(30, tr._reset_bottom),
                                Text(30, tr._select_skip_bottom)),
                            Row(Spacer(30),
                                PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                                PvKeypad(30, ['cancel'], cancel=3))
                        ])
