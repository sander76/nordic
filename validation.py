import json

from cerberus.cerberus import Validator

from nordic import COMMANDS

cmds = COMMANDS.keys()

schema = {'products':
              {'type': 'list',
               'schema':
                   {'type': 'dict',
                    'schema':
                        {'title': {'type': 'string'},
                         'steps': {'type': 'list',
                                   'schema': {'type': 'dict',
                                              'schema': {'title': {'type': 'string'},
                                                         'instructions': {'type': 'list',
                                                                          'schema': {'oneof': [
                                                                              {'type': 'string'},
                                                                              {'type': 'dict',
                                                                               'schema': {'type': {'type': 'string',
                                                                                                   'allowed': ['button']
                                                                                                   },
                                                                                          'caption': {'type': 'string'},
                                                                                          'commands': {'type': 'dict',
                                                                                                       'schema': {
                                                                                                           'commands': {
                                                                                                               'type': 'list',
                                                                                                               'allowed': cmds},
                                                                                                           'delay': {
                                                                                                               'type': 'integer'}
                                                                                                       }
                                                                                                       },
                                                                                          'keys': {'type': 'string'},
                                                                                          'confirm': {'type': 'boolean'}
                                                                                          }
                                                                               },
                                                                              {'type': 'dict',
                                                                               'schema': {'type': {'type': 'string',
                                                                                                   'allowed': ['remote']
                                                                                                   }
                                                                                          }
                                                                               },
                                                                              {'type': 'dict',
                                                                               'schema': {'type': {'type': 'string',
                                                                                                   'allowed': [
                                                                                                       'navbutton']
                                                                                                   },
                                                                                          'caption': {'type': 'string'},
                                                                                          'goto': {'type': 'integer'}}},
                                                                              {'type': 'dict',
                                                                               'schema': {'type': {'type': 'string',
                                                                                                   'allowed': [
                                                                                                       'image']},
                                                                                          'src': {'type': 'string'}}}

                                                                          ]}
                                                                          },
                                                         'buttons': {'type': 'list'},
                                                         'confirm': {'type': 'dict',
                                                                     'schema': {'img': {'type': 'string'},
                                                                                'text': {'type': 'string'},
                                                                                'next': {'type': 'integer'},
                                                                                'previous': {'type': 'integer'}}},
                                                         'next': {'type': ['boolean', 'string']},
                                                         'previous': {'type': ['boolean', 'string']}
                                                         }
                                              }
                                   }
                         }
                    }
               }
          }

if __name__ == "__main__":
    v = Validator(schema)

with open('static/app/instructions/instruction-test.json') as fl:
    dta = json.load(fl)
val = v.validate(dta)
print(val)
if val == False:
    print(v.errors)
