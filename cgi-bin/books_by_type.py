#!/usr/bin/python3

import cgi
import glob
import view

form_data = cgi.FieldStorage()
choiced_book_type = form_data['booktype'].value
form_data.__del__()
images = glob.glob('books/'+choiced_book_type+'/*.jpg')
view.__books_by_type__(choiced_book_type, images)

