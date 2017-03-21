class NumberedText:
    def __init__(self, txt_instance, number):
        self.number = number
        self.txt = txt_instance

    def get_text(self, lang):
        txt = self.txt.get_text(lang)
        # val = '<div>{}</div> <div>{}</div>'.format(self.number, txt)
        txt['bullet'] = self.number
        # return val
        return txt


class TXT:
    en = 'en'
    nl = 'nl'
    pl = 'pl'
    il = 'il'
    ru = 'ru'
    he = 'he'
    de = 'de'
    dk = 'dk'

    def __init__(self, en, nl, il=None, pl=None, ru=None, he=None, de=None,
                 dk=None):
        self.en = en
        self.nl = nl
        self.pl = pl
        self.il = il
        self.ru = ru
        self.he = he
        self.de = de
        self.dk = dk

    def get_text(self, lang):
        val = getattr(self, lang, TXT.en)
        # return val
        return {'content': val}

    def add_number(self, number):
        nt = NumberedText(self, number)
        return nt
