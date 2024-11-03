import importlib
import logging
import sys
from typing import Dict, Optional


class Scheme:
    name = "Scheme"
    src = "localhost"

    def __init__(self):
        pass

    def cyr_to_lat(self, text_in):
        pass

    def lat_to_cyr(self, text_in):
        pass


class Rule:
    def __init__(self):
        pass

    def work_with(self, text, pos, regexp):
        pass


SCHEME_MODULES = (
    "official",
    "gost1687671tb1",
    "gost1687671tb2",
    "gost7792000sysa",
    "gost7792000sysb",
    "classic",
)

logger = logging.getLogger(__name__)

schemes_dict = {}
for scheme_module in SCHEME_MODULES:
    try:
        lib = importlib.import_module("belat.schemes." + scheme_module)
        scheme = lib.Scheme()
        schemes_dict[scheme_module] = scheme

        logger.info(f"Loaded '{scheme_module}' ('{scheme.name}')")
    except Exception:
        logger.exception(f"Cannot load scheme '{scheme_module}'")
        sys.exit(-1)

SCHEMES: Dict[str, Scheme] = schemes_dict


def get_scheme_by_name(scheme_name: str) -> Optional[Scheme]:
    """Get scheme by it's `.name` property

    :param scheme_name: `.name` value of the searched scheme
    :type scheme_name: str
    :return: :class:`belat.schemes.Scheme` if found, `None` otherwise
    :rtype: Optional[Scheme]
    """
    global SCHEMES

    for v in SCHEMES.values():
        if v.name == scheme_name:
            return v

    return None
