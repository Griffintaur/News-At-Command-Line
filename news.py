import sys
from enum import Enum

from news_pulling import NewsPulling
from config_reader import ConfigurationReader
from extract_main_content import ExtractMainContent


class SelectionStatus(Enum):
    BACK = 1
    EXIT = 2
    READ = 3


def news_sources():
    news_sources = ConfigurationReader().websites_supported
    return news_sources


def display_sources(sources):
    for index, source in enumerate(sources):
        print(f'[{index + 1}]\t{source}')
    print("\nPlease enter the index, or indexes, of the news source(s)"
    " or type 'quit' to exit\nPlease separate source numbers with a comma")


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
            source_choices = parse_sources(source_choice.strip().split(','))
            for i in source_choices:
                if(i >= len(sources) or i < 0):
                    print("Please select an index between 1 and " +
                        str(len(sources)))
            return source_choices
        except ValueError:
            print("That is not a valid News Source Number")

def parse_sources(source_choices):
    source_numbers = list()
    for source in source_choices:
        if (int(source) - 1) not in source_numbers:
            source_numbers.append(int(source) - 1 )
    return source_numbers

def prompt_for_article(max=0):
    print("Do you want to read a story further? If yes, please select the "
          "number corresponding to the article")
    print("Enter 'back' to go back to the main menu")
    print("Press 'quit' to quit")
    while True:
        article_selection = input("Article No >>>> ")

        # Back
        if(article_selection.lower()[0] == 'b'):
            return SelectionStatus.BACK, None
        # Exit
        elif(article_selection.lower()[0] == 'q'):
            return SelectionStatus.EXIT, None

        article_selection = int(article_selection)
        if 0 > article_selection - 1 or article_selection > max:
            print(f'Please select an index between 1 and {max}.')
        else:
            return SelectionStatus.READ, article_selection - 1


def prompt_for_save():
    while True:
        print("Do you want to save this article in file")
        selection = str(input("Want to save? y/n >>> "))
        if selection[0].lower() == 'y':
            return True
        elif selection[0].lower() == 'n':
            return False

def display_articles(Articles):
    """Displays the articles choices from a list"""
    print("\n" + ("=" * 16) + " STORIES " + ("=" * 16))
    for i in range(len(Articles)):
        print("[" + str(i + 1) + "]", end=' ')
        # Title
        if Articles[i][1] is not None:
            print("\t" + Articles[i][1])
        # Summary
        if Articles[i][0] is not None:
        # Limit Summary Size
            summary = Articles[i][0][:85] + \
            (Articles[i][0][85:] and '...')
            print("\t" + summary)
            # Author
        if Articles[i][4] is not None:
            print("\t" + Articles[i][4])
        # Date
        if Articles[i][3] is not None:
            print("\t" + Articles[i][3] + "\n")
    print("=" * 40)

def collat_articles(source_choices, sources):    
    """Returns a list of articles from all sources passed"""
    articles, article_sources = list(), list()
    for choice in source_choices:
        puller = NewsPulling(sources[choice])
        # TODO: Implement more efficiently
        number_of_articles = len(articles)
        articles.extend(puller.beautify_articles())
        for i in range(len(articles) - number_of_articles):
            article_sources.append(choice)
    return articles, article_sources

def count_other_articles(source, sources):
    """Returns a count of articles that do not share the source passed"""
    other_sources = 0
    for s in sources:
        if s != source:
            other_sources += 1
    return other_sources

def main():
    display_title_banner()

    while True:
        sources = news_sources()
        source_choices = prompt_for_source(sources)

        while True:            
            articles, article_sources = collat_articles(source_choices, sources)
            display_articles(articles)            
            status, article_selection = prompt_for_article(max=len(articles))
            if status == SelectionStatus.EXIT:
                sys.exit()
            elif status == SelectionStatus.BACK:
                break
            else:
                print("\n" * 5)                
                extr = ExtractMainContent(
                    sources[article_sources[article_selection]], articles[article_selection][2])
                extr.beautify()

                if prompt_for_save():
                    extr.save()
                    print("File saved!\n")

if __name__ == "__main__":
    main()