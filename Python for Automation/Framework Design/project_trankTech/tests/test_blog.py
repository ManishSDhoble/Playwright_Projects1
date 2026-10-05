

import pytest

from pages.blog import blog
# from pages.contacts import contacts

@pytest.mark.blogs
def test_blog(page):
    blogs = blog(page)
    blogs.blog_horizontal_links()
    blogs.blog_categories()
    blogs.blog_links()

# @pytest.mark.contacts
# def test_contact(page):
#     con = contacts(page)
#     con.contact_page()

