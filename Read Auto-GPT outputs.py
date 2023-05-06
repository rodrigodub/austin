# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Austin
# Reading Auto-GPT command line outputs
#
# ##### Author: Rodrigo Nobrega
# ##### Version History
# - `v 0.01` 2023.04.30 Initial development
# - `v 0.02` 2023.05.06 Solved the recursive split of full text

# ## 1. Initialisation

from pathlib import Path
import pandas as pd
from IPython.display import Markdown


def read_output(input_file):
    """
    Reads and returns the contents of a file.

    Parameters:
    input_file (str): Path to the input file.

    Returns:
    str: Contents of the file.
    """
    with open(input_file, "r") as f:
        result = f.read()
    return result


def replace_headers(text, keywords):
    """
    Replaces the headers in the given text with markdown headings.

    Parameters:
    text (str): Input text.
    keywords (list): List of keywords to replace with markdown headings.

    Returns:
    str: Text with markdown headings instead of headers.
    """
    for keyword in keywords:
        text = text.replace(f"{keyword}: ", f"# {keyword}\n")
    return text


def interpret_output(input_file, keywords):
    """
    Reads the output file, replaces headers with markdown headings and returns the formatted text.

    Parameters:
    input_file (str): Path to the input file.
    keywords (list): List of keywords to replace with markdown headings.

    Returns:
    str: Formatted text with markdown headings.
    """
    markdown = ""
    separator = "-=-=-=-=-=-=-= COMMAND AUTHORISED BY USER -=-=-=-=-=-=-= "
    with open(input_file, "r") as f:
        file_contents = f.read()
    iterations_list = file_contents.split(separator)
    markdown = "\n".join(iterations_list)
    new_markdown = replace_headers(markdown, keywords)
    return new_markdown


directory = "/Users/rodrigo/Code/auto-gpt/Auto-GPT/auto_gpt_workspace/"
# file = "RodBot_Terminal-output_20230429.txt"
file = "RodBot_Terminal-dev_20230506.txt"
autogpt_output = Path(directory)  / file

print(autogpt_output)

# ## 2. Interpretation

read_output(autogpt_output)[:2000]

# interpret_output(autogpt_output)
Markdown(interpret_output(autogpt_output, keywords_list))



# # DEV



autogpt_output

a = read_output(autogpt_output)
a[:5000]



keywords_list = ['NEWS', 'SYSTEM', 'THOUGHTS', 'REASONING', 'PLAN', 'CRITICISM', 'NEXT ACTION']

a.find(keywords_list[2])


def return_smallest_index(full_text, keywords):
    index_list = []
    for key in keywords:
        if full_text.find(key) > 0:
            index_list.append(full_text.find(key))
    try:
        smallest_index = min(index_list)
    except:
        smallest_index = 0
    return smallest_index


return_smallest_index(a, keywords_list)


def pop_first_chunk(full_text, keywords):
    return (full_text[:return_smallest_index(full_text, keywords)],
            full_text[return_smallest_index(full_text, keywords):])


b, c = pop_first_chunk(a, keywords_list)[0], pop_first_chunk(a, keywords_list)[1]
b

d, e = pop_first_chunk(c, keywords_list)[0], pop_first_chunk(c, keywords_list)[1]
d


# +
# def split_recursively(full_text, keywords, result_list):
#     output = []
#     part_a = full_text[:return_smallest_index(full_text, keywords)] 
#     part_b = full_text[return_smallest_index(full_text, keywords):] 
#     return (,
#             split_recursively(full_text[return_smallest_index(full_text, keywords):], keywords)
#             )
# def split_recursively(full_text, keywords, initial=None):
#     part_a = ""
#     if return_smallest_index(full_text, keywords) > 0:
#         part_a = full_text[:return_smallest_index(full_text, keywords)] 
#         part_b = full_text[return_smallest_index(full_text, keywords):] 
#     if initial:
#         part_a = initial + part_a
#     return part_a + split_recursively(part_b, keywords, part_a)
# def split_recursively(full_text: str, keywords: list):
#     # 1 Take the full text
#     # 2 Take all the words in keywords and find the smallest index of them, greater then zero
#     # 3 Split the full text in two parts, separated by the index
#     # 4 Store the first part in a list, and recursively do the same process with the second part
#     # 5 Return a list with all the parts
#     return

def split_recursively(full_text: str, keywords: list):
    """
    Recursively splits a full text into parts based on the keywords.

    Args:
        full_text (str): The full text to split.
        keywords (list): List of keywords to search for.

    Returns:
        list: A list containing all the parts after splitting.
    """
    # 1 Take the full text
    parts = []
    
    # 2 Take all the words in keywords and find the smallest index of them, greater than zero
    smallest_index = len(full_text)
    for keyword in keywords:
        index = full_text.find(keyword)
        if index > 0 and index < smallest_index:
            smallest_index = index
    
    # 3 Split the full text into two parts, separated by the index
    part1 = full_text[:smallest_index]
    part2 = full_text[smallest_index:]
    
    # 4 Store the first part in a list and recursively do the same process with the second part
    parts.append(part1)
    if len(part2) > 0:
        parts.extend(split_recursively(part2, keywords))
    
    # 5 Return a list with all the parts
    return parts



# -

b = split_recursively(a, keywords_list)
b


