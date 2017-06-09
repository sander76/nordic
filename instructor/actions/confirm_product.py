from instructor.translations import Translations as Tr
from instructor.components import Row, Text, Step, \
    PvKeypadAlt, Commands, Spacer, \
    NavigationCommand
from instructor.constants import ID_CHOOSE_PRODUCT, ID_CHOOSE_SAME, ID_START


def get_confirm_product(product_title):
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
                        navigation_command=NavigationCommand(1))
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


confirm_rb = get_confirm_product(Tr.PRODUCT_PV_ROLLERBLIND)
confirm_twist = get_confirm_product(Tr.PRODUCT_PV_TWIST)
confirm_vb = get_confirm_product(Tr.PRODUCT_PV_M25S_VB)
confirm_duette = get_confirm_product(Tr.PRODUCT_PV_M25S_DUETTE)
confirm_duette_tensioned = get_confirm_product(Tr.PRODUCT_PV_M25S_DUETTE_TENSIONED)
confirm_vvb = get_confirm_product(Tr.PRODUCT_PV_M25S_VVB)
