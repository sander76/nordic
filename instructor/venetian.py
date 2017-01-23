import instructor.translations as tr

from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, Product, Spacer, DelayedCommand, Commands
from instructor.connect import connect_vb
from instructor.general import enter_program_mode_vb, test_blinds
from instructor.initialise import initialise_vb
from instructor.set_bottom_limit import set_bottom_limit_vb, re_set_bottom_limit_vb
from instructor.set_top_limit import set_top_limit_vb
from instructor.skip_step import skiptop, skipbottom_end

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
                       Confirm("/app/images/m25s_vb_motor_jog1x.png",
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

venetian16 = Product("VB 16", [connect_vb,
                               initialise_vb,
                               left_mount,
                               right_mount,
                               enter_program_mode_vb,
                               set_bottom_limit_vb,
                               enter_program_mode_vb,
                               set_top_limit_vb,
                               test_blinds,
                               skiptop,
                               enter_program_mode_vb,
                               set_top_limit_vb,
                               skipbottom_end,
                               enter_program_mode_vb,
                               re_set_bottom_limit_vb
                               ])
