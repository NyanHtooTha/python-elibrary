#!/usr/bin/python3

import cgi
import view
import db

form_data = cgi.FieldStorage()
book_to_read = form_data['bookname'].value.replace('.jpg', '.pdf')
#form_data.__del__()                        
choiced_book_type = book_to_read.split('\\')[0][1:].split('/')[1]
#images = glob.glob(book_to_read.split('\\')[0][1:]+'/*.jpg')
db.insert_update_data(choiced_book_type, book_to_read)
view.__read_book__(book_to_read)




