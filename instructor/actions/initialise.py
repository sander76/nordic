import instructor.translations as tr
from instructor.components import Row, Text, PvKeypad, Step, Image, Confirm, \
    DelayedCommand, Commands
from instructor.constants import RB_JOG_2, TWIST_JOG_2, VB_JOG_2, DUETTE_JOG_2
from server.nordic import M25S_VENETIAN_16MM, RESET, M25S_DUETTE_FREE, \
    M25S_DUETTE_TENSIONED, ROLLER, TWIST

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

# initialise_rb = Step(tr._initialise,
#                      [textrow,
#                       Row(PvKeypad(30, ['okay'], 'okay', Commands(RESET, DelayedCommand(ROLLER, 4))),
#                           Image(30, "/app/images/m25t_motor_jog2x.png"))
#                       ],
#                      Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

initialise_twist = get_initialise(TWIST_JOG_2)
initialise_twist.instructions[1].col1.okay = Commands(
    RESET, DelayedCommand(TWIST, PRODUCT_SET_DELAY))

# initialise_twist = Step(tr._initialise,
#                         [textrow,
#                          Row(PvKeypad(30, ['okay'], 'okay', Commands(RESET, DelayedCommand(TWIST, 4))),
#                              Image(30, "/app/images/m25t_motor_jog2x.png"))
#                          ],
#                         Confirm('/app/images/m25t_motor_jog2x.png', tr._did_the_motor_jog_two_times))

initialise_vb = get_initialise(VB_JOG_2)
initialise_vb.instructions[1].col1.okay = Commands(RESET, DelayedCommand(
    M25S_VENETIAN_16MM, PRODUCT_SET_DELAY))

# initialise_vb = Step(tr._initialise,
#                      [Row(Text(30, tr._press_okay_button.add_number(1)),
#                           Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
#                       Row(PvKeypad(30, ['okay'], 'okay', Commands(RESET, DelayedCommand(M25S_VENETIAN_16MM, 4))),
#                           Image(30, "/app/images/m25s_vb_motor_jog2x.png"))
#                       ],
#                      Confirm('/app/images/m25s_vb_motor_jog2x.png', tr._did_the_motor_jog_two_times))

initialise_duette = get_initialise(DUETTE_JOG_2)
initialise_duette.instructions[1].col1.okay = Commands(RESET, DelayedCommand(
    M25S_DUETTE_FREE, PRODUCT_SET_DELAY))

# initialise_duette = Step(tr._initialise,
#                          [Row(Text(30, tr._press_okay_button.add_number(1)),
#                               Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
#                           Row(PvKeypad(30, ['okay'], 'okay', Commands(RESET, DelayedCommand(M25S_DUETTE_FREE, 4))),
#                               Image(30, "/app/images/m25s_vb_motor_jog2x.png"))
#                           ],
#                          Confirm('/app/images/m25s_vb_motor_jog2x.png', tr._did_the_motor_jog_two_times))

initialise_duette_tensioned = get_initialise(DUETTE_JOG_2)
initialise_duette_tensioned.instructions[1].col1.okay = Commands(
    RESET,
    DelayedCommand(
        M25S_DUETTE_TENSIONED,
        PRODUCT_SET_DELAY))

# initialise_duette_tensioned = Step(tr._initialise,
#                                    [Row(Text(30, tr._press_okay_button.add_number(1)),
#                                         Text(30, tr._watch_the_blind_jog_two_times.add_number(2))),
#                                     Row(PvKeypad(30, ['okay'], 'okay',
#                                                  Commands(RESET, DelayedCommand(M25S_DUETTE_TENSIONED, 4))),
#                                         Image(30, "/app/images/m25s_vb_motor_jog2x.png"))
#                                     ],
#                                    Confirm('/app/images/m25s_vb_motor_jog2x.png', tr._did_the_motor_jog_two_times))
