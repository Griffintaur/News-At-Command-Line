# -*- coding: utf-8 -*-
"""
Created on  Jul 24 20:01:34 2016-2017

@author: Ankit Singh

Updated on June 6 2016
@author: Samantha Ryan
"""

import requests
from configReader import ConfigurationReader
from requests import ConnectionError
import sys

class NewsPulling(object):


    """This class is used to pull news from the internet depending on the source specified """
    def __init__(self,newsSource):
        self.Source=newsSource
        Configuration = ConfigurationReader()
        self.__APIKey = Configuration.GetAPIKEY()
        self.__Limit = Configuration.GetLimit()


    # Pulls news stories based on SOURCE -- self.Source will indicate the correctly formatted
    # news source to be included in the URL
    def PullNews(self):

        url='https://newsapi.org/v1/articles?source='+self.Source+'&sortBy=top&apiKey='+self.__APIKey
        try:
            req=requests.get(url)
            if(req.status_code==200):
                return req
            else:
                print "There is some issue in connecting to the internet. Please check your firewall or internet"
        except ConnectionError as e:
            print "A connection Attempt failed"
            print e.message
            sys.exit()


    # Pulls news stories based on TOPIC -- self.Source will indicate the correctly formatted
    # category to be included in the URL
    # Pulling by Topic is limited to US-based news stories
    def PullTopics(self):
        url='https://newsapi.org/v2/top-headlines?country=us&category='+self.Source+'&apiKey='+self.__APIKey
        try:
            req = requests.get(url)
            if (req.status_code == 200):
                return req
            else:
                print "There is some issue in connecting to the internet. Please check your firewall or internet"
        except ConnectionError as e:
            print "A connection Attempt failed"
            print e.message
            sys.exit()



    def JsonSourceRead(self):

        req=self.PullNews()

        # indicate if we need to convert to utf-8
        needsconversion = False
        if req.encoding != 'utf-8':
            needsconversion = True
        req=req.json()
        articles=req['articles']
        noofarticles=len(articles)
        maxarticles=min(noofarticles,self.__Limit)
        
        FilteredArticles=[]
        
        for i in xrange(maxarticles):
            article=articles[i]
            #print article
            if needsconversion:
                description=unicode(article['description'], 'utf-8')
                #print description
                title=unicode(article['title'], 'utf-8')
                Article_url=unicode(article['url'], 'utf-8')
                DateofPublication=unicode(article['publishedAt'], 'utf-8')
                Author=unicode(article['author'], 'utf-8')
                FilteredArticles.append([description,title,Article_url,DateofPublication,Author])
            else:
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


    def JsonTopicRead(self):

        req = self.PullTopics()

        # indicate if we need to convert to utf-8
        needsconversion = False
        if req.encoding != 'utf-8':
            needsconversion = True
        req = req.json()
        articles = req['articles']
        noofarticles = len(articles)
        maxarticles = min(noofarticles, self.__Limit)

        FilteredArticles = []

        for i in xrange(maxarticles):
            article = articles[i]
            # print article
            if needsconversion:
                description = unicode(article['description'], 'utf-8')
                # print description
                title = unicode(article['title'], 'utf-8')
                Article_url = unicode(article['url'], 'utf-8')
                DateofPublication = unicode(article['publishedAt'], 'utf-8')
                Author = unicode(article['author'], 'utf-8')
                FilteredArticles.append([description, title, Article_url, DateofPublication, Author])
            else:
                description = article['description']
                # print description
                title = article['title']
                Article_url = article['url']
                DateofPublication = article['publishedAt']
                Author = article['author']
                FilteredArticles.append([description, title, Article_url, DateofPublication, Author])
        return FilteredArticles


        
    def BeautifySourceArticles(self):
        self.Articles=self.JsonSourceRead()
        if self.Articles is None or len(self.Articles)==0:
            print "No articles found"
            sys.exit()
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
        print "***************************************************************"
        return self.Articles

    def BeautifyTopicArticles(self):
        self.Articles = self.JsonTopicRead()
        if self.Articles is None or len(self.Articles) == 0:
            print "No articles found"
            sys.exit()
        print "=================STORIES=================================="
        for i in xrange(len(self.Articles)):
            print "[" + str(i) + "]",
            # print(sequence,end='') used for python 3.x
            if self.Articles[i][1] is not None:
                print "\t" + self.Articles[i][1]
            if self.Articles[i][0] is not None:
                print "\t" + self.Articles[i][0]
            if self.Articles[i][4] is not None:
                print "\t" + self.Articles[i][4]
            if self.Articles[i][3] is not None:
                print "\t" + self.Articles[i][3] + "\n"
        print "***************************************************************"
        return self.Articles
        
        
