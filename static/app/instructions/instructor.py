from static.app.instructions.connect import connect

from static.app.instructions.components import Row, Text, PvKeypad, Step, Image, Confirm, Next, \
    Previous, Product, Instruction, ToJson, Spacer, DelayedCommand, Commands, NavigationCommand
from static.app.instructions.general import enter_program_mode

from static.app.instructions.motor_direction import left_frontroller, left_backroller, right_frontroller, \
    right_backroller, switch_direction, blind_direction

from static.app.instructions.helpers import TXT

import static.app.instructions.translations as tr
from static.app.instructions.roller import initialise_roller

from static.app.instructions.twist import connect_make_twist, re_set_twist_slat_open, skipbottom_twist, \
    set_twist_position, initialise_twist
from static.app.instructions.venetian import initialise_vb16, left_mount, right_mount

if __name__ == "__main__":
    hang_twist = Step(tr._hangtwist,
                      [
                          Row(Text(40, tr._proper_product_hang.add_number(1)),
                              Text(30, tr._proper_product_hang_confirm.add_number(2))),
                          Row(Image(40, "/app/images/m25t_20cm.png"),
                              PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)))
                      ],
                      nav_previous=Previous(active=False),
                      id='hoist')

    hang_rollo = Step(tr._hangrollo,
                      [
                          Row(Text(40, tr._proper_product_hang.add_number(1)),
                              Text(30, tr._proper_product_hang_confirm.add_number(2))),
                          Row(Image(40, "/app/images/m25t_20cm.png"),
                              PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)))
                      ],
                      nav_previous=Previous(active=False),
                      id='hoist')
    #
    # hoist = Step(tr._hangproduct,
    #              [
    #                  Row(Text(40, tr._proper_product_hang.add_number(1)),
    #                      Text(30, tr._proper_product_hang_confirm.add_number(2))),
    #                  Row(Image(40, "/app/images/m25t_20cm.png"),
    #                      PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)))
    #              ],
    #              nav_previous=Previous(active=False),
    #              id='hoist')









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

    skipslat = Step(tr._skipslattitle,
                    [
                        Row(Text(30, tr._make_choice),
                            Text(30, tr._reset_slat),
                            Text(30, tr._select_skip_slat)),
                        Row(Spacer(30),
                            PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                            PvKeypad(30, ['cancel'], cancel='testblinds'))
                    ])

    rollerblind1 = Product("Roller blind", [connect,
                                            initialise_roller,
                                            left_backroller,
                                            right_backroller,
                                            left_frontroller,
                                            right_frontroller,
                                            enter_program_mode,
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

    rollerblind_old = Product("Roller blind", [connect,
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

    twist = Product("Twist", [connect,
                              initialise_twist,
                              left_backroller,
                              right_backroller,
                              left_frontroller,
                              right_frontroller,
                              enter_program_mode,
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

    venetian16 = Product("VB 16", [connect,
                                   initialise_vb16,
                                   left_mount,
                                   right_mount,
                                   enter_program_mode,
                                   set_bottom_limit,
                                   enter_program_mode,
                                   set_top_limit,
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



    twist_old = Product("Twist", [connect,
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

    INSTRUCTION_VERSION = 1.6

    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

    nl = ToJson(lang='nl').encode(instruction)
    with open('instructions-luxaflex-nl.json', 'w') as fl:
        fl.write(nl)

    en = ToJson(lang='en').encode(instruction)
    with open('instructions-luxaflex-en.json', 'w') as fl:
        fl.write(en)

    with open('instructions-en.json', 'w') as fl:
        fl.write(en)


    instruction_vb = Instruction(INSTRUCTION_VERSION)
    instruction_vb.products.append(venetian16)

    en = ToJson(lang='en').encode(instruction_vb)
    with open('instructions-vb16-en.json','w') as fl:
        fl.write(en)

    make_twist = Product("make twist", [connect_make_twist])
    instruction3 = Instruction(INSTRUCTION_VERSION)
    instruction3.products.append(make_twist)
    twst = ToJson(lang='en').encode(instruction3)
    with open('instructions-set-id.json', 'w') as fl:
        fl.write(twst)

    test1 = Product("test1", [test_blinds])
    test2 = Product("test2", [hang_twist])
    test_instruction4 = Instruction(INSTRUCTION_VERSION)
    test_instruction4.products.append(test1)
    test_instruction4.products.append(test2)
    tst = ToJson(lang='en').encode(test_instruction4)
    with open('instructions-test.json', 'w') as fl:
        fl.write(tst)
