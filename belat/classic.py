import belat.scheme as bs
import re
import belat.utils as bu

# https://baltoslav.eu/lat/index.php?mova=by
class Scheme(bs.Scheme):

    name = "Класічная лацінка"
    src = "https://baltoslav.eu/lat/index.php?mova=by"

    def __init__(self, log):
        self.log = log

    # Праца з літарай г і Г
    # У некаторых каранях пішацца g
    # TODO Зрабіць для такіх опцый як няГеглы, нягеГлы і г.д.
    class ctlr_g(bs.Rule):
        # @ у каранях - г або Г
        karani = ["@узік","@анак","@онт",
                "@унзіч","@анач","@онц",
                "@анк", "ня@е@л"]

        def work_with(self, text, regexp):
            if regexp == "г":
                result = text
                for i in self.karani:
                    result = re.sub(i.replace("@","г"), i.replace("@","g"),
                        result)
                return re.sub("г", "h", result)

            elif regexp == "Г":
                result = text
                for i in self.karani:
                    result = re.sub(i.replace("@","Г"), i.replace("@","G"),
                        result)
                    i = i.upper()
                return re.sub("Г", "H", result)

    ctl_rules = {
        "г":ctlr_g, "Г":ctlr_g, 
        "Зь":"Ź", "зь":"ź",
        "Ль":"L", "ль":"l",
        "Нь":"Ń", "нь":"ń",
        "Сь":"Ś", "сь":"ś",
        "Ць":"Ć", "ць":"ć",
        "А":"A", "а":"a",
        "Б":"B", "б":"b",
        "В":"V", "в":"v",
        "Д":"D", "д":"d",
        "Е":"", "е":"", # TODO
        "Ё":"", "ё":"", # TODO
        "Ж":"Ž", "ж":"ž",
        "З":"Z", "з":"z",
        "І":"I", "і":"i",
        "Й":"J", "й":"j",
        "К":"K", "к":"k",
        "Л":"Ł", "л":"ł",
        "М":"M", "м":"m",
        "Н":"N", "н":"n",
        "О":"O", "о":"o",
        "П":"P", "п":"p",
        "Р":"R", "р":"r",
        "С":"S", "с":"s",
        "Т":"T", "т":"t",
        "У":"U", "у":"u",
        "Ў":"Ŭ", "ў":"ŭ",
        "Ф":"F", "ф":"f",
        "Х":"Ch", "х":"ch",
        "Ц":"C", "ц":"c",
        "Ч":"Č", "ч":"č",
        "Ш":"Š", "ш":"š",
        "Ы":"Y", "ы":"y",
        "Ь":"\u02ca", "ь":"\u02ca",
        "Э":"E", "э":"e",
        "Ю":"", "ю":"", # TODO
        "Я":"", "я":"", # TODO
        "Ґ":"G", "ґ":"g"
    }

    ltc_rules = {

    }

    def cyr_to_lat(self, text_in):
        result = text_in
        for character in self.ctl_rules.keys():
            if isinstance(self.ctl_rules[character], str):
                result = re.sub(character, self.ctl_rules[character], result)

            elif issubclass(self.ctl_rules[character], bs.Rule):
                result = self.ctl_rules[character]().work_with(text=result, regexp=character)
        return result

    def lat_to_cyr(self, text_in):
        result = text_in
        for character in self.ltc_rules.keys():
            result = re.sub(character, self.ltc_rules[character], result)
        return result
    