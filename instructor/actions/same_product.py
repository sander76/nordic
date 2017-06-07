from instructor.translations import Translations as Tr
from instructor.components import Row, Text, Step, \
    PvKeypadAlt, Commands, Spacer, \
    NavigationCommand
from instructor.constants import ID_CHOOSE_PRODUCT, ID_CHOOSE_SAME, ID_START


def get_same_product(product_title):
    return Step(
        Tr.CONNECT,
        [Row(
            Text(30, Tr.MAKE_CHOICE),
            Text(30, product_title),
            Text(30, Tr.ANOTHER_PRODUCT)
        ),
            Row(
                Spacer(30),
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        navigation_command=NavigationCommand(ID_START))
                ),
                PvKeypadAlt(
                    30,
                    cancel=Commands(
                        navigation_command=NavigationCommand(
                            ID_CHOOSE_PRODUCT)
                    )
                )
            )
        ],
        nav_id=ID_CHOOSE_SAME)


same_rb = get_same_product(Tr.PRODUCT_PV_ROLLERBLIND)
same_twist = get_same_product(Tr.PRODUCT_PV_TWIST)
same_vb = get_same_product(Tr.PRODUCT_PV_M25S_VB)
same_duette = get_same_product(Tr.PRODUCT_PV_M25S_DUETTE)
same_vvb = get_same_product(Tr.PRODUCT_PV_M25S_VVB)
