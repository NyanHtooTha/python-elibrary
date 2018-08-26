#!/usr/bin/python3

import cgi
import cgitb
import view
import db

#import sys

cgitb.enable()
form_data = cgi.FieldStorage()
book_to_read = form_data['bookname'].value.replace('.jpg', '.pdf')
if '\\' in book_to_read:
    book_to_read = book_to_read.replace('\\', '/')
#print('~~~', book_to_read, file=sys.stderr)
#form_data.__del__()                        
choiced_book_type = book_to_read.split('\\')[0][1:].split('/')[1]
#images = glob.glob(book_to_read.split('\\')[0][1:]+'/*.jpg')
db.insert_update_data(choiced_book_type, book_to_read)
view.__read_book__(book_to_read)




