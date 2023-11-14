import pytest

import belat.official as bc


@pytest.fixture
def scheme_official():
    return bc.Scheme(print)


def test_official_1(scheme_official):
    assert (
        scheme_official.cyr_to_lat(
            """Родная мова, цудоўная мова!
Ты нашых думак уток і аснова!

Матчын дарунак ад самай калыскі,
ты самацветаў яскравая нізка.

Кожны з іх барвы дзівосныя мае,
вечным агнём зіхаціць - не згарае.

Ты мне заўсёды была дапамогай,
дзе б і якой ні хадзіў я дарогай.

Чую ў табе перазвоны крыніцы,
чую ў табе і раскат навальніцы,

чую павевы зялёнага бору,
водгулле працы у родным прасторы.

Кожнай драбнічкай ты варта пашаны,
кожнае слова вякамі стварана.

І на вякі яно жыць застаецца,
вечнае так, як народнае сэрца."""
        )
        == """Rodnaja mova, cudoŭnaja mova!
Ty našych dumak utok i asnova!

Matčyn darunak ad samaj kalyski,
ty samacvietaŭ jaskravaja nizka.

Kožny z ich barvy dzivosnyja maje,
viečnym ahniom zichacić - nie zharaje.

Ty mnie zaŭsiody byla dapamohaj,
dzie b i jakoj ni chadziŭ ja darohaj.

Čuju ŭ tabie pierazvony krynicy,
čuju ŭ tabie i raskat navaĺnicy,

čuju pavievy zialionaha boru,
vodhullie pracy u rodnym prastory.

Kožnaj drabničkaj ty varta pašany,
kožnaje slova viakami stvarana.

I na viaki jano žyć zastajecca,
viečnaje tak, jak narodnaje serca."""
    )


def test_official_2(scheme_official):
    assert (
        scheme_official.cyr_to_lat(
            """Ад родных ніў, ад роднай хаты
У панскі двор дзеля красы
Яны, бяздольныя, узяты
Ткаць залатыя паясы.
І цягам доўгія часіны,
Дзявочыя забыўшы сны,
Свае шырокія тканіны
На лад персідскі ткуць яны.
А за сцяной смяецца поле,
Зіяе неба з-за акна, –
І думкі мкнуцца мімаволі
Туды, дзе расцвіла вясна;
Дзе блішча збожжа ў яснай далі,
Сінеюць міла васількі,
Халодным срэбрам ззяюць хвалі
Між гор ліючайся ракі;
Цямнее край зубчаты бора...
І тчэ, забыўшыся, рука,
Заміж персідскага узора,
Цвяток радзімы васілька."""
        )
        == """Ad rodnych niŭ, ad rodnaj chaty
U panski dvor dzielia krasy
Jany, biazdoĺnyja, uziaty
Tkać zalatyja pajasy.
I ciaham doŭhija časiny,
Dziavočyja zabyŭšy sny,
Svaje šyrokija tkaniny
Na lad piersidski tkuć jany.
A za scianoj smiajecca polie,
Zijaje nieba z-za akna, –
I dumki mknucca mimavoli
Tudy, dzie rascvila viasna;
Dzie blišča zbožža ŭ jasnaj dali,
Siniejuć mila vasiĺki,
Chalodnym srebram zziajuć chvali
Miž hor lijučajsia raki;
Ciamnieje kraj zubčaty bora...
I tče, zabyŭšysia, ruka,
Zamiž piersidskaha uzora,
Cviatok radzimy vasiĺka."""
    )


def test_official_3(scheme_official):
    assert (
        scheme_official.cyr_to_lat(
            """Магутнае слова, ты, роднае слова!
       Са мной ты на яве і ў сне;
Душу мне затрэсла пагудкаю новай,
       Ты песень наўчыла мяне.

Бяссмертнае слова, ты, роднае слова!
       Ты крыўды, няпраўды змагло;
Хоць гналі цябе, накладалі аковы,
       Дый дарма: жывеш як жыло!

Свабоднае слова, ты, роднае слова!
       Зайграй ты смялей, весялей!
Хоць гадзіны сыкаюць, кружацца совы,
       Жывеш ты на хвалу людзей.

Загнанае слова, ты, роднае слова!
       Грымі ж над радзімай зямлёй:
Што родная мова, хоць бедная мова,
       Мілей найбагатшай чужой!"""
        )
        == """Mahutnaje slova, ty, rodnaje slova!
       Sa mnoj ty na javie i ŭ snie;
Dušu mnie zatresla pahudkaju novaj,
       Ty piesień naŭčyla mianie.

Biassmiertnaje slova, ty, rodnaje slova!
       Ty kryŭdy, niapraŭdy zmahlo;
Choć hnali ciabie, nakladali akovy,
       Dyj darma: žyvieš jak žylo!

Svabodnaje slova, ty, rodnaje slova!
       Zajhraj ty smialiej, viesialiej!
Choć hadziny sykajuć, kružacca sovy,
       Žyvieš ty na chvalu liudziej.

Zahnanaje slova, ty, rodnaje slova!
       Hrymi ž nad radzimaj ziamlioj:
Što rodnaja mova, choć biednaja mova,
       Miliej najbahatšaj čužoj!"""
    )


def test_official_4(scheme_official):
    assert (
        scheme_official.cyr_to_lat(
            """Несупыннай хваляй плыні
За парою йшла пара,
І прабіла час хлапчыне
Гнаць у поле са двара.
Ён праслухаў навучанку,
Як быць добрым пастухом,
Справіў пугу-павіванку,
Вузлы вывязаў гурком
І пагнаў авечкі ў поле
На папары і на ролі.
Ён цяпер глядзеў больш стала:
Ён – асоба, пастушок,
Нават права меў на сала
І на цёплы кажушок."""
        )
        == """Niesupynnaj chvaliaj plyni
Za paroju jšla para,
I prabila čas chlapčynie
Hnać u polie sa dvara.
Jon prasluchaŭ navučanku,
Jak być dobrym pastuchom,
Spraviŭ puhu-pavivanku,
Vuzly vyviazaŭ hurkom
I pahnaŭ aviečki ŭ polie
Na papary i na roli.
Jon ciapier hliadzieŭ boĺš stala:
Jon – asoba, pastušok,
Navat prava mieŭ na sala
I na cioply kažušok."""
    )


def test_official_5(scheme_official):
    assert (
        scheme_official.cyr_to_lat(
            """Я бачыў, як змяняе дзень
Вакол мяне гукі на колер,
Як небасхіл пакінуў цень,
Глытаючы слова «ніколі».
Я бачыў праз туман вачэй
Усё часцей ціхае «Хопіць!».
Вядзі мяне. Глядзі ў мяне.
Не ведаю, дзе мы і хто ты.

Баюсь цябе! Баюсь цябе!
І мне цяпер немагчыма збегчы
Ад хуткіх сноў тваіх, але
Мне быць з табой, неба, небяспечна.

Я бачыў, як вяртае час
Зімовых нас, толькі на поўдзень,
Дзе прамяні не пра мяне
Зрываюць дах, нібыта злодзей.
Я бачыў, як яе далонь
здымае боль сярод пустэчы
Ратуй мяне! Ратуй мяне!
Я ведаю, што будзе лепшым.

Баюсь цябе! Баюсь цябе!
І мне цяпер немагчыма збегчы
Ад хуткіх сноў тваіх, але
Мне быць з табой, неба, небяспечна.
неба, небяспечна
неба, небяспечна
неба, небяспечна.
Баюсь цябе! Баюсь цябе!
І мне цяпер немагчыма збегчы
Ад хуткіх сноў тваіх, але
Мне быць з табой.
Баюсь цябе! Баюсь цябе!
І мне цяпер немагчыма збегчы
Ад хуткіх сноў тваіх, але
Мне быць з табой, неба, небяспечна.
неба, небяспечна
неба, небяспечна
неба, небяспечна."""
        )
        == """Ja bačyŭ, jak zmianiaje dzień
Vakol mianie huki na kolier,
Jak niebaschil pakinuŭ cień,
Hlytajučy slova «nikoli».
Ja bačyŭ praz tuman vačej
Usio časciej cichaje «Chopić!».
Viadzi mianie. Hliadzi ŭ mianie.
Nie viedaju, dzie my i chto ty.

Bajuś ciabie! Bajuś ciabie!
I mnie ciapier niemahčyma zbiehčy
Ad chutkich snoŭ tvaich, alie
Mnie być z taboj, nieba, niebiaspiečna.

Ja bačyŭ, jak viartaje čas
Zimovych nas, toĺki na poŭdzień,
Dzie pramiani nie pra mianie
Zryvajuć dach, nibyta zlodziej.
Ja bačyŭ, jak jaje daloń
zdymaje boĺ siarod pustečy
Ratuj mianie! Ratuj mianie!
Ja viedaju, što budzie liepšym.

Bajuś ciabie! Bajuś ciabie!
I mnie ciapier niemahčyma zbiehčy
Ad chutkich snoŭ tvaich, alie
Mnie być z taboj, nieba, niebiaspiečna.
nieba, niebiaspiečna
nieba, niebiaspiečna
nieba, niebiaspiečna.
Bajuś ciabie! Bajuś ciabie!
I mnie ciapier niemahčyma zbiehčy
Ad chutkich snoŭ tvaich, alie
Mnie być z taboj.
Bajuś ciabie! Bajuś ciabie!
I mnie ciapier niemahčyma zbiehčy
Ad chutkich snoŭ tvaich, alie
Mnie być z taboj, nieba, niebiaspiečna.
nieba, niebiaspiečna
nieba, niebiaspiečna
nieba, niebiaspiečna."""
    )


def test_official_6(scheme_official):
    assert (
        scheme_official.cyr_to_lat(
            """ДОБРА Ў ПОЛІ: ВОЛІ МНОГА
І ПРАСТОРУ-ШЫРЫНІ,
ВАБЯЦЬ ДАЛІ ТАМ МАЛОГА,
ЯК ПРЫНАДНЫЯ АГНІ.
ШТО ЁСЦЬ ТАМ, ЗА ТЫМ, УНЬ, ГАЕМ,
ДЗЕ ЗЛЯГЛІ НЯБЁС ВЯНЦЫ?
НОВЫ КРАЙ І КРАЙ ЗА КРАЕМ
І КРАІ ВА ЎСЕ КАНЦЫ!
І СНУЕЦЦА ДУМКА ТАЯ,
КАБ ПАШЫРЫЦЬ СВОЙ ПРАСТОР;
ДУМКА ЎСЮДЫ ЗАЛЯТАЕ:
ЗА СЯЛО, ЗА ХВАЛІ ГОР
І НА ХМАРКІ КІНЕ ВОКА,
ШТО, ЯК ГУСАНЬКІ, ПЛЫЛІ,
ЗАПЫТАЕ, ЯК ДАЛЁКА
ТОЕ СОНЦА АД ЗЯМЛІ.
ЯК ГЛЫБОК ТОЙ ПРАСТОР НЕМЫ,
І ЦІ МЕРЫЎ ЯГО ХТО?
І АДКАЖА ПА-СВАЕМУ:
ВЁРСТ НАПЭЎНА БУДЗЕ СТО!"""
        )
        == """DOBRA Ŭ POLI: VOLI MNOHA
I PRASTORU-ŠYRYNI,
VABIAĆ DALI TAM MALOHA,
JAK PRYNADNYJA AHNI.
ŠTO JOSĆ TAM, ZA TYM, UŃ, HAJEM,
DZIE ZLIAHLI NIABIOS VIANCY?
NOVY KRAJ I KRAJ ZA KRAJEM
I KRAI VA ŬSIE KANCY!
I SNUJECCA DUMKA TAJA,
KAB PAŠYRYĆ SVOJ PRASTOR;
DUMKA ŬSIUDY ZALIATAJE:
ZA SIALO, ZA CHVALI HOR
I NA CHMARKI KINIE VOKA,
ŠTO, JAK HUSAŃKI, PLYLI,
ZAPYTAJE, JAK DALIOKA
TOJE SONCA AD ZIAMLI.
JAK HLYBOK TOJ PRASTOR NIEMY,
I CI MIERYŬ JAHO CHTO?
I ADKAŽA PA-SVAJEMU:
VIORST NAPEŬNA BUDZIE STO!"""
    )


def test_official_7(scheme_official):
    assert (
        scheme_official.cyr_to_lat(
            """І ЯШЧЭ БЫЛО ЧЫМ МІЛА
ТОЕ ПОЛЕ ХЛАПЧУКУ,
ГЭТА ТЫМ, ШТО ДЗЕД КУРЫЛА
ТАМ ЯГО ТРЫМАЎ РУКУ.
ГЭТЫ ДЗЕД – ПАСТУХ ГУРТОВЫ,
СЛАЎНЫ ДЗЕД, ДЗЯДОК – ДУША,
ГАВАРКІ, МАСТАК НА СЛОВЫ,
І ЛЮБІЎ ЁН МАЛЫША!
НЕ СМЯЯЎСЯ ДЗЕД З СЫМОНКІ,
НЕ ЎСЧУВАЎ ЯГО НІ-НІ,
ЧАСТАВАЎ З СВАЕ СКАРБОНКІ,
БАВІЎ ЦЭЛЫЯ З ІМ ДНІ.
ЗАБЯРУЦЦА Ў ЦЕНЬ ПАД ГРУШУ
І ГАВОРКУ РАСПАЧНУЦЬ.
ТУТ СЫМОНКА СВАЮ ДУШУ
МОГ ПРАД ДЗЕДАМ РАЗГАРНУЦЬ,
ЗАПЫТАЦЬ ПРА СЁЕ-ТОЕ
ДЗЕДКУ ДОБРАГА СВАЙГО,
БО СЫМОН НЕ МЕЎ СПАКОЮ –
ЎСЁ ЦІКАВІЛА ЯГО."""
        )
        == """I JAŠČE BYLO ČYM MILA
TOJE POLIE CHLAPČUKU,
HETA TYM, ŠTO DZIED KURYLA
TAM JAHO TRYMAŬ RUKU.
HETY DZIED – PASTUCH HURTOVY,
SLAŬNY DZIED, DZIADOK – DUŠA,
HAVARKI, MASTAK NA SLOVY,
I LIUBIŬ JON MALYŠA!
NIE SMIAJAŬSIA DZIED Z SYMONKI,
NIE ŬSČUVAŬ JAHO NI-NI,
ČASTAVAŬ Z SVAJE SKARBONKI,
BAVIŬ CELYJA Z IM DNI.
ZABIARUCCA Ŭ CIEŃ PAD HRUŠU
I HAVORKU RASPAČNUĆ.
TUT SYMONKA SVAJU DUŠU
MOH PRAD DZIEDAM RAZHARNUĆ,
ZAPYTAĆ PRA SIOJE-TOJE
DZIEDKU DOBRAHA SVAJHO,
BO SYMON NIE MIEŬ SPAKOJU –
ŬSIO CIKAVILA JAHO."""
    )
