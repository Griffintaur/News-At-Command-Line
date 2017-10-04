# -*- coding: utf-8 -*-
"""
Created on Jul 24 16:15:11 2016-2017

@author: Ankit Singh
"""
from NewsPulling import NewsPulling
from configReader import ConfigurationReader
from ExtractMainContent import ExtractMainContent
import sys
import codecs

EXIT = 99
BACK = 66


def NewsSources():
    NewsSources = ConfigurationReader().GetWebsiteSupported()
    return NewsSources


def App():
    newsSources = NewsSources()
    while True:
        for i, newsSource in enumerate(newsSources):
            print "[%s] \t %s " % (i, newsSource)
        print "Please enter the index of the news source or press 99 to quit"
        try:
            newsSourceNumber = raw_input("News Source Number >>>> ")
        except ValueError:
            print "That is not a valid News Source Number"
        newsSourceNumber = int(newsSourceNumber)
        if newsSourceNumber == EXIT:
            sys.exit()
        if (newsSourceNumber >= len(newsSources)):
            print "Please select the index no less than %s" % len(newsSources)
        obj = NewsPulling(newsSources[newsSourceNumber])
        Articles = obj.BeautifyArticles()
        while True:
            print "Do you want to read any story further? If yes, please select the number corresponding to the article"
            print "Press 66 to go back to the main menu"
            print "Press 99 to quit"
            try:
                articleNumber = int(raw_input("Article No >>>> "))
            except ValueError:
                print("That is not a valid Article Number")
                continue
            if articleNumber == EXIT:
                sys.exit()
            elif articleNumber == BACK:
                break
            elif articleNumber >= len(Articles):
                print "Please select the index no less than %s" % len(Articles)
            else:
                extr = ExtractMainContent(newsSources[newsSourceNumber],
                                          Articles[articleNumber][2])
                extr.Beautify()
                print("Do you want to save this article in file")
                YesorNo = int(raw_input("Press 1 to save else press 0 to continue >>> "))
                if YesorNo == 1:
                    extr.FileSave()


if __name__ == "__main__":
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    App()
