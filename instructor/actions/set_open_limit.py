from instructor.translations import Translations as Tr
from instructor.actions.general import keypad_move_buttons
from instructor.components import (
    NordicCommands,
    Step,
    Row,
    Text,
    Image,
    Confirm,
    DelayedCommand,
    Spacer,
    NavigationCommand,
    PvKeypadAlt,
    Commands,
)
from instructor.constants import (
    VB_JOG_1,
    RB_JOG_1,
    DUETTE_JOG_1,
    PLEATED_JOG_1,
    VVB_JOG_1,
)
from server.nordic import Nd


# keypad_save_top = PvKeypadAlt(
#     30,
#     okay=Commands(
#         nordic_commands=NordicCommands(Nd.SAVE_POSITION_TOP),
#         confirm_command=Confirm(jog_image, tr.DID_THE_MOTOR_JOG)
#     )
# )


def get_open_limit(jog_image, title=Tr.TITLE_SET_OPEN_LIMIT):
    return Step(
        title,
        [
            Row(
                Text(30, Tr.MOVE_BLIND_TOP.add_number(1)),
                Text(30, Tr.SAVE_TOP.add_number(2)),
                Text(30, Tr.WATCH_THE_BLIND_JOG.add_number(3)),
            ),
            Row(
                keypad_move_buttons,
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        nordic_commands=NordicCommands(Nd.SAVE_POSITION_TOP),
                        confirm_command=Confirm(
                            jog_image, Tr.DID_THE_MOTOR_JOG
                        ),
                    ),
                ),
                Image(30, jog_image),
            ),
        ],
    )


def get_top_limit_alternative(
    title=Tr.TITLE_SET_OPEN_LIMIT,
    confirm_message=Tr.IS_BLIND_OPENED,
    introtext=Tr.START_OPEN_PROGRAMMING,
):
    return Step(
        title,
        [
            Row(
                Spacer(30),
                Text(30, Tr.PRESS_OKAY_BUTTON.add_number(1)),
                Text(30, introtext.add_number(2)),
            ),
            Row(
                Spacer(30),
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        nordic_commands=NordicCommands(Nd.open),
                        confirm_command=Confirm(None, confirm_message),
                    ),
                ),
                Spacer(30),
            ),
        ],
    )


def get_confirm_open_limit(
    jog_image, title=Tr.TITLE_SET_OPEN_LIMIT, intro_text=Tr.SAVE_THIS_AS_OPEN
):
    return Step(
        title,
        [
            Row(Text(30, intro_text)),
            Row(
                Spacer(30),
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        nordic_commands=NordicCommands(Nd.SAVE_POSITION_TOP),
                        confirm_command=Confirm(
                            jog_image,
                            Tr.DID_THE_MOTOR_JOG,
                            yes=NavigationCommand(2),
                        ),
                    ),
                ),
                PvKeypadAlt(
                    30,
                    cancel=Commands(navigation_command=NavigationCommand(1)),
                ),
            ),
        ],
    )


# ****** Roller
set_top_limit_roller = get_open_limit(RB_JOG_1)

# ****** VB
set_top_limit_vb = get_open_limit(VB_JOG_1)

set_top_limit_vb_moveup = get_top_limit_alternative()

confirm_top_limit_vb = get_confirm_open_limit(VB_JOG_1)

# ****** Duette


duette_set_top_limit_moveup = get_top_limit_alternative()

duette_tensioned_set_top_limit_moveup = get_top_limit_alternative()

duette_confirm_top_limit = get_confirm_open_limit(DUETTE_JOG_1)
duette_set_top_limit = get_open_limit(DUETTE_JOG_1)

pleated_set_top_limit_moveup = get_top_limit_alternative()

pleated_confirm_top_limit = get_confirm_open_limit(PLEATED_JOG_1)
pleated_set_top_limit = get_open_limit(PLEATED_JOG_1)

vvb_set_open_limit_moveup = get_top_limit_alternative(
    title=Tr.TITLE_VVB_SET_OPEN_LIMIT,
    confirm_message=Tr.IS_BLIND_OPENED,
    introtext=Tr.START_OPEN_PROGRAMMING,
)

vvb_confirm_open_limit = get_confirm_open_limit(
    VVB_JOG_1,
    title=Tr.TITLE_VVB_SET_OPEN_LIMIT,
    intro_text=Tr.SAVE_THIS_AS_OPEN,
)

vvb_set_open_limit = Step(
    Tr.TITLE_VVB_SET_OPEN_LIMIT,
    [
        Row(
            Text(30, Tr.MOVE_BLIND_OPEN.add_number(1)),
            Text(30, Tr.SAVE_OPEN.add_number(2)),
            Text(30, Tr.WATCH_THE_BLIND_JOG.add_number(3)),
        ),
        Row(
            keypad_move_buttons,
            PvKeypadAlt(
                30,
                okay=Commands(
                    nordic_commands=NordicCommands(Nd.SAVE_POSITION_TOP),
                    confirm_command=Confirm(VVB_JOG_1, Tr.DID_THE_MOTOR_JOG),
                ),
            ),
            Image(30, VVB_JOG_1),
        ),
    ],
)
