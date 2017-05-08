from instructor.translations import Translations as tr
from instructor.components import Step, Row, Text, NavigationCommand, \
    PvKeypad, Spacer
from instructor.constants import ID_TEST_BLINDS

"""
Skips setting bottom limits and returns to testblinds screen.
"""
skipbottom_end = Step(tr.TITLE_SKIP_BOTTOM,
                      [
                          Row(Text(30, tr.MAKE_CHOICE),
                              Text(30, tr.RESET_BOTTOM),
                              Text(30, tr.SELECT_SKIP_BOTTOM)),
                          Row(Spacer(30),
                              PvKeypad(30, ['okay'],
                                       okay=NavigationCommand(goto=1)),
                              PvKeypad(30, ['cancel'], cancel=NavigationCommand(ID_TEST_BLINDS)))
                      ])

skipclose_end = Step(tr.TITLE_SKIP_CLOSE,
                     [])

"""
skip setting bottom limits and proceeds to next question.
"""
skipbottom_next = Step(tr.TITLE_SKIP_BOTTOM,
                       [
                           Row(Text(30, tr.MAKE_CHOICE),
                               Text(30, tr.RESET_BOTTOM),
                               Text(30, tr.SELECT_SKIP_BOTTOM)),
                           Row(Spacer(30),
                               PvKeypad(30, ['okay'],
                                        okay=NavigationCommand(goto=1)),
                               PvKeypad(30, ['cancel'], cancel=NavigationCommand(3)))
                       ])

skiptop = Step(tr.TITLE_SKIP_TOP,
               [
                   Row(Text(30, tr.MAKE_CHOICE),
                       Text(30, tr.RESET_TOP),
                       Text(30, tr.SELECT_SKIP_TOP)),
                   Row(Spacer(30),
                       PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                       PvKeypad(30, ['cancel'], cancel=NavigationCommand(3)))
               ])


skipopen = Step(tr.TITLE_SKIP_OPEN,
                [
                   Row(Text(30, tr.MAKE_CHOICE),
                       Text(30, tr.RESET_OPEN),
                       Text(30, tr.SELECT_SKIP_OPEN)),
                   Row(Spacer(30),
                       PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)),
                       PvKeypad(30, ['cancel'], cancel=NavigationCommand(3)))
               ])

