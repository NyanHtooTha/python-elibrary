#!/usr/bin/python3

import os
import view

book_types = os.listdir('books')
data = os.listdir('data')

if not data:
    import db
    db.create_tables(book_types)
    view.__main_page__(book_types)
else:
    import db
    db.check_for_update(book_types)
    view.__main_page__(book_types, data=True)
    
