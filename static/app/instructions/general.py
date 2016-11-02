from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands, Spacer, NavigationCommand

import static.app.instructions.translations as tr


enter_program_mode = Step(tr._enterprogrammode,
                              [Row(Text(30, tr._press_okay_button.add_number(1)),
                                   Text(30, tr._watch_the_blind_jog.add_number(2))),
                               Row(PvKeypad(30, ['okay'], 'okay', Commands('startprogram')),
                                   Image(30, "/app/images/m25t_motor_jog1x.png"))
                               ], Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))