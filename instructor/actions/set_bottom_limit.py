import instructor.translations as tr
from instructor.actions.general import keypad_move_buttons
from instructor.components import PvKeypad, Commands, Step, Row, Text, Image, \
    Confirm
from instructor.constants import RB_JOG_1, VB_JOG_1, RB_MOVE_UP, \
    DUETTE_JOG_1, TWIST_MOVE_UP, ID_TEST_BLINDS, PLEATED_JOG_1
from server.nordic import Nd

savepositionBottom = PvKeypad(30, ['okay'], 'okay',
                              Commands(Nd.SAVE_POSITION_BOTTOM))

textrow = Row(Text(30, tr.MOVE_BLIND_BOTTOM.add_number(1)),
              Text(30, tr.SAVE_BOTTOM.add_number(2)),
              Text(30, tr.WATCH_THE_BLIND_JOG.add_number(3)))


def get_bottom_limit(
        jog_image=RB_JOG_1, confirm_image=RB_JOG_1,
        confirm_text=tr.DID_THE_MOTOR_JOG, confirm_yes_goto=1):
    return Step(tr.SET_BOTTOM_LIMIT,
                [
                    textrow,
                    Row(keypad_move_buttons,
                        savepositionBottom,
                        Image(30, jog_image))
                ],
                Confirm(confirm_image, confirm_text, yes=confirm_yes_goto))


set_bottom_limit = get_bottom_limit(RB_JOG_1)
# Same as normal setting the bottom limits,
# but confirm dialog navigates to different page when ok.
re_set_bottom_limit = get_bottom_limit(RB_MOVE_UP)
re_set_bottom_limit.confirm = Confirm(RB_MOVE_UP, tr.DID_THE_MOTOR_MOVE_UP,
                                      yes=ID_TEST_BLINDS)

# Same as normal setting the bottom limits,
# but confirm dialog navigates to different page when ok.
re_set_bottom_limit_twist = get_bottom_limit(TWIST_MOVE_UP)
re_set_bottom_limit_twist.confirm = Confirm(TWIST_MOVE_UP,
                                            tr.DID_THE_MOTOR_MOVE_UP)

set_bottom_limit_vb = get_bottom_limit(VB_JOG_1)
# Same as normal setting the bottom limits,
# but confirm dialog navigates to different page when ok.
re_set_bottom_limit_vb = get_bottom_limit(VB_JOG_1)
re_set_bottom_limit_vb.confirm = Confirm(VB_JOG_1, tr.DID_THE_MOTOR_JOG,
                                         yes=ID_TEST_BLINDS)

# Duette and Pleated
set_bottom_limit_duette = get_bottom_limit(DUETTE_JOG_1)

re_set_bottom_limit_duette = get_bottom_limit(DUETTE_JOG_1)
re_set_bottom_limit_duette.confirm = Confirm(DUETTE_JOG_1,
                                             tr.DID_THE_MOTOR_JOG,
                                             yes=ID_TEST_BLINDS)

set_bottom_limit_pleated = get_bottom_limit(PLEATED_JOG_1, PLEATED_JOG_1)

re_set_bottom_limit_pleated = get_bottom_limit(
    PLEATED_JOG_1, PLEATED_JOG_1, confirm_yes_goto=ID_TEST_BLINDS)
