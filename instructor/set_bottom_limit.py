import instructor.translations as tr
from instructor.components import PvKeypad, Commands, Step, Row, Text, Image, Confirm
from instructor.general import keypad_move_buttons

savepositionBottom = PvKeypad(30, ['okay'], 'okay', Commands('savepositionbottom'))

textrow = Row(Text(30, tr._moveblind_bottom.add_number(1)),
              Text(30, tr._savebottom.add_number(2)),
              Text(30, tr._watch_the_blind_jog.add_number(3)))

set_bottom_limit = Step(tr._setbottomlimit,
                        [
                            textrow,
                            Row(keypad_move_buttons,
                                savepositionBottom,
                                Image(30, "/app/images/m25t_motor_jog1x.png"))
                        ],
                        Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

set_bottom_limit_vb = Step(tr._setbottomlimit,
                           [
                               textrow,
                               Row(keypad_move_buttons,
                                   savepositionBottom,
                                   Image(30, "/app/images/m25s_vb_motor_jog1x.png"))
                           ],
                           Confirm("/app/images/m25s_vb_motor_jog1x.png", tr._did_the_motor_jog))

'''
Same as normal setting the bottom limits, but confirm dialog navigates to different page when ok.
'''
re_set_bottom_limit = Step(tr._setbottomlimit,
                           set_bottom_limit.instructions,
                           Confirm("/app/images/m25t_motor_top_limit_move_up_rollo.png", tr._did_the_motor_move_up,
                                   yes="testblinds"))

'''
same as setting bottom limit.
'''
re_set_bottom_limit_twist = Step(tr._setbottomlimit,
                                 set_bottom_limit.instructions,
                                 Confirm("/app/images/m25t_motor_top_limit_move_up_rollo.png",
                                         tr._did_the_motor_move_up))

re_set_bottom_limit_vb = Step(tr._setbottomlimit,
                              [
                                  textrow,
                                  Row(keypad_move_buttons,
                                      savepositionBottom,
                                      Image(30, "/app/images/m25s_vb_motor_jog1x.png"))
                              ],
                              Confirm("/app/images/m25s_vb_motor_jog1x.png", tr._did_the_motor_jog,yes="testblinds"))
