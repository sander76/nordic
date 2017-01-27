import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, \
    Confirm, Spacer, DelayedCommand, Commands
from instructor.constants import RB_JOG_1, DUETTE_JOG_1, RB_JOG_2, VB_JOG_1
from server.nordic import BACKROLLER_RIGHT, BACKROLLER_LEFT, STARTPROGRAM, STOP, \
    TILT_CLOSE, REVERSE


def get_direction(jog_image):
    return Step(tr.BACKROLLER_LEFT_TITLE,
                [
                    Row(Text(30, tr.IS_LEFT_BACKROLLER),
                        Text(30, tr.YES),
                        Text(30, tr.NO)
                        ),
                    Row(
                        Spacer(30),
                        PvKeypad(30,
                                 [PvKeypad.okay],
                                 confirm=PvKeypad.okay,
                                 okay=Commands(BACKROLLER_LEFT)),
                        PvKeypad(30,
                                 [PvKeypad.cancel],
                                 cancel=1),

                    )
                ],
                Confirm(jog_image,
                        tr.DID_THE_MOTOR_JOG, yes=4)
                )


# left_backroller = Step(tr._backroller_left_title,
#                        [
#                            Row(Text(30, tr._is_left_backroller),
#                                Text(30, tr._yes),
#                                Text(30, tr._no)
#                                ),
#                            Row(
#                                Spacer(30),
#                                PvKeypad(30,
#                                         [PvKeypad.okay],
#                                         confirm=PvKeypad.okay,
#                                         okay=Commands(BACKROLLER_LEFT)),
#                                PvKeypad(30,
#                                         [PvKeypad.cancel],
#                                         cancel=1),
#
#                            )
#                        ],
#                        Confirm("/app/images/m25t_motor_jog1x.png",
#                                tr._did_the_motor_jog, yes=4)
#                       )

left_backroller = get_direction(RB_JOG_1)

right_backroller = get_direction(RB_JOG_1)
right_backroller.title = tr.BACKROLLER_RIGHT_TITLE
right_backroller.instructions[0].col1.content = tr.IS_RIGHT_BACKROLLER
right_backroller.instructions[1].col2.okay = Commands(BACKROLLER_RIGHT)
right_backroller.confirm.yes = 3

# right_backroller = Step(tr._backroller_right_title,
#                         [
#                             Row(Text(30, tr._is_right_backroller),
#                                 Text(30, tr._yes),
#                                 Text(30, tr._no)
#                                 ),
#                             Row(
#                                 Spacer(30),
#                                 PvKeypad(30,
#                                          [PvKeypad.okay],
#                                          confirm=PvKeypad.okay,
#                                          okay=Commands(BACKROLLER_RIGHT)),
#                                 PvKeypad(30,
#                                          [PvKeypad.cancel],
#                                          cancel=1),
#                             )
#                         ],
#                         Confirm("/app/images/m25t_motor_jog1x.png",
#                                 tr._did_the_motor_jog,
#                                 yes=3)
#                         )

left_frontroller = get_direction(RB_JOG_1)
left_frontroller.title = tr.FRONTROLLER_LEFT_TITLE
left_frontroller.instructions[0].col1.content = tr.IS_LEFT_FRONTROLLER
left_frontroller.instructions[1].col2.okay = Commands(BACKROLLER_RIGHT)
left_frontroller.confirm.yes = 2

# left_frontroller = Step(tr._frontroller_left_title,
#                         [
#                             Row(Text(30, tr._is_left_frontroller),
#                                 Text(30, tr._yes),
#                                 Text(30, tr._no)
#                                 ),
#                             Row(
#                                 Spacer(30),
#                                 PvKeypad(30,
#                                          [PvKeypad.okay],
#                                          confirm=PvKeypad.okay,
#                                          okay=Commands(BACKROLLER_RIGHT),
#                                          ),
#                                 PvKeypad(30,
#                                          [PvKeypad.cancel],
#                                          cancel=1)
#                             )
#                         ], Confirm("/app/images/m25t_motor_jog1x.png",
#                                    tr._did_the_motor_jog,
#                                    yes=2)
#                         )

right_frontroller = get_direction(RB_JOG_1)
right_frontroller.title = tr.FRONTROLLER_RIGHT_TITLE
right_frontroller.instructions[0].col1.content = tr.IS_RIGHT_FRONTROLLER
right_frontroller.instructions[1].col2.okay = Commands(BACKROLLER_LEFT)
right_frontroller.instructions[1].col3.cancel = -3
right_frontroller.confirm.yes = 1

# right_frontroller = Step(tr._frontroller_right_title,
#                          [
#                              Row(Text(30, tr._is_right_frontroller),
#                                  Text(30, tr._yes),
#                                  Text(30, tr._no)
#                                  ),
#                              Row(
#                                  Spacer(30),
#                                  PvKeypad(30,
#                                           [PvKeypad.okay],
#                                           confirm=PvKeypad.okay,
#                                           okay=Commands(BACKROLLER_LEFT)),
#                                  PvKeypad(30,
#                                           [PvKeypad.cancel],
#                                           cancel=-3)
#                              )
#                          ],
#                          Confirm("/app/images/m25t_motor_jog1x.png",
#                                  tr._did_the_motor_jog,
#                                  yes=1)
#                          )

right_mount_duette = get_direction(DUETTE_JOG_1)
right_mount_duette.title = tr.IS_RIGHT_MOUNT
right_mount_duette.instructions[0].col1.content = tr.IS_RIGHT_MOUNT
right_mount_duette.instructions[1].col2.okay = Commands(BACKROLLER_LEFT)
right_mount_duette.confirm = Confirm(DUETTE_JOG_1, tr.DID_THE_MOTOR_JOG,
                                     yes=2)

# right_mount = Step(tr._right_mount,
#                    [
#                        Row(Text(30, tr._is_right_mount),
#                            Text(30, tr._yes),
#                            Text(30, tr._no)),
#                        Row(
#                            Spacer(30),
#                            PvKeypad(30, [PvKeypad.okay],
#                                     confirm=PvKeypad.okay,
#                                     okay=Commands(BACKROLLER_RIGHT)),
#                            PvKeypad(30, [PvKeypad.cancel],
#                                     cancel=1)
#                        )
#                    ],
#                    Confirm("/app/images/m25t_motor_jog1x.png",
#                            tr._did_the_motor_jog, yes=2))

left_mount_duette = get_direction(DUETTE_JOG_1)
left_mount_duette.title = tr.IS_LEFT_MOUNT
left_mount_duette.instructions[0].col1.content = tr.IS_LEFT_MOUNT
# BACKROLLER_RIGHT seems to be wrong, but it is actually correct.
left_mount_duette.instructions[1].col2.okay = Commands(BACKROLLER_RIGHT)
left_mount_duette.instructions[1].col3.cancel = -1
left_mount_duette.confirm = Confirm(DUETTE_JOG_1,
                                    tr.DID_THE_MOTOR_JOG, yes=1)

right_mount_vb = get_direction(VB_JOG_1)
right_mount_vb.title = tr.IS_RIGHT_MOUNT
right_mount_vb.instructions[0].col1.content = tr.IS_RIGHT_MOUNT
right_mount_vb.instructions[1].col2.okay = Commands(BACKROLLER_LEFT)
right_mount_vb.confirm = Confirm(VB_JOG_1, tr.DID_THE_MOTOR_JOG,
                                     yes=2)


left_mount_vb = get_direction(VB_JOG_1)
left_mount_vb.title = tr.IS_LEFT_MOUNT
left_mount_vb.instructions[0].col1.content = tr.IS_LEFT_MOUNT
# BACKROLLEvbT seems to be wrong, but it is actually correct.
left_mount_vb.instructions[1].col2.okay = Commands(BACKROLLER_RIGHT)
left_mount_vb.instructions[1].col3.cancel = -1
left_mount_vb.confirm = Confirm(VB_JOG_1,
                                    tr.DID_THE_MOTOR_JOG, yes=1)

# left_mount = Step(tr._left_mount,
#                   [
#                       Row(Text(30, tr._is_left_mount),
#                           Text(30, tr._yes),
#                           Text(30, tr._no)),
#                       Row(
#                           Spacer(30),
#                           PvKeypad(30, [PvKeypad.okay],
#                                    confirm=PvKeypad.okay,
#                                    okay=Commands(BACKROLLER_LEFT)),
#                           PvKeypad(30, [PvKeypad.cancel],
#                                    cancel=-1)
#                       )
#                   ],
#                   Confirm("/app/images/m25t_motor_jog1x.png",
#                           tr._did_the_motor_jog, yes=1))

blind_direction = Step(
    tr.BLIND_DIRECTION,
    [
        Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
            Text(30,
                 tr.MOTOR_SHOULD_MOVE_DOWN.add_number(2))),
        Row(PvKeypad(30, ['okay'], 'okay',
                     Commands(TILT_CLOSE,
                              DelayedCommand(STOP, 3),
                              DelayedCommand(STOP, 0.4),
                              DelayedCommand(STOP, 0.4)),
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
                     Commands(STARTPROGRAM,
                              DelayedCommand(REVERSE,
                                             2))),
            Image(30, RB_JOG_2))
    ],
    Confirm(RB_JOG_2,
            tr.DID_THE_MOTOR_JOG_TWO_TIMES))
