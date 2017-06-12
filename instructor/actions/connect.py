from instructor.translations import Translations as Tr
from instructor.components import Row, Text, Step, Image, Confirm, \
    DelayedCommand, NordicCommands, PvKeypadAlt, Commands
from instructor.constants import TWIST_JOG_1, TWIST_BUTTON_PUSH_HOLD, \
    TWIST_BUTTON_RELEASE, RB_JOG_1, RB_BUTTON_PUSH_HOLD, RB_BUTTON_RELEASE, \
    ID_START, VB_JOG_1, VB_BUTTON_PUSH_HOLD, VB_BUTTON_RELEASE, DUETTE_JOG_1, \
    DUETTE_BUTTON_PUSH_HOLD, DUETTE_BUTTON_RELEASE, VVB_JOG_1, \
    VVB_BUTTON_PUSH_HOLD, VVB_BUTTON_RELEASE, PLEATED_JOG_1, \
    PLEATED_BUTTON_PUSH_HOLD, PLEATED_BUTTON_RELEASE
from server.nordic import Nd

connect_text = Row(Text(25, Tr.PRESS_HOLD_BLIND_BUTTON.add_number(1)),
                   Text(25, Tr.KEEP_PRESSING_AND_OKAY.add_number(2)),
                   Text(25, Tr.WATCH_THE_BLIND_JOG.add_number(3)),
                   Text(25, Tr.RELEASE_THE_BLIND_BUTTON.add_number(4)))


def get_connect(jog_image, button_push_hold_image, button_release_image):
    return Step(Tr.CONNECT,
                [connect_text,
                 Row(Image(25, button_push_hold_image),
                     PvKeypadAlt(
                         25,
                         okay=Commands(
                             nordic_commands=NordicCommands(Nd.NETWORKADD,
                                                            DelayedCommand(
                                                                Nd.GROUP_ADD,
                                                                1)),
                             confirm_command=Confirm(jog_image,
                                                     Tr.DID_THE_MOTOR_JOG)
                         )
                     ),
                     Image(25, jog_image),
                     Image(25, button_release_image))
                 ]
                )


connect_rb = get_connect(
    RB_JOG_1, RB_BUTTON_PUSH_HOLD, RB_BUTTON_RELEASE)

connect_twist = get_connect(
    TWIST_JOG_1, TWIST_BUTTON_PUSH_HOLD, TWIST_BUTTON_RELEASE)

connect_m25s_vb = get_connect(
    VB_JOG_1, VB_BUTTON_PUSH_HOLD, VB_BUTTON_RELEASE)

connect_m25s_duette = get_connect(
    DUETTE_JOG_1, DUETTE_BUTTON_PUSH_HOLD, DUETTE_BUTTON_RELEASE)

connect_m25s_pleated = get_connect(
    PLEATED_JOG_1, PLEATED_BUTTON_PUSH_HOLD, PLEATED_BUTTON_RELEASE)

connect_m25s_vvb = get_connect(
    VVB_JOG_1, VVB_BUTTON_PUSH_HOLD, VVB_BUTTON_RELEASE)
