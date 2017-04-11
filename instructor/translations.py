from instructor.helpers import TXT

HANGPRODUCT = TXT(
    "HANG PRODUCT.",  # English language.
    "PRODUCT OPHANGEN.",  # Dutch language.
    il=None,  # Israeli language.
    de="Produkt aufhängen",  # German language
    dk=None,  # Danish language
    pl=None,  # Polish language
    to_upper=True
)

HANG_TWIST = TXT(
    "HANG THE TWIST BLIND",  # English language.
    "HANG DE TWIST BLIND OP",  # Dutch language.
    il=None,
    de="Hängen Sie das Doppelrollo auf",
    dk=None,
    pl=None,
    to_upper=True)

HANG_RB = TXT(
    "HANG THE ROLLERBLIND",
    "HANG HET ROLGORDIJN OP",
    il=None,
    de="Hängen Sie das Rollo auf",
    dk=None,
    pl=None,
    to_upper=True)

CONNECT = TXT(
    "CONNECT.",
    "VERBINDEN.",
    il=None,
    de="VERBINDEN",
    pl=None,
    dk=None)

INITIALISE = TXT(
    "INIT.",
    "INITALISEREN.",
    il=None,
    de="Initialisieren",
    pl=None,
    dk=None)

ENTER_PROGRAM_MODE = TXT(
    "ENTER PROGRAM MODE.",
    "PROGRAMMEER MODUS.",
    il=None,
    de="Programmiermodus",
    dk=None,
    pl=None,
    to_upper=True)

BLIND_DIRECTION = TXT(
    "CHECK BLIND DIRECTION.",
    "CONTROLEER BLIND RICHTING.",
    il=None,
    de="Kontrollieren Sie die Laufrichtung",
    pl=None,
    dk=None)

LEFT_MOUNT = TXT(
    "MOTOR ON THE LEFT",
    "MOTOR LINKS",
    pl=None,
    de="Motor Links")

IS_LEFT_MOUNT = TXT(
    "Is the motor on the **left** ?",
    "Is de motor **links** gemonteerd ?",
    de="Ist der Motor **links** montiert?",
    pl=None, )

IS_RIGHT_MOUNT = TXT(
    "Is the motor on the **right** ?",
    "Is de motor **rechts** gemonteerd ?",
    de="Ist der Motor **rechts** montiert?",
    pl=None, )

RIGHT_MOUNT = TXT(
    "MOTOR ON THE RIGHT",
    "MOTOR RECHTS",
    de="MOTOR RECHTS",
    pl=None)

ORIENT_VVB_BACK = TXT(
    "MOTOR ON THE BACK",
    "MOTOR ACHTER",
    de=None,
    pl=None
)
ORIENT_VVB_UPRIGHT = TXT(
    "MOTOR ABOVE",
    "MOTOR BOVEN",
    de=None,
    pl=None
)

IS_LEFT_BACKROLLER = TXT(
    "Is the motor on the **left** and **backroller** ?",
    "Is de motor **links** gemonteerd en **backroller** ?",
    il=None,
    de="Ist der Motor **links** montiert hinten abrollend?",
    dk=None,
    pl=None)

IS_RIGHT_BACKROLLER = TXT(
    "Is the motor on the **right** and **backroller** ?",
    "Is de motor **rechts** gemonteerd en **backroller** ?",
    il=None,
    de="Ist der Motor **rechts** montiert und hinten abrollend?",
    dk=None,
    pl=None)

IS_LEFT_FRONTROLLER = TXT(
    "Is the motor on the **left** and **frontroller** ?",
    "Is de motor **links** gemonteerd en **contrarollend** ?",
    il=None,
    de="Ist der Motor links montiert und vorne abrollend?",
    dk=None,
    pl=None)

IS_RIGHT_FRONTROLLER = TXT(
    "Is the motor on the **right** and **frontroller** ?",
    "Is de motor **rechts** gemonteerd en **contrarollend** ?",
    il=None,
    de="Ist der Motor rechts montiert und vorne abrollend?",
    dk=None,
    pl=None)

SWITCH_DIRECTION = TXT(
    "CHANGE BLIND DIRECTION.",
    "WISSEL BLIND RICHTING.",
    il=None,
    de="Laufrichtung ändern",
    dk=None,
    pl=None)

IS_BLIND_AT_TOP = TXT(
    "IS THE BLIND AT THE TOP ?",
    "IS DE BLIND HELEMAAL BOVEN ?",
    de="ist die Anlage hochgefahren?",
    pl=None)

SET_TWIST_SLAT_POSITION = TXT(
    "SET TWIST SLAT POSITION.",
    "STEL TWIST SLAT POSITIE IN.",
    il=None,
    de="einstellen der Lamellenposition des Doppelrollos",
    dk=None,
    pl=None)

PROPER_PRODUCT_HANG = TXT(
    "Make sure *BOTTOM* bar is approximately 20cm down.",
    "Zorg dat de *ONDERLAT* ongeveer 20cm gezakt is.", il=None,
    de="sicherstellen, dass die Unterschiene ungefähr 20cm unten ist",
    dk=None,
    pl=None)

PROPER_PRODUCT_HANG_CONFIRM = TXT(
    "Product fixed *OK*.",
    "Product is correct opgehangen.",
    il=None,
    de="Produkt is korrekt montiert",
    dk=None,
    pl=None)

MAKE_CHOICE = TXT(
    "Make a choice:",
    "Maak een keuze:",
    il=None,
    de="auswählen",
    dk=None,
    pl=None)

SELECT_SKIP_TOP = TXT(
    "I don't want to set the TOP limit",
    "BOVENLIMIET niet opnieuw instellen",
    il=None,
    de="OBERE Endlage nicht einstellen",
    dk=None,
    pl=None)

SELECT_SKIP_BOTTOM = TXT(
    "I don't want to set the *BOTTOM* limit",
    "*ONDERLIMIET* niet opnieuw instellen",
    il=None,
    de="untere Endlage nicht einstellen",
    dk=None,
    pl=None)

SELECT_SKIP_SLAT = TXT(
    "Don't re-set the *SLAT* position.",
    "*SLAT OPEN* positie niet opnieuw instellen.",
    il=None,
    de="Lamellenposition nicht erneut festlegen",
    dk=None,
    pl=None)

RESET_TOP = TXT(
    "Re-set the TOP limit.",
    "BOVENLIMIET opnieuw instellen.",
    il=None,
    de="OBERE Endlage erneut festlegen",
    dk=None,
    pl=None)

START_TOP_PROGRAMMING = TXT(
    "The blind will move completely to the top.",
    "De blind zal helemaal naar boven bewegen.",
    de="die Anlage wird ganz nach oben fahren",
    pl=None)

RESET_BOTTOM = TXT(
    "Re-set the BOTTOM limit.",
    "ONDERLIMIET opnieuw instellen.",
    il=None,
    de="Untere Endlage erneut festlegen",
    dk=None,
    pl=None)

RESET_SLAT = TXT(
    "Re-set the SLAT position",
    "SLAT positie opnieuw instellen.",
    il=None,
    de="Lamellenposition erneut festlegen",
    dk=None,
    pl=None)

TEST_BLINDS = TXT(
    "TEST BLINDS",
    "TEST BLINDS",
    il=None,
    de="Anlagentest",
    dk=None,
    pl=None)

DID_THE_MOTOR_JOG = TXT(
    "Did the motor jog?",
    "Heeft de motor kort bewogen?",
    il=None,
    de="hat sich der Motor kurz bewegt?",
    dk=None,
    pl=None)

DID_THE_MOTOR_MOVE_UP = TXT(
    "Did the blind move to the top?",
    "Is de blind naar boven bewogen?",
    il=None,
    de="Ist die Anlage hochgefahren?",
    dk=None,
    pl=None)

DID_THE_MOTOR_JOG_TWO_TIMES = TXT(
    "Did the motor jog two times?",
    "Heeft de motor twee keer bewogen?",
    il=None,
    de="Hat sich der Motor zweimal kurz bewegt?",
    dk=None,
    pl=None)

DID_MOTOR_MOVE_DOWN = TXT(
    "Did the blind move down?",
    "Is de blind naar beneden bewogen?",
    il=None,
    de="Ist die Anlage runtergefahren?",
    dk=None,
    pl=None)

PRESS_HOLD_BLIND_BUTTON = TXT(
    "`Press` and `hold` the *BLIND BUTTON* .",
    "`Druk` de *BLIND BUTTON*  in en `houd vast`.",
    il=None,
    de="Drücken und halten Sie die Motortaste",
    dk=None,
    pl=None)

KEEP_PRESSING_AND_OKAY = TXT(
    "Keep pressing the *BLIND BUTTON* and press the OK button.",
    "Blijf de *BLIND BUTTON* indrukken en druk op de OK knop.",
    il=None,
    de="Motortaste gedrückt halten und die OK Taste drücken",
    dk=None,
    pl=None)

RELEASE_THE_BLIND_BUTTON = TXT(
    "Release the *BLIND BUTTON*",
    "Laat de *BLIND BUTTON* los.",
    il=None,
    de="Motortaste loslassen",
    dk=None,
    pl=None)

PRESS_OKAY_BUTTON = TXT(
    "Press OK button",
    "Druk op de OK knop",
    il=None,
    de="OK Taste drücken",
    dk=None,
    pl=None)

WATCH_THE_BLIND_JOG = TXT(
    "Watch the *BLIND* jog.",
    "Zie de *BLIND* bewegen.",
    il=None,
    de="Gucken Sie, ob die Anlage sich bewegt",
    dk=None,
    pl=None)

WATCH_THE_BLIND_MOVE_UP = TXT(
    "Watch the *BLIND* move up.",
    "Zie de *BLIND* naar boven bewegen.",
    il=None,
    de="Gucken Sie, ob die Anlage hochfährt",
    dk=None,
    pl=None)

WATCH_THE_BLIND_JOG_TWO_TIMES = TXT(
    "Motor jogs two times.",
    "Motor beweegt twee keer.",
    il=None,
    de="Motor bewegt sich zweimal kurz",
    dk=None,
    pl=None)

MOTOR_SHOULD_MOVE_DOWN = TXT(
    "Blind should move down/close.",
    "Blind moet naar beneden bewegen/sluiten.",
    il=None,
    de="Anlage sollte herunterfahren/schließen",
    dk=None,
    pl=None
)

MOVE_BLIND_BOTTOM = TXT(
    "Move the *BLIND* to the desired BOTTOM position.",
    "Stuur de *BLIND* naar de gewenste ONDER positie.",
    il=None,
    de="Bewegen Sie die Anlage auf die gewünschte untere Endlage",
    dk=None,
    pl=None)

MOVE_BLIND_TOP = TXT(
    "Move the *BLIND* to the desired TOP position.",
    "Stuur de *BLIND* naar de gewenste BOVEN positie.",
    il=None,
    de="Bewegen Sie die Anlage in die gewünschte obere Endlage",
    dk=None,
    pl=None)

MOVE_BLIND_SLAT_OPEN = TXT(
    "Move the *BLIND* to the desired SLAT OPEN position.",
    "Stuur de *BLIND* naar de gewenste SLAT OPEN positie.",
    il=None,
    de="Bewegen Sie die Lamellen in die gewünschte Position",
    dk=None,
    pl=None)

TEST_MOVE_BLINDS = TXT(
    "Check TOP and BOTTOM limits.",
    "Controleer BOVEN en ONDER limiet.",
    il=None,
    de="Kontrollieren Sie obere und untere Endlage",
    dk=None)

SAVE_BOTTOM = TXT(
    "Save this as BOTTOM limit.",
    "Stel in als ONDER positie.",
    il=None,
    de="Speichern als untere Endlage",
    dk=None,
    pl=None)

SAVE_TOP = TXT(
    "Save this as TOP limit.",
    "Stel in als BOVEN positie.",
    il=None,
    de="Speichern als OBERE Endlage",
    dk=None,
    pl=None)

SAVE_THIS_AS_TOP = TXT(
    "Save this as the TOP limit?",
    "Deze positie als BOVEN limiet instellen?",
    de="Diese Position als OBERE Endlage einstellen?",
    pl=None)

SAVE_SLAT = TXT(
    "Save this as SLAT OPEN position.",
    "Stel in als SLAT OPEN positie.",
    il=None,
    de="Diese Lamellenposition als OFFEN sichern",
    dk=None,
    pl=None)

LIMITS_OK = TXT(
    "Limits are OK. Do a new blind.",
    "Limieten zijn OK. Nieuwe *BLIND* inprogrammeren.",
    il=None,
    de="Endlagen sind OK. Neue Anlage programmieren",
    dk=None,
    pl=None)

LIMITS_NOT_OK = TXT(
    "Limits are NOT OK. Re-set them",
    "Limieten zijn NIET OK. Opnieuw instellen.",
    il=None,
    de="Endlagen sind NICHT OK. Erneut einstellen",
    dk=None,
    pl=None)

YES = TXT(
    "yes",
    "ja",
    il=None,
    de="ja",
    dk=None,
    pl=None)

NO = TXT(
    "no",
    "nee",
    il=None,
    de="nein",
    dk=None,
    pl=None)

TITLE_VVB_SET_CLOSE_LIMIT = TXT(
    "Set the close limit",
    "Sluit-limiet instellen",
    de=None,
    pl=None,
    to_upper=True)

TITLE_VVB_SET_OPEN_LIMIT = TXT(
    "Set the open limit",
    "Open limit instellen",
    de=None,
    pl=None,
    to_upper=True
)

TITLE_SKIP_TOP = TXT(
    "SET *TOP* LIMIT?",
    "STEL *BOVENLIMIET* IN?",
    il=None,
    de="Obere Endlage einstellen?",
    dk=None,
    pl=None,
    to_upper=True)

TITLE_SKIP_BOTTOM = TXT(
    "SET *BOTTOM* LIMIT?",
    "STEL *ONDERLIMIET* IN?",
    il=None,
    de="*Untere* Endlage einstellen?",
    dk=None,
    pl=None,
    to_upper=True)

TITLE_SKIP_SLAT = TXT(
    "SET SLAT POSITION?",
    "STEL SLAT POSITIE IN?",
    il=None,
    de="Lamellenposition einstellen?",
    dk=None,
    pl=None,
    to_upper=True)

TITLE_ORIENT_VVB_BACK = TXT(
    "Is the motor mounted on the **back** ?",
    "Is the motor **achter** gemonteerd ?",
    de=None,
    pl=None,
    to_upper=True)

TITLE_ORIENT_VVB_UPRIGHT = TXT(
    "Is the motor mounted **above** ?",
    "Is de motor **boven** gemonteerd ?",
    de=None,
    pl=None,
    to_upper=True)

TITLE_BACKROLLER_LEFT = TXT(
    "LEFT BACKROLLER", "LINKS BACKROLLER",
    il=None,
    de="links, hinten abrollend",
    dk=None,
    pl=None,
    to_upper=True)

TITLE_BACKROLLER_RIGHT = TXT(
    "RIGHT BACKROLLER",
    "RECHTS BACKROLLER",
    il=None,
    de="Rechts, vorne abrollend",
    dk=None,
    pl=None,
    to_upper=True)

TITLE_FRONTROLLER_LEFT = TXT(
    "LEFT FRONTROLLER",
    "LINKS FRONTROLLER",
    il=None,
    de="links, vorne abrollend",
    dk=None,
    pl=None,
    to_upper=True)

TITLE_FRONTROLLER_RIGHT = TXT(
    "RIGHT FRONTROLLER", "RECHTS FRONTROLLER",
    il=None,
    de="rechts, vorne abrollend",
    dk=None,
    pl=None,
    to_upper=True)

TITLE_SET_BOTTOM_LIMIT = TXT(
    "SET BOTTOM LIMIT.",
    "STEL ONDERLIMIET IN.",
    il=None,
    de="Untere Endlageneinstellung",
    dk=None,
    pl=None,
    to_upper=True)

TITLE_SET_TOP_LIMIT = TXT(
    "SET TOP LIMIT.",
    "STEL BOVENLIMIET IN.",
    il=None,
    de="obere Endlageneinstellung",
    dk=None,
    pl=None,
    to_upper=True)
