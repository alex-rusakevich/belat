import belat.scheme as bs
import re

# https://files.stroyinf.ru/Data2/1/4294816/4294816248.pdf
class Scheme(bs.Scheme):

    name = "ГОСТ 7.79-2000, система Б"
    src = "https://files.stroyinf.ru/Data2/1/4294816/4294816248.pdf"

    ctl_rules = {
        "А":"A", "а":"a",
        "Б":"B", "б":"b",
        "В":"V", "в":"v",
        "Г":"G", "г":"g",
        "Д":"D", "д":"d",
        "Е":"E", "е":"e",
        "Ё":"Yo", "ё":"yo",
        "Ж":"Zh", "ж":"zh",
        "З":"Z", "з":"z",
        "І":"I", "і":"i",
        "Й":"J", "й":"j",
        "К":"K", "к":"k",
        "Л":"L", "л":"l",
        "М":"M", "м":"m",
        "Н":"N", "н":"n",
        "О":"O", "о":"o",
        "П":"P", "п":"p",
        "Р":"R", "р":"r",
        "С":"S", "с":"s",
        "Т":"T", "т":"t",
        "У":"U", "у":"u",
        "Ў":"U`", "ў":"u`",
        "Ф":"F", "ф":"f",
        "Х":"X", "х":"x",
        "Ц":"C", "ц":"c",
        "Ч":"Ch", "ч":"ch",
        "Ш":"Sh", "ш":"sh",
        "Ы":"Y`", "ы":"y`",
        "Ь":"`", "ь":"`",
        "Э":"E`", "э":"e`",
        "Ю":"Yu", "ю":"yu",
        "Я":"Ya", "я":"ya"
    }

    ltc_rules = {
        "Yu":"Ю", "yu":"ю",
        "Ya":"Я", "ya":"я",
        "U`":"Ў", "u`":"ў",
        "Ch":"Ч", "ch":"ч",
        "Cz|C":"Ц", "cz|c":"ц",
        "Sh":"Ш", "sh":"ш",
        "Y`":"Ы", "y`":"ы",
        "E`":"Э", "e`":"э",
        "Yo":"Ё", "yo":"ё",
        "Zh":"Ж", "zh":"ж",
        "A":"А", "a":"а",
        "B":"Б", "b":"б",
        "V":"В", "v":"в",
        "G":"Г", "g":"г",
        "D":"Д", "d":"д",
        "E":"Е", "e":"е",
        "Z":"З", "z":"з",
        "J":"Й", "j":"й",
        "I":"І", "i":"і",
        "K":"К", "k":"к",
        "L":"Л", "l":"л",
        "M":"М", "m":"м",
        "N":"Н", "n":"н",
        "O":"О", "o":"о",
        "P":"П", "p":"п",
        "R":"Р", "r":"р",
        "S":"С", "s":"с",
        "T":"Т", "t":"т",
        "U":"У", "u":"у",
        "F":"Ф", "f":"ф",
        "X":"Х", "x":"х",
        "`":"ь"
    }

    def __init__(self, log):
        self.log = log

    def cyr_to_lat(self, text_in):
        result = text_in
        for character in self.ctl_rules.keys():
            result = re.sub(character, self.ctl_rules[character], result)
        return result

    def lat_to_cyr(self, text_in):
        result = text_in
        for character in self.ltc_rules.keys():
            result = re.sub(character, self.ltc_rules[character], result)
        return result