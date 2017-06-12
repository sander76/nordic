from instructor.translations import Translations as Tr
from instructor.actions.general import keypad_move_buttons
from instructor.components import NordicCommands, Step, Row, Text, Image, \
    Confirm, PvKeypadAlt, Commands, NavigationCommand
from instructor.constants import RB_JOG_1, VB_JOG_1, RB_MOVE_UP, \
    DUETTE_JOG_1, TWIST_MOVE_UP, ID_TEST_BLINDS, PLEATED_JOG_1, VVB_JOG_1
from server.nordic import Nd


# savepositionBottom = PvKeypad(30, ['okay'], 'okay',
#                               NordicCommands(Nd.SAVE_POSITION_BOTTOM))


def get_bottom_limit(
        jog_image=RB_JOG_1,
        confirm_image=RB_JOG_1,
        confirm_text=Tr.DID_THE_MOTOR_JOG,
        title=Tr.TITLE_SET_BOTTOM_LIMIT,
        confirm_yes_goto=1,
        move_blind_message=Tr.MOVE_BLIND_BOTTOM,
        save_position=Tr.SAVE_BOTTOM):
    return Step(
        title,
        [
            Row(Text(30, move_blind_message.add_number(1)),
                Text(30, save_position.add_number(2)),
                Text(30, Tr.WATCH_THE_BLIND_JOG.add_number(3))),
            Row(keypad_move_buttons,
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        nordic_commands=NordicCommands(
                            Nd.SAVE_POSITION_BOTTOM),
                        confirm_command=Confirm(confirm_image, confirm_text,
                                                yes=NavigationCommand(
                                                    confirm_yes_goto))
                    )
                ),
                Image(30, jog_image))
        ]
    )


set_bottom_limit = get_bottom_limit(RB_JOG_1)
# Same as normal setting the bottom limits,
# but confirm dialog navigates to different page when ok.
re_set_bottom_limit = get_bottom_limit(RB_MOVE_UP)
re_set_bottom_limit.confirm = Confirm(RB_MOVE_UP, Tr.DID_THE_MOTOR_MOVE_UP,
                                      yes=NavigationCommand(ID_TEST_BLINDS))

# Same as normal setting the bottom limits,
# but confirm dialog navigates to different page when ok.
re_set_bottom_limit_twist = get_bottom_limit(TWIST_MOVE_UP)
re_set_bottom_limit_twist.confirm = Confirm(TWIST_MOVE_UP,
                                            Tr.DID_THE_MOTOR_MOVE_UP)

set_bottom_limit_vb = get_bottom_limit(VB_JOG_1)
# Same as normal setting the bottom limits,
# but confirm dialog navigates to different page when ok.
re_set_bottom_limit_vb = get_bottom_limit(VB_JOG_1)
re_set_bottom_limit_vb.confirm = Confirm(VB_JOG_1, Tr.DID_THE_MOTOR_JOG,
                                         yes=NavigationCommand(ID_TEST_BLINDS))

# Duette and Pleated
duette_set_bottom_limit = get_bottom_limit(DUETTE_JOG_1)
duette_re_set_bottom_limit = get_bottom_limit(
    DUETTE_JOG_1, DUETTE_JOG_1, Tr.DID_THE_MOTOR_JOG,
    confirm_yes_goto=ID_TEST_BLINDS)

# Pleated
pleated_set_bottom_limit = get_bottom_limit(PLEATED_JOG_1, PLEATED_JOG_1)
pleated_re_set_bottom_limit = get_bottom_limit(
    PLEATED_JOG_1, PLEATED_JOG_1, confirm_yes_goto=ID_TEST_BLINDS)

# VVB
vvb_set_close_limit = get_bottom_limit(
    VVB_JOG_1, VVB_JOG_1,
    title=Tr.TITLE_VVB_SET_CLOSE_LIMIT,
    move_blind_message=Tr.MOVE_BLIND_CLOSE,
    save_position=Tr.SAVE_CLOSE)

vvb_re_set_close_limit = get_bottom_limit(
    VVB_JOG_1, VVB_JOG_1,
    title=Tr.TITLE_VVB_SET_CLOSE_LIMIT,
    confirm_yes_goto=ID_TEST_BLINDS,
    move_blind_message=Tr.MOVE_BLIND_CLOSE,
    save_position=Tr.SAVE_CLOSE
)
