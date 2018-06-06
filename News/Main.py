# -*- coding: utf-8 -*-
"""
Created on Jul 24 16:15:11 2016-2017

@author: Ankit Singh

Updated on June 6 2016
@author: Samantha Ryan
"""
from NewsPulling import NewsPulling
from configReader import ConfigurationReader
from ExtractMainContent import ExtractMainContent
import sys
import codecs


def NewsSources():
    NewsSources=ConfigurationReader().GetWebsiteSupported()
    return NewsSources

def NewsTopics():
    NewsTopics=ConfigurationReader().GetTopicsSupported()
    return NewsTopics

def Source():
    newsSources=NewsSources()

    while True:
        for i in xrange(len(newsSources)):
            print ("["+str(i)+"]" +"\t" +newsSources[i])
        print ("Please enter the index of the news source")
        print( "Press 99 to quit")
        print( "Press 66 to return to main menu")
        try:
            newsSourceNumber=raw_input("News Source Number >>>> ")
        except ValueError:  
            print ("That is not a valid News Source Number")
        newsSourceNumber=int(newsSourceNumber)
        if newsSourceNumber==99:
            sys.exit()
        if newsSourceNumber==66:
            Choice()
        if (newsSourceNumber >=len(newsSources)):
            print ("Please select the index no less than "+ str(len(newsSources)))  
        obj=NewsPulling(newsSources[newsSourceNumber])
        Articles=obj.BeautifySourceArticles();
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

def Topic():
    newsTopics = NewsTopics()

    while True:
        for i in xrange(len(newsTopics)):
            print ("[" + str(i) + "]" + "\t" + newsTopics[i])
        print ("Please enter the index of the news topic")
        print("Press 99 to quit")
        print("Press 66 to return to main menu")
        try:
            newsTopicNumber = raw_input("News Topic Number >>>> ")
        except ValueError:
            print ("That is not a valid News Source Number")
        newsTopicNumber = int(newsTopicNumber)
        if newsTopicNumber == 99:
            sys.exit()
        if newsTopicNumber == 66:
            Choice()
        if (newsTopicNumber >= len(newsTopics)):
            print ("Please select the index no less than " + str(len(newsTopics)))
        obj = NewsPulling(newsTopics[newsTopicNumber])
        Articles = obj.BeautifyTopicArticles();
        while True:
            print (
                "Do you want to read any story further? If yes, please select the number corresponding to the article")
            print ("Press 66 to go back to the main menu")
            print ("Press 99 to quit")
            try:
                articleNumber = raw_input("Article No >>>> ")
            except ValueError:
                print ("That is not a valid Article Number")
            articleNumber = int(articleNumber)
            if articleNumber == 99:
                sys.exit()
            elif articleNumber == 66:
                break
            elif (articleNumber >= len(Articles)):
                print ("Please select the index no less than " + str(len(Articles)))
            # print Articles[articleNumber][2]
            else:
                extr = ExtractMainContent(newsTopics[newsTopicNumber], Articles[articleNumber][2])
                extr.Beautify()
                print ("Do you want to save this article in file")
                YesorNo = int(raw_input("Press 1 to save else press 0 to continue >>> "))
                if YesorNo == 1:
                    extr.FileSave()


def Choice():
    print ("How would you like to read your news?\n\n")
    print ("[0] By News Source")
    print ("[1] By News Topic")
    print ("[99] To Quit")

    try:
        choice = raw_input(">>>> ")
    except ValueError:
        print ("That is not a valid Option")
    choice = int(choice)
    if choice == 99:
        sys.exit()
    if choice == 0:
        Source()
    if choice == 1:
        Topic()



def Main():
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    Choice()


if __name__ == '__main__':
    Main()
