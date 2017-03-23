import instructor.translations as tr
from instructor.actions.general import keypad_move_buttons
from instructor.components import PvKeypad, Commands, Step, Row, Text, \
    Image, Confirm, DelayedCommand, Spacer, NavigationCommand
from instructor.constants import VB_JOG_1, RB_JOG_1, DUETTE_JOG_1, \
    PLEATED_JOG_1, VVB_JOG_1
from server.nordic import Nd

textrow = Row(Text(30, tr.MOVE_BLIND_TOP.add_number(1)),
              Text(30, tr.SAVE_TOP.add_number(2)),
              Text(30, tr.WATCH_THE_BLIND_JOG.add_number(3)))

keypad_save_top = PvKeypad(
    30, ['okay'], 'okay', Commands(Nd.SAVE_POSITION_TOP))


def get_top_limit(jog_image, title=tr.TITLE_SET_TOP_LIMIT):
    return Step(
        title,
        [
            textrow,
            Row(keypad_move_buttons,
                keypad_save_top,
                Image(30, jog_image))
        ],
        Confirm(jog_image, tr.DID_THE_MOTOR_JOG))


def get_top_limit_alternative(title=tr.TITLE_SET_TOP_LIMIT):
    return Step(
        title,
        [
            Row(
                Text(30, tr.START_TOP_PROGRAMMING),
                PvKeypad(30, [PvKeypad.okay, PvKeypad.stop], PvKeypad.okay,
                         Commands(Nd.STARTPROGRAM, DelayedCommand(Nd.open, 3)))
            )
        ], Confirm(None, tr.IS_BLIND_AT_TOP))


def get_confirm_top_limit(jog_image, title=tr.TITLE_SET_TOP_LIMIT):
    return Step(
        title,
        [
            Row(Text(30, tr.SAVE_THIS_AS_TOP)),
            Row(Spacer(30),
                keypad_save_top,
                PvKeypad(30, [PvKeypad.cancel], cancel=NavigationCommand(1)))

        ], Confirm(jog_image, tr.DID_THE_MOTOR_JOG, yes=2)
    )


# ****** Roller
set_top_limit_roller = get_top_limit(RB_JOG_1)

# ****** VB
set_top_limit_vb = get_top_limit(VB_JOG_1)

set_top_limit_alternative_vb = get_top_limit_alternative()

confirm_top_limit_vb = get_confirm_top_limit(VB_JOG_1)

# ****** Duette


duette_set_top_limit_moveup = get_top_limit_alternative()
duette_confirm_top_limit = get_confirm_top_limit(DUETTE_JOG_1)
duette_set_top_limit = get_top_limit(DUETTE_JOG_1)

pleated_set_top_limit_moveup = get_top_limit_alternative()
pleated_confirm_top_limit = get_confirm_top_limit(PLEATED_JOG_1)
pleated_set_top_limit = get_top_limit(PLEATED_JOG_1)

vvb_set_open_limit_moveup = get_top_limit_alternative(
    title=tr.TITLE_VVB_SET_OPEN_LIMIT)
vvb_confirm_open_limit = get_confirm_top_limit(
    VVB_JOG_1, title=tr.TITLE_VVB_SET_OPEN_LIMIT)
vvb_set_open_limit = get_top_limit(
    VVB_JOG_1, title=tr.TITLE_VVB_SET_OPEN_LIMIT)
