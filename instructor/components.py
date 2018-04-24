import json

# from server.nordic import COMMANDS
import server.nordic
from instructor.constants import DEFAULT_DELAY
# import instructor.translations as tr
from instructor.helpers import TXT, NumberedText
from instructor.translations import Translations as Tr
from server.nordic import Nd

COMMANDS = server.nordic.__dict__
COMMAND_FORMAT = "{:<10}{}"
CONFIRM_FORMAT = "{:<10}{}"
STEP_FORMAT = "{:<10}{}"
ROW_FORMAT = "{:<45}{:<45}{:<45}{:<45}"
TEXT_FORMAT = "{:<10}{}"
IMG_FORMAT = "{:<10}{}"
TITLE_FORMAT = "{:<10}{}"

PROPERTY_FORMAT = '{:<12}{}'


class Component:
    def string_rep(self) -> []:
        return ['not implemented']


class NavigationCommand(Component):
    def __init__(self, goto):
        self.goto = goto

    def string_rep(self, indent='|'):
        _arr = [indent + 'NAVIGATION COMMAND']
        indent = indent + ' '
        _arr.append(indent + PROPERTY_FORMAT.format('goto', self.goto))
        return _arr


class NextPrevious(NavigationCommand):
    def __init__(self, button_text, goto, active):
        NavigationCommand.__init__(self, goto)
        self.caption = button_text
        self.active = active


class Next(NextPrevious):
    def __init__(self, button_text=Tr.NEXT, goto=1, active=True):
        NextPrevious.__init__(self, button_text, goto, active)


class Previous(NextPrevious):
    def __init__(self, button_text=Tr.PREVIOUS, goto=-1, active=True):
        NextPrevious.__init__(self, button_text, goto, active)


class DelayedCommand:
    def __init__(self, command, delay=DEFAULT_DELAY):
        if not isinstance(command, Nd):
            raise UserWarning("Command is not correct")
        self.command = command.name
        self.delay = delay

    def string_def(self, indent='|'):
        _arr = [indent + PROPERTY_FORMAT.format('command', self.command)]
        _arr.append(indent + PROPERTY_FORMAT.format('delay', self.delay))
        return _arr


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


class Instruction(Component):
    def __init__(self, version):
        self.version = version
        self.products = []

    def create_file(self, language):
        return json


class Product(Component):
    def __init__(self, title, steps):
        self.title = title
        self.steps = steps

    def string_rep(self):
        arr = []
        arr.append(self.title.string_def())
        for _step in self.steps:
            arr.extend(_step.string_rep())
        return arr


class Step(Component):
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

    def string_rep(self):
        arr = []
        arr.append(STEP_FORMAT.format('title', self.title.string_def()))
        arr.append(STEP_FORMAT.format('id', self.id))
        for _instruction in self.instructions:
            arr.extend(_instruction.string_rep())
        return arr


class UiElement(Component):
    def __init__(self, width):
        if isinstance(width, int):
            self.width = str(width) + '%'
        else:
            raise UserWarning("not an integer : {}".format(width))

    def string_rep_title(self, content, indent='|'):
        arr = [content.upper()]
        return arr


class Confirm(Component):
    def __init__(self, img, text, yes_text=Tr.YES, no_text=Tr.NO,
                 yes: NavigationCommand = NavigationCommand(1),
                 no: NavigationCommand = NavigationCommand(0)):
        if not isinstance(text, TXT):
            raise Exception("Text content not of class TXT")
        if (not isinstance(yes, NavigationCommand) or
                not isinstance(no, NavigationCommand)):
            raise Exception("Confirm yes and/or no not correct type")
        self.img = img
        self.text = text
        self.yes = yes
        self.no = no
        self.yes_text = yes_text
        self.no_text = no_text

    def string_rep(self, indent='|'):
        _arr = ['+' + "CONFIRM"]
        indent = '| '
        _arr.append(PROPERTY_FORMAT.format(indent + 'img', self.img))
        _arr.append(
            PROPERTY_FORMAT.format(indent + 'text', self.text.string_def()))
        _arr.append(PROPERTY_FORMAT.format(indent + 'yes_text',
                                           self.yes_text.string_def()))
        _arr.append(PROPERTY_FORMAT.format(indent + 'no_text',
                                           self.no_text.string_def()))
        _arr.append(indent + "yes nav")
        _arr.extend(self.yes.string_rep(indent=indent + ' '))
        _arr.append(indent + "no nav")
        _arr.extend(self.no.string_rep(indent=indent + ' '))
        return _arr


class NordicCommands(Component):
    def __init__(self, first_command: Nd, *next_commands):
        if not isinstance(first_command, Nd):
            raise UserWarning("Command is not correct.")
        for _cmd in next_commands:
            if not isinstance(_cmd, DelayedCommand):
                raise UserWarning(
                    "Only delayed commands allowed after command.")
        self.commands = [first_command.name] + [cmd for cmd in
                                                next_commands]

    def string_rep(self, indent='|'):
        # assuming no more than 4 commands in a single nordic command.
        _arr = [indent + 'NORDIC COMMANDS']
        indent = indent + ' '
        _arr.append(
            indent + PROPERTY_FORMAT.format('command', self.commands[0]))
        for _cmd in self.commands[1:]:
            _arr.extend(_cmd.string_def(indent))
        return _arr


class Commands(Component):
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

    def string_rep(self, indent='|'):
        _arr = []
        if self.nordic_commands:
            _arr.extend(self.nordic_commands.string_rep(indent))
        if self.confirm_command:
            _arr.extend(self.confirm_command.string_rep(indent))
        if self.navigation_command:
            _arr.extend(self.navigation_command.string_rep(indent))
        return _arr


class Spacer(UiElement):
    def __init__(self, width):
        UiElement.__init__(self, width)
        self.type = 'spacer'

    def string_rep(self, indent='|'):
        _arr = self.string_rep_title(self.type, indent)
        return _arr


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
        if (not (open is None or isinstance(open, Commands)) and
                (close is None or isinstance(close, Commands)) and
                (stop is None or not isinstance(stop, Commands)) and
                (tiltup is None or isinstance(tiltup, Commands)) and
                (tiltdown is None or isinstance(tiltdown, Commands)) and
                (cancel is None or isinstance(cancel, Commands)) and
                (okay is None or isinstance(okay, Commands))):
            raise Exception("keypad command type not correct.")

        self.type = 'pv-keypad-alt'
        self.open = open
        self.close = close
        self.stop = stop
        self.tiltup = tiltup
        self.tiltdown = tiltdown
        self.cancel = cancel
        self.okay = okay

    def string_rep(self, indent='|'):
        arr = self.string_rep_title(self.type)
        indent = '+'
        new_indent = '| '
        if self.open:
            arr.append(indent + 'OPEN')
            arr.extend(self.open.string_rep(indent=new_indent))
        if self.close:
            arr.append(indent + 'CLOSE')
            arr.extend(self.close.string_rep(indent=new_indent))
        if self.stop:
            arr.append(indent + 'STOP')
            arr.extend(self.stop.string_rep(indent=new_indent))
        if self.tiltup:
            arr.append(indent + 'TIlTUP')
            arr.extend(self.tiltup.string_rep(indent=new_indent))
        if self.tiltdown:
            arr.append(indent + 'TILTDOWN')
            arr.extend(self.tiltdown.string_rep(indent=new_indent))
        if self.cancel:
            arr.append(indent + 'CANCEL')
            arr.extend(self.cancel.string_rep(indent=new_indent))
        if self.okay:
            arr.append(indent + 'OKAY')
            arr.extend(self.okay.string_rep(indent=new_indent))
        return arr


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


class Text(UiElement):
    def __init__(self, width_percentage, content):
        UiElement.__init__(self, width_percentage)
        self.type = 'text'
        self.content = content

    def string_rep(self):
        _arr = self.string_rep_title(self.type)
        _arr.append(TEXT_FORMAT.format('text', self.content.string_def()))
        return _arr


class Image(UiElement):
    def __init__(self, width, src):
        UiElement.__init__(self, width)
        self.type = "image"
        self.src = src

    def string_rep(self):
        _arr = self.string_rep_title(self.type)
        return _arr


class Row(Component):
    allowed = [PvKeypadAlt, PvKeypad, Text, Image, Spacer]

    def __init__(self, col1, col2=None, col3=None, col4=None):
        self._check(col1)
        self.col1 = col1
        # self.col2 = None
        # self.col3 = None
        # self.col4 = None
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

    def _get_item(self, lst, idx):
        return lst[idx] if len(lst) > idx else ''

    def string_rep(self):
        _arr = []
        _col1 = self.col1.string_rep()
        if self.col2:
            _col2 = self.col2.string_rep()
        else:
            _col2 = []
        if self.col3:
            _col3 = self.col3.string_rep()
        else:
            _col3 = []
        if self.col4:
            _col4 = self.col4.string_rep()
        else:
            _col4 = []

        _max_rows = max(len(_col1), len(_col2), len(_col3), len(_col4))
        for _row in range(_max_rows):
            _str = ROW_FORMAT.format(self._get_item(_col1, _row),
                                     self._get_item(_col2, _row),
                                     self._get_item(_col3, _row),
                                     self._get_item(_col4, _row))
            _arr.append(_str)
        return _arr
