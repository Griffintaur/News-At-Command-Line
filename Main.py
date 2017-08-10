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
            print "["+str(i)+"]" +"\t" +newsSources[i]
        print "Please enter the index of the news source or press 99 to quit"

        sourceNumberOkay = False
        while sourceNumberOkay == False:
            try:
                newsSourceNumber=raw_input("News Source Number >>>>")
                newsSourceNumber=int(newsSourceNumber)

                if newsSourceNumber==99:
                    sys.exit()

                if (newsSourceNumber >=len(newsSources)):
                    print "please select an index less than "+ str(len(newsSources))
                else:
                    sourceNumberOkay = True
                
            except ValueError:
                print("That is not a valid News source number")    

        
          
        obj=NewsPulling(newsSources[newsSourceNumber])
        Articles=obj.BeautifyArticles();   
        while True:
            print """Do you want to read any story further?.if yes,Please Select the Number corresponding to the article """
            print "Press 66 to go back to the main menu"
            print "Press 99 to quit"
            
            articleNumberOkay = False
            while articleNumberOkay == False:
                try:
                    articleNumber=raw_input("Article No >>>>")
                    articleNumber=int(articleNumber)

                    if articleNumber==99 :
                        sys.exit()
                    if articleNumber==66 :
                        break

                    if (articleNumber >= len(Articles)):
                        print "please select an index less than "+ str(len(Articles))
                    else:
                        articleNumberOkay = True

                except ValueError:
                    print ("That's not a valid article number")

            
            
            
            #print Articles[articleNumber][2]
            extr=ExtractMainContent(newsSources[newsSourceNumber],Articles[articleNumber][2])
            extr.Beautify()
                    

if __name__== "__main__":
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    App();
