import os

from instructor.components import ToJson, Instruction
from instructor.helpers import TXT
from instructor.products.m25s_duette import m25s_duette_free, \
    m25s_duette_free_alt
from instructor.products.m25s_pleated import m25s_pleated_free
from instructor.products.m25s_vb import m25s_25mm_vb_free, \
    m25s_25mm_vb_free_alt, \
    m25s_16mm_vb_free_alt
from instructor.products.m25s_vvb import m25s_vvb_right
from instructor.products.roller import rollerblind1, rollerblind_old
from instructor.products.test_products import test1
from instructor.products.twist import twist_old, twist

# from instructor.products.venetian import venetian16

INSTRUCTION_VERSION = "1.7.0"
MAIN_PATH = "../static/app/instructions"


def make_luxaflex_nl():
    _path = os.path.join(MAIN_PATH, 'instructions-luxaflex-nl.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(rollerblind_old)
    instruction.products.append(twist)
    instruction.products.append(twist_old)

    nl = ToJson(lang='nl').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(nl)


def make_luxaflex_uk():
    _path = os.path.join(MAIN_PATH, 'instructions-luxaflex-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

    en = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(en)


def make_test():
    _path = os.path.join(MAIN_PATH, 'instructions-test-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(m25s_duette_free)
    instruction.products.append(m25s_duette_free_alt)
    instruction.products.append(m25s_25mm_vb_free)
    instruction.products.append(m25s_16mm_vb_free_alt)

    en = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(en)


def make_default():
    _path = os.path.join(MAIN_PATH, 'instructions-en.json')
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


def make_holis():
    _path = os.path.join(MAIN_PATH, 'instructions-holis-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(twist)
    holis = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(holis)


def make_test1():
    _path = os.path.join(MAIN_PATH, 'instructions-test1-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(test1)
    products = ToJson(lang='en').encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(products)


germania1_file_name = "instructions-germania1-en.json"
germania1_products = [m25s_duette_free_alt, m25s_pleated_free,
                      m25s_16mm_vb_free_alt, m25s_25mm_vb_free_alt]
germania1_lang = TXT.en

germania2_file_name = "instructions-germania2-en.json"
germania2_products = [rollerblind1, twist,m25s_vvb_right]
germania2_lang = TXT.en


def make_instruction(file_name, products, lang):
    _path = os.path.join(MAIN_PATH, file_name)
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products = products
    _products = ToJson(lang=lang).encode(instruction)
    with open(_path, 'w') as fl:
        fl.write(_products)


if __name__ == "__main__":
    make_default()
    make_test()
    make_luxaflex_uk()
    make_luxaflex_nl()
    # make_vb(outputpath)
    make_holis()
    make_test1()
    make_instruction(germania1_file_name, germania1_products, germania1_lang)
    make_instruction(germania2_file_name, germania2_products, germania2_lang)
