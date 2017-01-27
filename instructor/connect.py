import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands
from instructor.constants import TWIST_JOG_1, TWIST_BUTTON_PUSH_HOLD, \
    TWIST_BUTTON_RELEASE, RB_JOG_1, RB_BUTTON_PUSH_HOLD, RB_BUTTON_RELEASE, \
    ID_START, VB_JOG_1, VB_BUTTON_PUSH_HOLD, VB_BUTTON_RELEASE, DUETTE_JOG_1, \
    DUETTE_BUTTON_PUSH_HOLD, DUETTE_BUTTON_RELEASE
from server.nordic import NETWORKADD, GROUP_ADD

connect_text = Row(Text(25, tr.PRESS_HOLD_BLIND_BUTTON.add_number(1)),
                   Text(25, tr.KEEP_PRESSING_AND_OKAY.add_number(2)),
                   Text(25, tr.RELEASE_THE_BLIND_BUTTON.add_number(3)),
                   Text(25, tr.WATCH_THE_BLIND_JOG.add_number(4)))

keypad = PvKeypad(25, ['okay'], 'okay',
                  Commands(NETWORKADD, DelayedCommand(GROUP_ADD, 1)))


def get_connect(jog_image, button_push_hold_image, button_release_image):
    return Step(tr.CONNECT,
                [connect_text,
                 Row(Image(25, button_push_hold_image),
                     keypad,
                     Image(25, button_release_image),
                     Image(25, jog_image))
                 ],
                Confirm(jog_image, tr.DID_THE_MOTOR_JOG)
                , nav_id=ID_START)


connect_rb = get_connect(RB_JOG_1, RB_BUTTON_PUSH_HOLD, RB_BUTTON_RELEASE)

# connect_rb = Step(tr._connect,
#                    [connect_text,
#                     Row(Image(25, "/app/images/m25t_motor_button_push_top_limit_rollo.png"),
#                         keypad,
#                         Image(25, "/app/images/m25t_motor_button_release_top_limit_rollo.png"),
#                         Image(25, "/app/images/m25t_motor_jog1x.png"))
#                     ],
#                    Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog)
#                ,id="start")

connect_twist = get_connect(TWIST_JOG_1,
                            TWIST_BUTTON_PUSH_HOLD,
                            TWIST_BUTTON_RELEASE)

connect_m25s_vb = get_connect(VB_JOG_1,
                              VB_BUTTON_PUSH_HOLD,
                              VB_BUTTON_RELEASE)

# connect_vb = Step(tr._connect,
#                   [connect_text,
#                    Row(Image(25, "/app/images/m25s_vb_motor_button_push.png"),
#                        keypad,
#                        Image(25,
#                              "/app/images/m25s_vb_motor_button_release.png"),
#                        Image(25, "/app/images/m25s_vb_motor_jog1x.png"))
#                    ],
#                   Confirm("/app/images/m25s_vb_motor_jog1x.png",
#                           tr._did_the_motor_jog)
#                   , id="start")

connect_m25s_duette = get_connect(DUETTE_JOG_1,
                                  DUETTE_BUTTON_PUSH_HOLD,
                                  DUETTE_BUTTON_RELEASE)

# connect_m25s_duette = Step(tr._connect,
#                            [connect_text,
#                             Row(Image(25,
#                                       "/app/images/m25t_motor_button_push_top_limit_rollo.png"),
#                                 keypad,
#                                 Image(25,
#                                       "/app/images/m25t_motor_button_release_top_limit_rollo.png"),
#                                 Image(25, "/app/images/m25t_motor_jog1x.png"))
#                             ],
#                            Confirm("/app/images/m25t_motor_jog1x.png",
#                                    tr._did_the_motor_jog)
#                            , id="start")

connect_m25s_duette_tensioned = Step(tr.CONNECT,
                                     [connect_text,
                                      ])
