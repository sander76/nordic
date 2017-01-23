import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands
connect_text = Row(Text(25, tr._press_hold_blind_button.add_number(1)),
                        Text(25, tr._keep_pressing_and_okay.add_number(2)),
                        Text(25, tr._release_the_blind_button.add_number(3)),
                        Text(25, tr._watch_the_blind_jog.add_number(4)))

keypad = PvKeypad(25, ['okay'], 'okay', Commands('networkadd', DelayedCommand('group1add', 1)))

connect_rb = Step(tr._connect,
                   [connect_text,
                    Row(Image(25, "/app/images/m25t_motor_button_push_top_limit_rollo.png"),
                        keypad,
                        Image(25, "/app/images/m25t_motor_button_release_top_limit_rollo.png"),
                        Image(25, "/app/images/m25t_motor_jog1x.png"))
                    ],
                   Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog)
               ,id="start")

connect_vb = Step(tr._connect,
                  [connect_text,
                   Row(Image(25, "/app/images/m25s_vb_motor_button_push.png"),
                       keypad,
                       Image(25, "/app/images/m25s_vb_motor_button_release.png"),
                       Image(25, "/app/images/m25s_vb_motor_jog1x.png"))
                   ],
                  Confirm("/app/images/m25s_vb_motor_jog1x.png", tr._did_the_motor_jog)
                  , id="start")


connect_m25s_duette = Step(tr._connect,
                   [connect_text,
                    Row(Image(25, "/app/images/m25t_motor_button_push_top_limit_rollo.png"),
                        keypad,
                        Image(25, "/app/images/m25t_motor_button_release_top_limit_rollo.png"),
                        Image(25, "/app/images/m25t_motor_jog1x.png"))
                    ],
                   Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog)
               ,id="start")