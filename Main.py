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


def NewsSources():
    NewsSources=ConfigurationReader().GetWebsiteSupported()
    return NewsSources

def App():
    newsSources=NewsSources()
    while True:
        for i in xrange(len(newsSources)):
            print ("["+str(i)+"]" +"\t" +newsSources[i])
        print ("Please enter the index of the news source or press 99 to quit")
        try:
            newsSourceNumber=raw_input("News Source Number >>>> ")
        except ValueError:  
            print ("That is not a valid News Source Number")
        newsSourceNumber=int(newsSourceNumber)
        if newsSourceNumber==99:
            sys.exit()
        if (newsSourceNumber >=len(newsSources)):
            print ("Please select the index no less than "+ str(len(newsSources)))  
        obj=NewsPulling(newsSources[newsSourceNumber])
        Articles=obj.BeautifyArticles();   
        while True:
            print ("Do you want to read any story further? If yes, please select the number corresponding to the article")
            print ("Press 66 to go back to the main menu")
            print ("Press 99 to quit")
            try:
                articleNumber=raw_input("Article No >>>> ")
            except ValueError:
                print ("That is not a valid Article Number")
            articleNumber=int(articleNumber)
            if articleNumber==99 :
                sys.exit()
            elif articleNumber==66 :
                break
            elif (articleNumber >= len(Articles)):
                print ("Please select the index no less than "+ str(len(Articles)))
            #print Articles[articleNumber][2]
            else:
                extr=ExtractMainContent(newsSources[newsSourceNumber],Articles[articleNumber][2])
                extr.Beautify()
                print ("Do you want to save this article in file")
                YesorNo = int(raw_input("Press 1 to save else press 0 to continue >>> "))
                if YesorNo == 1:
                    extr.FileSave()
                    

if __name__== "__main__":
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    App();
