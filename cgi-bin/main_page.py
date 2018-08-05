#!/usr/bin/python3

import os
import view

book_types = os.listdir('books')
data = os.listdir('data')

if not data:
    view.__main_page__(book_types)
else:
    pass
