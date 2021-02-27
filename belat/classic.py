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

    gram_baza = {"l_galosn_lit":l_galosn_lit, "l_zychn_lit":l_zychn_lit, 
                   "l_vialik_lit":l_vialik_lit, "l_mal_lit":l_mal_lit,

                   "c_galosn_lit":c_galosn_lit, "c_zychn_lit":c_zychn_lit, 
                   "c_vialik_lit":c_vialik_lit, "c_mal_lit":c_mal_lit}
    
    # Праца з літарай г і Г
    # У некаторых каранях пішацца g(выбухны гук) замест h(фрыкатыўны)
    class ctlr_g(bs.Rule):
        # @ у каранях - г або Г
        karani = ["@узік","@анак","@онт",
                "@узіч","@анач","@онц",
                "@анк", "ня@е@л", "маз@і"]

        def work_with(self, text, regexp_rule):
            result = text

            for i in self.karani:
                cur_state = 0
                while re.match(i.replace("@","г"), result[cur_state:], re.IGNORECASE):
                    cur_state = re.search(i.replace("@","г"), result[cur_state:], re.IGNORECASE).start()
                    # Параўноўваем
                    # @узік
                    # ГуЗіК
                    # GуЗіК
                    try:
                        count = 0
                        while not re.match("\s",result[cur_state]):
                            if i[count] == "@":
                                if result[cur_state] == "Г":
                                    result = result[:cur_state]+"G"+result[(cur_state+1):]
                                elif result[cur_state] == "г":
                                    result = result[:cur_state]+"g"+result[(cur_state+1):]
                            count += 1
                            cur_state +=1
                    except IndexError:
                        continue

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
            je_regexp = "(?<=["+self.gram_baza["l_galosn_lit"]+self.gram_baza["c_galosn_lit"]+"'ўЎ\s\n])"
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
                while "I"+mtch in e_res[cur_st:]:
                    cur_st = e_res.index("I"+mtch, cur_st)
                    try:
                        if re.match(vialik_lit,e_res[cur_st-1]) or re.match(vialik_lit, e_res[cur_st+2]):
                            e_res = e_res[:cur_st+1] + mtch.upper() + e_res[cur_st+2:]
                    except IndexError:
                        continue
                return e_res

    # Выбар паміж Ł і L
    class ctlr_l(bs.Rule):
        def work_with(self, text, regexp_rule):
            excepts = "еёіюяЕЁІЮЯ"
            if regexp_rule == "л":
                li = re.sub("л(?=["+excepts+"])", "l", text) 
                return re.sub("л(?!["+excepts+"])", "ł", li)
            elif regexp_rule == "Л":
                li = re.sub("Л(?=["+excepts+"])", "L", text) 
                return re.sub("Л(?!["+excepts+"])", "Ł", li)

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
                return ch_text

    # Праца з З С Н 
    # Асіміляцыя па мягкасці
    class assimil_pa_miahk(bs.Rule):
        def __init__(self, gram_baza):
            self.gram_baza = gram_baza
            self.use_lat_lit = gram_baza["l_vialik_lit"]+gram_baza["l_mal_lit"]
        
        zmiahch = "LŹŃŚĆJlźńśćj"
        post_zmiahch = "Ií"

        assim_para = {
            "Ł":"L",
            "ł":"l",
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
            for i in self.assim_para.keys():
                result = re.sub(i+"(?=["+self.zmiahch+"])", self.assim_para[i], result)
                result = re.sub(i+"(?=["+self.use_lat_lit+"]["+self.post_zmiahch+"])", 
                    self.assim_para[i], result)
            return result

    ctl_rules = {
        "г":ctlr_g(), "Г":ctlr_g(),
        "Л":ctlr_l(), "л":ctlr_l(),
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
        "Ь":"\u0301", "ь":"\u0301",
        "Э":"E", "э":"e",
        "Ґ":"G", "ґ":"g",
        "assimil":assimil_pa_miahk(gram_baza)
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
    