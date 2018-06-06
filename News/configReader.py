# -*- coding: utf-8 -*-
"""
Created on  Jul 24 20:14:29 2016-2017

@author: Ankit Singh
"""
import yaml

##to do
#implement singleton pattern here
class ConfigurationReader():
    __APIKEY=None
    __WebsiteSupported=[]
    __TopicsSupported=[]
    __Limit=None
    def __init__(self):
        with open("/Users/Stormy/PycharmProjects/News-At-Command-Line/config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        ConfigurationReader.__APIKEY=cfg['Apikey']
        #print ConfigurationReader.__APIKEY
        ConfigurationReader.__Limit=cfg['Limit']
        #print ConfigurationReader.__Limit
        ConfigurationReader.__WebsiteSupported=cfg['WebsiteSupported']
        #print ConfigurationReader.__WebsiteSupported
        ConfigurationReader.__TopicsSupported=cfg['TopicsSupported']
    @staticmethod    
    def GetAPIKEY():
        return ConfigurationReader.__APIKEY
    
    @staticmethod
    def GetLimit():
        return ConfigurationReader.__Limit
    
    @staticmethod
    def GetWebsiteSupported():
        return ConfigurationReader.__WebsiteSupported

    @staticmethod
    def GetTopicsSupported():
        return ConfigurationReader.__TopicsSupported
    
    