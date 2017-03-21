import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, \
    Confirm, Spacer, DelayedCommand, Commands
from instructor.constants import RB_JOG_1, DUETTE_JOG_1, RB_JOG_2, VB_JOG_1, \
    VVB_JOG_1, PLEATED_JOG_1
from server.nordic import Nd


def get_direction(
        jog_image,
        title=tr.BACKROLLER_LEFT_TITLE,
        orientation_question=tr.IS_LEFT_BACKROLLER,
        confirm_orientation_command=Nd.ORIENT_BACKROLLER_LEFT,
        cancel_no=1,
        confirm_yes=4
):
    return Step(title,
                [
                    Row(Text(30, orientation_question),
                        Text(30, tr.YES),
                        Text(30, tr.NO)
                        ),
                    Row(
                        Spacer(30),
                        PvKeypad(30,
                                 [PvKeypad.okay],
                                 confirm=PvKeypad.okay,
                                 okay=Commands(confirm_orientation_command)),
                        PvKeypad(30,
                                 [PvKeypad.cancel],
                                 cancel=cancel_no),

                    )
                ],
                Confirm(jog_image,
                        tr.DID_THE_MOTOR_JOG, yes=confirm_yes)
                )


left_backroller = get_direction(RB_JOG_1)

right_backroller = get_direction(
    RB_JOG_1,
    tr.BACKROLLER_RIGHT_TITLE,
    tr.IS_RIGHT_BACKROLLER,
    Nd.ORIENT_BACKROLLER_RIGHT
)
right_backroller.confirm.yes = 3

left_frontroller = get_direction(RB_JOG_1)
left_frontroller.title = tr.FRONTROLLER_LEFT_TITLE
left_frontroller.instructions[0].col1.content = tr.IS_LEFT_FRONTROLLER
left_frontroller.instructions[1].col2.okay = Commands(
    Nd.ORIENT_BACKROLLER_RIGHT)
left_frontroller.confirm.yes = 2

right_frontroller = get_direction(RB_JOG_1)
right_frontroller.title = tr.FRONTROLLER_RIGHT_TITLE
right_frontroller.instructions[0].col1.content = tr.IS_RIGHT_FRONTROLLER
right_frontroller.instructions[1].col2.okay = Commands(
    Nd.ORIENT_BACKROLLER_LEFT)
right_frontroller.instructions[1].col3.cancel = -3
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
    Nd.ORIENT_M25S_DUETTE_RIGHT, confirm_yes=2)

left_mount_pleated = get_direction(
    PLEATED_JOG_1, tr.IS_LEFT_MOUNT, tr.IS_LEFT_MOUNT,
    Nd.ORIENT_M25S_DUETTE_LEFT, cancel_no=-1, confirm_yes=1)

left_mount_duette = get_direction(DUETTE_JOG_1)
left_mount_duette.title = tr.IS_LEFT_MOUNT
left_mount_duette.instructions[0].col1.content = tr.IS_LEFT_MOUNT
left_mount_duette.instructions[1].col2.okay = Commands(
    Nd.ORIENT_M25S_DUETTE_LEFT)
left_mount_duette.instructions[1].col3.cancel = -1
left_mount_duette.confirm = Confirm(DUETTE_JOG_1,
                                    tr.DID_THE_MOTOR_JOG, yes=1)

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
left_mount_vb.instructions[1].col3.cancel = -1
left_mount_vb.confirm = Confirm(VB_JOG_1,
                                tr.DID_THE_MOTOR_JOG, yes=1)

vvb_back_left = get_direction(VVB_JOG_1, )

blind_direction = Step(
    tr.BLIND_DIRECTION,
    [
        Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
            Text(30,
                 tr.MOTOR_SHOULD_MOVE_DOWN.add_number(2))),
        Row(PvKeypad(30, ['okay'], 'okay',
                     Commands(Nd.TILT_CLOSE,
                              DelayedCommand(Nd.STOP, 3),
                              DelayedCommand(Nd.STOP, 0.4),
                              DelayedCommand(Nd.STOP, 0.4)),
                     cancel=1),
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
