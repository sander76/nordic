from instructor.helpers import TXT
from instructor.translations import Translations as Tr
from instructor.components import (
    Row,
    Text,
    Step,
    PvKeypadAlt,
    Commands,
    Spacer,
    NavigationCommand,
)
from instructor.constants import ID_CHOOSE_PRODUCT, ID_CHOOSE_SAME, ID_START


def get_confirm_product(product_title):
    return Step(
        Tr.CORRECT_PRODUCT,
        [
            Row(
                Text(30, Tr.MAKE_CHOICE),
                Text(30, product_title),
                Text(30, Tr.ANOTHER_PRODUCT),
            ),
            Row(
                Spacer(30),
                PvKeypadAlt(
                    30, okay=Commands(navigation_command=NavigationCommand(1))
                ),
                PvKeypadAlt(
                    30,
                    cancel=Commands(
                        navigation_command=NavigationCommand(ID_CHOOSE_PRODUCT)
                    ),
                ),
            ),
        ],
        nav_id=ID_START,
    )


def get_confirm_product_alt(product_title, jumbo):

    return Step(
        Tr.CORRECT_PRODUCT,
        [
            Row(
                Text(30, product_title),
                Text(30, Tr.YES.to_upper()),
                Text(30, Tr.NO.to_upper()),
            ),
            Row(
                Text(30, TXT("# *{}*".format(jumbo))),
                PvKeypadAlt(
                    30, okay=Commands(navigation_command=NavigationCommand(1))
                ),
                PvKeypadAlt(
                    30,
                    cancel=Commands(
                        navigation_command=NavigationCommand(ID_CHOOSE_PRODUCT)
                    ),
                ),
            ),
        ],
        nav_id=ID_START,
    )


confirm_rb = get_confirm_product(Tr.PRODUCT_PV_ROLLERBLIND)
confirm_twist = get_confirm_product(Tr.PRODUCT_PV_TWIST)
confirm_vb = get_confirm_product(Tr.PRODUCT_PV_M25S_VB)

confirm_vb16 = get_confirm_product_alt(Tr.PRODUCT_PV_M25S_VB16, "16mm.")
confirm_vb25 = get_confirm_product_alt(Tr.PRODUCT_PV_M25S_VB25, "25mm.")
confirm_vb35 = get_confirm_product_alt(Tr.PRODUCT_PV_M25S_VB35, "35mm.")
confirm_mhz_vb = get_confirm_product_alt(Tr.PRODUCT_PV_M25S_VB, "")

confirm_duette = get_confirm_product(Tr.PRODUCT_PV_M25S_DUETTE)
confirm_duette_tensioned = get_confirm_product(
    Tr.PRODUCT_PV_M25S_DUETTE_TENSIONED
)
confirm_pleated = get_confirm_product(Tr.PRODUCT_PV_M25S_PLEATED)
confirm_pleated_tensioned = get_confirm_product(
    Tr.PRODUCT_PV_M25S_PLEATED_TENSIONED
)
confirm_vvb = get_confirm_product(Tr.PRODUCT_PV_M25S_VVB)
