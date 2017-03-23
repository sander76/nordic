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

    def __init__(self, en: str, nl: str, il: str = None, pl=None, ru=None,
                 he=None,
                 de=None,
                 dk=None, to_upper=False):
        self.en = en
        self.nl = nl
        self.pl = pl
        self.il = il
        self.ru = ru
        self.he = he
        self.de = de
        self.dk = dk
        self.to_upper = to_upper

    def get_text(self, lang):
        val = getattr(self, lang)
        if val is None:
            val = getattr(self, TXT.en)
        if self.to_upper:
            val = val.upper()

        return {'content': val}

    def add_number(self, number):
        nt = NumberedText(self, number)
        return nt
