import belat.scheme as bs
import re

# https://baltoslav.eu/lat/index.php?mova=by
class Scheme(bs.Scheme):

    name = "Афіцыйная лацінка"
    src = "https://baltoslav.eu/lat/index.php?mova=by https://www.zedlik.com/pragramy/kir2lac-online/"

    def __init__(self, log):
        self.log = log

    #Наборы літар
    l_galosn_lit = "AEOIUYaeoiuy"
    l_zychn_lit = "BVGDJŽZRMNOPRSTFCHČŠĹLŹŃŚǓbvgdjžzrlĺmnoprstfchčšźńśŭ"
    l_vialik_lit = "BVGDJŽZRMNOPRSTFCHČŠĹLŹŃŚǓAEOIUY"
    l_mal_lit = "bvgdjžzrlĺmnoprstfchčšźńśŭaeoiuy"

    c_galosn_lit = "АЕОІУЫЯЮЁаеоіуыяюё"
    c_zychn_lit = "БВГДЖЗЙКЛМНОПРСТУЎФХЦЧШбвгджзйклмнпрстфхцчш"
    c_vialik_lit = "БВГДЖЗЙКЛМНОПРСТУЎФХЦЧШАЕОІУЫЯЮ"
    c_mal_lit = "бвгджзйклмнпрстфхцчшаеоіуыяю"

    gram_baza = {"l_galosn_lit":l_galosn_lit, "l_zychn_lit":l_zychn_lit, 
                   "l_vialik_lit":l_vialik_lit, "l_mal_lit":l_mal_lit,

                   "c_galosn_lit":c_galosn_lit, "c_zychn_lit":c_zychn_lit, 
                   "c_vialik_lit":c_vialik_lit, "c_mal_lit":c_mal_lit}
    
    # Праца з літарай г і Г
    class ctlr_g(bs.Rule):

        def work_with(self, text, regexp_rule):
            result = text

            if regexp_rule == "г":
                return re.sub("г", "h", result)

            elif regexp_rule == "Г":
                return re.sub("Г", "H", result)

    # Праца з літарамі Е, Ю, Ё, Я, е, ю, ё, я (з ётавымі)
    # Правіла (на прыкладзе Е):
    # Je je - у пачатку слова, пасля галосных, пасля апострафа, пасля ў
    # Ie ie - пасля зычных, акрамя ў і л
    # E e - пасля л
    class ctlr_je_jo_ju_ja(bs.Rule):
        def re_find(what, where, start):
            return re.search(what, where, )

        def __init__(self, gram_baza):
            self.gram_baza = gram_baza

        def work_with(self, text, regexp_rule):
            je_regexp = "(?<=["+self.gram_baza["l_galosn_lit"]+self.gram_baza["c_galosn_lit"]+r"'ўЎ\s\n])"
            ie_regexp = "(?<=["+self.gram_baza["l_zychn_lit"]+self.gram_baza["c_zychn_lit"]+"])(?<![ўЎŭǓ])"
            e_regexp = ie_regexp

            work_group_small = "еёюя"
            work_group_big = "ЕЁЮЯ"

            matching = {
                "е":"e",
                "ё":"o",
                "ю":"u",
                "я":"a"
            }

            if regexp_rule in work_group_small:
                mtch = matching[regexp_rule]

                je_res = re.sub(je_regexp+regexp_rule,"j"+mtch,text)
                je_res = re.sub("^"+regexp_rule,"j"+mtch,je_res)
                ie_res = re.sub(ie_regexp+regexp_rule,"i"+mtch,je_res)
                return re.sub(e_regexp+regexp_rule,mtch,ie_res)
            # З улікам суседніх літар, т.е БЕРАСТ павінен быць BIERAST, а не BIeRAST
            elif regexp_rule in work_group_big:
                mtch = matching[regexp_rule.lower()]

                je_res = re.sub(je_regexp+regexp_rule,"J"+mtch,text)
                je_res = re.sub("^"+regexp_rule,"J"+mtch,je_res)
                ie_res = re.sub(ie_regexp+regexp_rule,"I"+mtch,je_res)
                e_res = re.sub(e_regexp+regexp_rule,mtch.upper(),ie_res)

                cur_st = 0
                vialik_lit = "["+self.gram_baza["l_vialik_lit"]+self.gram_baza["c_vialik_lit"]+"]"
                while "J"+mtch in e_res[cur_st:]:
                    cur_st = e_res.index("J"+mtch, cur_st)
                    try:
                        if re.match(vialik_lit,e_res[cur_st-1]) or re.match(vialik_lit, e_res[cur_st+2]):
                            e_res = e_res[:cur_st+1] + mtch.upper() + e_res[cur_st+2:]
                    except IndexError:
                        continue
                    cur_st += 2
                cur_st = 0
                while "I"+mtch in e_res[cur_st:]:
                    cur_st = e_res.index("I"+mtch, cur_st)
                    try:
                        if re.match(vialik_lit,e_res[cur_st-1]) or re.match(vialik_lit, e_res[cur_st+2]):
                            e_res = e_res[:cur_st+1] + mtch.upper() + e_res[cur_st+2:]
                    except IndexError:
                        continue
                    cur_st += 2
                return e_res
    
    # Дадатковая шліфоўка вялікіх ётавых
    class ctlr_vial_jot(bs.Rule):
        def __init__(self, gram_baza):
            self.gram_baza = gram_baza

        def work_with(self, text, regexp_rule):
            cur_st = 0
            vialik_lit = "["+self.gram_baza["l_vialik_lit"]+self.gram_baza["c_vialik_lit"]+"]"
            e_res = text
            for mtch in ["e","o","u","a"]:
                while "J"+mtch in e_res[cur_st:]:
                    cur_st = e_res.index("J"+mtch, cur_st)
                    try:
                        if re.match(vialik_lit,e_res[cur_st-1]) or re.match(vialik_lit, e_res[cur_st+2]):
                            e_res = e_res[:cur_st+1] + mtch.upper() + e_res[cur_st+2:]
                    except IndexError:
                        continue
                    cur_st += 2
                cur_st = 0
                while "I"+mtch in e_res[cur_st:]:
                    cur_st = e_res.index("I"+mtch, cur_st)
                    try:
                        if re.match(vialik_lit,e_res[cur_st-1]) or re.match(vialik_lit, e_res[cur_st+2]):
                            e_res = e_res[:cur_st+1] + mtch.upper() + e_res[cur_st+2:]
                    except IndexError:
                        continue
                    cur_st += 2
            return e_res

    # Выбар паміж CH і Ch, ch
    class ctrl_ch(bs.Rule):
        def __init__(self, gram_baza):
            self.gram_baza = gram_baza

        def work_with(self, text, regexp_rule):
            if regexp_rule == "х":
                return re.sub("х", "ch", text)
            elif regexp_rule == "Х":
                ch_text = re.sub("Х", "Ch", text)
                cur_st = 0
                vialik_lit = "["+self.gram_baza["l_vialik_lit"]+self.gram_baza["c_vialik_lit"]+"]"
                while "Ch" in ch_text[cur_st:]:
                    cur_st = ch_text.index("Ch", cur_st)
                    try:
                        if re.match(vialik_lit,ch_text[cur_st-1]) or re.match(vialik_lit, ch_text[cur_st+2]):
                            ch_text = ch_text[:cur_st+1] + "H" + ch_text[cur_st+2:]
                    except IndexError:
                        continue
                    cur_st += +2
                return ch_text

    # Праца з мягкім знакам
    class miahk_zn(bs.Rule):
        def __init__(self):
            pass

        maihk_para = {
            "L":"Ĺ",
            "l":"ĺ",
            "Z":"Ź",
            "z":"ź",
            "N":"Ń",
            "n":"ń",
            "S":"Ś",
            "s":"ś",
            "C":"Ć",
            "c":"ć"
        }

        def work_with(self, text, regexp_rule):
            result = text
            for i in self.maihk_para.keys():
                result = re.sub(i+"[Ьь]", self.maihk_para[i], result)
            return result

    ctl_rules = {
        "г":ctlr_g(), "Г":ctlr_g(),
        "Л":"L", "л":"l",
        "Х":ctrl_ch(gram_baza), "х":ctrl_ch(gram_baza),
        "Е":ctlr_je_jo_ju_ja(gram_baza), "е":ctlr_je_jo_ju_ja(gram_baza),
        "Ё":ctlr_je_jo_ju_ja(gram_baza), "ё":ctlr_je_jo_ju_ja(gram_baza),
        "Ю":ctlr_je_jo_ju_ja(gram_baza), "ю":ctlr_je_jo_ju_ja(gram_baza),
        "Я":ctlr_je_jo_ju_ja(gram_baza), "я":ctlr_je_jo_ju_ja(gram_baza),
        
        "З":"Z", "з":"z",
        "Н":"N", "н":"n",
        "С":"S", "с":"s",
        "Ц":"C", "ц":"c",
        
        "Зь|ЗЬ":"Ź", "зь":"ź",
        "Ль|ЛЬ":"L", "ль":"l",
        "Нь|НЬ":"Ń", "нь":"ń",
        "Сь|СЬ":"Ś", "сь":"ś",
        "Ць|ЦЬ":"Ć", "ць":"ć",

        "А":"A", "а":"a",
        "Б":"B", "б":"b",
        "В":"V", "в":"v",
        "Д":"D", "д":"d",
        "Ж":"Ž", "ж":"ž",
        "І":"I", "і":"i",
        "Й":"J", "й":"j",
        "К":"K", "к":"k",
        "М":"M", "м":"m",
        "О":"O", "о":"o",
        "П":"P", "п":"p",
        "Р":"R", "р":"r",
        "Т":"T", "т":"t",
        "У":"U", "у":"u",
        "Ў":"Ŭ", "ў":"ŭ",
        "Ф":"F", "ф":"f",
        "Ч":"Č", "ч":"č",
        "Ш":"Š", "ш":"š",
        "Ы":"Y", "ы":"y",
        "Э":"E", "э":"e",
        "Ґ":"G", "ґ":"g",
        "Ь":miahk_zn(), "ь":miahk_zn(),
        "vial_jot":ctlr_vial_jot(gram_baza),
        "'":""
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
        self.log("<THIS OPTION IS NOT READY YET>\n")
        return ""
    