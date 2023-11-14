import pytest

import belat.gost7792000sysa as bgsysa
import belat.gost7792000sysb as bgsysb


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
    return """Rodnaâ mova, cudoŭnaâ mova!
Ty našyh dumak utok ì asnova!

Matčyn darunak ad samaj kalyskì,
ty samacvetaŭ âskravaâ nìzka.

Kožny z ìh barvy dzìvosnyâ mae,
večnym agnëm zìhacìc´ - ne zgarae.

Ty mne zaŭsëdy byla dapamogaj,
dze b ì âkoj nì hadzìŭ â darogaj.

Čuû ŭ tabe perazvony krynìcy,
čuû ŭ tabe ì raskat naval´nìcy,

čuû pavevy zâlënaga boru,
vodgulle pracy u rodnym prastory.

Kožnaj drabnìčkaj ty varta pašany,
kožnae slova vâkamì stvarana.

Ì na vâkì âno žyc´ zastaecca,
večnae tak, âk narodnae sèrca."""


@pytest.fixture
def dubouka_lat2():
    return """Rodnaya mova, cudou`naya mova!
Ty` nashy`x dumak utok i asnova!

Matchy`n darunak ad samaj kaly`ski,
ty` samacvetau` yaskravaya nizka.

Kozhny` z ix barvy` dzivosny`ya mae,
vechny`m agnyom zixacic` - ne zgarae.

Ty` mne zau`syody` by`la dapamogaj,
dze b i yakoj ni xadziu` ya darogaj.

Chuyu u` tabe perazvony` kry`nicy`,
chuyu u` tabe i raskat naval`nicy`,

chuyu pavevy` zyalyonaga boru,
vodgulle pracy` u rodny`m prastory`.

Kozhnaj drabnichkaj ty` varta pashany`,
kozhnae slova vyakami stvarana.

I na vyaki yano zhy`c` zastaecca,
vechnae tak, yak narodnae se`rca."""


@pytest.fixture
def scheme_sysa():
    return bgsysa.Scheme(print)


@pytest.fixture
def scheme_sysb():
    return bgsysb.Scheme(print)


# Тэст на транслітэрацыю з кір у лат
def test_gost16_sysa_1(dubouka_cyr, dubouka_lat1, scheme_sysa):
    assert scheme_sysa.cyr_to_lat(dubouka_cyr) == dubouka_lat1


# Тэст з лат у кір
def test_gost16_sysa_2(dubouka_cyr, dubouka_lat1, scheme_sysa):
    assert scheme_sysa.lat_to_cyr(dubouka_lat1) == dubouka_cyr


# Тэст з кір у лат і наадварот
def test_gost16_sysa_3(dubouka_cyr, scheme_sysa):
    assert scheme_sysa.lat_to_cyr(scheme_sysa.cyr_to_lat(dubouka_cyr)) == dubouka_cyr


# Тэст з кір у лат і наадварот
def test_gost16_sysa_4(dubouka_lat1, scheme_sysa):
    assert scheme_sysa.cyr_to_lat(scheme_sysa.lat_to_cyr(dubouka_lat1)) == dubouka_lat1


# ===================================================================================


# Тэст на транслітэрацыю з кір у лат
def test_gost16_sysb_1(dubouka_cyr, dubouka_lat2, scheme_sysb):
    assert scheme_sysb.cyr_to_lat(dubouka_cyr) == dubouka_lat2


# Тэст з лат у кір
def test_gost16_sysb_2(dubouka_cyr, dubouka_lat2, scheme_sysb):
    assert scheme_sysb.lat_to_cyr(dubouka_lat2) == dubouka_cyr


# Тэст з кір у лат і наадварот
def test_gost16_sysb_3(dubouka_cyr, scheme_sysb):
    assert scheme_sysb.lat_to_cyr(scheme_sysb.cyr_to_lat(dubouka_cyr)) == dubouka_cyr


# Тэст з кір у лат і наадварот
def test_gost16_sysb_4(dubouka_lat2, scheme_sysb):
    assert scheme_sysb.cyr_to_lat(scheme_sysb.lat_to_cyr(dubouka_lat2)) == dubouka_lat2
