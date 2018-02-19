import yaml

# TODO: implement singleton pattern here
class ConfigurationReader():
    __APIKEY=None
    __WebsiteSupported=[]
    __Limit=None
    def __init__(self):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        ConfigurationReader.__APIKEY=cfg['Apikey']
        #print ConfigurationReader.__APIKEY
        ConfigurationReader.__Limit=cfg['Limit']
        #print ConfigurationReader.__Limit
        ConfigurationReader.__WebsiteSupported=cfg['WebsiteSupported']
        #print ConfigurationReader.__WebsiteSupported
    @staticmethod    
    def GetAPIKEY():
        return ConfigurationReader.__APIKEY
    
    @staticmethod
    def GetLimit():
        return ConfigurationReader.__Limit
    
    @staticmethod
    def GetWebsiteSupported():
        return ConfigurationReader.__WebsiteSupported
    
    