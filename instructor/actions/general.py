import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    Commands, Spacer, NavigationCommand
from instructor.constants import ID_TEST_BLINDS, RB_JOG_1, VB_JOG_1, ID_START, \
    DUETTE_JOG_1, PLEATED_JOG_1, VVB_JOG_1
from server.nordic import Nd

keypad_move_buttons = PvKeypad(
    30,
    [PvKeypad.open, PvKeypad.close, PvKeypad.tiltup,
     PvKeypad.tiltdown, PvKeypad.stop])

textrow = Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
              Text(30, tr.WATCH_THE_BLIND_JOG.add_number(2)))

keypad = PvKeypad(30, [PvKeypad.okay], PvKeypad.okay, Commands(Nd.STARTPROGRAM))


def get_enter_program_mode(jog_image):
    return Step(
        tr.ENTER_PROGRAM_MODE,
        [textrow,
         Row(keypad,
             Image(30, jog_image))
         ], Confirm(jog_image,
                    tr.DID_THE_MOTOR_JOG))


enter_program_mode = get_enter_program_mode(RB_JOG_1)

enter_program_mode_vb = get_enter_program_mode(VB_JOG_1)

enter_program_mode_duette = get_enter_program_mode(DUETTE_JOG_1)

enter_program_mode_pleated = get_enter_program_mode(PLEATED_JOG_1)

enter_program_mode_vvb = get_enter_program_mode(VVB_JOG_1)

test_blinds = Step(
    tr.TEST_BLINDS,
    [
        Row(Text(30, tr.TEST_MOVE_BLINDS),
            Text(30, tr.LIMITS_OK),
            Text(30, tr.LIMITS_NOT_OK)),
        Row(keypad_move_buttons,
            PvKeypad(30, [PvKeypad.okay],
                     okay=NavigationCommand(goto=ID_START)),
            PvKeypad(30, [PvKeypad.cancel], cancel=NavigationCommand(1)))
    ], nav_id=ID_TEST_BLINDS)

skipslat = Step(
    tr.TITLE_SKIP_SLAT,
    [
        Row(Text(30, tr.MAKE_CHOICE),
            Text(30, tr.RESET_SLAT),
            Text(30, tr.SELECT_SKIP_SLAT)),
        Row(Spacer(30),
            PvKeypad(30, [PvKeypad.okay], okay=NavigationCommand(goto=1)),
            PvKeypad(30, [PvKeypad.cancel], cancel=NavigationCommand(ID_TEST_BLINDS)))
    ])
