import os

from instructor.components import ToJson, Instruction
from instructor.helpers import TXT

from instructor.products.m25s_duette import m25s_duette_free_alt, \
    m25s_duette_tensioned, m25s_duette_tensioned_alt
from instructor.products.m25s_pleated import m25s_pleated_free, \
    m25s_pleated_tensioned
from instructor.products.m25s_vb import m25s_25mm_vb_free_alt, \
    m25s_16mm_vb_free_alt
from instructor.products.m25s_vvb import m25s_vvb
from instructor.products.roller import rollerblind1, rollerblind_old
from instructor.products.test_products import test1, test_blinds1
from instructor.products.twist import twist_old, twist
from instructor.translations import load_translations

INSTRUCTION_VERSION = "1.7.5"
MAIN_PATH = "../static/app/instructions"


def make_luxaflex_nl():
    instructions = [rollerblind1,
                    rollerblind_old,
                    twist,
                    twist_old,
                    m25s_25mm_vb_free_alt,
                    m25s_16mm_vb_free_alt,
                    m25s_duette_free_alt,
                    m25s_duette_tensioned_alt,
                    m25s_pleated_free,
                    m25s_pleated_tensioned
                    ]
    make_instruction('instructions-luxaflex-nl.json', instructions, TXT.nl)


def make_luxaflex_uk():
    _path = os.path.join(MAIN_PATH, 'instructions-luxaflex-en.json')
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

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


def make_germania2():
    germania2_products = [rollerblind1, twist, m25s_vvb]

    make_instruction(
        "instructions-germania2-en.json", germania2_products, TXT.en)
    make_instruction(
        "instructions-germania2-de.json", germania2_products, TXT.de)


def make_germania1():
    germania1_products = [m25s_duette_free_alt, m25s_pleated_free,
                          m25s_16mm_vb_free_alt, m25s_25mm_vb_free_alt]
    make_instruction(
        "instructions-germania1-en.json", germania1_products, TXT.en)
    make_instruction(
        "instructions-germania1-de.json", germania1_products, TXT.de
    )


def make_poland():
    poland_products = [rollerblind1, m25s_vvb, m25s_vvb]

    make_instruction("instructions-hdfab-pl.json", poland_products, TXT.pl)
    make_instruction("instructions-hdfab-en.json", poland_products, TXT.en)


def make_test():
    test_products = [test_blinds1]
    make_instruction("instructions-tester-en.json", test_products, TXT.en)


def make_ts():
    ts_products = [
        m25s_duette_free_alt,
        m25s_duette_tensioned,
        m25s_pleated_free,
        m25s_pleated_tensioned,
        m25s_16mm_vb_free_alt,
        m25s_25mm_vb_free_alt]

    make_instruction("instructions-ts-en.json", ts_products, TXT.en)


def make_all():
    products = [
        m25s_duette_free_alt,
        m25s_duette_tensioned,
        m25s_duette_tensioned_alt,
        m25s_pleated_free,
        m25s_pleated_tensioned,
        m25s_25mm_vb_free_alt,
        m25s_16mm_vb_free_alt,
        m25s_vvb,
        rollerblind1,
        twist
    ]
    make_instruction("instructions-all-en.json", products, TXT.en)


def make_tensioned():
    tensioned = [m25s_duette_tensioned,
                 m25s_duette_tensioned_alt]
    make_instruction("instructions-tensioned-en.json", tensioned, TXT.en)


def make_leha():
    products = [m25s_vvb]
    make_instruction("instructions-leha-de.json", products, TXT.de)


def make_instruction(file_name, products, lang):
    _path = os.path.join(MAIN_PATH, file_name)
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products = products
    _products = ToJson(lang=lang).encode(instruction)
    with open(_path, 'w', encoding='utf-8') as fl:
        fl.write(_products)


if __name__ == "__main__":
    # load translation files.
    load_translations()

    make_default()
    make_test()
    make_luxaflex_uk()
    make_luxaflex_nl()
    make_holis()
    make_test1()
    make_germania1()
    make_germania2()
    make_poland()
    make_ts()
    make_all()
    make_tensioned()
    make_leha()
