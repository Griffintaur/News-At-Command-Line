import yaml


class ConfigurationReader:
    def __init__(self):
        with open('config.yml') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.APIKEY = cfg['Apikey']
        self.limit = cfg['Limit']
        self.websites_supported = cfg['WebsiteSupported']
        self.user_agent = cfg.get('User-Agent',
                                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                  ' AppleWebKit/537.36 (KHTML, like Gecko '
                                  'Chrome/59.0.3071.115 Safari/537.36')
