import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands

textrow = Row(Text(30, tr._press_okay_button.add_number(1)),
              Text(30, tr._watch_the_blind_jog_two_times.add_number(2)))

keypad = PvKeypad(30, ['okay'], 'okay', Commands('reset', DelayedCommand('roller', 4)))

initialise_rb = Step(tr._initialise,
                         [textrow,
                          Row(keypad,
                              Image(30, "/app/images/m25t_motor_jog2x.png"))
                          ],
                         Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

initialise_twist = Step(tr._initialise,
                        [textrow,
                         Row(keypad,
                             Image(30, "/app/images/m25t_motor_jog2x.png"))
                         ],
                        Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

initialise_vb = Step(tr._initialise,
                     [Row(Text(30, tr._press_okay_button.add_number(1)),
                             Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
                         Row(PvKeypad(30, ['okay'], 'okay', Commands('reset', DelayedCommand('m25s_venetian_16mm', 4))),
                             Image(30, "/app/images/m25s_vb_motor_jog2x.png"))
                         ],
                     Confirm('/app/images/m25s_vb_motor_jog2x.png', tr._did_the_motor_jog_two_times))

initialise_duette = Step(tr._initialise,
                     [Row(Text(30, tr._press_okay_button.add_number(1)),
                             Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
                         Row(PvKeypad(30, ['okay'], 'okay', Commands('reset', DelayedCommand('m25s_duette_free', 4))),
                             Image(30, "/app/images/m25s_vb_motor_jog2x.png"))
                         ],
                     Confirm('/app/images/m25s_vb_motor_jog2x.png', tr._did_the_motor_jog_two_times))