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

        # TODO: Move to using this, and reading it from env, config, defaults
        self.user_agent = cfg.get('User-Agent',
                                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                  ' AppleWebKit/537.36 (KHTML, like Gecko '
                                  'Chrome/59.0.3071.115 Safari/537.36')
