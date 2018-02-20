import requests
from configReader import ConfigurationReader
from Extractor import *
import textwrap


class ExtractMainContent:
    def __init__(self, source, articleurl):
        self.extractorlist = [HuffingtonPost(), NYT(), BBC(
        ), BloomBerg(), Guardian(), TheHindu(), TimesOfIndia()]
        websites = ConfigurationReader().websites_supported
        self.Mapping = {}
        for index, website in enumerate(websites):
            self.Mapping[website] = self.extractorlist[index]
        self.Source = source
        self.url = articleurl
        self.textWrap = textwrap.TextWrapper(
            initial_indent='\t', subsequent_indent='\t', width=100)

    def download(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/59.0.3071.115 Safari/537.36'}
        req = requests.get(self.url, headers=headers)
        return req.text

    def AddExtractorList(self, extractor):
        self.extractorlist.append(extractor)

    def Extract(self):
        self.ExtractStrategy = self.Mapping[self.Source]
        text = self.download()
        return self.ExtractStrategy.ExtractionAlgo(text)

    def Beautify(self):
        title, output = self.Extract()
        print("=" * (len(title) + 15))
        print("\t" + title)
        print("=" * (len(title) + 15))

        print((self.textWrap.fill(output)))  # wrap of the line
        print("*********************************************************************************")
        if len(output) == 0:
            print("Sorry :(")
            print("There isn't much text on the site besides video/image. To further view the media post, Go to the below link")
            print(self.url)
            print(
                "*********************************************************************************")
            print("\n\n")

    def save(self):
        title, output = self.Extract()

        # Remove Chars not allowed in filenames
        for char in ['<', '>', "/", ":", '"', "\\", "|", "?", "*"]:
            if char in title:
                title = title.replace(char, "")

        with open(f'saved_articles/{title}.txt', "w+") as f:
            f.write(output)
