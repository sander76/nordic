from instructor.components import (
    Step,
    Row,
    Spacer,
    Text,
    PvKeypadAlt,
    Commands,
    NordicCommands,
    Confirm,
    default_stop,
    default_tiltclose,
    default_tiltopen,
    NavigationCommand,
)
from instructor.translations import Translations as Tr
from server.nordic import Nd


def start_slat_redefine(
    title=Tr.TITLE_SET_SLAT_POSITION,
    confirm_message=Tr.IS_BLIND_CLOSED,
    introtext=Tr.START_TILT_PROGRAMMING,
):
    return Step(
        title.add_number(1),
        [
            Row(
                Spacer(30),
                Text(30, Tr.PRESS_OKAY_BUTTON.add_number(1)),
                Text(30, introtext.add_number(2)),
            ),
            Row(
                Spacer(30),
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        nordic_commands=NordicCommands(Nd.close),
                        confirm_command=Confirm(None, confirm_message),
                    ),
                ),
                Spacer(30),
            ),
        ],
    )


def enable_slat_redefine():
    return Step(
        title=Tr.TITLE_SET_SLAT_POSITION.add_number(2),
        instructions=[
            Row(
                Text(30, Tr.SLAT_EXPLAIN.add_number(1)),
                Text(30, Tr.PRESS_OKAY_BUTTON.add_number(2)),
            ),
            Row(
                Spacer(30),
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        nordic_commands=NordicCommands(Nd.ENABLE_SLAT),
                        navigation_command=NavigationCommand(1),
                    ),
                ),
            ),
        ],
    )


def redefine_slat():
    return Step(
        title=Tr.TITLE_SET_SLAT_POSITION.add_number(3),
        instructions=[
            Row(Text(30, Tr.SLAT_MOVE_OPPOSITE.add_number(1)),
                Text(30, Tr.SAVE_POSITION.add_number(2))),
            Row(
                PvKeypadAlt(
                    30,
                    stop=default_stop,
                    tiltdown=default_tiltclose,
                    tiltup=default_tiltopen,
                ),
                PvKeypadAlt(
                    30,
                    okay=Commands(
                        nordic_commands=NordicCommands(Nd.SAVE_VENETIAN_SLAT),
                        navigation_command=NavigationCommand(1)
                    )
                ),
            ),
        ],
    )
