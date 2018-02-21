from bs4 import BeautifulSoup


class Reader:
    def _extraction_algo(self, text, htmlelement, classname):
        soup = BeautifulSoup(text, 'html.parser')
        title = soup.title.string
        result = []
        # print soup
        maincontent = soup.find_all(htmlelement, class_=classname)
        # print maincontent
        for content in maincontent:
            scripttags = content.find_all(["script", "br", "figure", "image"])
            for scripttag in scripttags:
                scripttag.extract()
            # print content.text
            result.append(content.text)
        result = ''.join(result)
        return (title, result)
