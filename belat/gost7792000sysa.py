import belat.scheme as bs
import re

# https://files.stroyinf.ru/Data2/1/4294816/4294816248.pdf
class Scheme(bs.Scheme):

    name = "ГОСТ 7.79-2000, система А"
    src = "https://files.stroyinf.ru/Data2/1/4294816/4294816248.pdf"

    ctl_rules = {
        "ь":"´",
        "А":"A", "а":"a",
        "Б":"B", "б":"b",
        "В":"V", "в":"v",
        "Г":"G", "г":"g",
        "Д":"D", "д":"d",
        "Е":"E", "е":"e",
        "Ё":"Ë", "ё":"ë",
        "Ж":"Ž", "ж":"ž",
        "З":"Z", "з":"z",
        "І":"Ì", "і":"ì",
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
        "Э":"È", "э":"è",
        "Ю":"Û", "ю":"û",
        "Я":"Â", "я":"â",
        "'":"'", "Ь":"´"
    }

    ltc_rules = {
        '´': 'ь', 
        'A': 'А', 'a': 'а', 
        'B': 'Б', 'b': 'б', 
        'V': 'В', 'v': 'в', 
        'G': 'Г', 'g': 'г', 
        'D': 'Д', 'd': 'д', 
        'E': 'Е', 'e': 'е', 
        'Ë': 'Ё', 'ë': 'ё', 
        'Ž': 'Ж', 'ž': 'ж', 
        'Z': 'З', 'z': 'з', 
        'Ì': 'І', 'ì': 'і', 
        'J': 'Й', 'j': 'й', 
        'K': 'К', 'k': 'к', 
        'L': 'Л', 'l': 'л', 
        'M': 'М', 'm': 'м', 
        'N': 'Н', 'n': 'н', 
        'O': 'О', 'o': 'о', 
        'P': 'П', 'p': 'п', 
        'R': 'Р', 'r': 'р', 
        'S': 'С', 's': 'с', 
        'T': 'Т', 't': 'т', 
        'U': 'У', 'u': 'у', 
        'Ǔ': 'Ў', 'ŭ': 'ў', 
        'F': 'Ф', 'f': 'ф', 
        'H': 'Х', 'h': 'х', 
        'C': 'Ц', 'c': 'ц', 
        'Č': 'Ч', 'č': 'ч', 
        'Š': 'Ш', 'š': 'ш', 
        'Y': 'Ы', 'y': 'ы', 
        'È': 'Э', 'è': 'э', 
        'Û': 'Ю', 'û': 'ю', 
        'Â': 'Я', 'â': 'я', 
        "'": "'"
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