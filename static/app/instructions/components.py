import json

from server.nordic import COMMANDS

import static.app.instructions.translations as tr

#from static.app.instructions.translations import _yes
from static.app.instructions.helpers import TXT, NumberedText


class NextPrevious:
    def __init__(self, button_text, goto, active):
        self.caption = button_text
        self.goto = goto
        self.active = active


class Next(NextPrevious):
    def __init__(self, button_text="next", goto=1, active=True):
        NextPrevious.__init__(self, button_text, goto, active)


class Previous(NextPrevious):
    def __init__(self, button_text="previous", goto=-1, active=True):
        NextPrevious.__init__(self, button_text, goto, active)








class ToJson(json.JSONEncoder):
    def __init__(self, lang='en'):
        json.JSONEncoder.__init__(self, sort_keys=True)
        self.lang = lang

    def default(self, o):
        if isinstance(o, TXT) or isinstance(o, NumberedText):
            return o.get_text(self.lang)
            # return getattr(o, self.lang)
        else:
            return o.__dict__


class Instruction:
    def __init__(self, version='1.3'):
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
    def __init__(self, title, instructions, confirm=None, nav_next=Next(), nav_previous=Previous(),id=None):
        for instruction in instructions:
            if not isinstance(instruction, Row):
                raise UserWarning("instruction is not of type Row.")
        self.title = title
        self.instructions = instructions
        self.confirm = confirm
        self.next = nav_next
        self.previous = nav_previous
        self.id=id


'''
instruction = {'type': 'dict', 'schema': {
    'col1': col, 'col2': col, 'col3': col, 'col4': col}}

'''

'''
confirm = {'img': {'type': 'string', 'required': True},
           'text': {'type': 'string', 'required': True},
           'yes': {'type': 'integer'},
           'no': {'type': 'integer'}}
'''


class Confirm:
    def __init__(self, img, text,yes_text=tr._yes,no_text=tr._no, yes=1, no=0):
        self.img = img
        self.text = text
        self.yes = yes
        self.no = no
        self.yes_text=yes_text
        self.no_text=no_text



class UiElement:
    def __init__(self, width):
        if isinstance(width, int):
            self.width = str(width) + '%'
        else:
            raise UserWarning("not an integer : {}".format(width))


class ApiCommand:
    def __init__(self, commands, delay=None):
        for command in commands:
            if command not in COMMANDS.keys():
                raise UserWarning("{} not a valid nordic command".format(command))
        self.commands = {'commands': commands}
        if delay is not None:
            # self.delay = delay
            self.commands['delay'] = delay


class OkayCommand(ApiCommand):
    def __init__(self, commands=None, delay=None, goto=None):
        if commands is not None:
            ApiCommand.__init__(self, commands, delay)
        if goto is not None:
            self.goto = goto


class Spacer(UiElement):
    def __init__(self, width):
        UiElement.__init__(self, width)


'''
pv_keypad = {'width': {'type': 'string', 'regex': '\d{1,2}%'},
             'type': {'type': 'string', 'required': True, 'allowed': 'pv-keypad'},
             'active_buttons': {'type': 'list',
                                'allowed': ['open', 'close', 'stop', 'tiltup', 'tiltdown', 'okay', 'cancel'],
                                'required': True},
             'confirm': {'type': 'string',
                         'allowed': ['open', 'close', 'stop', 'tiltup', 'tiltdown', 'okay', 'cancel']},
             'okay': {'type': 'dict',
                      'schema': {'commands': {'type': 'dict', 'schema': api_commands}, 'goto': {'type': 'integer'}}},
             'cancel': {'type': 'integer', 'required': True}}
'''


class PvKeypad(UiElement):
    allowed = ['open', 'close', 'tiltup', 'tiltdown', 'stop', 'okay', 'cancel']

    def __init__(self, width, active_buttons, confirm=None, okay=None, cancel=None):
        '''
        :param width: defines the width in percentage of the element.
        :param active_buttons: which buttons to activate
        :param confirm: which button will have an "open confirm dialog" method to it.
        :param okay: what actions should be taken when ok is clicked.
        :param cancel: where should cancel take you ?
        '''
        UiElement.__init__(self, width)
        self.type = 'pv-keypad'
        self.active_buttons = active_buttons
        for button in active_buttons:
            if button not in PvKeypad.allowed:
                raise UserWarning("'{}' not allowed as pvkeypad button".format(button))
        if confirm is not None:
            if confirm not in active_buttons:
                raise UserWarning("'{}' not allowed as it is not an active button".format(confirm))
            self.confirm = confirm
        if okay is not None:
            if 'okay' not in PvKeypad.allowed:
                raise UserWarning("'okay' defined but not defined as an active button.")
            self.okay = okay
        if cancel is not None:
            if 'cancel' not in PvKeypad.allowed:
                raise UserWarning("'cancel' defined but not defined as an active button.")
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


'''
next_prev_buttons = [{'type': 'boolean'},
                     {'type': 'dict',
                      'schema': {'caption': {'type': 'string', 'required': True},
                                 'goto': {'type': 'integer'}}}]
'''


class Row:
    allowed = [PvKeypad, Text, Image,Spacer]

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
        raise UserWarning("not allowed: {} {}".format(repr(instance), repr(_allowed)))
