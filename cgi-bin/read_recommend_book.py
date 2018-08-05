#!/usr/bin/python3

import cgi
import view

form_data = cgi.FieldStorage()
book_to_read = form_data['bookname'].value
view.__read_book__(book_to_read)




