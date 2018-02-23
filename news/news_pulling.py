import sys

import requests
from requests import ConnectionError

from .config_reader import ConfigurationReader


class NewsPulling:
    """Pull news from the internet depending on the source specified."""

    def __init__(self, source):
        self.source = source

    def pull_news(self):
        config = ConfigurationReader()
        self.__Limit = config.limit
        url = 'https://newsapi.org/v1/articles?source=' + \
            self.source + '&sortBy=top&apiKey=' + config.APIKEY
        try:
            req = requests.get(url)
            print(req)
            if req.status_code == 200:
                return req
            else:
                print("There is some issue in connecting to the internet."
                      "Please check your firewall or internet")
        except ConnectionError as e:
            print("A connection attempt failed")
            print(e.message)
            sys.exit()

    def json_read(self):
        req = self.pull_news()
        # indicate if we need to convert to utf-8
        needsconversion = False
        if req.encoding != 'utf-8':
            needsconversion = True
        req = req.json()
        articles = req['articles']
        noofarticles = len(articles)
        maxarticles = min(noofarticles, self.__Limit)

        FilteredArticles = []

        for i in range(maxarticles):
            article = articles[i]
            if needsconversion:
                description = str(article['description'], 'utf-8')
                # print description
                title = str(article['title'], 'utf-8')
                Article_url = str(article['url'], 'utf-8')
                DateofPublication = str(article['publishedAt'], 'utf-8')
                Author = str(article['author'], 'utf-8')
                FilteredArticles.append([description, title, Article_url,
                                         DateofPublication, Author])
            else:
                description = article['description']
                # print description
                title = article['title']
                Article_url = article['url']
                DateofPublication = article['publishedAt']
                Author = article['author']
                FilteredArticles.append(
                    [description, title, Article_url,
                     DateofPublication, Author])
        return FilteredArticles

    def beautify_articles(self):
        self.Articles = self.json_read()
        if self.Articles is None or len(self.Articles) == 0:
            print("No articles found")
            sys.exit()
        print("\n" + ("=" * 16) + " STORIES " + ("=" * 16))
        for i in range(len(self.Articles)):
            print("[" + str(i + 1) + "]", end=' ')
            # Title
            if self.Articles[i][1] is not None:
                print("\t" + self.Articles[i][1])
            # Summary
            if self.Articles[i][0] is not None:
                # Limit Summary Size
                summary = self.Articles[i][0][:85] + \
                    (self.Articles[i][0][85:] and '...')
                print("\t" + summary)
            # Author
            if self.Articles[i][4] is not None:
                print("\t" + self.Articles[i][4])
            # Date
            if self.Articles[i][3] is not None:
                print("\t" + self.Articles[i][3] + "\n")
        print("=" * 40)
        return self.Articles
