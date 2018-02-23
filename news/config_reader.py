import os
from contextlib import suppress

import yaml
from appdirs import AppDirs

from .__version__ import __app_name__
from .constants import constants

dirs = AppDirs(__app_name__)


class ConfigurationReader:
    def __init__(self):
        try:
            with open(f'{dirs.user_config_dir}/config.yml') as ymlfile:
                cfg = yaml.load(ymlfile)
        except FileNotFoundError:
            with suppress(FileExistsError):
                os.makedirs(dirs.user_config_dir)
            with open(f'{dirs.user_config_dir}/config.yml', 'w') as ymlfile:
                ymlfile.write(yaml.dump(constants['config_defaults']))
            cfg = constants['config_defaults']

        self.APIKEY = cfg['api_key']
        self.limit = cfg['article_limit']
