# import instructor.translations as tr
from instructor.translations import Translations as Tr
from instructor.components import Step, Row, Text, \
    NavigationCommand, Image, Previous, PvKeypadAlt, Commands
from instructor.constants import ID_HOIST

textrow = Row(Text(40, Tr.PROPER_PRODUCT_HANG.add_number(1)),
              Text(30, Tr.PROPER_PRODUCT_HANG_CONFIRM.add_number(2)))

hang_twist = Step(
    Tr.HANG_TWIST,
    [
        textrow,
        Row(
            Image(40, "/app/images/m25t_20cm.png"),
            PvKeypadAlt(
                30,
                okay=Commands(
                    navigation_command=NavigationCommand(goto=1))))
    ],
    nav_previous=Previous(active=False),
    nav_id=ID_HOIST)

hang_rollo = Step(
    Tr.HANG_RB,
    [
        textrow,
        Row(Image(40, "/app/images/m25t_20cm.png"),
            PvKeypadAlt(
                30,
                okay=Commands(navigation_command=NavigationCommand(goto=1))))
    ],
    nav_previous=Previous(active=False),
    nav_id=ID_HOIST)
