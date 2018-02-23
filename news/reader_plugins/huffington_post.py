from news.reader import Reader


class HuffingtonPost(Reader):
    """class for Huffington Post parsing"""
    source_name = 'the-huffington-post'

    def extractor(self, text):
        return self._extraction_algo(text, "div",
                                     "content-list-component text")
