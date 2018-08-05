#!/usr/bin/python3

import cgi
import glob
import html_render

form_data = cgi.FieldStorage()
choiced_book_type = form_data['booktype'].value
form_data.__del__()
images = glob.glob('books/'+choiced_book_type+'/*.jpg')

print(html_render.start_response())
print(html_render.include_header("MTU E-Library"))
print(html_render.u_list_one(choiced_book_type))
print(html_render.blank_line())
print(html_render.start_form('read_book.py'))
print(html_render.make_book_gallery(images))
print(html_render.end_form())
print(html_render.end_response())


