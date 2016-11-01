from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, Next, \
    Previous, Product, Instruction, ToJson, Spacer, DelayedCommand, Commands, NavigationCommand

from static.app.instructions.helpers import TXT

import static.app.instructions.translations as tr

initialise_vb16 = Step(tr._initialise,
                        [Row(Text(30, tr._press_okay_button.add_number(1)),
                             Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
                         Row(PvKeypad(30, ['okay'], 'okay', Commands('reset', DelayedCommand('m25s_venetian_16mm', 4))),
                             Image(30, "/app/images/m25t_motor_jog2x.png"))
                         ],
                        Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

left_mount = Step(tr._left_mount,
                       [
                           Row(Text(30, tr._is_left_mount),
                               Text(30, tr._yes),
                               Text(30, tr._no)
                               ),
                           Row(
                               Spacer(30),
                               PvKeypad(30,
                                        [PvKeypad.okay],
                                        confirm=PvKeypad.okay,
                                        okay=Commands('backroller_left')),
                               PvKeypad(30,
                                        [PvKeypad.cancel],
                                        cancel=1),

                           )
                       ],
                       Confirm("/app/images/m25t_motor_jog1x.png",
                               tr._did_the_motor_jog, yes=2)
                       )

right_mount = Step(tr._right_mount,
                       [
                           Row(Text(30, tr._is_right_mount),
                               Text(30, tr._yes),
                               Text(30, tr._no)
                               ),
                           Row(
                               Spacer(30),
                               PvKeypad(30,
                                        [PvKeypad.okay],
                                        confirm=PvKeypad.okay,
                                        okay=Commands('backroller_right')),
                               PvKeypad(30,
                                        [PvKeypad.cancel],
                                        cancel=1),

                           )
                       ],
                       Confirm("/app/images/m25t_motor_jog1x.png",
                               tr._did_the_motor_jog, yes=1)
                       )


save_slat_position = Step(tr._blinddirection,
                       [
                           Row(Text(30, tr._press_okay_button.add_number(1)),
                               Text(30, tr._motor_should_move_down.add_number(2))),
                           Row(PvKeypad(30, ['okay'], 'okay', Commands('tiltclose', DelayedCommand('stop', 3),
                                                                       DelayedCommand('stop', 0.4),
                                                                       DelayedCommand('stop', 0.4)), cancel=1),
                               Image(30, "/app/images/m25t_motor_top_limit_move_down_rollo.png"))
                       ],
                       Confirm("/app/images/m25t_motor_top_limit_move_down_rollo.png", tr._did_motor_move_down,
                               yes=2,
                               no=1))