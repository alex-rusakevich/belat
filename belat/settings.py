import importlib
import logging.config
import os
import sys
from pathlib import Path
from typing import Dict, Optional

from dotenv import load_dotenv

from belat.schemes import Scheme

load_dotenv("./.env", verbose=True)

BASE_DIR: Path = Path(
    os.environ.get("BELAT_BASE_DIR", os.path.join(os.path.expanduser("~"), ".belat"))
)

DEBUG: bool = os.environ.get("BELAT_DEBUG", False) in ["t", True, "true"]

LOG_LVL: str = "DEBUG" if DEBUG else "INFO"

LOG_DIR: Path = Path(os.path.join(BASE_DIR, "logs"))

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "default": {
            "level": LOG_LVL,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "belat.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 2,
            "formatter": "standard",
            "encoding": "utf8",
        },
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {"handlers": ["default", "console"], "level": LOG_LVL, "propagate": False},
        "invoke": {"handlers": ["default", "console"], "level": "WARNING"},
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

BASE_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.config.dictConfig(LOGGING)

logger = logging.getLogger(__name__)

schemes_dict = {}
for scheme_module in SCHEME_MODULES:
    try:
        lib = importlib.import_module("belat.schemes." + scheme_module)
        scheme = lib.Scheme()
        schemes_dict[scheme_module] = scheme

        logger.info(f"Loaded '{scheme_module}' ('{scheme.name}')")
    except Exception as e:
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


RESOURCE_PATH = Path(getattr(sys, "_MEIPASS", os.path.abspath(".")))
