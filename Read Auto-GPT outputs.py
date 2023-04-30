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


def read_output(input_file):
    with open(input_file, "r") as f:
        result = f.read()
    return result


directory = "/Users/rodrigo/Code/auto-gpt/Auto-GPT/auto_gpt_workspace/"
file = "RodBot_Terminal-output_20230429.txt"
autogpt_output = Path(directory)  / file

print(autogpt_output)

# ## 2. Interpretation

read_output(autogpt_output)






