
from static.app.instructions.components import TXT, Row, Text, PvKeypad, Step, Image, OkayCommand, Confirm, Next, \
    Previous, Product, Instruction, ToJson

import static.app.instructions.translations as tr

if __name__ == "__main__":
    instruction2 = [
        Row(Text(30, "Testing content"), PvKeypad(30, ['open', 'close'])),
        Row(Text(30, "another testing of content."), Image(30, '/testing/testing.png'))
    ]

    hoist = Step(tr._hangproduct,
                 [
                     Row(Text(40, tr._proper_product_hang.add_number(1)),
                         Text(30, tr._proper_product_hang_confirm.add_number(2))),
                     Row(Image(40, "/app/images/m25t_20cm.png"),
                         PvKeypad(30, ['okay'], okay=OkayCommand(goto=1)))
                 ])

    connect = Step(tr._connect,
                   [Row(Text(25, tr._press_hold_blind_button),
                        Text(25, tr._keep_pressing_and_okay),
                        Text(25, tr._release_the_blind_button),
                        Text(25, tr._watch_the_blind_jog.add_number(4))),
                    Row(Image(25, "/app/images/m25t_motor_button_push_top_limit_rollo.png"),
                        PvKeypad(25, ['okay'], 'okay', OkayCommand(['networkadd', 'group1add'], 1)),
                        Image(25, "/app/images/m25t_motor_button_release_top_limit_rollo.png"),
                        Image(25, "/app/images/m25t_motor_jog1x.png"))
                    ],
                   Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog),
                   Next(),
                   Previous(active=False))

    initialise = Step(tr._initialise,
                      [Row(Text(30, tr._press_okay_button.add_number(1)),
                           Text(30, tr._motor_jogs_two_times.add_number(2))),
                       Row(PvKeypad(30, ['okay'], 'okay', OkayCommand(['reset', 'roller'], 4)),
                           Image(30, "/app/images/m25t_motor_jog2x.png"))
                       ],
                      Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times),
                      Next(),
                      Previous())

    enter_program_mode = Step(tr._enterprogrammode,
                              [Row(Text(30, tr._press_okay_button.add_number(1)),
                                   Text(30, tr._motor_jogs.add_number(2))),
                               Row(PvKeypad(30, ['okay'], 'okay', OkayCommand(['startprogram'])),
                                   Image(30, "/app/images/m25t_motor_jog1x.png"))
                               ], Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

    blind_direction = Step(tr._blinddirection,
                           [
                               Row(Text(30, tr._press_okay_button.add_number(1)),
                                   Text(30, tr._motor_should_move_down.add_number(2))),
                               Row(PvKeypad(30, ['okay'], 'okay', OkayCommand(['tiltclose', 'stop'], 3), cancel=1),
                                   Image(30, "/app/images/m25t_motor_top_limit_move_down_rollo.png"))
                           ],
                           Confirm("/app/images/m25t_motor_top_limit_move_down_rollo.png", tr._did_motor_move_down, yes=2,
                                   no=1))

    switch_direction = Step(tr._switchdirection,
                            [
                                Row(Text(30, tr._press_okay_button.add_number(1)),
                                    Text(30, tr._motor_jogs.add_number(2))),
                                Row(PvKeypad(30, ['okay'], 'okay', OkayCommand(['startprogram', 'reverse'], delay=2)),
                                    Image(30, "/app/images/m25t_motor_jog1x.png"))
                            ],
                            Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

    set_bottom_limit = Step(tr._setbottomlimit,
                            [
                                Row(Text(30, tr._moveblind),
                                    Text(30, tr._savebottom),
                                    Text(30, tr._motor_jogs)),
                                Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                    PvKeypad(30, ['okay'], 'okay', OkayCommand(['savepositionbottom'])),
                                    Image(30, "/app/images/m25t_motor_jog1x.png"))
                            ],
                            Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

    set_top_limit = Step(tr._settoplimit,
                         [
                             Row(Text(30, tr._moveblind),
                                 Text(30, tr._savetop),
                                 Text(30, tr._motor_jogs)),
                             Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                 PvKeypad(30, ['okay'], 'okay', OkayCommand(['savepositiontop'])),
                                 Image(30, "/app/images/m25t_motor_jog1x.png"))
                         ],
                         Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

    test_blinds = Step(tr._testblinds,
                       [
                           Row(Text(30, tr._test_move_blinds)),
                           Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                               PvKeypad(30, ['okay'], okay=OkayCommand(goto=-9)),
                               PvKeypad(30, ['cancel'], cancel=1))
                       ])

    skiptop = Step(tr._skiptoptitle,
                   [
                       Row(Text(80, tr._make_choice)),
                       Row(Text(30, tr._reset_bottom),
                           Text(30, tr._select_skip_top)),
                       Row(PvKeypad(30, ['okay'], okay=OkayCommand(goto=1)),
                           PvKeypad(30, ['cancel'], cancel=3))
                   ])

    skipbottom = Step(tr._skipbottomtitle,
                      [
                          Row(Text(80, tr._make_choice)),
                          Row(Text(30, tr._reset_top),
                              Text(30, tr._select_skip_bottom)),
                          Row(PvKeypad(30, ['okay'], okay=OkayCommand(goto=1)),
                              PvKeypad(30, ['cancel'], cancel=-3))
                      ])
    set_bottom_limit_final = Step(tr._setbottomlimit,
                                  [
                                      Row(Text(30, tr._moveblind),
                                          Text(30, tr._savebottom),
                                          Text(30, tr._motor_jogs)),
                                      Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                          PvKeypad(30, ['okay'], 'okay', OkayCommand(['savepositionbottom'])),
                                          Image(30, "/app/images/m25t_motor_jog1x.png"))
                                  ],
                                  Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog, yes=-4))

    rollerblind1 = Product("Roller blind", [hoist,
                                            connect,
                                            initialise,
                                            enter_program_mode,
                                            blind_direction,
                                            switch_direction,
                                            set_bottom_limit,
                                            enter_program_mode,
                                            set_top_limit,
                                            test_blinds,
                                            skiptop,
                                            enter_program_mode,
                                            set_top_limit,
                                            skipbottom,
                                            enter_program_mode,
                                            set_bottom_limit_final
                                            ])

    instruction = Instruction()
    instruction.products.append(rollerblind1)

    nl = ToJson(lang='nl').encode(instruction)
    with open('instructions-test-nl.json', 'w') as fl:
        fl.write(nl)

    en = ToJson(lang='en').encode(instruction)
    with open('instructions-test-en.json', 'w') as fl:
        fl.write(en)
