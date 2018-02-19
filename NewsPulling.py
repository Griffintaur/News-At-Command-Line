import requests
from configReader import ConfigurationReader
from requests import ConnectionError
import sys

class NewsPulling(object):
    """This class is used to pull news from the internet depending on the source specified """
    def __init__(self,newsSource):
        self.Source=newsSource
        
    def PullNews(self):
        Configuration = ConfigurationReader()
        self.__APIKey=Configuration.GetAPIKEY()
        self.__Limit=Configuration.GetLimit()
        url='https://newsapi.org/v1/articles?source='+self.Source+'&sortBy=top&apiKey='+self.__APIKey
        try:
            req=requests.get(url)
            if(req.status_code==200):
                return req
            else:
                print("There is some issue in connecting to the internet. Please check your firewall or internet")
        except ConnectionError as e:
            print("A connection Attempt failed")
            print(e.message)
            sys.exit()
    
    def JsonRead(self):
        req=self.PullNews()
        # indicate if we need to convert to utf-8
        needsconversion = False
        if req.encoding != 'utf-8':
            needsconversion = True
        req=req.json()
        articles=req['articles']
        noofarticles=len(articles)
        maxarticles=min(noofarticles,self.__Limit)
        
        FilteredArticles=[]
        
        for i in range(maxarticles):
            article=articles[i]
            if needsconversion:
                description=str(article['description'], 'utf-8')
                #print description
                title=str(article['title'], 'utf-8')
                Article_url=str(article['url'], 'utf-8')
                DateofPublication=str(article['publishedAt'], 'utf-8')
                Author=str(article['author'], 'utf-8')
                FilteredArticles.append([description,title,Article_url,DateofPublication,Author])
            else:
                description=article['description']
                #print description
                title=article['title']
                Article_url=article['url']
                DateofPublication=article['publishedAt']
                Author=article['author']
                FilteredArticles.append([description,title,Article_url,DateofPublication,Author])
        return FilteredArticles
        
    def BeautifyArticles(self):
        self.Articles=self.JsonRead()
        if self.Articles is None or len(self.Articles)==0:
            print("No articles found")
            sys.exit()
        print("\n" + ("="*16) + " STORIES " + ("="*16))
        for i in range(len(self.Articles)):
            print("[" +str(i+1) +"]", end=' ')
            # Title
            if self.Articles[i][1] is not None:
                print("\t"+self.Articles[i][1])
            # Summary
            if self.Articles[i][0] is not None:
                # Limit Summary Size
                summary = self.Articles[i][0][:85] + (self.Articles[i][0][85:] and '...')
                print("\t"+summary)
            # Author
            if self.Articles[i][4] is not None:
                print("\t"+self.Articles[i][4])
            # Date
            if self.Articles[i][3] is not None:
                print("\t"+self.Articles[i][3]+"\n")
        print("="*40)
        return self.Articles 
    
        
        
        
