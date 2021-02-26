import belat.scheme as bs
import re

# https://meganorm.ru/Data2/1/4294835/4294835719.pdf
class Scheme(bs.Scheme):
    
    name = "ГОСТ 16876-71 от 1981 г. (табл. 1)"
    src = "https://meganorm.ru/Data2/1/4294835/4294835719.pdf"
    
    ctl_rules = {
        "'":"''",
        "А":"A", "а":"a",
        "Б":"B", "б":"b",
        "В":"V", "в":"v",
        "Г":"G", "г":"g",
        "Д":"D", "д":"d",
        "Е":"Je", "е":"je",
        "Ё":"E", "ё":"e",
        "Ж":"Ž", "ж":"ž",
        "З":"Z", "з":"z",
        "І":"Ì", "і":"i",
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
        "Ў":"Ǔ", "ў":"ŭ",
        "Ф":"F", "ф":"f",
        "Х":"H", "х":"h",
        "Ц":"C", "ц":"c",
        "Ч":"Č", "ч":"č",
        "Ш":"Š", "ш":"š",
        "Ы":"Y", "ы":"y",
        "Ь":"'", "ь":"'",
        "Э":"È", "э":"è",
        "Ю":"Ju", "ю":"ju",
        "Я":"Ja", "я":"ja"
    }

    ltc_rules = {
        "Ch|H":"Х", "ch|h":"х",
        "Ju|Û":"Ю", "ju|û":"ю",
        "Ja":"Я", "ja":"я",
        "A":"А", "a":"а",
        "B":"Б", "b":"б",
        "V":"В", "v":"в",
        "G":"Г", "g":"г",
        "D":"Д", "d":"д",
        "Je":"Е", "je":"е",
        "Ë|E":"Ё", "ë|e":"ё",
        "Ž":"Ж", "ž":"ж",
        "Z":"З", "z":"з",
        "Ì":"І", "i":"і",
        "J":"Й", "j":"й",
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
        "Ǔ":"Ў", "ŭ":"ў",
        "F":"Ф", "f":"ф",
        "C":"Ц", "c":"ц",
        "Č":"Ч", "č":"ч",
        "Š":"Ш", "š":"ш",
        "Y":"Ы", "y":"ы",
        "'":"ь", "''":"'", 
        "È":"Э", "è":"э"
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
