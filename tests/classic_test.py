import pytest
import belat.classic as bc

@pytest.fixture
def scheme_classic():
    return bc.Scheme(print)

def test_classic_1(scheme_classic):
    assert scheme_classic.cyr_to_lat("""Родная мова, цудоўная мова!
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
вечнае так, як народнае сэрца.""") == """Rodnaja mova, cudoŭnaja mova!
Ty našych dumak utok i asnova!

Matčyn darunak ad samaj kałyski,
ty samaćvietaŭ jaskravaja nizka.

Kožny z ich barvy dzivosnyja maje,
viečnym ahniom zichacić - nie zharaje.

Ty mnie zaŭsiody była dapamohaj,
dzie b i jakoj ni chadziŭ ja darohaj.

Čuju ŭ tabie pierazvony krynicy,
čuju ŭ tabie i raskat navalnicy,

čuju pavievy zialonaha boru,
vodhulle pracy u rodnym prastory.

Kožnaj drabničkaj ty varta pašany,
kožnaje słova viakami stvarana.

I na viaki jano žyć zastajecca,
viečnaje tak, jak narodnaje serca."""

def test_classic_2(scheme_classic):
    assert scheme_classic.cyr_to_lat("""Ад родных ніў, ад роднай хаты
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
Цвяток радзімы васілька.""") == """Ad rodnych niŭ, ad rodnaj chaty
U panski dvor dziela krasy
Jany, biazdolnyja, uziaty
Tkać załatyja pajasy.
I ciaham doŭhija časiny,
Dziavočyja zabyŭšy sny,
Svaje šyrokija tkaniny
Na ład piersidski tkuć jany.
A za ścianoj śmiajecca pole,
Zijaje nieba z-za akna, –
I dumki mknucca mimavoli
Tudy, dzie raśćviła viasna;
Dzie blišča zbožža ŭ jasnaj dali,
Siniejuć miła vasilki,
Chałodnym srebram źziajuć chvali
Miž hor lijučajsia raki;
Ciamnieje kraj zubčaty bora...
I tče, zabyŭšysia, ruka,
Zamiž piersidskaha uzora,
Cviatok radzimy vasilka."""

def test_classic_3(scheme_classic):
    assert scheme_classic.cyr_to_lat("""Магутнае слова, ты, роднае слова!
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
       Мілей найбагатшай чужой!""") == """Mahutnaje słova, ty, rodnaje słova!
       Sa mnoj ty na javie i ŭ śnie;
Dušu mnie zatresła pahudkaju novaj,
       Ty piesień naŭčyła mianie.

Biasśmiertnaje słova, ty, rodnaje słova!
       Ty kryŭdy, niapraŭdy zmahło;
Choć hnali ciabie, nakładali akovy,
       Dyj darma: žyvieš jak žyło!

Svabodnaje słova, ty, rodnaje słova!
       Zajhraj ty śmialej, viesialej!
Choć hadziny sykajuć, kružacca sovy,
       Žyvieš ty na chvału ludziej.

Zahnanaje słova, ty, rodnaje słova!
       Hrymi ž nad radzimaj ziamloj:
Što rodnaja mova, choć biednaja mova,
       Milej najbahatšaj čužoj!"""

def test_classic_4(scheme_classic):
    assert scheme_classic.cyr_to_lat("""Несупыннай хваляй плыні
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
І на цёплы кажушок.""") == """Niesupynnaj chvalaj płyni
Za paroju jšła para,
I prabiła čas chłapčynie
Hnać u pole sa dvara.
Jon prasłuchaŭ navučanku,
Jak być dobrym pastuchom,
Spraviŭ puhu-pavivanku,
Vuzły vyviazaŭ hurkom
I pahnaŭ aviečki ŭ pole
Na papary i na roli.
Jon ciapier hladzieŭ bolš stała:
Jon – asoba, pastušok,
Navat prava mieŭ na sała
I na ciopły kažušok."""

def test_classic_5(scheme_classic):
    assert scheme_classic.cyr_to_lat("""Я бачыў, як змяняе дзень
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
неба, небяспечна.""") == """Ja bačyŭ, jak źmianiaje dzień
Vakoł mianie huki na koler,
Jak niebaschił pakinuŭ cień,
Hłytajučy słova «nikoli».
Ja bačyŭ praz tuman vačej
Usio čaściej cichaje «Chopić!».
Viadzi mianie. Hladzi ŭ mianie.
Nie viedaju, dzie my i chto ty.

Bajuś ciabie! Bajuś ciabie!
I mnie ciapier niemahčyma źbiehčy
Ad chutkich snoŭ tvaich, ale
Mnie być z taboj, nieba, niebiaśpiečna.

Ja bačyŭ, jak viartaje čas
Zimovych nas, tolki na poŭdzień,
Dzie pramiani nie pra mianie
Zryvajuć dach, nibyta złodziej.
Ja bačyŭ, jak jaje dałoń
zdymaje bol siarod pustečy
Ratuj mianie! Ratuj mianie!
Ja viedaju, što budzie lepšym.

Bajuś ciabie! Bajuś ciabie!
I mnie ciapier niemahčyma źbiehčy
Ad chutkich snoŭ tvaich, ale
Mnie być z taboj, nieba, niebiaśpiečna.
nieba, niebiaśpiečna
nieba, niebiaśpiečna
nieba, niebiaśpiečna.
Bajuś ciabie! Bajuś ciabie!
I mnie ciapier niemahčyma źbiehčy
Ad chutkich snoŭ tvaich, ale
Mnie być z taboj.
Bajuś ciabie! Bajuś ciabie!
I mnie ciapier niemahčyma źbiehčy
Ad chutkich snoŭ tvaich, ale
Mnie być z taboj, nieba, niebiaśpiečna.
nieba, niebiaśpiečna
nieba, niebiaśpiečna
nieba, niebiaśpiečna."""

def test_classic_6(scheme_classic):
    assert scheme_classic.cyr_to_lat("""ДОБРА Ў ПОЛІ: ВОЛІ МНОГА
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
ВЁРСТ НАПЭЎНА БУДЗЕ СТО!""") == """DOBRA Ŭ POLI: VOLI MNOHA
I PRASTORU-ŠYRYNI,
VABIAĆ DALI TAM MAŁOHA,
JAK PRYNADNYJA AHNI.
ŠTO JOSĆ TAM, ZA TYM, UŃ, HAJEM,
DZIE ZLAHLI NIABIOS VIANCY?
NOVY KRAJ I KRAJ ZA KRAJEM
I KRAI VA ŬSIE KANCY!
I SNUJECCA DUMKA TAJA,
KAB PAŠYRYĆ SVOJ PRASTOR;
DUMKA ŬSIUDY ZALATAJE:
ZA SIAŁO, ZA CHVALI HOR
I NA CHMARKI KINIE VOKA,
ŠTO, JAK HUSAŃKI, PŁYLI,
ZAPYTAJE, JAK DALOKA
TOJE SONCA AD ZIAMLI.
JAK HŁYBOK TOJ PRASTOR NIEMY,
I CI MIERYŬ JAHO CHTO?
I ADKAŽA PA-SVAJEMU:
VIORST NAPEŬNA BUDZIE STO!"""

def test_classic_7(scheme_classic):
    assert scheme_classic.cyr_to_lat("""І ЯШЧЭ БЫЛО ЧЫМ МІЛА
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
ЎСЁ ЦІКАВІЛА ЯГО.""") == """I JAŠČE BYŁO ČYM MIŁA
TOJE POLE CHŁAPČUKU,
HETA TYM, ŠTO DZIED KURYŁA
TAM JAHO TRYMAŬ RUKU.
HETY DZIED – PASTUCH HURTOVY,
SŁAŬNY DZIED, DZIADOK – DUŠA,
HAVARKI, MASTAK NA SŁOVY,
I LUBIŬ JON MAŁYŠA!
NIE SMIAJAŬSIA DZIED Z SYMONKI,
NIE ŬSČUVAŬ JAHO NI-NI,
ČASTAVAŬ Z SVAJE SKARBONKI,
BAVIŬ CEŁYJA Z IM DNI.
ZABIARUCCA Ŭ CIEŃ PAD HRUŠU
I HAVORKU RASPAČNUĆ.
TUT SYMONKA SVAJU DUŠU
MOH PRAD DZIEDAM RAZHARNUĆ,
ZAPYTAĆ PRA SIOJE-TOJE
DZIEDKU DOBRAHA SVAJHO,
BO SYMON NIE MIEŬ SPAKOJU –
ŬSIO CIKAVIŁA JAHO."""

def test_classic_7(scheme_classic):
    assert scheme_classic.cyr_to_lat("гузік ганак гонт мазгі нягеглы") == "guzik ganak gont mazgi niagiegły"

def test_classic_8(scheme_classic):
    assert scheme_classic.cyr_to_lat("ГУЗІК ГАНАК ГОНТ МАЗГІ НЯГЕГЛЫ") == "GUZIK GANAK GONT MAZGI NIAGIEGŁY"

def test_classic_9(scheme_classic):
    assert scheme_classic.cyr_to_lat("НЕ ДЗЕ НЕДЗЕ") == "NIE DZIE NIEDZIE"
