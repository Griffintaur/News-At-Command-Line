#!/usr/bin/env python3

import sys
from enum import Enum

from .news_pulling import NewsPulling
from .extract_main_content import ExtractMainContent
from .reader_plugins.plugin_registration import sites


class SelectionStatus(Enum):
    BACK = 1
    EXIT = 2
    READ = 3


def news_sources():
    news_sources = tuple(sites.keys())
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
            return SelectionStatus.BACK, None
        # Exit
        elif(article_selection.lower()[0] == 'q'):
            return SelectionStatus.EXIT, None

        article_selection = int(article_selection)
        if 0 > article_selection - 1 or article_selection > max:
            print(f'Please select an index between 1-{max}.')
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


def main():
    display_title_banner()

    while True:
        sources = news_sources()
        source_choice = prompt_for_source(sources)

        while True:
            # TODO: This is ugly, but functional.
            # Getting the name of thesource as used in the API from the plugin.
            puller = NewsPulling(sites[sources[source_choice]]().source_name)
            articles = puller.beautify_articles()
            status, article_selection = prompt_for_article(max=len(articles))
            if status == SelectionStatus.EXIT:
                sys.exit()
            elif status == SelectionStatus.BACK:
                break
            else:
                print("\n" * 5)
                extr = ExtractMainContent(
                    sources[source_choice], articles[article_selection][2])
                extr.beautify()

                if prompt_for_save():
                    extr.save()
                    print("File saved!\n")


if __name__ == "__main__":
    main()
