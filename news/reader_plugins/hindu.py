from bs4 import BeautifulSoup

from news.reader import Reader


class TheHindu(Reader):
    """class for The Hindu parsing"""
    source_name = 'the-hindu'

    def extractor(self, text):
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
