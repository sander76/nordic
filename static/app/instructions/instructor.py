from static.app.instructions.connect import connect_vb

from static.app.instructions.components import Row, Text, PvKeypad, Step, \
    Product, Instruction, ToJson, Spacer, NavigationCommand



import static.app.instructions.translations as tr
from static.app.instructions.roller import rollerblind1, rollerblind_old

from static.app.instructions.twist import twist_old, twist
from static.app.instructions.venetian import venetian16

INSTRUCTION_VERSION = "1.6.4"














def make_luxaflex_nl():
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(rollerblind_old)
    instruction.products.append(twist)
    instruction.products.append(twist_old)

    nl = ToJson(lang='nl').encode(instruction)
    with open('instructions-luxaflex-nl.json', 'w') as fl:
        fl.write(nl)

def make_luxaflex_uk():
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

    en = ToJson(lang='en').encode(instruction)
    with open('instructions-luxaflex-en.json', 'w') as fl:
        fl.write(en)

def make_default():
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

    en = ToJson(lang='en').encode(instruction)
    with open('instructions-en.json', 'w') as fl:
        fl.write(en)

def make_vb():
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(venetian16)

    en = ToJson(lang='en').encode(instruction)
    with open('instructions-vb16-en.json', 'w') as fl:
        fl.write(en)

def make_holis():
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(twist)
    holis = ToJson(lang='en').encode(instruction)
    with open('instructions-holis-en.json', 'w') as fl:
        fl.write(holis)


if __name__ == "__main__":
    make_default()
    make_luxaflex_uk()
    make_luxaflex_nl()
    make_vb()
    make_holis()
