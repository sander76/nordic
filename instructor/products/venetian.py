# import instructor.translations as tr
# from instructor.actions.connect import connect_m25s_vb
# from instructor.actions.general import enter_program_mode_vb, test_blinds
# from instructor.actions.initialise import initialise_vb
# from instructor.actions.set_bottom_limit import set_bottom_limit_vb, \
#     re_set_bottom_limit_vb
# from instructor.actions.set_top_limit import set_top_limit_vb
# from instructor.actions.skip_step import skiptop, skipbottom_end
# from instructor.components import Row, Text, PvKeypad, Step, Confirm, \
#     Product, Spacer, Commands
# from instructor.constants import VB_JOG_1
# from server.nordic import BACKROLLER_RIGHT, BACKROLLER_LEFT
#
# left_mount = Step(tr.LEFT_MOUNT,
#                   [
#                       Row(Text(30, tr.IS_LEFT_MOUNT),
#                           Text(30, tr.YES),
#                           Text(30, tr.NO)
#                           ),
#                       Row(
#                           Spacer(30),
#                           PvKeypad(30,
#                                    [PvKeypad.okay],
#                                    confirm=PvKeypad.okay,
#                                    okay=Commands(BACKROLLER_LEFT)),
#                           PvKeypad(30,
#                                    [PvKeypad.cancel],
#                                    cancel=1),
#
#                       )
#                   ],
#                   Confirm(VB_JOG_1,
#                           tr.DID_THE_MOTOR_JOG, yes=2)
#                   )
#
# right_mount = Step(tr.RIGHT_MOUNT,
#                    [
#                        Row(Text(30, tr.IS_RIGHT_MOUNT),
#                            Text(30, tr.YES),
#                            Text(30, tr.NO)
#                            ),
#                        Row(
#                            Spacer(30),
#                            PvKeypad(30,
#                                     [PvKeypad.okay],
#                                     confirm=PvKeypad.okay,
#                                     okay=Commands(BACKROLLER_RIGHT)),
#                            PvKeypad(30,
#                                     [PvKeypad.cancel],
#                                     cancel=1),
#
#                        )
#                    ],
#                    Confirm(VB_JOG_1,
#                            tr.DID_THE_MOTOR_JOG, yes=1)
#                    )
#
# venetian16 = Product(
#     "VB 16", [connect_m25s_vb,
#               initialise_vb,
#               left_mount,
#               right_mount,
#               enter_program_mode_vb,
#               set_bottom_limit_vb,
#               enter_program_mode_vb,
#               set_top_limit_vb,
#               test_blinds,
#               skiptop,
#               enter_program_mode_vb,
#               set_top_limit_vb,
#               skipbottom_end,
#               enter_program_mode_vb,
#               re_set_bottom_limit_vb
#               ])
