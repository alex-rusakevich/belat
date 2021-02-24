import belat.scheme as bs
import re

# https://meganorm.ru/Data2/1/4294835/4294835719.pdf
class Scheme(bs.Scheme):
    
    name = "ГОСТ 16876-71 от 1981 г. (табл. 2)"
    
    ctl_rules = {
        "'":"''",
        "А":"A", "а":"a",
        "Б":"B", "б":"b",
        "В":"V", "в":"v",
        "Г":"G", "г":"g",
        "Д":"D", "д":"d",
        "Е":"E", "е":"e",
        "Ё":"Jo", "ё":"jo",
        "Ж":"Zh", "ж":"zh",
        "З":"Z", "з":"z",
        "І":"Ih", "і":"ih",
        "Й":"Jh", "й":"jj",
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
        "Ў":"Uh", "ў":"uh",
        "Ф":"F", "ф":"f",
        "Х":"Kh", "х":"kh",
        "Ц":"C", "ц":"c",
        "Ч":"Ch", "ч":"ch",
        "Ш":"Sh", "ш":"sh",
        "Ы":"Y", "ы":"y",
        "Ь":"'", "ь":"'",
        "Э":"Eh", "э":"eh",
        "Ю":"Ju", "ю":"ju",
        "Я":"Ja", "я":"ja"
    }

    ltc_rules = {
        "Kh":"Х", "kh":"х",
        "Ju":"Ю", "ju":"ю",
        "Ja":"Я", "ja":"я",
        "Eh":"Э", "eh":"э",
        "Ch":"Ч", "ch":"ч",
        "Sh":"Ш", "sh":"ш",
        "A":"А", "a":"а",
        "B":"Б", "b":"б",
        "V":"В", "v":"в",
        "G":"Г", "g":"г",
        "D":"Д", "d":"д",
        "E":"Е", "e":"е",
        "Jo":"Ё", "jo":"ё",
        "Zh":"Ж", "zh":"ж",
        "Z":"З", "z":"з",
        "Ih":"І", "ih":"і",
        "Jh":"Й", "jj":"й",
        "K":"К", "k":"к",
        "L":"Л", "l":"л",
        "M":"М", "m":"м",
        "N":"Н", "n":"н",
        "O":"О", "o":"о",
        "P":"П", "p":"п",
        "R":"Р", "r":"р",
        "S":"С", "s":"с",
        "T":"Т", "t":"т",
        "Uh":"Ў", "uh":"ў",
        "U":"У", "u":"у",
        "F":"Ф", "f":"ф",
        "C":"Ц", "c":"ц",
        "Y":"Ы", "y":"ы",
        "'":"ь", "''":"'"
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
