#!/usr/bin/python3

from string import Template

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

def include_header(the_title):
    with open('templates/template.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def u_list_one(book_type):
    return('<ul><li class="one">%s</li></ul>' %book_type)

def u_list_menu(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li><a><input onclick="bookmenu.submit();" type="submit" name="booktype" value="%s"></a></li>' %item
    u_string += '</ul>'
    return(u_string)

def start_form(the_url, menu=False):
    if menu:
        return('<form id="bookmenu" action="%s" method="POST">' %the_url)
    else: 
        return('<form action="%s" method="POST">' %the_url)

def end_form():
    return('</form>')

def make_book_gallery(items, recommend=False):
    book_gallery = ''
    if not recommend:
        for image in items:
            book_gallery += '<div class="gallery"><a href="/%s" target="_blank"><img src="/%s"></a><div class="desc"><button name="bookname" value="/%s">Read</button></div></div>' %(image, image, image)
        return book_gallery
    else:
        for book in items:
            image = book.replace('.pdf', '.jpg')
            book_gallery += '<div style="display: inline-block;"><div class="gallery"><a href="%s" target="_blank"><img src="%s"></a><div class="desc"><button name="bookname" value="%s">Read</button></div></div></div>' %(image, image, book)
        return book_gallery

def blank_line():
    return('</br>')

def end_response():
    return('</body></html>')

