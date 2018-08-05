import html_render

def __main_page__(book_types, data=False):
    if data is False:
        print(html_render.start_response())
        print(html_render.include_header("MTU E-Library"))
        print(html_render.start_form("books_by_type.py", menu=True))
        print(html_render.u_list_menu(book_types))
        print(html_render.end_form())
        print(html_render.blank_line())
        print('<marquee behavior="alternate"><p><h4>There is no Popular Books in the Library now !</h4></p></marquee>')
        print(html_render.end_response())
    else:
        pass

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
    print('<div align="center"><embed src="%s" width="1200px" height="2100px" /></div>' % book_to_read)
    print(html_render.end_response())
    
