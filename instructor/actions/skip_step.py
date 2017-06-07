from instructor.translations import Translations as Tr
from instructor.components import Step, Row, Text, NavigationCommand, \
    Spacer, PvKeypadAlt, Commands
from instructor.constants import ID_TEST_BLINDS

"""
Skips setting bottom limits and returns to testblinds screen.
"""
skipbottom_end = Step(
    Tr.TITLE_SKIP_BOTTOM,
    [
        Row(Text(30, Tr.MAKE_CHOICE),
            Text(30, Tr.RESET_BOTTOM),
            Text(30, Tr.SELECT_SKIP_BOTTOM)),
        Row(Spacer(30),
            PvKeypadAlt(
                30,
                okay=Commands(
                    navigation_command=NavigationCommand(1))),
            PvKeypadAlt(
                30,
                cancel=Commands(
                    navigation_command=NavigationCommand(ID_TEST_BLINDS))))
    ])

skipclose_end = Step(Tr.TITLE_SKIP_CLOSE,
                     [])

"""
skip setting bottom limits and proceeds to next question.
"""
skipbottom_next = Step(
    Tr.TITLE_SKIP_BOTTOM,
    [
        Row(Text(30, Tr.MAKE_CHOICE),
            Text(30, Tr.RESET_BOTTOM),
            Text(30, Tr.SELECT_SKIP_BOTTOM)),
        Row(Spacer(30),
            PvKeypadAlt(
                30,
                okay=Commands(
                    navigation_command=NavigationCommand(goto=1))),
            PvKeypadAlt(
                30,
                cancel=Commands(
                    navigation_command=NavigationCommand(3))))
    ])

skiptop = Step(
    Tr.TITLE_SKIP_TOP,
    [
        Row(Text(30, Tr.MAKE_CHOICE),
            Text(30, Tr.RESET_TOP),
            Text(30, Tr.SELECT_SKIP_TOP)),
        Row(Spacer(30),
            PvKeypadAlt(
                30,
                okay=Commands(
                    navigation_command=NavigationCommand(goto=1))),
            PvKeypadAlt(
                30,
                cancel=Commands(
                    navigation_command=NavigationCommand(3))))
    ])

skipopen = Step(
    Tr.TITLE_SKIP_OPEN,
    [
        Row(Text(30, Tr.MAKE_CHOICE),
            Text(30, Tr.RESET_OPEN),
            Text(30, Tr.SELECT_SKIP_OPEN)),
        Row(Spacer(30),
            PvKeypadAlt(
                30,
                okay=Commands(navigation_command=NavigationCommand(goto=1))),
            PvKeypadAlt(
                30,
                cancel=Commands(navigation_command=NavigationCommand(3))))
    ])

# skipping this step returns to ID_TEST_BLINDS
skipclose = Step(
    Tr.TITLE_SKIP_CLOSE,
    [
        Row(Text(30, Tr.MAKE_CHOICE),
            Text(30, Tr.RESET_CLOSE),
            Text(30, Tr.SELECT_SKIP_CLOSE)),
        Row(Spacer(30),
            PvKeypadAlt(
                30,
                okay=Commands(navigation_command=NavigationCommand(goto=1))),
            PvKeypadAlt(
                30,
                cancel=Commands(
                    navigation_command=NavigationCommand(ID_TEST_BLINDS))))
    ])
