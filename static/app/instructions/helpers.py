class NumberedText:
    def __init__(self, txt_instance, number):
        self.number = number
        self.txt = txt_instance

    def get_text(self, lang):
        txt = self.txt.get_text(lang)
        val = '{}. {}'.format(self.number, txt)
        return val

class TXT:
    def __init__(self, en, nl):
        self.en = en
        self.nl = nl

    def get_text(self, lang):
        val = getattr(self, lang, 'en')
        return val

    def add_number(self, number):
        nt = NumberedText(self, number)
        return nt