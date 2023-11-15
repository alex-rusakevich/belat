import logging
import os

import belat.settings

logger = logging.getLogger(__name__)

CURR_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

__version__ = (
    open(os.path.join(CURR_SCRIPT_DIR, "VERSION.txt"), "r", encoding="utf8")
    .read()
    .strip()
)

logger.info(
    f"Loaded belat v{__version__} in {'debug' if belat.settings.DEBUG else 'production'} mode"
)
