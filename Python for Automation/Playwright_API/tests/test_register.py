

import pytest

from pages.register import registers

@pytest.mark.smoke
def test_registeration(page):
    register_page = registers(page)
    register_page.register()

@pytest.mark.smoke
def test_logins(page):
    login_page = registers(page)
    login_page.login()