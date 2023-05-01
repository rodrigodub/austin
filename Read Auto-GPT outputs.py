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
# ##### `Version 0.01` 2023.04.30

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


keywords_list = ["NEXT ACTION", "CRITICISM", "PLAN", "REASONING", "THOUGHTS", "SYSTEM", "NEWS"]


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
file = "RodBot_Terminal-output_20230429.txt"
autogpt_output = Path(directory)  / file

print(autogpt_output)

# ## 2. Interpretation

read_output(autogpt_output)[:2000]

# interpret_output(autogpt_output)
Markdown(interpret_output(autogpt_output, keywords_list))






