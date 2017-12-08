# -*- coding: utf-8 -*-
"""
Created on  Dec 5 '17

@author: Andres Rivero
"""
import os
import sys
import json
import textwrap

class Article(object):
    """ Article defines an article object.
    Articles are composed of its title and content.
    """
    def __init__(self, fileName):
        self.path = fileName
        with open(fileName) as f:
            self.data = json.load(f)
        self.textWrap=textwrap.TextWrapper(initial_indent='\t',subsequent_indent='\t',width=100)

    def __str__(self):
        foo = self.data.get('title', "No Title")
        bar = foo.encode('ascii', 'ignore').decode('ascii')
        return bar

    def getPath(self):
        return self.path

    def getTitle(self):
        """getTitle()
        return: (string) title name of article
        """
        return self.data.get('title', "")

    def getContent(self):
        """getContent()
        return: (string) full content of article (if available)
        """
        return self.data.get('content', "")

    def getUrl(self):
        """getUrl()
        return: (string) saved url for article
        """
        return self.data.get('url', "")

    def delete(self):
        print "path is: %s" %self.path
        if os.path.exists(self.path):
            print "it exists"
            os.remove(self.path)

    def prettyPrint(self):
        """prettyPrint()
        uses textwrap to wrap whole content in terminal screen
        """
        print "=========================================================================="
        print "\t"+self.getTitle()
        print "=========================================================================="
        print(self.textWrap.fill(self.getContent())) #wrap of the line
        print "\n\n%s" %self.getUrl()
        print "*********************************************************************************"
        print "\n\n"

class SavedArticle(object):
    """SavedArticle defines an object list with articles.
    The saved articles are stored under <path>/saved, where path
    is the location where the script executes.
    """
    def __init__(self):
        self.folderPath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'saved'))
        self.savedArticleList = list()
        
    def loadArticle(self, index):
        return self.savedArticleList[index]

    def getFolderPath(self):
        return self.folderPath
    
    def getSavedArticleList(self):
        self.savedArticleList = self.fillSavedArticleList()
        return self.savedArticleList

    def printSavedArticleMenu(self):
        articleList = self.getSavedArticleList()
        for i, v in enumerate(articleList):
            print "[%d]\t'%s" %(i, v)
        print("Please enter the index of the news source")
        print("Press 66 to go back")
        print("Press 99 to quit")

    def fillSavedArticleList(self):
        """fillSavedArticle()
        Checks the files in /saved folder and appends to savedList
        if the file was not already in the list.
        """
        if not os.path.exists(self.folderPath):
            os.makedirs(self.folderPath)
        if len(os.listdir(self.folderPath)) == 0:
            print "\n\t\tEmpty folder\n"
        for f in os.listdir(self.folderPath):
            thisPathName = os.path.abspath(os.path.dirname(__file__))
            filePath = os.path.join(thisPathName, 'saved', f)
            article = Article(filePath)
            #if article not in self.savedArticleList:
            if not any(x for x in self.savedArticleList if x.getPath() == filePath):
                self.savedArticleList.append(article)
        return self.savedArticleList

    def mainLoop(self):
        """mainLoop()
        prints the list of articles that are saved, then asks for user input
        to select article to read, or go back to main menu. if article is selected
        it prints it to the terminal
        """
        self.printSavedArticleMenu()
        articleList = self.getSavedArticleList()
        savedSourceNumber=raw_input("Saved Source Number >>>> ")
        if not savedSourceNumber.isdigit():
            raise ValueError("value '%s' cannot be converted to integer" %savedSourceNumber)
        savedSourceNumber = int(savedSourceNumber)
        if savedSourceNumber == 99:
            sys.exit()
        elif savedSourceNumber == 66:
            raise Exception("going to back to main menu")
        
        if savedSourceNumber < 0 or savedSourceNumber > len(articleList) - 1:
            raise ValueError("value '%d' is not a valid saved source number" %savedSourceNumber)
        else:
            article = articleList[savedSourceNumber]
            article.prettyPrint()
            YesorNo = int(raw_input("Press 1 to delete article else press 0 to continue >>> "))
            if YesorNo == 1:
                    del self.savedArticleList[self.savedArticleList.index(article)]
                    article.delete()