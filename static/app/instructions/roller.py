from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands

import static.app.instructions.translations as tr


initialise_roller = Step(tr._initialise,
                         [Row(Text(30, tr._press_okay_button.add_number(1)),
                              Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
                          Row(PvKeypad(30, ['okay'], 'okay', Commands('reset', DelayedCommand('roller', 4))),
                              Image(30, "/app/images/m25t_motor_jog2x.png"))
                          ],
                         Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))
