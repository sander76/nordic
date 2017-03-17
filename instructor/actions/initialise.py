import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands
from instructor.constants import RB_JOG_2, TWIST_JOG_2, VB_JOG_2, DUETTE_JOG_2, \
    VVB_JOG_2
from server.nordic import M25S_VENETIAN_16MM, RESET, M25S_DUETTE_FREE, \
    M25S_DUETTE_TENSIONED, ROLLER, TWIST, M25S_VENETIAN_25MM

textrow = Row(Text(30, tr.PRESS_OKAY_BUTTON.add_number(1)),
              Text(30, tr.WATCH_THE_BLIND_JOG_TWO_TIMES.add_number(2)))

PRODUCT_SET_DELAY = 6


def get_initialise(jog_image):
    return Step(tr.INITIALISE,
                [textrow,
                 Row(PvKeypad(30, ['okay'], 'okay',
                              Commands(RESET,
                                       DelayedCommand(ROLLER,
                                                      PRODUCT_SET_DELAY))),
                     Image(30, jog_image))
                 ],
                Confirm(jog_image, tr.DID_THE_MOTOR_JOG_TWO_TIMES))


initialise_rb = get_initialise(RB_JOG_2)
initialise_rb.instructions[1].col1.okay = Commands(
    RESET, DelayedCommand(ROLLER, PRODUCT_SET_DELAY))

initialise_twist = get_initialise(TWIST_JOG_2)
initialise_twist.instructions[1].col1.okay = Commands(
    RESET, DelayedCommand(TWIST, PRODUCT_SET_DELAY))

initialise_vb_16 = get_initialise(VB_JOG_2)
initialise_vb_16.instructions[1].col1.okay = Commands(RESET, DelayedCommand(
    M25S_VENETIAN_16MM, PRODUCT_SET_DELAY))

initialise_vb_25 = get_initialise(VB_JOG_2)
initialise_vb_25.instructions[1].col1.okay = Commands(RESET, DelayedCommand(
    M25S_VENETIAN_25MM, PRODUCT_SET_DELAY))


initialise_duette = get_initialise(DUETTE_JOG_2)
initialise_duette.instructions[1].col1.okay = Commands(RESET, DelayedCommand(
    M25S_DUETTE_FREE, PRODUCT_SET_DELAY))

initialise_duette_tensioned = get_initialise(DUETTE_JOG_2)
initialise_duette_tensioned.instructions[1].col1.okay = Commands(
    RESET,
    DelayedCommand(
        M25S_DUETTE_TENSIONED,
        PRODUCT_SET_DELAY))

