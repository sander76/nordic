from instructor.helpers import TXT
from instructor.instruction_generator import make_instruction
from instructor.products.test_products import test_roller
from instructor.translations import load_translations


def make_test():
    test_products = [test_roller]
    make_instruction("instructions-test-en.json", test_products, TXT.en)


if __name__ == "__main__":
    # load translation files.
    load_translations()

    make_test()
