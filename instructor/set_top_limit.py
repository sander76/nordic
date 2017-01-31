import instructor.translations as tr
from instructor.components import PvKeypad, Commands, Step, Row, Text, \
    Image, Confirm, DelayedCommand, Spacer
from instructor.constants import VB_JOG_1, RB_JOG_1, DUETTE_JOG_1
from instructor.general import keypad_move_buttons
from server.nordic import STARTPROGRAM, OPEN, SAVE_POSITION_TOP

textrow = Row(Text(30, tr.MOVE_BLIND_TOP.add_number(1)),
              Text(30, tr.SAVE_TOP.add_number(2)),
              Text(30, tr.WATCH_THE_BLIND_JOG.add_number(3)))

keypad_save_top = PvKeypad(30, ['okay'], 'okay', Commands(SAVE_POSITION_TOP))


def get_top_limit(jog_image):
    return Step(tr.SET_TOP_LIMIT,
                [
                    textrow,
                    Row(keypad_move_buttons,
                        keypad_save_top,
                        Image(30, jog_image))
                ],
                Confirm(jog_image, tr.DID_THE_MOTOR_JOG))


def get_top_limit_alternative(jog_image):
    return Step(
        tr.SET_TOP_LIMIT,
        [
            Row(
                Text(30, tr.START_TOP_PROGRAMMING),
                PvKeypad(30, [PvKeypad.okay, PvKeypad.stop], PvKeypad.okay,
                         Commands(STARTPROGRAM, DelayedCommand(OPEN, 3)))
            )
        ], Confirm(None, tr.IS_BLIND_AT_TOP))


def get_confirm_top_limit(jog_image):
    return Step(
        tr.SET_TOP_LIMIT,
        [
            Row(Text(30, tr.SAVE_THIS_AS_TOP)),
            Row(Spacer(30),
                keypad_save_top,
                PvKeypad(30, [PvKeypad.cancel], cancel=1))

        ], Confirm(jog_image, tr.DID_THE_MOTOR_JOG, yes=2)
    )


# ****** Roller
set_top_limit_roller = get_top_limit(RB_JOG_1)

# ****** VB
set_top_limit_vb = get_top_limit(VB_JOG_1)

set_top_limit_alternative_vb = get_top_limit_alternative(VB_JOG_1)

confirm_top_limit_vb = get_confirm_top_limit(VB_JOG_1)

# ****** Duette
set_top_limit_duette = get_top_limit(DUETTE_JOG_1)

set_top_limit_duette_alternative = get_top_limit_alternative(DUETTE_JOG_1)

confirm_top_limit_duette = get_confirm_top_limit(DUETTE_JOG_1)
