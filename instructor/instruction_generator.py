import os

from instructor.components import ToJson, Instruction
from instructor.helpers import TXT
from instructor.products.advanced import advanced
from instructor.products.m25s_duette import (
    m25s_duette_free,
    m25s_duette_tensioned,
)
from instructor.products.m25s_pleated import (
    m25s_pleated_free,
    m25s_pleated_tensioned,
)
from instructor.products.m25s_vb import (
    m25s_vb_free,
    m25s_vb_35_only,
    mhz_m35s_vb_free_slat_adjust,
    mhz_m16s_vb_free,
    mhz_m25s_vb_free, mhz_m35s_vb_free_slat_adjust_top_first)
from instructor.products.m25s_vvb import m25s_vvb
from instructor.products.roller import rollerblind1, rollerblind_old
from instructor.products.test_products import test_roller
from instructor.products.twist import twist_old, twist
from instructor.translations import load_translations

INSTRUCTION_VERSION = "1.7.22"
MAIN_PATH = "../static/instructions/"


def make_vb_free():
    make_instruction("instructions-vb-en.json", [m25s_vb_free], TXT.en)


def make_kadan_1():
    instructions = [
        m25s_vb_free,
        m25s_duette_free,
        m25s_duette_tensioned,
        m25s_pleated_free,
        m25s_pleated_tensioned,
        rollerblind1,
    ]
    make_instruction("instructions-kadan1-en.json", instructions, TXT.en)
    make_instruction("instructions-kadan1-cz.json", instructions, TXT.cz)


def make_luxaflex_nl():
    instructions = [
        rollerblind1,
        rollerblind_old,
        twist,
        twist_old,
        m25s_duette_free,
        m25s_duette_tensioned,
        m25s_pleated_free,
        m25s_pleated_tensioned,
        m25s_vb_free,
    ]
    make_instruction("instructions-luxaflex-nl.json", instructions, TXT.nl)


def make_mhz_de():
    instructions = [m25s_vvb]
    make_instruction("instructions-mhz1-de.json", instructions, TXT.de)

    instructions = [
        #m25s_vb_35_only,
        #m25s_vb_free,
        mhz_m16s_vb_free,
        mhz_m25s_vb_free,
        mhz_m35s_vb_free_slat_adjust,
        #mhz_m35s_vb_free_slat_adjust_top_first
    ]

    make_instruction("instructions-mhz2-de.json", instructions, TXT.de)

    make_instruction("instructions-mhz3-de.json", [rollerblind1], TXT.de)

    make_instruction(
        "instructions-mhz4-de.json",
        [m25s_duette_free, m25s_pleated_free],
        TXT.de,
    )


def make_luxaflex_uk():
    instructions = [rollerblind1, twist, m25s_vb_free]
    make_instruction("instructions-luxaflex-en.json", instructions, TXT.en)


def make_default():
    _path = os.path.join(MAIN_PATH, "instructions-en.json")
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products.append(rollerblind1)
    instruction.products.append(twist)

    en = ToJson(lang="en").encode(instruction)
    with open(_path, "w") as fl:
        fl.write(en)


def make_holis():
    instructions = [twist, rollerblind1, m25s_vb_free]

    make_instruction("instructions-holis-en.json", instructions, TXT.en)


def make_germania2():
    germania2_products = [rollerblind1, twist, m25s_vvb]

    make_instruction(
        "instructions-germania2-en.json", germania2_products, TXT.en
    )
    make_instruction(
        "instructions-germania2-de.json", germania2_products, TXT.de
    )


def make_germania1():
    germania1_products = [
        m25s_duette_free,
        m25s_pleated_free,
        m25s_vb_free,
        m25s_duette_tensioned,
        m25s_pleated_tensioned,
    ]
    make_instruction(
        "instructions-germania1-en.json", germania1_products, TXT.en
    )
    make_instruction(
        "instructions-germania1-de.json", germania1_products, TXT.de
    )


def make_poland():
    poland_products = [rollerblind1, m25s_vvb]
    make_instruction("instructions-hdfab-pl.json", poland_products, TXT.pl)
    make_instruction("instructions-hdfab-en.json", poland_products, TXT.en)


def make_test():
    test_products = [test_roller]
    make_instruction("instructions-tester-en.json", test_products, TXT.en)


def make_ts():
    ts_products = [
        m25s_duette_free,
        m25s_duette_tensioned,
        m25s_pleated_free,
        m25s_pleated_tensioned,
    ]

    make_instruction("instructions-ts-en.json", ts_products, TXT.en)


def make_all():
    products = [
        m25s_duette_free,
        m25s_duette_tensioned,
        m25s_pleated_free,
        m25s_pleated_tensioned,
        m25s_vvb,
        m25s_vb_free,
        rollerblind1,
        twist,
    ]
    make_instruction("instructions-all-en.json", products, TXT.en)
    make_instruction("instructions-all-cz.json", products, TXT.cz)
    make_instruction("instructions-all-de.json", products, TXT.de)
    make_instruction("instructions-all-nl.json", products, TXT.nl)
    make_instruction("instructions-all-pl.json", products, TXT.pl)


def make_tensioned():
    tensioned = [m25s_duette_tensioned]
    make_instruction("instructions-tensioned-en.json", tensioned, TXT.en)


def make_leha():
    products = [m25s_vvb, rollerblind1, twist]
    make_instruction("instructions-leha-de.json", products, TXT.de)


def make_advanced():
    products = [advanced]
    make_instruction("instructions-_advanced.json", products, TXT.en)


def make_instruction(file_name, products, lang):
    _path = os.path.join(MAIN_PATH, file_name)
    instruction = Instruction(INSTRUCTION_VERSION)
    instruction.products = products
    _products = ToJson(lang=lang).encode(instruction)
    with open(_path, "w", encoding="utf-8") as fl:
        fl.write(_products)


if __name__ == "__main__":
    # load translation files.
    load_translations()
    make_vb_free()
    make_default()
    make_luxaflex_uk()
    make_luxaflex_nl()
    make_holis()
    make_test()
    make_germania1()
    make_germania2()
    make_poland()
    make_ts()
    make_all()
    make_tensioned()
    make_leha()
    make_kadan_1()
    make_mhz_de()
    make_advanced()
