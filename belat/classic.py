import belat.scheme as bs
import re

# https://baltoslav.eu/lat/index.php?mova=by
class Scheme(bs.Scheme):

    name = "Класічная лацінка"
    src = "https://baltoslav.eu/lat/index.php?mova=by"

    def __init__(self, log):
        self.log = log

    #Наборы літар
    l_galosn_lit = "AEOIUYaeoiuy"
    l_zychn_lit = "BVGDJŽZRMNOPRSTFCHČŠŁLŹŃŚǓbvgdjžzrlłmnoprstfchčšźńśŭ"
    l_vialik_lit = "BVGDJŽZRMNOPRSTFCHČŠŁLŹŃŚǓAEOIUY"
    l_mal_lit = "bvgdjžzrlłmnoprstfchčšźńśŭaeoiuy"

    c_galosn_lit = "АЕОІУЫЯЮаеоіуыяю"
    c_zychn_lit = "БВГДЖЗЙКЛМНОПРСТУЎФХЦЧШбвгджзйклмнпрстфхцчш"
    c_vialik_lit = "БВГДЖЗЙКЛМНОПРСТУЎФХЦЧШАЕОІУЫЯЮ"
    c_mal_lit = "бвгджзйклмнпрстфхцчшаеоіуыяю"

    gram_baza_je = {"l_galosn_lit":l_galosn_lit, "l_zychn_lit":l_zychn_lit, 
                   "l_vialik_lit":l_vialik_lit, "l_mal_lit":l_mal_lit,

                   "c_galosn_lit":c_galosn_lit, "c_zychn_lit":c_zychn_lit, 
                   "c_vialik_lit":c_vialik_lit, "c_mal_lit":c_mal_lit}
    
    # Праца з літарай г і Г
    # У некаторых каранях пішацца g(выбухны гук) замест h(фрыкатыўны)
    # TODO Зрабіць для такіх опцый як няГеглы, нягеГлы і г.д.
    class ctlr_g(bs.Rule):
        # @ у каранях - г або Г
        karani = ["@узік","@анак","@онт",
                "@узіч","@анач","@онц",
                "@анк", "ня@е@л"]

        def work_with(self, text, regexp_rule):
            if regexp_rule == "г":
                result = text
                for i in self.karani:
                    result = re.sub(i.replace("@","г"), i.replace("@","g"),
                        result)
                return re.sub("г", "h", result)

            elif regexp_rule == "Г":
                result = text
                for i in self.karani:
                    result = re.sub(i.replace("@","Г"), i.replace("@","G"),
                        result)
                    i = i.upper()
                    result = re.sub(i.replace("@","Г"), i.replace("@","G"),
                        result)
                return re.sub("Г", "H", result)

    # Праца з літарамі Е, Ю, Ё, Я, е, ю, ё, я
    # Правіла (на прыкладзе Е):
    # Je je - у пачатку слова, пасля галосных, пасля апострафа, пасля ў
    # Ie ie - пасля зычных, акрамя ў і л
    # E e - пасля л
    class ctr_je_jo_ju_ja(bs.Rule):
        def re_find(what, where, start):
            return re.search(what, where, )

        def __init__(self, gram_baza):
            self.gram_baza = gram_baza

        def work_with(self, text, regexp_rule):
            je_regexp = "(?<=["+self.gram_baza["l_galosn_lit"]+self.gram_baza["c_galosn_lit"]+"'ўЎ\s\n])"
            print(je_regexp)
            ie_regexp = "(?<=["+self.gram_baza["l_zychn_lit"]+self.gram_baza["c_zychn_lit"]+"])(?<![ўЎлЛŭǓlL])"
            e_regexp = "(?<=[лЛlL])"

            work_group_small = "еёюя"
            work_group_big = "ЕЁЮЯ"

            matching = {
                "е":"e",
                "ё":"o",
                "ю":"u",
                "я":"a"
            }

            if regexp_rule in work_group_small:
                je_res = re.sub(je_regexp+regexp_rule,"j"+matching[regexp_rule],text)
                je_res = re.sub("^"+regexp_rule,"j"+matching[regexp_rule],je_res)
                ie_res = re.sub(ie_regexp+regexp_rule,"i"+matching[regexp_rule],je_res)
                return re.sub(e_regexp+regexp_rule,matching[regexp_rule],ie_res)
            # З улікам суседніх літар, т.е БЕРАСТ павінен быць BIERAST, а не BIeRAST
            elif regexp_rule in work_group_big:
                je_res = re.sub(je_regexp+regexp_rule,"J"+matching[regexp_rule.lower()],text)
                je_res = re.sub("^"+regexp_rule,"J"+matching[regexp_rule.lower()],je_res)
                ie_res = re.sub(ie_regexp+regexp_rule,"I"+matching[regexp_rule.lower()],je_res)
                e_res = re.sub(e_regexp+regexp_rule,matching[regexp_rule.lower()].upper(),ie_res)

                cur_st = 0
                vialik_lit = "["+self.gram_baza["l_vialik_lit"]+self.gram_baza["c_vialik_lit"]+"]"
                while "J"+matching[regexp_rule.lower()] in e_res[cur_st:]:
                    cur_st = e_res.index("J"+matching[regexp_rule.lower()], cur_st)
                    try:
                        if re.match(vialik_lit,e_res[cur_st-1]) or re.match(vialik_lit, e_res[cur_st+2]):
                            e_res = e_res[:cur_st+1] + matching[regexp_rule.lower()].upper() + e_res[cur_st+2:]
                    except IndexError:
                        continue
                while "I"+matching[regexp_rule.lower()] in e_res[cur_st:]:
                    cur_st = e_res.index("I"+matching[regexp_rule.lower()], cur_st)
                    try:
                        if re.match(vialik_lit,e_res[cur_st-1]) or re.match(vialik_lit, e_res[cur_st+2]):
                            e_res = e_res[:cur_st+1] + matching[regexp_rule.lower()].upper() + e_res[cur_st+2:]
                    except IndexError:
                        continue
                return e_res

    class ctr_l(bs.Rule):
        def work_with(self, text, regexp):
            pass

    class ctr_z(bs.Rule):
        def work_with(self, text, regexp):
            pass

    class ctr_s(bs.Rule):
        def work_with(self, text, regexp):
            pass

    class ctr_c(bs.Rule):
        def work_with(self, text, regexp):
            pass

    ctl_rules = {
        "г":ctlr_g(), "Г":ctlr_g(), 
        "Е":ctr_je_jo_ju_ja(gram_baza_je), "е":ctr_je_jo_ju_ja(gram_baza_je),
        "Зь|ЗЬ":"Ź", "зь":"ź",
        "Ль|ЛЬ":"L", "ль":"l",
        "Нь|НЬ":"Ń", "нь":"ń",
        "Сь|СЬ":"Ś", "сь":"ś",
        "Ць|ЦЬ":"Ć", "ць":"ć",
        "А":"A", "а":"a",
        "Б":"B", "б":"b",
        "В":"V", "в":"v",
        "Д":"D", "д":"d",
        "Ё":ctr_je_jo_ju_ja(gram_baza_je), "ё":ctr_je_jo_ju_ja(gram_baza_je),
        "Ж":"Ž", "ж":"ž",
        "З":ctr_z, "з":ctr_z, # TODO
        "І":"I", "і":"i",
        "Й":"J", "й":"j",
        "К":"K", "к":"k",
        "Л":ctr_l, "л":ctr_l, # TODO
        "М":"M", "м":"m",
        "Н":"N", "н":"n",
        "О":"O", "о":"o",
        "П":"P", "п":"p",
        "Р":"R", "р":"r",
        "С":ctr_s, "с":ctr_s, # TODO
        "Т":"T", "т":"t",
        "У":"U", "у":"u",
        "Ў":"Ŭ", "ў":"ŭ",
        "Ф":"F", "ф":"f",
        "Х":"Ch", "х":"ch",
        "Ц":ctr_c, "ц":ctr_c, # TODO
        "Ч":"Č", "ч":"č",
        "Ш":"Š", "ш":"š",
        "Ы":"Y", "ы":"y",
        "Ь":"\u0301", "ь":"\u0301",
        "Э":"E", "э":"e",
        "Ю":ctr_je_jo_ju_ja(gram_baza_je), "ю":ctr_je_jo_ju_ja(gram_baza_je),
        "Я":ctr_je_jo_ju_ja(gram_baza_je), "я":ctr_je_jo_ju_ja(gram_baza_je),
        "Ґ":"G", "ґ":"g"
    }

    ltc_rules = {

    }

    def cyr_to_lat(self, text_in):
        result = text_in
        for character in self.ctl_rules.keys():
            if isinstance(self.ctl_rules[character], str):
                result = re.sub(character, self.ctl_rules[character], result)

            elif isinstance(self.ctl_rules[character], bs.Rule):
                result = self.ctl_rules[character].work_with(text=result, regexp_rule=character)
        return result

    def lat_to_cyr(self, text_in):
        self.log("<THIS OPTION IS NOT READY YET>")
        return ""
    