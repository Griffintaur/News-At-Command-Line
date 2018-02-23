from bs4 import BeautifulSoup

from news.reader import Reader


class TimesOfIndia(Reader):
    """class for Times of India parsing"""
    source_name = 'the-times-of-india'

    def extractor(self, text):
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
