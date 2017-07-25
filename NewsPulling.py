# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:01:34 2017

@author: 310247467
"""

import requests
from configReader import ConfigurationReader

class NewsPulling(object):
    """This class is used to pull news from the internet depending on the source specified """
    def __init__(self,newsSource):
        self.Source=newsSource
        
    def PullNews(self):
        Configuration = ConfigurationReader()
        self.__APIKey=Configuration.GetAPIKEY()
        self.__Limit=Configuration.GetLimit()
        url='https://newsapi.org/v1/articles?source='+self.Source+'&sortBy=top&apiKey='+self.__APIKey
        req=requests.get(url)
        #if(req.status_code==200):
            #print req.json()   
        return req
    
    def JsonRead(self):
        req=self.PullNews()
        req=req.json()
        articles=req['articles']
        noofarticles=len(articles)
        maxarticles=min(noofarticles,self.__Limit)
        
        FilteredArticles=[]
        
        for i in xrange(maxarticles):
            article=articles[i]
            #print article
            description=article['description']
            #print description
            title=article['title']
            Article_url=article['url']
            DateofPublication=article['publishedAt']
            Author=article['author']
            FilteredArticles.append([description,title,Article_url,DateofPublication,Author])
        return FilteredArticles
            
        #jsondict=json.load(req.json())
        #print jsondict
        
    def BeautifyArticles(self):
        self.Articles=self.JsonRead()
        print "=================STORIES=================================="
        for i in xrange(len(self.Articles)):
            print "[" +str(i) +"]",
           # print(sequence,end='') used for python 3.x
            if self.Articles[i][1] is not None:
                print "\t"+self.Articles[i][1]
            if self.Articles[i][0] is not None:
                print "\t"+self.Articles[i][0]
            if self.Articles[i][4] is not None:
                print "\t"+self.Articles[i][4]
            if self.Articles[i][3] is not None:
                print "\t"+self.Articles[i][3]+"\n"
        print "==========================================================="
        return self.Articles 
    
        
        
        
