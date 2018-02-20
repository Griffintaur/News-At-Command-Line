from NewsPulling import NewsPulling
from configReader import ConfigurationReader
from ExtractMainContent import ExtractMainContent
import sys


def NewsSources():
    NewsSources = ConfigurationReader().GetWebsiteSupported()
    return NewsSources


def App():

    # Cool Title/Banner
    print("=" * 40)
    print("\tNews at the Command Line")
    print("=" * 40)
    print()

    while True:
        newsSources = NewsSources()
        # Output News Sources
        for i in range(len(newsSources)):
            print("[" + str(i + 1) + "]" + "\t" + newsSources[i])
        print("\nPlease enter the index of the news source or type 'quit' to exit")

        # Validate Input
        while True:
            newsSourceNumber = input("News Source Number >>>> ")
            # Quit
            if(newsSourceNumber.lower() == "quit"):
                sys.exit()
            try:
                newsSourceNumber = int(newsSourceNumber) - 1
                if(newsSourceNumber >= len(newsSources) or newsSourceNumber < 0):
                    print("Please select an index between 1-" +
                          str(len(newsSources)))
                # Good Input, break
                else:
                    break
            except ValueError:
                print("That is not a valid News Source Number")

        while True:

            obj = NewsPulling(newsSources[newsSourceNumber])
            Articles = obj.BeautifyArticles()
            print("Do you want to read a story further? If yes, please select the number corresponding to the article")
            print("Enter 'back' to go back to the main menu")
            print("Press 'quit' to quit")
            articleNumber = input("Article No >>>> ")
            # Back
            if(articleNumber.lower() == "back"):
                break
            # Exit
            if(articleNumber.lower() == "quit"):
                sys.exit()

            try:
                articleNumber = int(articleNumber) - 1
                if (articleNumber >= len(Articles) or articleNumber < 0):
                    print("Please select an index between 1-" + str(len(Articles)))

                else:
                    print("\n" * 5)
                    extr = ExtractMainContent(
                        newsSources[newsSourceNumber], Articles[articleNumber][2])
                    extr.Beautify()
                    print("Do you want to save this article in file")
                    YesorNo = str(input("Want to save? y/n >>> "))
                    if YesorNo.lower() == "yes" or YesorNo.lower() == "y":
                        extr.FileSave()
                        print("File saved!")
                    print("\n")

            except ValueError:
                print("That is not a valid Article Number")


if __name__ == "__main__":
    App()
