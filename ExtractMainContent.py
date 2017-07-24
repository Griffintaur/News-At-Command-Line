# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:42:05 2017

@author: 310247467
"""
import requests
from configReader import ConfigurationReader
from Extractor import * 


class ExtractMainContent(object):
    
    def __init__(self,source,articleurl):
        self.extractorlist=[HuffingtonPost()]
        websites=ConfigurationReader().GetWebsiteSupported()
        self.Mapping={}
        for index,website in enumerate(websites):
            self.Mapping[website]=extractorlist[index]
        self.Source=source
        self.url=articleurl
        
        
    def DownloadContent():
        req=requests.get(self.url)
        return req.text()
    
    def AddExtractorList(self,extractor):
        self.extractorlist.append(extractor)
    
    def Extract(self):
        self.ExtractStrategy=self.Mapping[self.Source]
        text=self.DownloadContent()
        self.ExtractStrategy.ExtractionAlgo(text)
    
    
    
