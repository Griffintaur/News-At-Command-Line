import requests
import textwrap

from .reader_plugins.plugin_registration import sites


class ExtractMainContent:
    def __init__(self, source, articleurl):
        self.source = source
        self.url = articleurl
        self.textWrap = textwrap.TextWrapper(
            initial_indent='\t', subsequent_indent='\t', width=100)

    def download(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/59.0.3071.115 Safari/537.36'}
        req = requests.get(self.url, headers=headers)
        return req.text

    def _extract(self):
        text = self.download()
        return sites[self.source]().extractor(text)

    def beautify(self):
        title, output = self._extract()
        print("=" * (len(title) + 15))
        print("\t" + title)
        print("=" * (len(title) + 15))

        print((self.textWrap.fill(output)))  # wrap of the line
        print("*" * 80)
        if len(output) == 0:
            print("Sorry :(")
            print("There isn't much text on the site besides video/image. To "
                  "further view the media post, Go to the below link")
            print(self.url)
            print('*' * 80)
            print("\n\n")

    def save(self):
        title, output = self._extract()

        # Remove Chars not allowed in filenames
        for char in ['<', '>', "/", ":", '"', "\\", "|", "?", "*"]:
            if char in title:
                title = title.replace(char, "")

        with open(f'saved_articles/{title}.txt', "w+") as f:
            f.write(output)
