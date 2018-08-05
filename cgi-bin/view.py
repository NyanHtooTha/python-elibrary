#!/usr/bin/python3

import html_render

def __main_page__(book_types, data=False):
    if not data:
        print(html_render.start_response())
        print(html_render.include_header("MTU E-Library"))
        print(html_render.start_form("books_by_type.py", menu=True))
        print(html_render.u_list_menu(book_types))
        print(html_render.end_form())
        print(html_render.blank_line())
        print('<marquee behavior="alternate"><p><h4>Book Recommendation System Is Not Available Now !</h4></p></marquee>')
        print(html_render.end_response())
    else:
        import db
        print(html_render.start_response())
        print(html_render.include_header("MTU E-Library"))
        print(html_render.start_form("books_by_type.py", menu=True))
        print(html_render.u_list_menu(book_types))
        print(html_render.end_form())
        #print(html_render.blank_line())
        print(html_render.start_form('read_recommend_book.py'))
        for book_type in book_types:
            recommend_books = db.get_recommend_books(book_type)
            if recommend_books:
                print('<p style="border-left: 6px solid blue; background-color: lightgrey;">&nbsp; Recommended %s Books</p>' %book_type)
                print(html_render.make_book_gallery(recommend_books, recommend=True))
                #print(html_render.blank_line())
            else:
                pass
        print(html_render.end_form())
        print(html_render.end_response())

def __books_by_type__(choiced_book_type, images):
    print(html_render.start_response())
    print(html_render.include_header("MTU E-Library"))
    print(html_render.u_list_one(choiced_book_type))
    print(html_render.blank_line())
    print(html_render.start_form('read_book.py'))
    print(html_render.make_book_gallery(images))
    print(html_render.end_form())
    print(html_render.end_response())
    
def __read_book__(book_to_read):
    print(html_render.start_response())
    print('<div align="center"><embed src="%s" width="100%%" height="2100px" /></div>' % book_to_read)
    print(html_render.end_response())
    
