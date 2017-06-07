# import instructor.translations as tr
from instructor.translations import Translations as Tr
from instructor.components import Row, Text, Step, Image, Confirm, \
    DelayedCommand, NordicCommands, PvKeypadAlt, Commands
from instructor.constants import RB_JOG_2, TWIST_JOG_2, VB_JOG_2, \
    DUETTE_JOG_2, VVB_JOG_1, PLEATED_JOG_2, DUETTE_JOG_3, PRODUCT_SET_DELAY
from server.nordic import Nd

textrow = Row(Text(30, Tr.PRESS_OKAY_BUTTON.add_number(1)),
              Text(30, Tr.WATCH_THE_BLIND_JOG_TWO_TIMES.add_number(2)))


def get_initialise(jog_image, product_command=Nd.M25T_ROLLER):
    return Step(
        Tr.INITIALISE,
        [textrow,
         Row(
             PvKeypadAlt(
                 30,
                 okay=Commands(
                     nordic_commands=NordicCommands(
                         Nd.RESET,
                         DelayedCommand(product_command, PRODUCT_SET_DELAY)),
                     confirm_command=Confirm(
                         jog_image, Tr.DID_THE_MOTOR_JOG_TWO_TIMES))),
             Image(30, jog_image))
         ]
    )


initialise_rb = get_initialise(RB_JOG_2, Nd.M25T_ROLLER)
# initialise_rb.instructions[1].col1.okay = NordicCommands(
#     Nd.RESET, DelayedCommand(Nd.M25T_ROLLER, PRODUCT_SET_DELAY))

initialise_twist = get_initialise(TWIST_JOG_2, Nd.TWIST)
# initialise_twist.instructions[1].col1.okay = NordicCommands(
#     Nd.RESET, DelayedCommand(Nd.TWIST, PRODUCT_SET_DELAY))

initialise_vb_16 = get_initialise(VB_JOG_2, Nd.M25S_VENETIAN_16MM)

initialise_vb_25 = get_initialise(VB_JOG_2, Nd.M25S_VENETIAN_25MM)

initialise_duette = get_initialise(
    DUETTE_JOG_2, Nd.M25S_DUETTE_FREE)

initialise_duette_tensioned = get_initialise(
    DUETTE_JOG_2, Nd.M25S_DUETTE_TENSIONED)

# initialization including motor position on the right.
initialise_duette_tensioned_alt = Step(
    Tr.INITIALISE,
    [Row(Text(30, Tr.PRESS_OKAY_BUTTON.add_number(1)),
         Text(30, Tr.WATCH_THE_BLIND_JOG_THREE_TIMES.add_number(2))),
     Row(PvKeypadAlt(
         30,
         okay=Commands(
             nordic_commands=NordicCommands(
                 Nd.RESET,
                 DelayedCommand(Nd.M25S_DUETTE_TENSIONED, PRODUCT_SET_DELAY),
                 DelayedCommand(Nd.ORIENT_M25S_DUETTE_RIGHT,
                                PRODUCT_SET_DELAY)),
             confirm_command=Confirm(
                 DUETTE_JOG_3, Tr.DID_THE_MOTOR_JOG_THREE_TIMES)

         )),
         Image(30, DUETTE_JOG_3))]
)

initialise_pleated = get_initialise(
    PLEATED_JOG_2, Nd.M25S_PLEATED_FREE)

initialise_pleated_tensioned = get_initialise(
    PLEATED_JOG_2, Nd.M25S_PLEATED_TENSIONED)

initialise_vvb_right = get_initialise(
    VVB_JOG_1, Nd.M25S_VVB_RIGHT_STACK)

initialise_vvb_left = get_initialise(
    VVB_JOG_1, Nd.M25S_VVB_LEFT_STACK)

initialise_vvb_center = get_initialise(
    VVB_JOG_1, Nd.M25S_VVB_CENTER_STACK)

initialise_vvb_split = get_initialise(
    VVB_JOG_1, Nd.M25S_VVB_SPLIT_STACK)
