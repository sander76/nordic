import json

from instructor.constants import DEFAULT_DELAY
from instructor.translations import Translations as Tr
# import instructor.translations as tr
from instructor.helpers import TXT, NumberedText
# from server.nordic import COMMANDS
import server.nordic
from server.nordic import Nd

COMMANDS = server.nordic.__dict__


class NavigationCommand:
    def __init__(self, goto):
        self.goto = goto


class NextPrevious(NavigationCommand):
    def __init__(self, button_text, goto, active):
        NavigationCommand.__init__(self, goto)
        self.caption = button_text
        self.active = active


class Next(NextPrevious):
    def __init__(self, button_text="next", goto=1, active=True):
        NextPrevious.__init__(self, button_text, goto, active)


class Previous(NextPrevious):
    def __init__(self, button_text="previous", goto=-1, active=True):
        NextPrevious.__init__(self, button_text, goto, active)


class DelayedCommand:
    def __init__(self, command, delay=DEFAULT_DELAY):
        if not isinstance(command, Nd):
            raise UserWarning("Command is not correct")
        self.command = command.name
        self.delay = delay


class ToJson(json.JSONEncoder):
    def __init__(self, lang='en'):
        json.JSONEncoder.__init__(self, sort_keys=True, ensure_ascii=False)
        self.lang = lang

    def default(self, o):
        if isinstance(o, TXT) or isinstance(o, NumberedText):
            return o.get_text(self.lang)
            # return getattr(o, self.lang)
        else:
            return o.__dict__


class Instruction:
    def __init__(self, version):
        self.version = version
        self.products = []

    def create_file(self, language):
        return json


'''
product = {'type': 'dict',
           'schema': {'title': {'type': 'string', 'required': True},
                      'steps': {'type': 'list', 'schema': step}}}
'''


class Product:
    def __init__(self, title, steps):
        self.title = title,
        self.steps = steps


class Step:
    title = None
    instructions = None

    def __init__(self, title, instructions, nav_next=Next(),
                 nav_previous=Previous(), nav_id=None):
        """
        :type instructions: list[Row]
        """
        for instruction in instructions:
            if not isinstance(instruction, Row):
                raise UserWarning("instruction is not of type Row.")
        self.title = title
        self.instructions = instructions

        self.next = nav_next
        self.previous = nav_previous
        self.id = nav_id


class UiElement:
    def __init__(self, width):
        if isinstance(width, int):
            self.width = str(width) + '%'
        else:
            raise UserWarning("not an integer : {}".format(width))


class Confirm:
    def __init__(self, img, text, yes_text=Tr.YES, no_text=Tr.NO,
                 yes: NavigationCommand = NavigationCommand(1),
                 no: NavigationCommand = NavigationCommand(0)):
        self.img = img
        self.text = text
        self.yes = yes
        self.no = no
        self.yes_text = yes_text
        self.no_text = no_text


class NordicCommands:
    def __init__(self, first_command: Nd, *next_commands):
        if not isinstance(first_command, Nd):
            raise UserWarning("Command is not correct.")
        self.commands = [first_command.name] + [cmd for cmd in
                                                next_commands]


class Commands:
    def __init__(self,
                 nordic_commands=None,
                 confirm_command=None,
                 navigation_command=None):
        if ((nordic_commands is None or isinstance(nordic_commands,
                                                   NordicCommands))
            and
                (confirm_command is None or isinstance(confirm_command,
                                                       Confirm))
            and
                (navigation_command is None or isinstance(navigation_command,
                                                          NavigationCommand))):
            # typing is ok. continue.

            self.nordic_commands = nordic_commands
            self.confirm_command = confirm_command
            self.navigation_command = navigation_command
        else:
            raise Exception("command parameters are not correct.")


class Spacer(UiElement):
    def __init__(self, width):
        UiElement.__init__(self, width)


default_open = Commands(
    NordicCommands(Nd.open)
)
default_close = Commands(
    NordicCommands(Nd.close)
)
default_stop = Commands(
    NordicCommands(Nd.stop)
)
default_tiltopen = Commands(
    NordicCommands(Nd.tiltopen)
)
default_tiltclose = Commands(
    NordicCommands(Nd.tiltclose)
)


class PvKeypadAlt(UiElement):
    def __init__(self,
                 width,
                 open=None,
                 close=None,
                 stop=None,
                 tiltup=None,
                 tiltdown=None,
                 cancel=None,
                 okay=None):
        UiElement.__init__(self, width)
        self.type = 'pv-keypad-alt'
        self.open = open
        self.close = close
        self.stop = stop
        self.tiltup = tiltup
        self.tiltdown = tiltdown
        self.cancel = cancel
        self.okay = okay


class PvKeypad(UiElement):
    allowed = ['open', 'close', 'tiltup', 'tiltdown', 'stop', 'okay', 'cancel']
    open = 'open'
    close = 'close'
    cancel = 'cancel'
    okay = 'okay'
    stop = 'stop'
    tiltup = 'tiltup'
    tiltdown = 'tiltdown'

    def __init__(self, width, active_buttons, confirm=None, okay=None,
                 cancel=None):
        """
        :param width: defines the width in percentage of the element.
        :param active_buttons: which buttons to activate
        :param confirm: which button will have an "open confirm dialog"
        method to it.
        :param okay: what actions should be taken when ok is clicked.
        :param cancel: where should cancel take you ?
        """
        UiElement.__init__(self, width)
        self.type = 'pv-keypad'
        self.active_buttons = active_buttons
        for button in active_buttons:
            if button not in PvKeypad.allowed:
                raise UserWarning(
                    "'{}' not allowed as pvkeypad button".format(button))
        if confirm is not None:
            if confirm not in active_buttons:
                raise UserWarning(
                    "'{}' not allowed as it is not an active button".format(
                        confirm))
            self.confirm = confirm
        if okay is not None:
            if 'okay' not in PvKeypad.allowed:
                raise UserWarning(
                    "'okay' defined but not defined as an active button.")
            self.okay = okay
        if cancel is not None:
            if 'cancel' not in PvKeypad.allowed:
                raise UserWarning(
                    "'cancel' defined but not defined as an active button.")
            self.cancel = cancel


'''
text = {'width': {'type': 'string', 'regex': '\d{1,2}%'},
        'type': {'type': 'string', 'required': True, 'allowed': ['text']},
        'content': {'type': 'string', 'required': True}}

'''


class Text(UiElement):
    def __init__(self, width_percentage, content):
        UiElement.__init__(self, width_percentage)
        self.type = 'text'
        self.content = content


'''
image = {'width': {'type': 'string', 'regex': '\d{1,2}%'},
         'type': {'type': 'string', 'required': True, 'allowed': ['image']},
         'src': {'type': 'string', 'required': True}}
'''


class Image(UiElement):
    def __init__(self, width, src):
        UiElement.__init__(self, width)
        self.type = "image"
        self.src = src


class Row:
    allowed = [PvKeypadAlt, PvKeypad, Text, Image, Spacer]

    def __init__(self, col1, col2=None, col3=None, col4=None):
        self._check(col1)
        self.col1 = col1
        if col2 is not None:
            self._check(col2)
            self.col2 = col2
        if col3 is not None:
            self._check(col3)
            self.col3 = col3
        if col4 is not None:
            self._check(col4)
            self.col4 = col4

    def _check(self, instance):
        for _allowed in Row.allowed:
            if isinstance(instance, _allowed):
                return
        raise UserWarning(
            "not allowed: {} {}".format(repr(instance), repr(_allowed)))
