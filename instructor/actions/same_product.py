from instructor.translations import Translations as tr
from instructor.components import Row, Text, Step, Image, Confirm, \
    DelayedCommand, NordicCommands, PvKeypadAlt, Commands, Spacer, \
    NavigationCommand
from instructor.constants import TWIST_JOG_1, TWIST_BUTTON_PUSH_HOLD, \
    TWIST_BUTTON_RELEASE, RB_JOG_1, RB_BUTTON_PUSH_HOLD, RB_BUTTON_RELEASE, \
    ID_START, VB_JOG_1, VB_BUTTON_PUSH_HOLD, VB_BUTTON_RELEASE, DUETTE_JOG_1, \
    DUETTE_BUTTON_PUSH_HOLD, DUETTE_BUTTON_RELEASE, VVB_JOG_1, \
    VVB_BUTTON_PUSH_HOLD, VVB_BUTTON_RELEASE, PLEATED_JOG_1, \
    PLEATED_BUTTON_PUSH_HOLD, PLEATED_BUTTON_RELEASE, ID_CHOOSE_PRODUCT, \
    ID_CHOOSE_SAME
from server.nordic import Nd


def get_same_product(product_title):
    return Step(
        tr.CONNECT,
        [Row(
            Text(30, tr.MAKE_CHOICE),
            Text(30, product_title),
            Text(30, tr.ANOTHER_PRODUCT)
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


same_rb = get_same_product(tr.PRODUCT_PV_ROLLERBLIND)
same_twist = get_same_product(tr.PRODUCT_PV_TWIST)
same_vb = get_same_product(tr.PRODUCT_PV_M25S_VB)
same_duette = get_same_product(tr.PRODUCT_PV_M25S_DUETTE)
same_vvb = get_same_product(tr.PRODUCT_PV_M25S_VVB)
