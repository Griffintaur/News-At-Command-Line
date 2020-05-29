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
    __Limit=None
    __ProxyIP=None
    __ProxyPortNumber=None
    def __init__(self):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        ConfigurationReader.__APIKEY=cfg['Apikey']
        #print ConfigurationReader.__APIKEY
        ConfigurationReader.__Limit=cfg['Limit']
        #print ConfigurationReader.__Limit
        ConfigurationReader.__WebsiteSupported=cfg['WebsiteSupported']
        #print ConfigurationReader.__WebsiteSupported
        ConfigurationReader.__ProxyIP = cfg['ProxyIP']
        # print ConfigurationReader.__ProxyIP
        ConfigurationReader.__ProxyPortNumber = cfg['ProxyPortNumber']
        # print ConfigurationReader.__ProxyPortNumber
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
    def GetProxyIP():
        return ConfigurationReader.__ProxyIP

    @staticmethod
    def GetProxyPortNumber():
        return ConfigurationReader.__ProxyPortNumber
    
    