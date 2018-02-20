import sys

from NewsPulling import NewsPulling
from configReader import ConfigurationReader
from ExtractMainContent import ExtractMainContent


def news_sources():
    news_sources = ConfigurationReader().websites_supported
    return news_sources


def display_sources(sources):
    for index, source in enumerate(sources):
        print(f'[{index + 1}]\t{source}')
    print("\nPlease enter the index of the news source or type 'quit' to exit")


def display_title_banner():
    # Cool Title/Banner
    print("=" * 40)
    print("\tNews at the Command Line")
    print("=" * 40)
    print()


def prompt_for_source(sources):
    while True:
        display_sources(sources)
        source_choice = input("News Source Number >>>> ")
        # Quit
        if(source_choice.lower() == "quit"):
            sys.exit()
        try:
            source_choice = int(source_choice) - 1
            if(source_choice >= len(sources) or source_choice < 0):
                print("Please select an index between 1-" +
                      str(len(sources)))
            else:
                return source_choice
        except ValueError:
            print("That is not a valid News Source Number")


def prompt_for_article(max=0):
    print("Do you want to read a story further? If yes, please select the"
          "number corresponding to the article")
    print("Enter 'back' to go back to the main menu")
    print("Press 'quit' to quit")
    while True:
        article_selection = input("Article No >>>> ")

        # Back
        if(article_selection.lower()[0] == 'b'):
            return -2  # TODO: This is terrible, improve this.
        # Exit
        elif(article_selection.lower()[0] == 'q'):
            return -1

        article_selection = int(article_selection)
        if 0 > article_selection - 1 or article_selection > max:
            print(f'Please select an index between 1-{max}.')
        else:
            return article_selection - 1


def prompt_for_save():
    while True:
        print("Do you want to save this article in file")
        selection = str(input("Want to save? y/n >>> "))
        if selection[0].lower() == 'y':
            return True
        elif selection[0].lower() == 'n':
            return False


def main():
    display_title_banner()

    while True:
        sources = news_sources()
        source_choice = prompt_for_source(sources)

        while True:
            obj = NewsPulling(sources[source_choice])
            Articles = obj.BeautifyArticles()
            article_selection = prompt_for_article(max=len(Articles))
            if article_selection == -1:
                sys.exit()
            elif article_selection == -2:
                break
            else:
                print("\n" * 5)
                extr = ExtractMainContent(
                    sources[source_choice], Articles[article_selection][2])
                extr.Beautify()

                if prompt_for_save():
                    extr.save()
                    print("File saved!\n")


if __name__ == "__main__":
    main()
