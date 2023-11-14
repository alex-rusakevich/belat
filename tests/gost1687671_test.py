import pytest

import belat.gost1687671tb1 as bgtb1
import belat.gost1687671tb2 as bgtb2


@pytest.fixture
def dubouka_cyr():
    return """Родная мова, цудоўная мова!
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


@pytest.fixture
def dubouka_lat1():
    return """Rodnaja mova, cudoŭnaja mova!
Ty našyh dumak utok i asnova!

Matčyn darunak ad samaj kalyski,
ty samacvjetaŭ jaskravaja nizka.

Kožny z ih barvy dzivosnyja maje,
vječnym agnem zihacic' - nje zgaraje.

Ty mnje zaŭsedy byla dapamogaj,
dzje b i jakoj ni hadziŭ ja darogaj.

Čuju ŭ tabje pjerazvony krynicy,
čuju ŭ tabje i raskat naval'nicy,

čuju pavjevy zjalenaga boru,
vodgullje pracy u rodnym prastory.

Kožnaj drabničkaj ty varta pašany,
kožnaje slova vjakami stvarana.

Ì na vjaki jano žyc' zastajecca,
vječnaje tak, jak narodnaje sèrca."""


@pytest.fixture
def dubouka_lat2():
    return """Rodnaja mova, cudouhnaja mova!
Ty nashykh dumak utok ih asnova!

Matchyn darunak ad samajj kalyskih,
ty samacvetauh jaskravaja nihzka.

Kozhny z ihkh barvy dzihvosnyja mae,
vechnym agnjom zihkhacihc' - ne zgarae.

Ty mne zauhsjody byla dapamogajj,
dze b ih jakojj nih khadzihuh ja darogajj.

Chuju uh tabe perazvony krynihcy,
chuju uh tabe ih raskat naval'nihcy,

chuju pavevy zjaljonaga boru,
vodgulle pracy u rodnym prastory.

Kozhnajj drabnihchkajj ty varta pashany,
kozhnae slova vjakamih stvarana.

Ih na vjakih jano zhyc' zastaecca,
vechnae tak, jak narodnae sehrca."""


@pytest.fixture
def scheme_tb1():
    return bgtb1.Scheme(print)


@pytest.fixture
def scheme_tb2():
    return bgtb2.Scheme(print)


# Тэст на транслітэрацыю з кір у лат
def test_gost16_tb1_1(dubouka_cyr, dubouka_lat1, scheme_tb1):
    assert scheme_tb1.cyr_to_lat(dubouka_cyr) == dubouka_lat1


# Тэст з лат у кір
def test_gost16_tb1_2(dubouka_cyr, dubouka_lat1, scheme_tb1):
    assert scheme_tb1.lat_to_cyr(dubouka_lat1) == dubouka_cyr


# Тэст з кір у лат і наадварот
def test_gost16_tb1_3(dubouka_cyr, scheme_tb1):
    assert scheme_tb1.lat_to_cyr(scheme_tb1.cyr_to_lat(dubouka_cyr)) == dubouka_cyr


# Тэст з кір у лат і наадварот
def test_gost16_tb1_4(dubouka_lat1, scheme_tb1):
    assert scheme_tb1.cyr_to_lat(scheme_tb1.lat_to_cyr(dubouka_lat1)) == dubouka_lat1


# ===================================================================================


# Тэст на транслітэрацыю з кір у лат
def test_gost16_tb2_1(dubouka_cyr, dubouka_lat2, scheme_tb2):
    assert scheme_tb2.cyr_to_lat(dubouka_cyr) == dubouka_lat2


# Тэст з лат у кір
def test_gost16_tb2_2(dubouka_cyr, dubouka_lat2, scheme_tb2):
    assert scheme_tb2.lat_to_cyr(dubouka_lat2) == dubouka_cyr


# Тэст з кір у лат і наадварот
def test_gost16_tb2_3(dubouka_cyr, scheme_tb2):
    assert scheme_tb2.lat_to_cyr(scheme_tb2.cyr_to_lat(dubouka_cyr)) == dubouka_cyr


# Тэст з кір у лат і наадварот
def test_gost16_tb2_4(dubouka_lat2, scheme_tb2):
    assert scheme_tb2.cyr_to_lat(scheme_tb2.lat_to_cyr(dubouka_lat2)) == dubouka_lat2
