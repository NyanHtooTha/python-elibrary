#!/usr/bin/python

import cgi
import os
import view
import accounts

def header(title):
    print("Content-type: text/html\n")
    print("<HTML>\n<HEAD>\n<TITLE>%s</TITLE>\n</HEAD>\n<BODY bgcolor='navy'>\n" %(title))

def footer():
    print("</BODY></HTML>")

form = cgi.FieldStorage()
username = form["uname"].value 
password = form["psw"].value 

if not form:
    header("Login Response")
elif username in accounts.users.keys() and accounts.users[username]["password"] == password:
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
else:
    header("Connected ...")
    print('<center><hr><H3 style="color:white;">Username or Password was Incorrect!</H3>')
    print('<H4 style="color:white;">Please go back and enter a valid login.</H4><hr></center>')
footer()
