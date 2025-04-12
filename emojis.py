#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script is the workhorse to extract the emojis.

There are two main functions:
-   The preprocess function is intended to include different patterns in necessary.
-   The read_emoji_sequence reads the official unicode text file and creates a dictionary.
"""
import json
import re
from typing import NoReturn

def preprocess(workfile: str) -> NoReturn:
    """
    Simple preprocess function that handle mishaps in the text file.

    Args:
        workfile (str): Path for emoji file with mishap.
    """
    patterns = {'(#️⃣)': '(<KEYCAP_HASH>)'}

    with open(workfile, 'r', encoding='utf-8') as f:
        text = f.read()

        for pattern in patterns.items():
            if pattern[0] in text:
                text = text.replace(pattern[0], pattern[1])

    with open(workfile, 'w+', encoding='utf-8') as f:
        f.write(text)

def read_emoji_sequences(workfile: str) -> dict[str, str]:
    """
    Reads a text file and returns its contents as a dictionary.

    Args:
        workfile (str): Path for emoji file.

    Returns:
        dict[str, str]: Dictionary where the keys are emojis and the values
                        are the textual descriptions. 

                        E.g. {"⌚": " watch"}
    """
    emoji_dictionary = {}
    emoji_pattern = re.compile(r'\((.*)\)').findall

    with open(workfile, encoding='utf-8') as f:
        for line in f:
            if line.startswith(('#', '\n')):
                continue

            segments = line.rsplit(";", 1)[1].split("#") #fixed for spec2

            descriptions = segments[0].split("..")

            emojis = emoji_pattern(segments[-1])[0].split('..')

            for emoji, description in zip(emojis, descriptions):
                emoji_dictionary[emoji.strip()] = " " + description.strip()

    if "<KEYCAP_HASH>" in emoji_dictionary:
        emoji_dictionary['#️⃣'] = emoji_dictionary.pop("<KEYCAP_HASH>")

    return emoji_dictionary

def to_json(emj_dict: dict, path_spec: str, render_unicode: bool=True) -> NoReturn:
    """
    Simple function to convert dictionary to .py (or .json) file.

    Args:
        emj_dict (dict): A dictionary that contains emojis.
        path_spec (str): The path where the .json file is saved.
        render_unicode (bool): If True renders the actual emojis else renders their unicode.
    """
    with open(path_spec, 'w', encoding='utf-8') as fp:
        json.dump(emj_dict, fp, ensure_ascii=render_unicode, indent=4)
