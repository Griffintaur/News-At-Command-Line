from news.reader import Reader


class NYT(Reader):
    """class for New York Times parsing"""
    def extractor(self, text):
        return self._extraction_algo(text, "p",
                                     "story-body-text story-content")
