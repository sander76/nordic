# import instructor.translations as tr
from instructor.actions.initialise import PRODUCT_SET_DELAY
from instructor.translations import Translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, \
    Confirm, Spacer, DelayedCommand, Commands, NavigationCommand
from instructor.constants import RB_JOG_1, DUETTE_JOG_1, RB_JOG_2, VB_JOG_1, \
    VVB_JOG_1, PLEATED_JOG_1, VVB_JOG_2, VVB_LEFT_STACK, VVB_CENTER_STACK
from server.nordic import Nd


def get_direction(
        jog_image,
        title=tr.TITLE_BACKROLLER_LEFT,
        orientation_question=tr.IS_LEFT_BACKROLLER,
        confirm_orientation_command=Commands(Nd.ORIENT_BACKROLLER_LEFT),
        cancel_no=NavigationCommand(1),
        confirm_yes=NavigationCommand(4),
        orientation_image : str=None,
        nav_id=None):
    if orientation_image is not None:
        orientation_image = Image(30,orientation_image)
    else:
        orientation_image = Spacer(30)
    return Step(title,
                [
                    Row(Text(30, orientation_question),
                        Text(30, tr.YES),
                        Text(30, tr.NO)
                        ),
                    Row(
                        orientation_image,
                        PvKeypad(30,
                                 [PvKeypad.okay],
                                 confirm=PvKeypad.okay,
                                 okay=confirm_orientation_command),
                        PvKeypad(30,
                                 [PvKeypad.cancel],
                                 cancel=cancel_no),

                    )
                ],
                Confirm(jog_image,
                        tr.DID_THE_MOTOR_JOG, yes=confirm_yes),
                nav_id
                )


left_backroller = get_direction(RB_JOG_1)

right_backroller = get_direction(
    RB_JOG_1,
    tr.TITLE_BACKROLLER_RIGHT,
    tr.IS_RIGHT_BACKROLLER,
    Commands(Nd.ORIENT_BACKROLLER_RIGHT),
    confirm_yes=NavigationCommand(3)
)

left_frontroller = get_direction(RB_JOG_1)
left_frontroller.title = tr.TITLE_FRONTROLLER_LEFT
left_frontroller.instructions[0].col1.content = tr.IS_LEFT_FRONTROLLER
left_frontroller.instructions[1].col2.okay = Commands(
    Nd.ORIENT_BACKROLLER_RIGHT)
left_frontroller.confirm.yes = 2

right_frontroller = get_direction(RB_JOG_1)
right_frontroller.title = tr.TITLE_FRONTROLLER_RIGHT
right_frontroller.instructions[0].col1.content = tr.IS_RIGHT_FRONTROLLER
right_frontroller.instructions[1].col2.okay = Commands(
    Nd.ORIENT_BACKROLLER_LEFT)
right_frontroller.instructions[1].col3.cancel = NavigationCommand(-3)
right_frontroller.confirm.yes = 1

right_mount_duette = get_direction(DUETTE_JOG_1)
right_mount_duette.title = tr.IS_RIGHT_MOUNT
right_mount_duette.instructions[0].col1.content = tr.IS_RIGHT_MOUNT
right_mount_duette.instructions[1].col2.okay = Commands(
    Nd.ORIENT_M25S_DUETTE_RIGHT)
right_mount_duette.confirm = Confirm(DUETTE_JOG_1, tr.DID_THE_MOTOR_JOG,
                                     yes=2)

right_mount_pleated = get_direction(
    PLEATED_JOG_1, tr.IS_RIGHT_MOUNT, tr.IS_RIGHT_MOUNT,
    Commands(Nd.ORIENT_M25S_DUETTE_RIGHT),
    confirm_yes=NavigationCommand(2))

left_mount_pleated = get_direction(
    PLEATED_JOG_1,
    title=tr.IS_LEFT_MOUNT,
    orientation_question=tr.IS_LEFT_MOUNT,
    confirm_orientation_command=Commands(Nd.ORIENT_M25S_DUETTE_LEFT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=NavigationCommand(1))

left_mount_duette = get_direction(
    DUETTE_JOG_1,
    title=tr.IS_LEFT_MOUNT,
    orientation_question=tr.IS_LEFT_MOUNT,
    confirm_orientation_command=Commands(Nd.ORIENT_M25S_DUETTE_LEFT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=NavigationCommand(1)

)

left_mount_duette.confirm = Confirm(DUETTE_JOG_1,
                                    tr.DID_THE_MOTOR_JOG,
                                    yes=NavigationCommand(1))

right_mount_vb = get_direction(VB_JOG_1)
right_mount_vb.title = tr.IS_RIGHT_MOUNT
right_mount_vb.instructions[0].col1.content = tr.IS_RIGHT_MOUNT
right_mount_vb.instructions[1].col2.okay = Commands(Nd.ORIENT_BACKROLLER_LEFT)
right_mount_vb.confirm = Confirm(VB_JOG_1, tr.DID_THE_MOTOR_JOG,
                                 yes=2)

left_mount_vb = get_direction(VB_JOG_1)
left_mount_vb.title = tr.IS_LEFT_MOUNT
left_mount_vb.instructions[0].col1.content = tr.IS_LEFT_MOUNT
# BACKROLLER RIGHT seems to be wrong, but it is actually correct.
left_mount_vb.instructions[1].col2.okay = Commands(Nd.ORIENT_BACKROLLER_RIGHT)
left_mount_vb.instructions[1].col3.cancel = NavigationCommand(-1)
left_mount_vb.confirm = Confirm(VB_JOG_1,
                                tr.DID_THE_MOTOR_JOG, yes=1)

vvb_left_stack = get_direction(
    VVB_JOG_2,
    title=tr.IS_VVB_LEFT_STACK,
    orientation_question=tr.IS_VVB_LEFT_STACK,
    confirm_orientation_command=Commands(
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
    confirm_orientation_command=Commands(
        Nd.RESET,
        DelayedCommand(Nd.M25S_VVB_RIGHT_STACK,
                       PRODUCT_SET_DELAY)),
    cancel_no=NavigationCommand(1),
    confirm_yes=NavigationCommand("vvb_start_program"),
    orientation_image=VVB_LEFT_STACK
)

vvb_center_stack = get_direction(
    VVB_JOG_2,
    title=tr.IS_VVB_CENTER_STACK,
    orientation_question=tr.IS_VVB_CENTER_STACK,
    confirm_orientation_command=Commands(
        Nd.RESET,
        DelayedCommand(Nd.M25S_VVB_CENTER_STACK,
                       PRODUCT_SET_DELAY)),
    cancel_no=NavigationCommand("vvb_left_stack"),
    confirm_yes=NavigationCommand("vvb_start_program"),
    orientation_image=VVB_CENTER_STACK
)

vvb_back_left = get_direction(
    VVB_JOG_1, tr.TITLE_ORIENT_VVB_BACK,
    tr.ORIENT_VVB_BACK, Commands(Nd.ORIENT_VVB_LEFT), confirm_yes=2)

vvb_above_left = get_direction(
    VVB_JOG_1, tr.TITLE_ORIENT_VVB_UPRIGHT,
    tr.ORIENT_VVB_UPRIGHT, Commands(Nd.ORIENT_VVB_UPRIGHT_LEFT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=1)

vvb_back_right = get_direction(
    VVB_JOG_1, tr.TITLE_ORIENT_VVB_BACK,
    tr.ORIENT_VVB_BACK, Commands(Nd.ORIENT_VVB_RIGHT), confirm_yes=2)

vvb_above_right = get_direction(
    VVB_JOG_1, tr.TITLE_ORIENT_VVB_UPRIGHT,
    tr.ORIENT_VVB_UPRIGHT, Commands(Nd.ORIENT_VVB_UPRIGHT_RIGHT),
    cancel_no=NavigationCommand(-1),
    confirm_yes=1)

tensioned_duette_direction = Step(
tr.BLIND_DIRECTION,
[
    Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
        Text(30,
             tr.MOTOR_SHOULD_MOVE_DOWN.add_number(2))),
    Row(PvKeypad(30, ['okay', 'stop'], 'okay',
                 Commands(Nd.close,
                          DelayedCommand(Nd.stop, 3),
                          DelayedCommand(Nd.stop, 0.4),
                          DelayedCommand(Nd.stop, 0.4)),
                 cancel=NavigationCommand(1)),
        Image(30,
              "/app/images/m25t_motor_top_limit_move_down_rollo.png"))
],
Confirm(
    "/app/images/m25t_motor_top_limit_move_down_rollo.png",
    tr.DID_BLIND_CLOSE,
    yes=2,
    no=1))

tensioned_duette_switch_direction = Step(
tr.SWITCH_DIRECTION,
[
    Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
        Text(30,
             tr.WATCH_THE_BLIND_JOG.add_number(
                 2))),
    Row(PvKeypad(30, ['okay'], 'okay',
                 Commands(Nd.ORIENT_M25S_DUETTE_LEFT)),
        Image(30, DUETTE_JOG_1))
],
Confirm(DUETTE_JOG_1,
        tr.DID_THE_MOTOR_JOG))

blind_direction = Step(
tr.BLIND_DIRECTION,
[
    Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
        Text(30,
             tr.MOTOR_SHOULD_MOVE_DOWN.add_number(2))),
    Row(PvKeypad(30, ['okay'], 'okay',
                 Commands(Nd.close,
                          DelayedCommand(Nd.stop, 3),
                          DelayedCommand(Nd.stop, 0.4),
                          DelayedCommand(Nd.stop, 0.4)),
                 cancel=NavigationCommand(1)),
        Image(30,
              "/app/images/m25t_motor_top_limit_move_down_rollo.png"))
],
Confirm(
    "/app/images/m25t_motor_top_limit_move_down_rollo.png",
    tr.DID_MOTOR_MOVE_DOWN,
    yes=2,
    no=1))

switch_direction = Step(
tr.SWITCH_DIRECTION,
[
    Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
        Text(30,
             tr.WATCH_THE_BLIND_JOG_TWO_TIMES.add_number(
                 2))),
    Row(PvKeypad(30, ['okay'], 'okay',
                 Commands(Nd.STARTPROGRAM,
                          DelayedCommand(Nd.REVERSE,
                                         2))),
        Image(30, RB_JOG_2))
],
Confirm(RB_JOG_2,
        tr.DID_THE_MOTOR_JOG_TWO_TIMES))
