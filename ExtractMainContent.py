# -*- coding: utf-8 -*-
"""
Created on  Jul 24 21:42:05 2016-2017

@author: 310247467
"""
import requests
from configReader import ConfigurationReader
from Extractor import *


class ExtractMainContent(object):
    
    def __init__(self,source,articleurl):
        self.extractorlist=[HuffingtonPost(),NYT(),BBC(),BloomBerg(),Guardian(),TheHindu(),TimesOfIndia()]
        websites=ConfigurationReader().GetWebsiteSupported()
        self.Mapping={}
        for index,website in enumerate(websites):
            self.Mapping[website]=self.extractorlist[index]
        self.Source=source
        self.url=articleurl
        
        
    def DownloadContent(self):
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        req=requests.get(self.url,headers=headers)
        return req.text
    
    def AddExtractorList(self,extractor):
        self.extractorlist.append(extractor)
    
    def Extract(self):
        self.ExtractStrategy=self.Mapping[self.Source]
        text=self.DownloadContent()
        return self.ExtractStrategy.ExtractionAlgo(text)
    
    def Beautify(self):
        title,output=self.Extract()            
        print "=========================================================================="
        print title
        print "=========================================================================="
        print output
        print "*********************************************************************************"
        print "\n\n"
        if len(output) == 0:
            print "There isn't much on the site .It is media(video/image) post.To further view the media post Go to the below link"
            print self.url
            print "*********************************************************************************"
            print "\n\n"
            
        
    
    
    
