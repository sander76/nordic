from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands

import static.app.instructions.translations as tr

connect = Step(tr._connect,
                   [Row(Text(25, tr._press_hold_blind_button.add_number(1)),
                        Text(25, tr._keep_pressing_and_okay.add_number(2)),
                        Text(25, tr._release_the_blind_button.add_number(3)),
                        Text(25, tr._watch_the_blind_jog.add_number(4))),
                    Row(Image(25, "/app/images/m25t_motor_button_push_top_limit_rollo.png"),
                        PvKeypad(25, ['okay'], 'okay', Commands('networkadd', DelayedCommand('group1add', 1))),
                        Image(25, "/app/images/m25t_motor_button_release_top_limit_rollo.png"),
                        Image(25, "/app/images/m25t_motor_jog1x.png"))
                    ],
                   Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))