import instructor.translations as tr
from instructor.components import PvKeypad, Commands, Step, Row, Text, Image, \
    Confirm
from instructor.constants import RB_JOG_1, VB_JOG_1, RB_MOVE_UP, \
    DUETTE_JOG_1, TWIST_MOVE_UP, ID_TEST_BLINDS
from instructor.general import keypad_move_buttons
from server.nordic import SAVE_POSITION_BOTTOM

savepositionBottom = PvKeypad(30, ['okay'], 'okay',
                              Commands(SAVE_POSITION_BOTTOM))

textrow = Row(Text(30, tr.MOVE_BLIND_BOTTOM.add_number(1)),
              Text(30, tr.SAVE_BOTTOM.add_number(2)),
              Text(30, tr.WATCH_THE_BLIND_JOG.add_number(3)))


def get_bottom_limit(jog_image):
    return Step(tr.SET_BOTTOM_LIMIT,
                [
                    textrow,
                    Row(keypad_move_buttons,
                        savepositionBottom,
                        Image(30, jog_image))
                ],
                Confirm(jog_image, tr.DID_THE_MOTOR_JOG))


set_bottom_limit = get_bottom_limit(RB_JOG_1)

# set_bottom_limit_vb = Step(tr._setbottomlimit,
#                            [
#                                textrow,
#                                Row(keypad_move_buttons,
#                                    savepositionBottom,
#                                    Image(30, "/app/images/m25s_vb_motor_jog1x.png"))
#                            ],
#                            Confirm("/app/images/m25s_vb_motor_jog1x.png", tr._did_the_motor_jog))


# set_bottom_limit_vb.instructions[1].col3.src = VB_JOG_1

'''
Same as normal setting the bottom limits,
but confirm dialog navigates to different page when ok.
'''
# re_set_bottom_limit = Step(tr._setbottomlimit,
#                            set_bottom_limit.instructions,
#                            Confirm("/app/images/m25t_motor_top_limit_move_up_rollo.png", tr._did_the_motor_move_up,
#                                    yes=ID_TEST_BLINDS))
re_set_bottom_limit = get_bottom_limit(RB_MOVE_UP)
re_set_bottom_limit.confirm = Confirm(RB_MOVE_UP, tr.DID_THE_MOTOR_MOVE_UP,
                                      yes=ID_TEST_BLINDS)

'''
same as setting bottom limit.
'''
# re_set_bottom_limit_twist = Step(tr._setbottomlimit,
#                                  set_bottom_limit.instructions,
#                                  Confirm("/app/images/m25t_motor_top_limit_move_up_rollo.png",
#                                          tr._did_the_motor_move_up))

re_set_bottom_limit_twist = get_bottom_limit(TWIST_MOVE_UP)
re_set_bottom_limit_twist.confirm = Confirm(TWIST_MOVE_UP,
                                            tr.DID_THE_MOTOR_MOVE_UP)

# re_set_bottom_limit_vb = Step(tr._setbottomlimit,
#                               [
#                                   textrow,
#                                   Row(keypad_move_buttons,
#                                       savepositionBottom,
#                                       Image(30, "/app/images/m25s_vb_motor_jog1x.png"))
#                               ],
#                               Confirm("/app/images/m25s_vb_motor_jog1x.png", tr._did_the_motor_jog, yes=ID_TEST_BLINDS))

set_bottom_limit_vb = get_bottom_limit(VB_JOG_1)

re_set_bottom_limit_vb = get_bottom_limit(VB_JOG_1)
re_set_bottom_limit_vb.confirm = Confirm(VB_JOG_1, tr.DID_THE_MOTOR_JOG,
                                         yes=ID_TEST_BLINDS)

"""
Duette and Pleated
"""
set_bottom_limit_duette = get_bottom_limit(DUETTE_JOG_1)

re_set_bottom_limit_duette = get_bottom_limit(DUETTE_JOG_1)
re_set_bottom_limit_duette.confirm = Confirm(DUETTE_JOG_1,
                                             tr.DID_THE_MOTOR_JOG,
                                             yes=ID_TEST_BLINDS)
