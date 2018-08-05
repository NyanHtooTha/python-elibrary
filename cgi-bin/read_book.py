#!/usr/bin/python3

import cgi
import sys
import glob
import json
import webbrowser
import html_render

localhost = 'http://localhost:8080/'

form_data = cgi.FieldStorage()
book_to_read = form_data['bookname'].value.replace('.jpg', '.pdf')
form_data.__del__()

choiced_book_type = book_to_read.split('\\')[0][1:].split('/')[1]
images = glob.glob(book_to_read.split('\\')[0][1:]+'/*.jpg')

print(html_render.start_response())
print('<div align="center"><embed src="%s" width="1200px" height="2100px" /></div>' % book_to_read)
print(html_render.end_response())


