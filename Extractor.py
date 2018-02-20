# -*- coding: utf-8 -*-
"""
Created on  Jul 24 23:05:13 2016-2017

@author: Ankit Singh
"""
from bs4 import BeautifulSoup


class Extractor(object):

    def ExtractionAlgo(self, text):
        pass

    def TextExtractionAlgo(self, text, htmlelement, classname):
        soup = BeautifulSoup(text, 'html.parser')
        title = soup.title.string
        Result = []
        # print soup
        maincontent = soup.find_all(htmlelement, class_=classname)
        # print maincontent
        for content in maincontent:
            scripttags = content.find_all(["script", "br", "figure", "image"])
            for scripttag in scripttags:
                scripttag.extract()
            # print content.text
            Result.append(content.text)
        Result = ''.join(Result)
        return (title, Result)


class HuffingtonPost(Extractor):
    """class for Huffington Post parsing"""

    def __init__(self):
        Extractor.__init__(self)

    def ExtractionAlgo(self, text):
        return Extractor.TextExtractionAlgo(
            self, text, "div", "content-list-component text")


class NYT(Extractor):
    """class for New York Times parsing"""

    def __init__(self):
        Extractor.__init__(self)

    def ExtractionAlgo(self, text):
        return Extractor.TextExtractionAlgo(
            self, text, "p", "story-body-text story-content")


class BBC(Extractor):
    """class for BBC News parsing"""

    def __init__(self):
        Extractor.__init__(self)

    def ExtractionAlgo(self, text):
        return Extractor.TextExtractionAlgo(
            self, text, "div", "story-body__inner")


class BloomBerg(Extractor):
    """class for BloomBerg parsing"""

    def __init__(self):
        Extractor.__init__(self)

    def ExtractionAlgo(self, text):
        return Extractor.TextExtractionAlgo(self, text, "div", "body-copy")


class Guardian(Extractor):
    """class for Guardian parsing"""

    def __init__(self):
        Extractor.__init__(self)

    def ExtractionAlgo(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        title = soup.title.string
        Result = []
        # print soup
        maincontent = soup.find_all(
            "div", class_="content__article-body from-content-api js-article__body")
        # print maincontent
        for content in maincontent:
            scripttags = content.find_all(["script", "br", "figure", "image"])
            for scripttag in scripttags:
                scripttag.extract()
            # print content.text
            for foundcontent in content.find_all("p"):
                Result.append(foundcontent.text)
        Result = ''.join(Result)
        return (title, Result)


class TheHindu(Extractor):
    """class for BloomBerg parsing"""

    def __init__(self):
        Extractor.__init__(self)

    def ExtractionAlgo(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        title = soup.title.string
        Result = []
        # print soup
        maincontent = soup.find_all("div", class_="article")
        # print maincontent
        for content in maincontent:
            scripttags = content.find_all(
                ["script", "br", "figure", "image", "span"])
            for scripttag in scripttags:
                scripttag.extract()
            # print content.text
            for foundcontent in content.find_all("p"):
                Result.append(foundcontent.text)
        Result = ''.join(Result)
        return (title, Result)


class TimesOfIndia(Extractor):
    """class for BloomBerg parsing"""

    def __init__(self):
        Extractor.__init__(self)

    def ExtractionAlgo(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        title = soup.title.string
        Result = []
        # print soup
        maincontent = soup.find_all("div", class_="Normal")
        # print maincontent
        for content in maincontent:
            # print content.text
            Result.append(content.text)
        Result = ''.join(Result)
        return (title, Result)
