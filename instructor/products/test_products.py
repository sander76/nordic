from instructor.components import Product, Step, Row, \
    PvKeypadAlt, default_open, default_close, default_tiltopen, \
    default_tiltclose, \
    default_stop, Commands, Confirm, NavigationCommand, NordicCommands
from instructor.constants import RB_JOG_1, RB_JOG_2
from instructor.translations import Translations as tr
from server.nordic import Nd

keypad_move_buttons_alt = PvKeypadAlt(
    30,
    open=default_open,
    close=default_close,
    tiltup=default_tiltopen,
    tiltdown=default_tiltclose,
    stop=default_stop,
    cancel=Commands(
        nordic_commands=NordicCommands(Nd.open),
        confirm_command=Confirm(RB_JOG_1, "did it jog")
    ),
    okay=Commands(
        navigation_command=NavigationCommand(1)
    )
)

keypad_move_buttons_alt1 = PvKeypadAlt(
    30,
    open=default_open,
    close=default_close,
    tiltup=default_tiltopen,
    tiltdown=default_tiltclose,
    stop=default_stop,
    cancel=Commands(
        nordic_commands=NordicCommands(Nd.stop),
        confirm_command=Confirm(RB_JOG_1, "did it jog")
    ),
    okay=Commands(
        nordic_commands=NordicCommands(Nd.open),
        confirm_command=Confirm(RB_JOG_2, "did it jog twice")
    )
)

test_blinds1 = Product(
    "tester",
    [
        Step(
            tr.TEST_BLINDS,
            [
                Row(keypad_move_buttons_alt)
            ]),
        Step(
            tr.BLIND_DIRECTION,
            [
                Row(keypad_move_buttons_alt1)
            ])
    ])

test1 = Product("test", [
    test_blinds1
])
