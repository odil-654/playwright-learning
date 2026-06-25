import pytest
from pages.basic_auth_page import BasicAuthPage


@pytest.fixture
def basic_auth_page(page):
    return BasicAuthPage(page)