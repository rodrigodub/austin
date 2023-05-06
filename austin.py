###########################################################################
# Austin
# A Python agent to interpret Auto-GPT outputs
# Author: Rodrigo Nobrega
# 20230506 / 
###########################################################################
__title__ = "Austin"
__version__ = 0.03


# import libraries
import os
from pathlib import Path
import pandas as pd
from IPython.display import Markdown


# Austin Class
class Austin(object):
    """"""
    def __init__(self, file):
        self.file = file
        self.keywords_list = ['NEWS', 'SYSTEM', 'THOUGHTS', 'REASONING', 'PLAN', 'CRITICISM', 'NEXT ACTION']
        self.contents = self.read_terminal()
        self.splitted_contents = self.split_recursively(self.contents)

    def read_terminal(self):
        """"""
        print(" Reading Terminal contents")
        with open(self.file, "r") as f:
            result = f.read()
        return result

    def replace_headers(self, atext):
        """"""
        print(" Formatting Markdown headers")
        for keyword in self.keywords_list:
            atext = atext.replace(f"{keyword}: ", f"# {keyword}\n")
        return atext

    def return_smallest_index(self, given_text):
        """"""
        index_list = []
        for key in self.keywords_list:
            if given_text.find(key) > 0:
                index_list.append(given_text.find(key))
        try:
            smallest_index = min(index_list)
        except:
            smallest_index = 0
        return smallest_index

    def split_recursively(self, given_text: str):
        """"""
        # 1 Take the full text
        parts = []

        # 2 Take all the words in keywords and find the smallest index of them, greater than zero
        smallest_index = len(given_text)
        for keyword in self.keywords_list:
            index = given_text.find(keyword)
            if 0 < index < smallest_index:
                smallest_index = index

        # 3 Split the full text into two parts, separated by the index
        part1 = given_text[:smallest_index]
        part2 = given_text[smallest_index:]

        # 4 Store the first part in a list and recursively do the same process with the second part
        parts.append(part1)
        if len(part2) > 0:
            parts.extend(self.split_recursively(part2))

        # 5 Return a list with all the parts
        return parts


# main loop
def main():
    # header --------------------------------------------------------------
    print(f'\n{75 * "="}')
    print(f'{f"{__title__} v.{__version__}":^75}')
    print(f'{75 * "="}\n')
    # ---------------------------------------------------------------------
    # main code goes here
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')


# test loop
def test():
    # header --------------------------------------------------------------
    print(f'\n{75 * "="}')
    print(f'{"TEST":^75}')
    print(f'{f"{__title__} v.{__version__}":^75}')
    print(f'{75 * "="}\n')
    # ---------------------------------------------------------------------
    # test code goes here
    directory = "/Users/rodrigo/Code/auto-gpt/Auto-GPT/auto_gpt_workspace/"
    # file = "RodBot_Terminal-output_20230429.txt"
    file = "RodBot_Terminal-dev_20230506.txt"
    autogpt_terminal = Path(directory) / file
    #
    agent = Austin(autogpt_terminal)
    [print(i) for i in agent.splitted_contents]
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')


# main, calling main loop
if __name__ == '__main__':
    # main()
    test()
