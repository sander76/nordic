import os

from instructor.components import ToJson, Instruction
from instructor.products.m25s_duette import m25s_duette_free, m25s_duette_free_alt
from instructor.products.m25s_vb import m25s_25mm_vb_free, m25s_25mm_vb_free_alt, \
    m25s_16mm_vb_free_alt
from instructor.products.roller import rollerblind1, rollerblind_old
from instructor.products.test_products import test1
from instructor.products.twist import twist_old, twist
# from instructor.products.venetian import venetian16

INSTRUCTION_VERSION = "1.6.8"


def make_luxaflex_nl(path):
    _path = os.path.join(path, 'instructions-luxaflex-nl.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(rollerblind_old)
    instruction.products.append(twist)
    instruction.products.append(twist_old)

    nl = ToJson(lang='nl').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(nl)


def make_luxaflex_uk(path):
    _path = os.path.join(path, 'instructions-luxaflex-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

    en = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(en)


def make_test(path):
    _path = os.path.join(path, 'instructions-test-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(m25s_duette_free)
    instruction.products.append(m25s_duette_free_alt)
    instruction.products.append(m25s_25mm_vb_free)
    instruction.products.append(m25s_16mm_vb_free_alt)

    en = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(en)


def make_default(path):
    _path = os.path.join(path, 'instructions-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

    en = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(en)


# def make_vb(path):
#     _path = os.path.join(path, 'instructions-vb16-en.json')
#     instruction = Instruction(INSTRUCTION_VERSION)
#     instruction.products.append(venetian16)
#
#     en = ToJson(lang='en').encode(instruction)
#     with open(_path, 'w') as fl:
#         fl.write(en)


def make_holis(path):
    _path = os.path.join(path, 'instructions-holis-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(twist)
    holis = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(holis)

def make_test1(path):
    _path = os.path.join(path, 'instructions-test1-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(test1)
    products = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(products)

if __name__ == "__main__":
    outputpath = "../static/app/instructions"
    make_default(outputpath)
    make_test(outputpath)
    make_luxaflex_uk(outputpath)
    make_luxaflex_nl(outputpath)
    # make_vb(outputpath)
    make_holis(outputpath)
    make_test1(outputpath)

