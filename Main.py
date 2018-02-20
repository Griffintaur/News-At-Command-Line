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
from lazyme.string import color_print


def NewsSources():
    NewsSources=ConfigurationReader().GetWebsiteSupported()
    return NewsSources

def App():
    newsSources=NewsSources()
    while True:
        for i in xrange(len(newsSources)):
            color_print ("["+str(i)+"]" +"\t" +newsSources[i],color='yellow')
        color_print ("Please enter the index of the news source or press 99 to quit", color='red')
        try:
            color_print("News Source Number >>>> ",color="red")
            newsSourceNumber=raw_input()
        except ValueError:  
            color_print ("That is not a valid News Source Number", color='red')
        newsSourceNumber=int(newsSourceNumber)
        if newsSourceNumber==99:
            sys.exit()
        if (newsSourceNumber >=len(newsSources)):
            color_print ("Please select the index no less than "+ str(len(newsSources)), color='red')  
        obj=NewsPulling(newsSources[newsSourceNumber])
        Articles=obj.BeautifyArticles();   
        while True:
            color_print ("Do you want to read any story further? If yes, please select the number corresponding to the article", color='red')
            color_print ("Press 66 to go back to the main menu", color='red')
            color_print ("Press 99 to quit", color='red')
            try:
                articleNumber=raw_input("Article No >>>> ")
            except ValueError:
                color_print ("That is not a valid Article Number", color='red')
            articleNumber=int(articleNumber)
            if articleNumber==99 :
                sys.exit()
            elif articleNumber==66 :
                break
            elif (articleNumber >= len(Articles)):
                color_print ("Please select the index no less than "+ str(len(Articles)), color='red')
            #color_print Articles[articleNumber][2]
            else:
                extr=ExtractMainContent(newsSources[newsSourceNumber],Articles[articleNumber][2])
                extr.Beautify()
                color_print ("Do you want to save this article in file", color='red')
                YesorNo = int(raw_input("Press 1 to save else press 0 to continue >>> "))
                if YesorNo == 1:
                    extr.FileSave()
                    

if __name__== "__main__":
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    App();
