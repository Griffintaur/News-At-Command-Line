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
            newsSourceNumber=int(newsSourceNumber)
        except ValueError:  
            print ("That is not a valid News Source Number")
        if newsSourceNumber==99:
            sys.exit()
        if (newsSourceNumber >=len(newsSources)):
            print ("Please select the index no less than "+ str(len(newsSources)))  
        obj=NewsPulling(newsSources[newsSourceNumber])
        Articles=obj.BeautifyArticles(); 
        extr = None
        pastarticleNum = -1
        while True:
            print ("Do you want to read any story further? If yes, please select the number corresponding to the article")
            print ("Press 66 to go back to the main menu")
            print ("Press 99 to quit")
            if extr != None:
                print ("Press s to save the article as a file")
            try:
                articleNumber=raw_input("Article No >>>> ")
                articleNumber=int(articleNumber)
            except ValueError:
                if articleNumber == 's' and extr != None:
                        extr.PrintToFile(Articles[pastarticleNum])
                else:
                    print ("That is not a valid Article Number")
                continue
            if articleNumber==99 : # quit the program
                sys.exit()
            if articleNumber==66 : # main menu
                break
            if (articleNumber >= len(Articles)): # invalid article number given
                print ("Please select the index no less than "+ str(len(Articles)))
            else: # valid article number given so proceed with extracting the content
                # index 2 has the article url
                extr = ExtractMainContent(newsSources[newsSourceNumber],Articles[articleNumber][2])
                pastarticleNum = articleNumber
                extr.Beautify()
                    

if __name__== "__main__":
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    App();
