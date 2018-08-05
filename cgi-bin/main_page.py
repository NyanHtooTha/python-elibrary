#!/usr/bin/python3

import os
import html_render

book_types = os.listdir('books')

print(html_render.start_response())
print(html_render.include_header("MTU E-Library"))
print(html_render.start_form("book_by_type.py", menu=True))
print(html_render.u_list_menu(book_types))
print(html_render.end_form())
print(html_render.end_response())
