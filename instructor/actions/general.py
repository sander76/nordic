# import instructor.translations as tr
from instructor.translations import Translations as tr
from instructor.components import Row, Text, Step, Image, Confirm, \
    NordicCommands, Spacer, NavigationCommand, PvKeypadAlt, default_open, \
    default_close, default_stop, default_tiltclose, default_tiltopen, Commands
from instructor.constants import ID_TEST_BLINDS, RB_JOG_1, VB_JOG_1, \
    ID_START, DUETTE_JOG_1, PLEATED_JOG_1, VVB_JOG_1, ID_CHOOSE_SAME
from server.nordic import Nd

# keypad_move_buttons = PvKeypad(
#     30,
#     [PvKeypad.open, PvKeypad.close, PvKeypad.tiltup,
#      PvKeypad.tiltdown, PvKeypad.stop])

keypad_move_buttons = PvKeypadAlt(
    30,
    open=default_open,
    close=default_close,
    stop=default_stop,
    tiltdown=default_tiltclose,
    tiltup=default_tiltopen
)

textrow = Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
              Text(30, tr.WATCH_THE_BLIND_JOG.add_number(2)))


def get_enter_program_mode(jog_image, nav_id=None):
    return Step(
        tr.ENTER_PROGRAM_MODE,
        [textrow,
         Row(
             PvKeypadAlt(
                 30,
                 okay=Commands(
                     nordic_commands=NordicCommands(Nd.STARTPROGRAM),
                     confirm_command=Confirm(jog_image,
                                             tr.DID_THE_MOTOR_JOG)
                 )
             ),
             Image(30, jog_image))
         ], nav_id=nav_id)


enter_program_mode = get_enter_program_mode(RB_JOG_1)

enter_program_mode_vb = get_enter_program_mode(VB_JOG_1)

enter_program_mode_duette = get_enter_program_mode(DUETTE_JOG_1)

enter_program_mode_pleated = get_enter_program_mode(PLEATED_JOG_1)

enter_program_mode_vvb = get_enter_program_mode(VVB_JOG_1)

enter_program_mode_vvb_id = get_enter_program_mode(
    VVB_JOG_1,
    nav_id="vvb_start_program"
)

test_blinds = Step(
    tr.TEST_BLINDS,
    [
        Row(Text(30, tr.TEST_MOVE_BLINDS),
            Text(30, tr.LIMITS_OK),
            Text(30, tr.LIMITS_NOT_OK)),
        Row(keypad_move_buttons,
            PvKeypadAlt(30,
                        okay=Commands(
                            navigation_command=NavigationCommand(ID_START))),

            PvKeypadAlt(30,
                        cancel=Commands(
                            navigation_command=NavigationCommand(1))))
    ], nav_id=ID_TEST_BLINDS)

test_blinds_open_close = Step(
    tr.TEST_BLINDS,
    [
        Row(Text(30, tr.TEST_CHECK_BLINDS_OPEN_CLOSE),
            Text(30, tr.LIMITS_OK),
            Text(30, tr.LIMITS_NOT_OK)),
        Row(keypad_move_buttons,
            PvKeypadAlt(30,
                        okay=Commands(
                            navigation_command=NavigationCommand(ID_START))),

            PvKeypadAlt(30,
                        cancel=Commands(
                            navigation_command=NavigationCommand(1))))
    ], nav_id=ID_TEST_BLINDS)

test_blinds_open_close_product_choice = Step(
    tr.TEST_BLINDS,
    [
        Row(Text(30, tr.TEST_CHECK_BLINDS_OPEN_CLOSE),
            Text(30, tr.LIMITS_OK),
            Text(30, tr.LIMITS_NOT_OK)),
        Row(keypad_move_buttons,
            PvKeypadAlt(30,
                        okay=Commands(
                            navigation_command=NavigationCommand(ID_CHOOSE_SAME))),

            PvKeypadAlt(30,
                        cancel=Commands(
                            navigation_command=NavigationCommand(1))))
    ], nav_id=ID_TEST_BLINDS)

test_blinds_alt = Step(
    tr.TEST_BLINDS,
    [
        Row(Text(30, tr.TEST_MOVE_BLINDS),
            Text(30, tr.LIMITS_OK),
            Text(30, tr.LIMITS_NOT_OK)),
        Row(keypad_move_buttons,
            PvKeypadAlt(30,
                        okay=Commands(
                            navigation_command=NavigationCommand(ID_CHOOSE_SAME))),

            PvKeypadAlt(30,
                        cancel=Commands(
                            navigation_command=NavigationCommand(1))))
    ], nav_id=ID_TEST_BLINDS)



skipslat = Step(
    tr.TITLE_SKIP_SLAT,
    [
        Row(Text(30, tr.MAKE_CHOICE),
            Text(30, tr.RESET_SLAT),
            Text(30, tr.SELECT_SKIP_SLAT)),
        Row(Spacer(30),
            PvKeypadAlt(30,
                        okay=Commands(
                            navigation_command=NavigationCommand(goto=1))),
            PvKeypadAlt(30,
                        cancel=Commands(
                            navigation_command=NavigationCommand(
                                ID_TEST_BLINDS))))
    ])
