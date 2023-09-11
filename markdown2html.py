#!/usr/bin/python3


import sys
import os
import markdown

if len(sys.argv) < 3:
    stderr "Usage: ./markdown2html.py README.md README.html"
    exit 1


