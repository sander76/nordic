import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    Commands, Spacer, NavigationCommand

keypad_move_buttons = PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop'])

textrow = Row(Text(30, tr._press_okay_button.add_number(1)),
              Text(30, tr._watch_the_blind_jog.add_number(2)))

keypad = PvKeypad(30, ['okay'], 'okay', Commands('startprogram'))



enter_program_mode = Step(tr._enterprogrammode,
                          [textrow,
                           Row(keypad,
                               Image(30, "/app/images/m25t_motor_jog1x.png"))
                           ], Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))

enter_program_mode_vb = Step(tr._enterprogrammode,
                             [textrow,
                              Row(keypad,
                                  Image(30, "/app/images/m25s_vb_motor_jog1x.png"))
                              ], Confirm("/app/images/m25s_vb_motor_jog1x.png", tr._did_the_motor_jog))

test_blinds = Step(tr._testblinds,
                   [
                       Row(Text(30, tr._test_move_blinds),
                           Text(30, tr._limits_ok),
                           Text(30, tr._limits_not_ok)),
                       Row(PvKeypad(30, ['open', 'close', 'tiltup', 'tiltdown', 'stop']),
                           PvKeypad(30, ['okay'], okay=NavigationCommand(goto="start")),
                           PvKeypad(30, ['cancel'], cancel=1))
                   ], id="testblinds")

skipslat = Step(tr._skipslattitle,
                [
                    Row(Text(30, tr._make_choice),
                        Text(30, tr._reset_slat),
                        Text(30, tr._select_skip_slat)),
                    Row(Spacer(30),
                        PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                        PvKeypad(30, ['cancel'], cancel='testblinds'))
                ])

