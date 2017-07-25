# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 16:15:11 2017

@author: 310247467
"""
from NewsPulling import NewsPulling
from configReader import ConfigurationReader
from ExtractMainContent import ExtractMainContent

def NewsSources():
    NewsSources=ConfigurationReader().GetWebsiteSupported()
    return NewsSources

def App():
    newsSources=NewsSources()
    for i in xrange(len(newsSources)):
        print "["+str(i)+"]" +"\t" +newsSources[i]
    print "Please enter the index of the news source"
    try:
        newsSourceNumber=raw_input()
    except ValueError:  
        print("That is not a valid News source number")
    newsSourceNumber=int(newsSourceNumber)
    if (newsSourceNumber >=len(newsSources)):
        print "please select the index no less than "+ str(len(newsSources))  
    obj=NewsPulling(newsSources[newsSourceNumber])
    Articles=obj.BeautifyArticles();
    print """Do you want to read any story further?.if yes,
    "Please Select the Number corresponding to the article"""
    try:
        articleNumber=raw_input()
    except ValueError:
        print ("That's not a valid article number")
    articleNumber=int(articleNumber)
    if (articleNumber >= len(Articles)):
        print "please select the index no less than "+ str(len(Articles))
    #print Articles[articleNumber][2]
    extr=ExtractMainContent('the-times-of-india',Articles[articleNumber][2])
    extr.Beautify()
                

if __name__== "__main__":
    App();