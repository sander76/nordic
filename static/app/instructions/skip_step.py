import static.app.instructions.translations as tr
from static.app.instructions.components import Step, Row, Text, NavigationCommand, PvKeypad, Spacer

"""
Skips setting bottom limits and returns to testblinds screen.
"""
skipbottom_end = Step(tr._skipbottomtitle,
                      [
                          Row(Text(30, tr._make_choice),
                              Text(30, tr._reset_bottom),
                              Text(30, tr._select_skip_bottom)),
                          Row(Spacer(30),
                              PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                              PvKeypad(30, ['cancel'], cancel="testblinds"))
                      ])

"""
skip setting bottom limits and proceeds to next question.
"""
skipbottom_next = Step(tr._skipbottomtitle,
                       [
                           Row(Text(30, tr._make_choice),
                               Text(30, tr._reset_bottom),
                               Text(30, tr._select_skip_bottom)),
                           Row(Spacer(30),
                               PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                               PvKeypad(30, ['cancel'], cancel=3))
                       ])

skiptop = Step(tr._skiptoptitle,
               [
                   Row(Text(30, tr._make_choice),
                       Text(30, tr._reset_top),
                       Text(30, tr._select_skip_top)),
                   Row(Spacer(30),
                       PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                       PvKeypad(30, ['cancel'], cancel=3))
               ])
