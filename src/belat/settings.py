import importlib
import logging.config
import os
import sys
from typing import Dict, Optional

from belat.schemes import Scheme

DEBUG: bool = os.environ.get("BELAT_DEBUG", False) in ["t", True, "true"]

LOG_LVL: str = "DEBUG" if DEBUG else "INFO"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {"handlers": ["default"], "level": LOG_LVL, "propagate": False},
        "invoke": {"handlers": ["default"], "level": "WARNING"},
    },
}

SCHEME_MODULES = (
    "official",
    "gost1687671tb1",
    "gost1687671tb2",
    "gost7792000sysa",
    "gost7792000sysb",
    "classic",
)

logging.config.dictConfig(LOGGING)

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
