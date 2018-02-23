from bs4 import BeautifulSoup

from news.reader import Reader


class Guardian(Reader):
    """class for Guardian parsing"""
    source_name = 'the-guardian-uk'

    def extractor(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        title = soup.title.string
        Result = []
        # print soup
        maincontent = soup.find_all(
            "div",
            class_="content__article-body from-content-api js-article__body"
        )
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
