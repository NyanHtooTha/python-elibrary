#!/usr/bin/python3

import cgi
import glob
import view

localhost = 'http://localhost:8080/'

form_data = cgi.FieldStorage()
book_to_read = form_data['bookname'].value.replace('.jpg', '.pdf')
form_data.__del__()
view.__read_book__(book_to_read)




