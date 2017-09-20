# -*- coding: utf-8 -*-
"""
Created on  Jul 24 21:42:05 2016-2017

@author: Ankit Singh
"""
import requests
from configReader import ConfigurationReader
from Extractor import *
import textwrap

class ExtractMainContent(object):
    def __init__(self,source,articleurl):
        self.extractorlist=[HuffingtonPost(),NYT(),BBC(),BloomBerg(),Guardian(),TheHindu(),TimesOfIndia()]
        websites=ConfigurationReader().GetWebsiteSupported()
        self.Mapping={}
        for index,website in enumerate(websites):
            self.Mapping[website]=self.extractorlist[index]
        self.Source=source
        self.url=articleurl
        self.textWrap=textwrap.TextWrapper(initial_indent='\t',subsequent_indent='\t',width=100)
        
        
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
        print "\t"+title
        print "=========================================================================="
        print (self.textWrap.fill(output)) #wrap of the line
        print "*********************************************************************************"
        print "\n\n"
        if len(output) == 0:
            print "There isn't much on the site .It is media(video/image) post.To further view the media post Go to the below link"
            print self.url
            print "*********************************************************************************"
            print "\n\n"

    def FileSave(self):
        title,output=self.Extract()
        article_file = open(title+".txt","w+")
        article_file.write(output.encode('utf-8'))
        article_file.close()
        
    
    
    
