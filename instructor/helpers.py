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

    def string_def(self):
        return self.get_text('en').get('content')

class TXT:
    en = 'en'
    nl = 'nl'
    pl = 'pl'
    il = 'il'
    ru = 'ru'
    he = 'he'
    de = 'de'
    dk = 'dk'
    cz = 'cz'

    def __init__(
            self, en: str, nl: str = None, il: str = None, pl=None, ru=None,
            he=None,
            de=None,
            dk=None, cz=None, to_upper=False):
        self.en = en
        self.nl = nl
        self.pl = pl
        self.il = il
        self.ru = ru
        self.he = he
        self.de = de
        self.dk = dk
        self.cz = cz
        self.to_upper = to_upper

    def get_text(self, lang):
        val = getattr(self, lang)
        if val is None or not val.strip():
            val = getattr(self, TXT.en)
        if self.to_upper:
            val = val.upper()

        return {'content': val}

    def get_plain_text(self, lang):
        val = getattr(self, lang, '')
        val = val if val else ''
        return val

    def add_number(self, number):
        nt = NumberedText(self, number)
        return nt

    def string_def(self):
        return self.get_text('en').get('content')