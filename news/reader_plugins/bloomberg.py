from news.reader import Reader


class Bloomberg(Reader):
    """class for BloomBerg parsing"""
    source_name = 'bloomberg'

    def extractor(self, text):
        return self._extraction_algo(text, "div", "body-copy")
