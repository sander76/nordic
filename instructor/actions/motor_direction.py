# import instructor.translations as tr
from instructor.actions.initialise import PRODUCT_SET_DELAY
from instructor.translations import Translations as tr
from instructor.components import Row, Text, Step, Image, \
    Confirm, Spacer, DelayedCommand, NordicCommands, NavigationCommand, \
    PvKeypadAlt, Commands
from instructor.constants import RB_JOG_1, DUETTE_JOG_1, RB_JOG_2, VB_JOG_1, \
    VVB_JOG_1, PLEATED_JOG_1, VVB_JOG_2, VVB_LEFT_STACK, VVB_SPLIT_STACK, \
    VVB_RIGHT_STACK, DUETTE_CLOSE
from server.nordic import Nd


def get_direction(
        jog_image,
        title=tr.TITLE_BACKROLLER_LEFT,
        orientation_question=tr.IS_LEFT_BACKROLLER,
        confirm_orientation_command=NordicCommands(Nd.ORIENT_BACKROLLER_LEFT),
        cancel_no=NavigationCommand(1),
        confirm_yes=NavigationCommand(4),
        orientation_image: str = None,
        nav_id=None):
    if orientation_image is not None:
        orientation_image = Image(30, orientation_image)
    else:
        orientation_image = Spacer(30)
    return Step(
        title,
        [
            Row(Text(30, orientation_question),
                Text(30, tr.YES),
                Text(30, tr.NO)
                ),
            Row(
                orientation_image,
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        nordic_commands=confirm_orientation_command,
                        confirm_command=Confirm(
                            jog_image,
                            tr.DID_THE_MOTOR_JOG,
                            yes=confirm_yes)
                    )),
                PvKeypadAlt(
                    30,
                    cancel=Commands(
                        navigation_command=cancel_no))

            )
        ],
        nav_id=nav_id
    )


left_backroller = get_direction(RB_JOG_1)

right_backroller = get_direction(
    RB_JOG_1,
    tr.TITLE_BACKROLLER_RIGHT,
    tr.IS_RIGHT_BACKROLLER,
    NordicCommands(Nd.ORIENT_BACKROLLER_RIGHT),
    confirm_yes=NavigationCommand(3)
)

left_frontroller = get_direction(
    RB_JOG_1,
    title=tr.TITLE_FRONTROLLER_LEFT,
    orientation_question=tr.IS_LEFT_FRONTROLLER,
    confirm_orientation_command=NordicCommands(
        Nd.ORIENT_BACKROLLER_RIGHT),
    confirm_yes=NavigationCommand(2)
)

right_frontroller = get_direction(
    RB_JOG_1,
    title=tr.TITLE_FRONTROLLER_RIGHT,
    orientation_question=tr.IS_RIGHT_FRONTROLLER,
    confirm_orientation_command=NordicCommands(
        Nd.ORIENT_BACKROLLER_LEFT),
    cancel_no=NavigationCommand(-3),
    confirm_yes=NavigationCommand(1)
)

right_mount_duette = get_direction(
    DUETTE_JOG_1,
    title=tr.IS_RIGHT_MOUNT,
    orientation_question=tr.IS_RIGHT_MOUNT,
    confirm_orientation_command=NordicCommands(
        Nd.ORIENT_M25S_DUETTE_RIGHT),
    confirm_yes=NavigationCommand(2)
)

right_mount_pleated = get_direction(
    PLEATED_JOG_1, tr.IS_RIGHT_MOUNT, tr.IS_RIGHT_MOUNT,
    NordicCommands(Nd.ORIENT_M25S_DUETTE_RIGHT),
    confirm_yes=NavigationCommand(2))

left_mount_pleated = get_direction(
    PLEATED_JOG_1,
    title=tr.IS_LEFT_MOUNT,
    orientation_question=tr.IS_LEFT_MOUNT,
    confirm_orientation_command=NordicCommands(Nd.ORIENT_M25S_DUETTE_LEFT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=NavigationCommand(1))

left_mount_duette = get_direction(
    DUETTE_JOG_1,
    title=tr.IS_LEFT_MOUNT,
    orientation_question=tr.IS_LEFT_MOUNT,
    confirm_orientation_command=NordicCommands(Nd.ORIENT_M25S_DUETTE_LEFT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=NavigationCommand(1)

)

right_mount_vb = get_direction(
    VB_JOG_1,
    title=tr.IS_RIGHT_MOUNT,
    orientation_question=tr.IS_RIGHT_MOUNT,
    confirm_orientation_command=NordicCommands(
        Nd.ORIENT_BACKROLLER_LEFT),
    confirm_yes=NavigationCommand(2)

)

left_mount_vb = get_direction(
    VB_JOG_1,
    title=tr.IS_LEFT_MOUNT,
    orientation_question=tr.IS_LEFT_MOUNT,
    confirm_orientation_command=NordicCommands(
        Nd.ORIENT_BACKROLLER_RIGHT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=NavigationCommand(1)


)

vvb_left_stack = get_direction(
    VVB_JOG_2,
    title=tr.IS_VVB_LEFT_STACK,
    orientation_question=tr.IS_VVB_LEFT_STACK,
    confirm_orientation_command=NordicCommands(
        Nd.RESET,
        DelayedCommand(Nd.M25S_VVB_LEFT_STACK,
                       PRODUCT_SET_DELAY)),
    cancel_no=NavigationCommand(1),
    confirm_yes=NavigationCommand("vvb_start_program"),
    orientation_image=VVB_LEFT_STACK,
    nav_id="vvb_left_stack"
)
vvb_right_stack = get_direction(
    VVB_JOG_2,
    title=tr.IS_VVB_RIGHT_STACK,
    orientation_question=tr.IS_VVB_RIGHT_STACK,
    confirm_orientation_command=NordicCommands(
        Nd.RESET,
        DelayedCommand(Nd.M25S_VVB_RIGHT_STACK,
                       PRODUCT_SET_DELAY)),
    cancel_no=NavigationCommand(1),
    confirm_yes=NavigationCommand("vvb_start_program"),
    orientation_image=VVB_RIGHT_STACK
)

vvb_split_stack = get_direction(
    VVB_JOG_2,
    title=tr.IS_VVB_SPLIT_STACK,
    orientation_question=tr.IS_VVB_SPLIT_STACK,
    confirm_orientation_command=NordicCommands(
        Nd.RESET,
        DelayedCommand(Nd.M25S_VVB_CENTER_STACK,
                       PRODUCT_SET_DELAY)),
    cancel_no=NavigationCommand("vvb_left_stack"),
    confirm_yes=NavigationCommand("vvb_start_program"),
    orientation_image=VVB_SPLIT_STACK
)

vvb_back_left = get_direction(
    VVB_JOG_1,
    title=tr.TITLE_ORIENT_VVB_BACK,
    orientation_question=tr.ORIENT_VVB_BACK,
    confirm_orientation_command=NordicCommands(Nd.ORIENT_VVB_LEFT),
    confirm_yes=NavigationCommand(2))

vvb_above_left = get_direction(
    VVB_JOG_1, tr.TITLE_ORIENT_VVB_UPRIGHT,
    tr.ORIENT_VVB_UPRIGHT, NordicCommands(Nd.ORIENT_VVB_UPRIGHT_LEFT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=NavigationCommand(1))

vvb_back_right = get_direction(
    VVB_JOG_1,
    tr.TITLE_ORIENT_VVB_BACK,
    tr.ORIENT_VVB_BACK, NordicCommands(Nd.ORIENT_VVB_RIGHT),
    confirm_yes=NavigationCommand(2))

vvb_above_right = get_direction(
    VVB_JOG_1, tr.TITLE_ORIENT_VVB_UPRIGHT,
    tr.ORIENT_VVB_UPRIGHT, NordicCommands(Nd.ORIENT_VVB_UPRIGHT_RIGHT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=NavigationCommand(1))

tensioned_duette_direction = Step(
    tr.BLIND_DIRECTION,
    [
        Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
            Text(30,
                 tr.MOTOR_SHOULD_MOVE_DOWN.add_number(2))),
        Row(PvKeypadAlt(
            30,
            okay=Commands(
                nordic_commands=NordicCommands(
                    Nd.close,
                    DelayedCommand(Nd.stop, 3),
                    DelayedCommand(Nd.stop, 0.4),
                    DelayedCommand(Nd.stop, 0.4)),
                confirm_command=Confirm(
                    DUETTE_CLOSE,
                    tr.DID_BLIND_CLOSE,
                    yes=NavigationCommand(2),
                    no=NavigationCommand(1))))
            ,
            Image(30,
                  DUETTE_CLOSE))
    ]
)

tensioned_duette_switch_direction = Step(
    tr.SWITCH_DIRECTION,
    [
        Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
            Text(30,
                 tr.WATCH_THE_BLIND_JOG.add_number(
                     2))),
        Row(PvKeypadAlt(
            30,
            okay=Commands(
                nordic_commands=NordicCommands(
                    Nd.ORIENT_M25S_DUETTE_LEFT),
                confirm_command=Confirm(
                    DUETTE_JOG_1,
                    tr.DID_THE_MOTOR_JOG)
            )),
            Image(30, DUETTE_JOG_1))
    ]
)

blind_direction = Step(
    tr.BLIND_DIRECTION,
    [
        Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
            Text(30,
                 tr.MOTOR_SHOULD_MOVE_DOWN.add_number(2))),
        Row(
            PvKeypadAlt(
                30,
                okay=Commands(
                    nordic_commands=NordicCommands(
                        Nd.close, DelayedCommand(Nd.stop, 3),
                        DelayedCommand(Nd.stop, 0.4),
                        DelayedCommand(Nd.stop, 0.4)),
                    confirm_command=Confirm(
                        "/app/images/m25t_motor_top_limit_move_down_rollo.png",
                        tr.DID_MOTOR_MOVE_DOWN,
                        yes=NavigationCommand(2),
                        no=NavigationCommand(1))),
                cancel=Commands(
                    navigation_command=NavigationCommand(1))
            ),
            Image(
                30,
                "/app/images/m25t_motor_top_limit_move_down_rollo.png"))
    ]
)

switch_direction = Step(
    tr.SWITCH_DIRECTION,
    [
        Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
            Text(30,
                 tr.WATCH_THE_BLIND_JOG_TWO_TIMES.add_number(
                     2))),
        Row(PvKeypadAlt(
            30,
            okay=Commands(
                nordic_commands=NordicCommands(
                    Nd.STARTPROGRAM, DelayedCommand(Nd.REVERSE, 2)),
                confirm_command=Confirm(
                    RB_JOG_2, tr.DID_THE_MOTOR_JOG_TWO_TIMES)
            )),
            Image(30, RB_JOG_2))
    ]
)
