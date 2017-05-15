"""
Work in progress.



"""

import json

import os

from instructor.helpers import TXT

# - create a base translation file by serializing below class
# - create new languages based on this file.
# - before instruction generator starts, populate the TXT
#   classes with the language files.
#
AVAILABLE_TRANSLATIONS = [
    'en',
    'nl',
    'de',
    'pl',
    'dk',
    'cz'
]

BASE_FOLDER = "i18n"


class Translations:
    HANGPRODUCT = TXT(
        "HANG PRODUCT.",  # English language.
        "PRODUCT OPHANGEN.",  # Dutch language.
        il=None,  # Israeli language.
        de="Produkt aufhängen",  # German language
        dk=None,  # Danish language
        pl="ZAWIEŚ PRODUKT",  # Polish language
        to_upper=True
    )

    HANG_TWIST = TXT(
        "HANG THE TWIST BLIND",  # English language.
        "HANG DE TWIST BLIND OP",  # Dutch language.
        il=None,
        de="Hängen Sie das Doppelrollo auf",
        dk=None,
        pl="ZAWIEŚ ROLETĘ TWIST",
        to_upper=True)

    HANG_RB = TXT(
        "HANG THE ROLLERBLIND",
        "HANG HET ROLGORDIJN OP",
        il=None,
        de="Hängen Sie das Rollo auf",
        dk=None,
        pl="ZAWIEŚ ROLETĘ",
        to_upper=True)

    CONNECT = TXT(
        "CONNECT.",
        "VERBINDEN.",
        il=None,
        de="VERBINDEN",
        pl="PODŁĄCZ",
        dk=None)

    INITIALISE = TXT(
        "INIT.",
        "INITALISEREN.",
        il=None,
        de="Initialisieren",
        pl="START",
        dk=None)

    ENTER_PROGRAM_MODE = TXT(
        "ENTER PROGRAM MODE.",
        "PROGRAMMEER MODUS.",
        il=None,
        de="Programmiermodus",
        dk=None,
        pl="WEJDŹ W TRYB PROGRAMOWANIA",
        to_upper=True)

    BLIND_DIRECTION = TXT(
        "CHECK BLIND DIRECTION.",
        "CONTROLEER BLIND RICHTING.",
        il=None,
        de="Kontrollieren Sie die Laufrichtung",
        pl="SPRAWDŹ KIERUNEK ZWIJANIA ROLETY",
        dk=None)

    LEFT_MOUNT = TXT(
        "MOTOR ON THE LEFT",
        "MOTOR LINKS",
        pl="MOTOR ZAMONTOWANY LEWA STRONA",
        de="Motor Links"
    )

    IS_LEFT_MOUNT = TXT(
        "Is the motor on the **left** ?",
        "Is de motor **links** gemonteerd ?",
        de="Ist der Motor **links** montiert?",
        pl="Czy motor jest po **lewej** stronie?"
    )

    IS_RIGHT_MOUNT = TXT(
        "Is the motor on the **right** ?",
        "Is de motor **rechts** gemonteerd ?",
        de="Ist der Motor **rechts** montiert?",
        pl="Czy motor jest po **prawej** stronie?"
    )

    IS_VVB_LEFT_STACK = TXT("Is the motor a left stack?")
    IS_VVB_RIGHT_STACK = TXT("Is the motor a right stack?")
    IS_VVB_SPLIT_STACK = TXT("Is the motor a split stack?")

    RIGHT_MOUNT = TXT(
        "MOTOR ON THE RIGHT",
        "MOTOR RECHTS",
        de="MOTOR RECHTS",
        pl="MOTOR ZAMONTOWANY PRAWA STRONA"
    )

    ORIENT_VVB_BACK = TXT(
        "MOTOR ON THE BACK",
        "MOTOR ACHTER",
        de=None,
        pl="MOTOR ZAMONTOWANY TYŁ"
    )

    ORIENT_VVB_UPRIGHT = TXT(
        "MOTOR ABOVE",
        "MOTOR BOVEN",
        de=None,
        pl="MOTOR ZAMONTOWANY GÓRA"
    )

    IS_LEFT_BACKROLLER = TXT(
        "Is the motor on the **left** and **backroller** ?",
        "Is de motor **links** gemonteerd en **backroller** ?",
        il=None,
        de="Ist der Motor **links** montiert hinten abrollend?",
        dk=None,
        pl="Czy jest motor **lewa** strona i **zwijanie normalne**?")

    IS_RIGHT_BACKROLLER = TXT(
        "Is the motor on the **right** and **backroller** ?",
        "Is de motor **rechts** gemonteerd en **backroller** ?",
        il=None,
        de="Ist der Motor **rechts** montiert und hinten abrollend?",
        dk=None,
        pl="Czy jest motor **prawa** strona i **zwijanie normalne**?")

    IS_LEFT_FRONTROLLER = TXT(
        "Is the motor on the **left** and **frontroller** ?",
        "Is de motor **links** gemonteerd en **contrarollend** ?",
        il=None,
        de="Ist der Motor links montiert und vorne abrollend?",
        dk=None,
        pl="Czy jest motor **lewa** strona i **zwijanie odwrotne**?")

    IS_RIGHT_FRONTROLLER = TXT(
        "Is the motor on the **right** and **frontroller** ?",
        "Is de motor **rechts** gemonteerd en **contrarollend** ?",
        il=None,
        de="Ist der Motor rechts montiert und vorne abrollend?",
        dk=None,
        pl="Czy jest motor **prawa** strona i **zwijanie odwrtone**?")

    SWITCH_DIRECTION = TXT(
        "CHANGE BLIND DIRECTION.",
        "WISSEL BLIND RICHTING.",
        il=None,
        de="Laufrichtung ändern",
        dk=None,
        pl="ZMIEŃ KIERUNEK ZWIJANIA"
    )

    IS_BLIND_AT_TOP = TXT(
        "IS THE BLIND AT THE TOP ?",
        "IS DE BLIND HELEMAAL BOVEN ?",
        de="ist die Anlage hochgefahren?",
        pl="CZY PRODUKT JEST W POZYCJI GÓRNEJ ?")

    IS_BLIND_OPENED = TXT(
        "Is the blind at open position ?",
        to_upper=True)

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
        pl="Upewnij sie, że listwa *DOLNA* jest ok 20cm od dołu")

    PROPER_PRODUCT_HANG_CONFIRM = TXT(
        "Product fixed *OK*.",
        "Product is correct opgehangen.",
        il=None,
        de="Produkt is korrekt montiert",
        dk=None,
        pl="Produkt ustawiony *OK*.")

    MAKE_CHOICE = TXT(
        "Make a choice:",
        "Maak een keuze:",
        il=None,
        de="auswählen",
        dk=None,
        pl="Wybierz:")

    SELECT_SKIP_TOP = TXT(
        "I don't want to set the TOP limit",
        "BOVENLIMIET niet opnieuw instellen",
        il=None,
        de="OBERE Endlage nicht einstellen",
        dk=None,
        pl="Nie chcę ustawić górnego limitu")

    SELECT_SKIP_OPEN = TXT("I don't want to set the OPEN limit.")

    SELECT_SKIP_BOTTOM = TXT(
        "I don't want to set the *BOTTOM* limit",
        "*ONDERLIMIET* niet opnieuw instellen",
        il=None,
        de="untere Endlage nicht einstellen",
        dk=None,
        pl="Nie chcę ustawić dolnego limitu")

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
        pl="Ustaw ponownie limit gorny")

    RESET_OPEN = TXT("Re-set the OPEN limit.")
    RESET_CLOSE = TXT("Re-set the CLOSE limit.")

    START_TOP_PROGRAMMING = TXT(
        "The blind will move completely to the top.",
        "De blind zal helemaal naar boven bewegen.",
        de="die Anlage wird ganz nach oben fahren",
        pl="Produkt zwija sie całkowicie")

    START_OPEN_PROGRAMMING = TXT(
        "The blind will move to the open position."
    )

    RESET_BOTTOM = TXT(
        "Re-set the BOTTOM limit.",
        "ONDERLIMIET opnieuw instellen.",
        il=None,
        de="Untere Endlage erneut festlegen",
        dk=None,
        pl="Ustaw ponownie limit dolny")

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
        pl="PRODUKT TESTOWY")

    DID_THE_MOTOR_JOG = TXT(
        "Did the motor jog?",
        "Heeft de motor kort bewogen?",
        il=None,
        de="hat sich der Motor kurz bewegt?",
        dk=None,
        pl="Czy produkt wykonał krótki ruch góra/dól?")

    DID_THE_MOTOR_MOVE_UP = TXT(
        "Did the blind move to the top?",
        "Is de blind naar boven bewogen?",
        il=None,
        de="Ist die Anlage hochgefahren?",
        dk=None,
        pl="Czy produkt sie zwija")

    DID_THE_MOTOR_JOG_TWO_TIMES = TXT(
        "Did the motor jog two times?",
        "Heeft de motor twee keer bewogen?",
        il=None,
        de="Hat sich der Motor zweimal kurz bewegt?",
        dk=None,
        pl="Czy produkt wykonał 2 x  krótki ruch góra/dól?")

    DID_THE_MOTOR_JOG_THREE_TIMES = TXT(
        "Did the motor jog three times?",
        "Heeft de motor drie keer bewogen?",
        il=None,
        de="Hat sich der Motor dreimal kurz bewegt?",
        dk=None,
        pl="Czy produkt wykonał 3 x  krótki ruch góra/dól?")

    DID_MOTOR_MOVE_DOWN = TXT(
        "Did the blind move down?",
        "Is de blind naar beneden bewogen?",
        il=None,
        de="Ist die Anlage runtergefahren?",
        dk=None,
        pl="Czy produkt sie rozwija ?")

    DID_BLIND_CLOSE = TXT(
        "Did the blind close?")

    PRESS_HOLD_BLIND_BUTTON = TXT(
        "`Press` and `hold` the *BLIND BUTTON* .",
        "`Druk` de *BLIND BUTTON*  in en `houd vast`.",
        il=None,
        de="Drücken und halten Sie die Motortaste",
        dk=None,
        pl="Naciśnij i przytrzymaj przycisk na motorze")

    KEEP_PRESSING_AND_OKAY = TXT(
        "Keep pressing the *BLIND BUTTON* and press the OK button.",
        "Blijf de *BLIND BUTTON* indrukken en druk op de OK knop.",
        il=None,
        de="Motortaste gedrückt halten und die OK Taste drücken",
        dk=None,
        pl="Trzymaj przycisk na motorze i jednocześnie naciśnij przycisk OK")

    RELEASE_THE_BLIND_BUTTON = TXT(
        "Release the *BLIND BUTTON*",
        "Laat de *BLIND BUTTON* los.",
        il=None,
        de="Motortaste loslassen",
        dk=None,
        pl="Puść przycisk na motorze")

    PRESS_OKAY_BUTTON = TXT(
        "Press OK button",
        "Druk op de OK knop",
        il=None,
        de="OK Taste drücken",
        dk=None,
        pl="Naciśnij przycisk OK")

    WATCH_THE_BLIND_JOG = TXT(
        "Watch the *BLIND* jog.",
        "Zie de *BLIND* bewegen.",
        il=None,
        de="Gucken Sie, ob die Anlage sich bewegt",
        dk=None,
        pl="Spójrz czy produkt wykonuje ruch góra/dół")

    WATCH_THE_BLIND_MOVE_UP = TXT(
        "Watch the *BLIND* move up.",
        "Zie de *BLIND* naar boven bewegen.",
        il=None,
        de="Gucken Sie, ob die Anlage hochfährt",
        dk=None,
        pl="Spójrz czy produkt sie zwija")

    WATCH_THE_BLIND_JOG_TWO_TIMES = TXT(
        "Motor jogs two times.",
        "Motor beweegt twee keer.",
        il=None,
        de="Motor bewegt sich zweimal kurz",
        dk=None,
        pl="Motor wykonuje 2x ruch góra/dół")

    WATCH_THE_BLIND_JOG_THREE_TIMES = TXT(
        "Motor jogs three times.")

    MOTOR_SHOULD_MOVE_DOWN = TXT(
        "Blind should move down/close.",
        "Blind moet naar beneden bewegen/sluiten.",
        il=None,
        de="Anlage sollte herunterfahren/schließen",
        dk=None,
        pl="Produkt powinien się rozwijać/zamykać"
    )

    MOVE_BLIND_CLOSE = TXT("Move the *BLIND* to the desired CLOSE position")

    MOVE_BLIND_BOTTOM = TXT(
        "Move the *BLIND* to the desired BOTTOM position.",
        "Stuur de *BLIND* naar de gewenste ONDER positie.",
        il=None,
        de="Bewegen Sie die Anlage auf die gewünschte untere Endlage",
        dk=None,
        pl="Produkt rozwija sie do pożądanej pozycji dolnej")

    MOVE_BLIND_TOP = TXT(
        "Move the *BLIND* to the desired TOP position.",
        "Stuur de *BLIND* naar de gewenste BOVEN positie.",
        il=None,
        de="Bewegen Sie die Anlage in die gewünschte obere Endlage",
        dk=None,
        pl="Produkt zwija sie do pożądanej pozycji górnej")

    MOVE_BLIND_OPEN = TXT(
        "Move the *BLIND* to the desired OPEN position"
    )

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
        dk="Sprawdź limit górny i dolny")

    SAVE_BOTTOM = TXT(
        "Save this as BOTTOM limit.",
        "Stel in als ONDER positie.",
        il=None,
        de="Speichern als untere Endlage",
        dk=None,
        pl="Zapisz dolną pozycję")

    SAVE_CLOSE = TXT("Save this as CLOSE position.")

    SAVE_TOP = TXT(
        "Save this as TOP limit.",
        "Stel in als BOVEN positie.",
        il=None,
        de="Speichern als OBERE Endlage",
        dk=None,
        pl="Sprawdź górną pozycję")

    SAVE_OPEN = TXT(
        "Save this as OPEN limit."
    )

    SAVE_THIS_AS_TOP = TXT(
        "Save this as the TOP limit?",
        "Deze positie als BOVEN limiet instellen?",
        de="Diese Position als OBERE Endlage einstellen?",
        pl="Czy zatwierdzić pozycję górna?")

    SAVE_THIS_AS_OPEN = TXT(
        "Save this an the OPEN limit?"
    )

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
        pl="Limity są poprawne. Przejdź do nowego produktu")

    LIMITS_NOT_OK = TXT(
        "Limits are NOT OK. Re-set them",
        "Limieten zijn NIET OK. Opnieuw instellen.",
        il=None,
        de="Endlagen sind NICHT OK. Erneut einstellen",
        dk=None,
        pl="Limity są niepoprawne. Ustaw ponownie")

    YES = TXT(
        "yes",
        "ja")

    NO = TXT(
        "no",
        "nee")

    TITLE_VVB_SET_CLOSE_LIMIT = TXT(
        "Set the close limit",
        "Sluit-limiet instellen",
        to_upper=True)

    TITLE_VVB_SET_OPEN_LIMIT = TXT(
        "Set the open limit",
        "Open limit instellen",
        to_upper=True
    )

    TITLE_SKIP_OPEN = TXT(
        "Set the open limit ?",
        "Open limit instellen ?",
        to_upper=True
    )

    TITLE_SKIP_CLOSE = TXT("Set the close limit ?")

    TITLE_SKIP_TOP = TXT(
        "SET *TOP* LIMIT?",
        "STEL *BOVENLIMIET* IN?",
        to_upper=True)

    TITLE_SKIP_BOTTOM = TXT(
        "SET *BOTTOM* LIMIT?",
        "STEL *ONDERLIMIET* IN?",
        to_upper=True)

    TITLE_SKIP_SLAT = TXT(
        "SET SLAT POSITION?",
        "STEL SLAT POSITIE IN?",
        to_upper=True)

    TITLE_ORIENT_VVB_BACK = TXT(
        "Is the motor mounted on the **back** ?",
        "Is the motor **achter** gemonteerd ?",
        to_upper=True)

    TITLE_ORIENT_VVB_UPRIGHT = TXT(
        "Is the motor mounted **above** ?",
        "Is de motor **boven** gemonteerd ?",
        to_upper=True)

    TITLE_BACKROLLER_LEFT = TXT(
        "LEFT BACKROLLER", "LINKS BACKROLLER",
        to_upper=True)

    TITLE_BACKROLLER_RIGHT = TXT(
        "RIGHT BACKROLLER",
        "RECHTS BACKROLLER",
        to_upper=True)

    TITLE_FRONTROLLER_LEFT = TXT(
        "LEFT FRONTROLLER",
        "LINKS FRONTROLLER",
        to_upper=True)

    TITLE_FRONTROLLER_RIGHT = TXT(
        "RIGHT FRONTROLLER", "RECHTS FRONTROLLER", to_upper=True)

    TITLE_SET_BOTTOM_LIMIT = TXT(
        "SET BOTTOM LIMIT.",
        "STEL ONDERLIMIET IN.",
        to_upper=True)

    TITLE_SET_TOP_LIMIT = TXT(
        "SET TOP LIMIT.",
        "STEL BOVENLIMIET IN.",
        to_upper=True)

    TITLE_VVB = TXT(
        "VVB title",
        "VVB titel")

    TITLE_MOTOR_CHECK_CLOSE = TXT(
        "CHECK CLOSE DIRECTION",
        "Sluit richting",
        to_upper=True)


def do_text(lang):
    def wrapper(o):
        if isinstance(o, TXT):
            txt = o.get_plain_text(lang)
            return {
                "ref_en": o.get_plain_text('en'),
                lang: txt}

        elif o is Translations:
            _dct = {key: value for key, value in vars(o).items() if
                    not key.startswith('_')}

            return _dct
            # return dict(o.__dict__)
        else:
            return

    return wrapper


def _get_translation_file_path(lang):
    fname = "powerview_instructions_{}.json".format(lang)
    full_name = os.path.join(BASE_FOLDER, fname)
    return full_name


def load_translations():
    """
    Loads all available json translation files and populates the Translations
     class. This function is called before creation of instructions is
     initiated.
    """
    for lang in AVAILABLE_TRANSLATIONS:
        full_name = _get_translation_file_path(lang)

        with open(full_name, 'r', encoding='utf-8')as _fl:
            _js = json.load(_fl)
        for key, value in _js.items():
            _txt = getattr(Translations, key)
            if isinstance(_txt, TXT):
                setattr(_txt, lang, value[lang])


def _open_current_translation(json_file):
    try:
        with open(json_file, 'r') as _fl:
            _js = json.load(_fl)
            return _js
    except (FileExistsError, FileNotFoundError) as e:
        return {}


def export_translations():
    """
    Loads the current json files with tranlations.
    It then checks the current Translation class for
    new entries and puts them in the above json file.
    """

    for lang in AVAILABLE_TRANSLATIONS:
        full_name = _get_translation_file_path(lang)

        # open the current file:
        _org_json = _open_current_translation(full_name)

        for key, value in Translations.__dict__.items():
            if not key.startswith("_"):
                if key not in _org_json:
                    try:
                        _val = getattr(value, lang)
                    except AttributeError as e:
                        print(e)
                    else:
                        _val = _val if _val else ""
                        _org_json[key] = {"ref_en": value.en,
                                          lang: _val}

        with open(full_name, 'w', encoding="utf-8") as _fl:
            json.dump(_org_json, _fl, ensure_ascii=False,
                      indent=4)


if __name__ == "__main__":
    export_translations()
    # load_translations()
