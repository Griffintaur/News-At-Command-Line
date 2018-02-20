import yaml


class ConfigurationReader:
    def __init__(self):
        with open('config.yml') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.APIKEY = cfg['Apikey']
        self.limit = cfg['Limit']
        self.websites_supported = cfg['WebsiteSupported']
