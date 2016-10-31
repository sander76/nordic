from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, Next, \
    Previous, Product, Instruction, ToJson, Spacer, DelayedCommand, Commands, NavigationCommand

from static.app.instructions.helpers import TXT

import static.app.instructions.translations as tr

left_backroller = Step(tr._backroller_left_title,
                       [
                           Row(Text(30, tr._is_left_backroller),
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
                               tr._did_the_motor_jog, yes=4)
                       )

right_backroller = Step(tr._backroller_right_title,
                        [
                            Row(Text(30, tr._is_right_backroller),
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
                                tr._did_the_motor_jog,
                                yes=3)
                        )

left_frontroller = Step(tr._frontroller_left_title,
                        [
                            Row(Text(30, tr._is_left_frontroller),
                                Text(30, tr._yes),
                                Text(30, tr._no)
                                ),
                            Row(
                                Spacer(30),
                                PvKeypad(30,
                                         [PvKeypad.okay],
                                         confirm=PvKeypad.okay,
                                         okay=Commands('backroller_right'),
                                         ),
                                PvKeypad(30,
                                         [PvKeypad.cancel],
                                         cancel=1)
                            )
                        ], Confirm("/app/images/m25t_motor_jog1x.png",
                                   tr._did_the_motor_jog,
                                   yes=2)
                        )

right_frontroller = Step(tr._frontroller_right_title,
                         [
                             Row(Text(30, tr._is_right_frontroller),
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
                                          cancel=-3)
                             )
                         ],
                         Confirm("/app/images/m25t_motor_jog1x.png",
                                 tr._did_the_motor_jog,
                                 yes=1)
                         )
