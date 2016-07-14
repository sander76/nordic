import json
import pprint
from cerberus.cerberus import Validator

from server.nordic import COMMANDS

cmds = COMMANDS.keys()

# columnschema = {"width": {"type": "string", "required": True},
#                 "type": {"type": "string", "required": True, "allowed": ['text', 'icon-button', 'keypad']},
#                 ''
#                 }

# Schemas

confirm = {'img': {'type': 'string', 'required': True},
           'text': {'type': 'string', 'required': True},
           'yes': {'type': 'integer'},
           'no': {'type': 'integer'}}

api_commands = {'commands': {'type': 'list', 'schema': {'type': 'string'}},
                'delay': {'type': 'integer'}}

next_prev_buttons = [{'type': 'boolean'},
                     {'type': 'dict',
                      'schema': {'caption': {'type': 'string', 'required': True},
                                 'goto': {'type': 'integer'}}}]

# tp = {'width':{'type':'string','required':True},
#       'type':{'type':'string','required':True,'allowed':['text','image','icon-button','keypad']},
#       'src':{'type':'string','dependencies':{'type':'image'}},
#       'content':{'type':'string','dependencies':{'type':}}
#       }


image = {'width': {'type': 'string', 'regex': '\d{1,2}%'},
         'type': {'type': 'string', 'required': True, 'allowed': ['image']},
         'src': {'type': 'string', 'required': True}}

text = {'width': {'type': 'string', 'regex': '\d{1,2}%'},
        'type': {'type': 'string', 'required': True, 'allowed': ['text']},
        'content': {'type': 'string', 'required': True}}

width_column = {'width': {'type': 'string', 'regex': '\d{1,2}%', 'required': True}}

icon_button = {'width': {'type': 'string', 'regex': '\d{1,2}%'},
               'type': {'type': 'string', 'required': True, 'allowed': ['icon-button']},
               'icon': {'type': 'string', 'required': True},
               'class': {'type': 'string', 'allowed': ['ok']},
               'confirm': {'type': 'boolean'},
               'keys': {'type': 'string'},
               'commands': {'type': 'dict', 'schema': api_commands}}

icon_nav_button = {'width': {'type': 'string', 'regex': '\d{1,2}%'},
                   'type': {'type': 'string', 'required': True, 'allowed': ['icon-nav-button']},
                   'icon': {'type': 'string', 'required': True},
                   'class': {'type': 'string', 'allowed': ['ok', 'cross']},
                   'keys': {'type': 'string'},
                   'goto': {'type': 'integer', 'required': True}}

key_pad = {'width': {'type': 'string', 'regex': '\d{1,2}%'},
           'type': {'type': 'string', 'required': True, 'allowed': 'keypad'}}

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

# allowed_types = [text, icon_button, key_pad]
# list schema for instructions
# col1 = {'col1': {'type': 'dict', 'schema': {'oneof': allowed_types}}}
# col2 = {'col2': {'type': 'dict', 'schema': {'oneof': allowed_types}}}
# col3 = {'col3': {'type': 'dict', 'schema': {'oneof': allowed_types}}}
col = {'type': 'dict', 'oneof': [
    {'schema': icon_button},
    {'schema': icon_nav_button},
    {'schema': key_pad},
    {'schema': text},
    {'schema': image},
    {'schema': width_column},
    {'schema': pv_keypad}]}

# instruction = {'type': 'dict', 'schema': {'oneof': [col1, col2, col3]}}

instruction = {'type': 'dict', 'schema': {
    'col1': col, 'col2': col, 'col3': col, 'col4': col}}

step = {'type': 'dict',
        'schema': {'title': {'type': 'string', 'required': True},
                   'instructions': {'type': 'list', 'schema': instruction, 'required': True},
                   'confirm': {'type': 'dict', 'schema': confirm},
                   'next': {'oneof': next_prev_buttons, 'required': True},
                   'previous': {'oneof': next_prev_buttons, 'required': True}
                   }}

product = {'type': 'dict',
           'schema': {'title': {'type': 'string', 'required': True},
                      'steps': {'type': 'list', 'schema': step}}}

total_instruction = {'version': {'type': 'string', 'required': True},
                     'products': {'type': 'list', 'schema': product}}

next_default = {'caption': 'next', 'goto': 1}
previous_default = {'caption': 'previous', 'goto': -1}


def set_defaults(instruction):
    for product in instruction['products']:
        for step in product['steps']:
            if 'previous' not in step:
                step['previous'] = previous_default
            if 'next' not in step:
                step['next'] = next_default


if __name__ == "__main__":
    v = Validator(total_instruction)

    with open('static/app/instructions/instructions-en.json') as fl:
        dta = json.load(fl)
        # set_defaults(dta)

    # with open('static/app/instructions/instructions-en.json','w') as fl:
    #     json.dump(dta, fl)



    val = v.validate(dta)
    print(val)
    if val == False:
        pprint.pprint(v.errors)
