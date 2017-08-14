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
import signal

def signal_handler(signal, frame):
        print('\nExiting gracefully')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def NewsSources():
    NewsSources=ConfigurationReader().GetWebsiteSupported()
    return NewsSources

def App():
    newsSources=NewsSources()
    while True:
        for i in xrange(len(newsSources)):
            print "["+str(i)+"]" +"\t" +newsSources[i]
        print "Please enter the index of the news source or press 99 to quit"
        try:
            newsSourceNumber=raw_input("News Source Number >>>>")
        except ValueError:  
            print("That is not a valid News source number")
        newsSourceNumber=int(newsSourceNumber)
        if newsSourceNumber==99:
            sys.exit()
        if (newsSourceNumber >=len(newsSources)):
            print "please select the index no less than "+ str(len(newsSources))  
        obj=NewsPulling(newsSources[newsSourceNumber])
        Articles=obj.BeautifyArticles();   
        while True:
            print """Do you want to read any story further?.if yes,Please Select the Number corresponding to the article """
            print "Press 66 to go back to the main menu"
            print "Press 99 to quit"
            try:
                articleNumber=raw_input("Article No >>>>")
            except ValueError:
                print ("That's not a valid article number")
            articleNumber=int(articleNumber)
            if articleNumber==99 :
                sys.exit()
            if articleNumber==66 :
                break
            if (articleNumber >= len(Articles)):
                print "please select the index no less than "+ str(len(Articles))
            #print Articles[articleNumber][2]
            extr=ExtractMainContent(newsSources[newsSourceNumber],Articles[articleNumber][2])
            extr.Beautify()
                    

if __name__== "__main__":
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    App();
