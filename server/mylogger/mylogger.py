import json
import logging.config
import os
from pathlib import Path

LOGGER = logging.getLogger(__name__)


def setup_logging(default_path='logging.json', default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """Setup logging configuration

    http://victorlin-blog.logdown.com/posts/2012/08/26/good-logging-practice-in-python

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def load_logging_config(default_path='logging.json'):
    path = Path(default_path)
    try:
        with open(str(path)) as fl:
            config = json.load(fl)
        logging.config.dictConfig(config)
    except Exception as err:
        LOGGER.error("Failed to load log config: %s", err)
