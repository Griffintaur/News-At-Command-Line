# -*- coding: utf-8 -*-
"""
Created on  Jul 24 20:01:34 2016-2017

@author: Ankit Singh
"""

import requests
from configReader import ConfigurationReader
from requests import ConnectionError
import sys


class NewsPulling(object):
    """This class is used to pull news from the internet depending on the source specified """

    def __init__(self, newsSource):
        self.Source = newsSource

    def PullNews(self):
        Configuration = ConfigurationReader()
        self.__APIKey = Configuration.GetAPIKEY()
        self.__Limit = Configuration.GetLimit()
        url = 'https://newsapi.org/v1/articles?source=' + \
            self.Source + '&sortBy=top&apiKey=' + self.__APIKey
        try:
            req = requests.get(url)
            if(req.status_code == 200):
                return req
            else:
                print "There is some issue in connecting to the internet. Please check your firewall or internet"
        except ConnectionError as e:
            print "A connection Attempt failed"
            print e.message
            sys.exit()

    def JsonRead(self):
        req = self.PullNews()
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
            if needsconversion:
                description = unicode(article['description'], 'utf-8')
                title = unicode(article['title'], 'utf-8')
                Article_url = unicode(article['url'], 'utf-8')
                DateofPublication = unicode(article['publishedAt'], 'utf-8')
                Author = unicode(article['author'], 'utf-8')
                FilteredArticles.append([description,
                                         title,
                                         Article_url,
                                         DateofPublication,
                                         Author])
            else:
                description = article['description']
                title = article['title']
                Article_url = article['url']
                DateofPublication = article['publishedAt']
                Author = article['author']
                FilteredArticles.append([description,
                                         title,
                                         Article_url,
                                         DateofPublication,
                                         Author])
        return FilteredArticles

    def BeautifyArticles(self):
        self.Articles = self.JsonRead()
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
