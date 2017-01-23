import instructor.translations as tr
from instructor.components import PvKeypad, Commands, Step, Row, Text, Image, Confirm
from instructor.general import keypad_move_buttons

textrow = Row(Text(30, tr._moveblind_top.add_number(1)),
              Text(30, tr._savetop.add_number(2)),
              Text(30, tr._watch_the_blind_jog.add_number(3)))

keypad_save_top = PvKeypad(30, ['okay'], 'okay', Commands('savepositiontop'))

set_top_limit_roller = Step(tr._settoplimit,
                     [
                         textrow,
                         Row(keypad_move_buttons,
                             keypad_save_top,
                             Image(30, "/app/images/m25t_motor_jog1x.png"))
                     ],
                     Confirm("/app/images/m25t_motor_jog1x.png", tr._did_the_motor_jog))


set_top_limit_vb = Step(tr._settoplimit,
                        [
                            textrow,
                            Row(keypad_move_buttons,
                                keypad_save_top,
                                Image(30,"/app/images/m25s_vb_motor_jog1x.png"))
                        ],
                        Confirm("/app/images/m25s_vb_motor_jog1x.png", tr._did_the_motor_jog))