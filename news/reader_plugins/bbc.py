from news.reader import Reader


class BBC(Reader):
    """class for BBC News parsing"""
    source_name = 'bbc-news'

    def extractor(self, text):
        return self._extraction_algo(text, "div", "story-body__inner")
