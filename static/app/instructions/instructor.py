from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, Next, \
    Previous, Product, Instruction, ToJson, Spacer, DelayedCommand, Commands, NavigationCommand

from static.app.instructions.helpers import TXT

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
                         PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)))
                 ],
                 nav_previous=Previous(active=False),
                 id='hoist')

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

    '''Instruction to quickly make a rb a twist. Not user friendly !'''
    connect_make_twist = Step(tr._connect,
                              [
                                  Row(Text(100, "Connect your blind using normal procedure")),
                                  Row(PvKeypad(25, ['okay'], 'okay', Commands('networkadd',
                                                                              DelayedCommand('group1add', 1),
                                                                              DelayedCommand('reset', 2),
                                                                              DelayedCommand('twist', 2))))
                              ],
                              Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog, yes=-1))

    initialise_roller = Step(tr._initialise,
                             [Row(Text(30, tr._press_okay_button.add_number(1)),
                                  Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
                              Row(PvKeypad(30, ['okay'], 'okay', Commands('reset', DelayedCommand('roller', 4))),
                                  Image(30, "/app/images/m25t_motor_jog2x.png"))
                              ],
                             Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

    initialise_twist = Step(tr._initialise,
                            [Row(Text(30, tr._press_okay_button.add_number(1)),
                                 Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
                             Row(PvKeypad(30, ['okay'], 'okay', Commands('reset', DelayedCommand('twist', 4))),
                                 Image(30, "/app/images/m25t_motor_jog2x.png"))
                             ],
                            Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

    enter_program_mode = Step(tr._enterprogrammode,
                              [Row(Text(30, tr._press_okay_button.add_number(1)),
                                   Text(30, tr._watch_the_blind_jog.add_number(2))),
                               Row(PvKeypad(30, ['okay'], 'okay', Commands('startprogram')),
                                   Image(30, "/app/images/m25t_motor_jog1x.png"))
                               ], Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

    blind_direction = Step(tr._blinddirection,
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

    switch_direction = Step(tr._switchdirection,
                            [
                                Row(Text(30, tr._press_okay_button.add_number(1)),
                                    Text(30, tr._watch_the_blind_jog.add_number(2))),
                                Row(PvKeypad(30, ['okay'], 'okay',
                                             Commands('startprogram', DelayedCommand('reverse', 2))),
                                    Image(30, "/app/images/m25t_motor_jog1x.png"))
                            ],
                            Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

    savepositionBottom = PvKeypad(30, ['okay'], 'okay', Commands('savepositionbottom'))

    set_bottom_limit = Step(tr._setbottomlimit,
                            [
                                Row(Text(30, tr._moveblind_bottom.add_number(1)),
                                    Text(30, tr._savebottom.add_number(2)),
                                    Text(30, tr._watch_the_blind_jog.add_number(3))),
                                Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                    savepositionBottom,
                                    Image(30, "/app/images/m25t_motor_jog1x.png"))
                            ],
                            Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

    set_top_limit = Step(tr._settoplimit,
                         [
                             Row(Text(30, tr._moveblind_top.add_number(1)),
                                 Text(30, tr._savetop.add_number(2)),
                                 Text(30, tr._watch_the_blind_jog.add_number(3))),
                             Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                 PvKeypad(30, ['okay'], 'okay', Commands('savepositiontop')),
                                 Image(30, "/app/images/m25t_motor_jog1x.png"))
                         ],
                         Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

    saveSlatOpen = PvKeypad(30, ['okay'], 'okay', Commands('saveslatopen'))

    set_twist_position = Step(tr._set_twist_slatposition,
                              [
                                  Row(Text(30, tr._moveblind_slatopen),
                                      Text(30, tr._saveslat),
                                      Text(30, tr._watch_the_blind_jog)),
                                  Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                      saveSlatOpen,
                                      Image(30, "/app/images/m25t_motor_jog1x.png"))
                              ],
                              Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

    test_blinds = Step(tr._testblinds,
                       [
                           Row(Text(30, tr._test_move_blinds),
                               Text(30, tr._limits_ok),
                               Text(30, tr._limits_not_ok)),
                           Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                               PvKeypad(30, ['okay'], okay=NavigationCommand(goto="hoist")),
                               PvKeypad(30, ['cancel'], cancel=1))
                       ], id="testblinds")

    skiptop = Step(tr._skiptoptitle,
                   [
                       Row(Text(30, tr._make_choice),
                           Text(30, tr._reset_top),
                           Text(30, tr._select_skip_top)),
                       Row(Spacer(30),
                           PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                           PvKeypad(30, ['cancel'], cancel=3))
                   ])

    skipbottom_blind = Step(tr._skipbottomtitle,
                            [
                                Row(Text(30, tr._make_choice),
                                    Text(30, tr._reset_bottom),
                                    Text(30, tr._select_skip_bottom)),
                                Row(Spacer(30),
                                    PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                                    PvKeypad(30, ['cancel'], cancel="testblinds"))
                            ])

    skipbottom_twist = Step(tr._skipbottomtitle,
                            [
                                Row(Text(30, tr._make_choice),
                                    Text(30, tr._reset_bottom),
                                    Text(30, tr._select_skip_bottom)),
                                Row(Spacer(30),
                                    PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                                    PvKeypad(30, ['cancel'], cancel=3))
                            ])

    '''
    Same as normal setting the bottom limits, but confirm dialog navigates to different page when ok.
    '''
    re_set_bottom_limit = Step(set_bottom_limit.title,
                               set_bottom_limit.instructions,
                               Confirm("/app/images/m25t_motor_top_limit_move_up_rollo.png", tr._did_the_motor_move_up,
                                       yes="testblinds"))

    '''
    same as setting bottom limit.
    '''
    re_set_bottom_limit_twist = Step(tr._setbottomlimit,
                                     set_bottom_limit.instructions,
                                     Confirm("/app/images/m25t_motor_top_limit_move_up_rollo.png",
                                             tr._did_the_motor_move_up))

    re_set_twist_slat_open = Step(tr._set_twist_slatposition,
                                  [
                                      Row(Text(30, tr._moveblind_slatopen),
                                          Text(30, tr._saveslat),
                                          Text(30, tr._watch_the_blind_jog)),
                                      Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                                          saveSlatOpen,
                                          Image(30, "/app/images/m25t_motor_jog1x.png"))
                                  ],
                                  Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog, yes="testblinds"))

    skipslat = Step(tr._skipslattitle,
                    [
                        Row(Text(30, tr._make_choice),
                            Text(30, tr._reset_slat),
                            Text(30, tr._select_skip_slat)),
                        Row(Spacer(30),
                            PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                            PvKeypad(30, ['cancel'], cancel='testblinds'))
                    ])

    rollerblind1 = Product("Roller blind", [hoist,
                                            connect,
                                            initialise_roller,
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
                                            skipbottom_blind,
                                            enter_program_mode,
                                            re_set_bottom_limit
                                            ])

    twist = Product("Twist", [hoist,
                              connect,
                              initialise_twist,
                              enter_program_mode,
                              blind_direction,
                              switch_direction,
                              set_bottom_limit,
                              enter_program_mode,
                              set_top_limit,
                              set_twist_position,
                              test_blinds,
                              skiptop,
                              enter_program_mode,
                              set_top_limit,
                              skipbottom_twist,
                              enter_program_mode,
                              re_set_bottom_limit_twist,
                              skipslat,
                              re_set_twist_slat_open
                              ])


    instruction = Instruction('1.4')
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

    nl = ToJson(lang='nl').encode(instruction)
    with open('instructions-luxaflex-nl.json', 'w') as fl:
        fl.write(nl)

    en = ToJson(lang='en').encode(instruction)
    with open('instructions-luxaflex-en.json', 'w') as fl:
        fl.write(en)

    make_twist = Product("make twist", [connect_make_twist])
    instruction3=Instruction('1.0')
    instruction3.products.append(make_twist)
    twst = ToJson(lang='en').encode(instruction3)
    with open('instructions-set-id.json','w') as fl:
        fl.write(twst)