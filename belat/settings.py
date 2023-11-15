import importlib
import logging.config
import os
import sys
from pathlib import Path

DEBUG = os.environ.get("BELAT_DEBUG", True) in ["t", True, "true"]

LOG_LVL = "DEBUG" if DEBUG else "WARNING"

LOG_DIR = Path(os.path.join(os.path.dirname(__file__), "..", "logs"))

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
            "backupCount": 5,
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
        "": {"handlers": ["default", "console"], "level": LOG_LVL, "propagate": True},
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

LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.config.dictConfig(LOGGING)

logger = logging.getLogger(__name__)

schemes_list = []
for scheme_module in SCHEME_MODULES:
    try:
        lib = importlib.import_module("belat." + scheme_module)
        scheme = lib.Scheme(print)
        schemes_list.append(scheme)

        logger.info(f"Loaded '{scheme_module}' ('{scheme.name}')")
    except Exception as e:
        logger.exception(f"Cannot load scheme '{scheme_module}'")
        sys.exit(-1)

SCHEMES = schemes_list
