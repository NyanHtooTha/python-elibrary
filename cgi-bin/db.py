#!/usr/bin/python3

import sqlite3
from datetime import datetime
import sys

connection = sqlite3.connect('data/data.db')
cursor = connection.cursor()
       
def create_tables(book_types):
    for each_type in book_types:
        cursor.execute('create table "%s" (id integer primary key autoincrement unique not null, the_book text not null, read_count integer not null, read_date date not null)' %each_type)
        cursor.execute('create index "idx%s" on "%s" (the_book, read_count, read_date)' %(each_type.replace(' ',''), each_type))
        connection.commit()
        
def check_for_update(book_types):
    current_tables = [each[0] for each in cursor.execute('select name from sqlite_master where type="table"').fetchall()]
    current_tables.remove('sqlite_sequence')
    new_tables = set(current_tables) ^ set(book_types)
    if new_tables:        
        create_tables(list(new_tables))
    else:
        pass

def insert_update_data(table_name, the_book):
    check = cursor.execute('select * from "%s" where the_book="%s"' %(table_name, the_book)).fetchall()
    if not check:
        cursor.execute('insert into "%s"(the_book, read_count, read_date) values (?, ?, ?)' %table_name, (the_book, 1, datetime.now())) 
    else:
        cursor.execute('update "%s" set read_count=read_count+1, read_date=? where the_book=?' %table_name, (datetime.now(), the_book))
    connection.commit()

#Core Algorithm SQL Query        
def get_recommend_books(book_type):
    raw_books = cursor.execute('select the_book from "%s" order by read_count desc, read_date desc limit 6' %book_type).fetchall()
    if raw_books:
        books = [book[0] for book in raw_books]
        return books
    else:
        return None
