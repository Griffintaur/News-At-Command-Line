# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 23:05:13 2017

@author: 310247467
"""
from bs4 import BeautifulSoup

class Extractor(object):
    
    def ExtractionAlgo(self,text):
        pass
    
    
    
class HuffingtonPost(Extractor):
    def ExtractionAlgo(self,text):
        soup = BeautifulSoup(text, 'html.parser')
        print soup.title.string
        maincontent= soup.find_all("div", class_="entry__body post-contents")
        print maincontent
        

class NYT(Extractor):
    def ExtractionAlgo(self,text):
        soup = BeautifulSoup(text, 'html.parser')
        print soup.title.string
        pass
        
class Guardian(Extractor):
    def ExtractionAlgo(self,text):
        soup = BeautifulSoup(text, 'html.parser')
        print soup.title.string
        pass
        

        