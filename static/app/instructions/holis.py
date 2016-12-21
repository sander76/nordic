'''
Holis instructions.

'''

from static.app.instructions.components import Instruction, ToJson
from static.app.instructions.instructor import INSTRUCTION_VERSION, twist

holis_instruction = Instruction(INSTRUCTION_VERSION)

holis_instruction.products.append(twist)

holis = ToJson(lang='en').encode(holis_instruction)
with open('instructions-holis-en.json', 'w') as fl:
    fl.write(holis)
