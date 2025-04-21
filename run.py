#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script extracts the current list of Unicode emoji characters and their textual 
description for natural language processing tasks. The idea was inspired by the paper
below.

** The program is intended to work with new releases approved by uncode. **

Full Emoji List, vNN.N: https://unicode.org/emoji/charts/full-emoji-list.html
    - emoji-sequences.txt
    - emoji-zwj-sequences.txt
    
Paper: https://aclanthology.org/N19-1214/
"""
import argparse
import ast

import emojis

def extract_emojis(parsed_args):
    """
    Main function to extract emojis.
    """
    if parsed_args.preprocess == 'yes':
        emojis.preprocess(parsed_args.file)

    if parsed_args.file and parsed_args.save_path and parsed_args.render_unicode:
        data = emojis.read_emoji_sequences(parsed_args.file)
        emojis.to_json(data, render_unicode=ast.literal_eval(parsed_args.render_unicode),
                       path_spec=parsed_args.save_path)

def parse_args():
    args = argparse.ArgumentParser(description="Extract emojis from the command line.")
    args.add_argument('--preprocess', type=str, choices=['yes', 'no'], required=True,
                    help='Preprocess only emoji-sequence.txt')
    args.add_argument('--file', type=str, required=True,
                    help='Text file to extract emojis.')
    args.add_argument('--render_unicode', type=str, choices=['True', 'False'],
                    help='Render as ascii or keep emoji.', default=False)
    args.add_argument('--save_path', type=str, required=True,
                    help="Path to save .py file.")

    args = args.parse_args()

    return args

if __name__ == "__main__":
    emj_args = parse_args()
    extract_emojis(emj_args)
