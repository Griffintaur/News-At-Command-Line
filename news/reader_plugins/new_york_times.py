from news.reader import Reader


class NYT(Reader):
    source_name = 'the-new-york-times'

    """class for New York Times parsing"""
    def extractor(self, text):
        return self._extraction_algo(text, "p",
                                     "story-body-text story-content")
